from tkinter import *
from tkinter import ttk
import rapidjson
import dataclasses
import copy

from core import FieldEncount
from gdatamanger import GDataManager
from trainer_data_frame import TrainerDataFrame
from trainer_party import TrainerPartyNotebook

class TrainerFrame(ttk.Frame):
    def __init__(self, master, padding=1):
        super().__init__(master, padding=padding)
        menubar = Menu(master)
        master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Save", command=self.onSave)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)

        self.trainerTable = GDataManager.getTrainerTable()
        # self.volknerFill()
        self.currIdx = 1
        
        self.treeViewFrame = ttk.Frame(self, borderwidth=3, relief='groove')
        self.containerFrame = ttk.Frame(self)
        self.treeView = ttk.Treeview(self.treeViewFrame, show='tree')
        self.ybar = Scrollbar(self.treeViewFrame, orient=VERTICAL, command=self.treeView.yview)
        self.treeView.configure(yscrollcommand=self.ybar.set)
        self.treeView.heading('#0', text='Trainers', anchor='w')
        self.treeView.bind('<ButtonRelease-1>', self.onTreeSelect)
        self.treeView.bind('<KeyRelease>', self.onTreeSelect)
        for i, trainerData in enumerate(self.trainerTable["TrainerData"]):
            trainerName = GDataManager.getTrainerNameByLabel(trainerData.NameLabel.replace('DP_Trainers_Name_TR_', ''))
            nodeText = '{} - {}'.format(i, trainerName)
            self.treeView.insert('', 'end', text=nodeText, open=False)
        self.trainerDataFrame = TrainerDataFrame(self.containerFrame, self.trainerTable["TrainerData"][self.currIdx])
        self.trainerPartyNotebookFrame = ttk.Frame(self.containerFrame, borderwidth=3, relief='groove')
        self.trainerPartyNotebook = TrainerPartyNotebook(self.trainerPartyNotebookFrame, self.trainerTable["TrainerPoke"][self.currIdx])
        # GRID
        self.trainerDataFrame.pack(side=TOP, fill=X)
        self.trainerPartyNotebookFrame.pack(fill=X)

        # TreeView Frame Layout
        self.ybar.pack(side=RIGHT, fill=Y, expand=True)
        self.treeView.pack(fill=Y, expand=True)

        # 
        self.containerFrame.pack(side=RIGHT, fill=BOTH)
        self.treeViewFrame.pack(fill=Y, expand=True)

        # Trainer Party Notebook Frame Layout
        self.trainerPartyNotebook.pack(fill=BOTH, expand=True)
    
    # def volknerFill(self):
    #     for i in range(707, 2208, 1):
    #         fill_party = copy.copy(VOLKNER_PARTY_FILL)
    #         fill_party.ID = i
    #         self.trainerTable["TrainerData"].append(VOLKNER_TRAINER_FILL)
    #         self.trainerTable["TrainerPoke"].append(fill_party)

    def onSave(self):
        # Serialize updated TrainerParty into the map
        trainerData = self.trainerDataFrame.getTrainerData()
        trainerParty = self.trainerPartyNotebook.getTrainerParty()
        self.trainerTable["TrainerData"][self.currIdx] = trainerData
        self.trainerTable["TrainerPoke"][self.currIdx] = trainerParty
        fullTrainerTable = {}
        with open("AssetFolder/masterdatas_Export/TrainerTable.json", "r", encoding='utf-8') as ifobj:
            fullTrainerTable = rapidjson.load(ifobj)
        
        trainerData = list(map(lambda item: dataclasses.asdict(item), self.trainerTable["TrainerData"]))
        trainerPoke = list(map(lambda item: item.serialize(), self.trainerTable["TrainerPoke"]))
        fullTrainerTable["TrainerData"] = trainerData
        fullTrainerTable["TrainerPoke"] = trainerPoke

        with open("AssetFolder/masterdatas_Export/TrainerTable.json", "w", encoding='utf-8') as ofobj:
            rapidjson.dump(fullTrainerTable, ofobj, indent=4)

    def onTreeSelect(self, event):
        curItem = self.treeView.focus()
        newIdx = self.treeView.index(curItem)
        # Serialize updated TrainerParty into the map
        trainerData = self.trainerDataFrame.getTrainerData()
        trainerParty = self.trainerPartyNotebook.getTrainerParty()
        self.trainerTable["TrainerData"][self.currIdx] = trainerData
        self.trainerTable["TrainerPoke"][self.currIdx] = trainerParty
        # Set frames to use the new data
        self.currIdx = newIdx
        self.trainerDataFrame.updateTrainerData(self.trainerTable["TrainerData"][self.currIdx])
        self.trainerPartyNotebook.updateTrainerParty(self.trainerTable["TrainerPoke"][self.currIdx])
        