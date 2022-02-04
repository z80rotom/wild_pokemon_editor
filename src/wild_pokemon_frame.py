from tkinter import *
from tkinter import ttk
from tokenize import String
from typing import List
import rapidjson
import dataclasses
import copy
from combobox import SpeciesOptionMenu

from core import EncEntry, FieldEncount, FieldEncountTable
from gdatamanger import GDataManager
from spinbox import LevelSpinbox, EncRateSpinBox
from time_encounters import TimeEncountersNotebook
from zoneid import ZoneID

class EncounterRateFrame(ttk.LabelFrame):
    def __init__(self, root, fieldEncount: FieldEncount, padding=3):
        super().__init__(root, padding=padding, borderwidth=3, relief='sunken', text="Encounter Rates")
        self.encRate_gr = StringVar(self, fieldEncount.encRate_gr)
        self.encRate_wat = StringVar(self, fieldEncount.encRate_wat)
        self.encRate_turi_boro = StringVar(self, fieldEncount.encRate_turi_boro)
        self.encRate_turi_ii = StringVar(self, fieldEncount.encRate_turi_ii)
        self.encRate_sugoi = StringVar(self, fieldEncount.encRate_sugoi)

        self.grLabel = ttk.Label(self, text="Ground")
        self.watLabel = ttk.Label(self, text="Water")
        self.turi_boroLabel = ttk.Label(self, text="Old Rod")
        self.turi_iiLabel = ttk.Label(self, text="Good Rod")
        self.sugoiLabel = ttk.Label(self, text="Super Rod")

        self.grSpinbox = EncRateSpinBox(self, self.encRate_gr)
        self.watSpinbox = EncRateSpinBox(self, self.encRate_wat)
        self.turi_boroSpinbox = EncRateSpinBox(self, self.encRate_turi_boro)
        self.turi_iiSpinbox = EncRateSpinBox(self, self.encRate_turi_ii)
        self.sugoiSpinbox = EncRateSpinBox(self, self.encRate_sugoi)

        self.grLabel.grid(column=0, row=0, padx=3, pady=3)
        self.watLabel.grid(column=0, row=1, padx=3, pady=3)
        self.turi_boroLabel.grid(column=0, row=2, padx=3, pady=3)
        self.turi_iiLabel.grid(column=0, row=3, padx=3, pady=3)
        self.sugoiLabel.grid(column=0, row=4, padx=3, pady=3)
        self.grSpinbox.grid(column=1, row=0, padx=3, pady=3)
        self.watSpinbox.grid(column=1, row=1, padx=3, pady=3)
        self.turi_boroSpinbox.grid(column=1, row=2, padx=3, pady=3)
        self.turi_iiSpinbox.grid(column=1, row=3, padx=3, pady=3)
        self.sugoiSpinbox.grid(column=1, row=4, padx=3, pady=3)

    def getData(self):
        return {
            "encRate_gr" : self.encRate_gr.get(),
            "encRate_wat" : self.encRate_wat.get(),
            "encRate_turi_boro" : self.encRate_turi_boro.get(),
            "encRate_turi_ii" : self.encRate_turi_ii.get(),
            "encRate_sugoi" : self.encRate_sugoi.get()
        }
    
    def updateData(self, fieldEncount: FieldEncount):
        self.encRate_gr.set(fieldEncount.encRate_gr)
        self.encRate_wat.set(fieldEncount.encRate_wat)
        self.encRate_turi_boro.set(fieldEncount.encRate_turi_boro)
        self.encRate_turi_ii.set(fieldEncount.encRate_turi_ii)
        self.encRate_sugoi.set(fieldEncount.encRate_sugoi)        

class FieldEncounterFrame:
    def populate(self, encounters: List[EncEntry]):
        self.speciesLabel = ttk.Label(self, text="Species")
        self.minLvlLabel = ttk.Label(self, text="Min Lvl")
        self.maxLvlLabel = ttk.Label(self, text="Max Lvl")

        self.speciesLabel.grid(column=1, row=0, padx=3, pady=3)
        self.minLvlLabel.grid(column=2, row=0, padx=3, pady=3)
        self.maxLvlLabel.grid(column=3, row=0, padx=3, pady=3)

        self.vars = []
        for i, enc in enumerate(encounters):
            species = StringVar(self, GDataManager.getPokemonById(enc.monsNo))
            minLvl = StringVar(self, enc.minlv)
            maxLvl = StringVar(self, enc.maxlv)
            self.vars.append({
                "species" : species,
                "minLvl" : minLvl,
                "maxLvl" : maxLvl
            })
            
            speciesOptionMenu = SpeciesOptionMenu(self, species)
            minLvlSpinBox = LevelSpinbox(self, minLvl)
            maxLvlSpinBox = LevelSpinbox(self, maxLvl)
            speciesOptionMenu.set(GDataManager.getPokemonById(enc.monsNo))
            minLvlSpinBox.set(str(enc.minlv))
            maxLvlSpinBox.set(str(enc.maxlv))
            
            speciesOptionMenu.grid(column=1, row=i+1, padx=3, pady=3)
            minLvlSpinBox.grid(column=2, row=i+1, padx=3, pady=3)
            maxLvlSpinBox.grid(column=3, row=i+1, padx=3, pady=3)

    def updateData(self, encounters: List[EncEntry]):
        for i, enc in enumerate(encounters):
            self.vars[i]["species"].set(GDataManager.getPokemonById(enc.monsNo))
            self.vars[i]["minLvl"].set(enc.minlv)
            self.vars[i]["maxLvl"].set(enc.maxlv)

    def getData(self):
        encounters = []
        for var in self.vars:
            encounters.append(EncEntry(**{
                "maxlv" : int(var["maxLvl"].get()),
                "minlv" : int(var["minLvl"].get()),
                "monsNo" : GDataManager.getPokemonList().index(var["species"].get())
            }))
        return encounters

class PokeradarFrame(ttk.LabelFrame, FieldEncounterFrame):
    def __init__(self, root, swayGrass: List[EncEntry], padding=3):
        super().__init__(root, padding=padding, borderwidth=3, relief='sunken', text="Pokeradar")
        self.populate(swayGrass)

class RodEncounterFrame(ttk.Frame, FieldEncounterFrame):
    def __init__(self, root, rod_encounters: List[EncEntry], padding=3):
        super().__init__(root, padding=padding)
        self.populate(rod_encounters)

class WaterMonsFrame(ttk.LabelFrame, FieldEncounterFrame):
    def __init__(self, root, water_mons: List[EncEntry], padding=3):
        super().__init__(root, padding=padding, borderwidth=3, relief='sunken', text="Surf Mons")
        self.populate(water_mons)

class RodEncountersNotebook(ttk.Notebook):
    def __init__(self, master, fieldencount: FieldEncount, padding=3):
        super().__init__(master, padding=padding)

        self.old_rod = RodEncounterFrame(self, fieldencount.boro_mons)
        self.good_rod = RodEncounterFrame(self, fieldencount.ii_mons)
        self.super_rod = RodEncounterFrame(self, fieldencount.sugoi_mons)

        self.add(self.old_rod, text="Old Rod")
        self.add(self.good_rod, text="Good Rod")
        self.add(self.super_rod, text="Super Rod")
    
    def updateData(self, fieldencount: FieldEncount):
        self.old_rod.updateData(fieldencount.boro_mons)
        self.good_rod.updateData(fieldencount.ii_mons)
        self.super_rod.updateData(fieldencount.sugoi_mons)

    def getData(self):
        return {
            "boro_mons" : self.old_rod.getData(),
            "ii_mons" : self.good_rod.getData(),
            "sugoi_mons" : self.super_rod.getData()
        }

class WildPokemonFrame(ttk.Frame):
    def __init__(self, master, fieldEncount: FieldEncount, padding=1):
        super().__init__(master, padding=padding)
        self.fieldEncount = fieldEncount
        self.container_frame_left = ttk.Frame(self)
        self.container_frame = ttk.Frame(self)

        self.time_encounters_notebook = TimeEncountersNotebook(self.container_frame_left, fieldEncount)
        self.enc_rate_frame = EncounterRateFrame(self.container_frame_left, fieldEncount)

        self.swayGrass_frame = PokeradarFrame(self.container_frame, fieldEncount.swayGrass)
        self.water_mons_frame = WaterMonsFrame(self.container_frame, fieldEncount.water_mons)
        self.rod_encounters_notebook = RodEncountersNotebook(self.container_frame, fieldEncount)

        self.time_encounters_notebook.pack()
        self.enc_rate_frame.pack()

        self.swayGrass_frame.pack()
        self.water_mons_frame.pack()
        self.rod_encounters_notebook.pack()

        self.container_frame_left.grid(row=0, column=0, padx=3, pady=3)
        self.container_frame.grid(row=0, column=1, padx=3, pady=3)
    
    def getData(self):
        fieldEncount = {
            "zoneID" : self.fieldEncount.zoneID,
            "Nazo" : self.fieldEncount.Nazo,
            "FormProb" : self.fieldEncount.FormProb,
            "AnnoonTable" : self.fieldEncount.AnnoonTable,
            'gbaRuby' : self.fieldEncount.gbaRuby, 
            'gbaSapp' : self.fieldEncount.gbaSapp, 
            'gbaEme' : self.fieldEncount.gbaEme, 
            'gbaFire' : self.fieldEncount.gbaFire,
            'gbaLeaf' : self.fieldEncount.gbaLeaf
        }
        fieldEncount.update(self.time_encounters_notebook.getData())
        fieldEncount.update(self.enc_rate_frame.getData())
        fieldEncount["swayGrass"] = self.swayGrass_frame.getData()
        fieldEncount["water_mons"] = self.water_mons_frame.getData()
        fieldEncount.update(self.rod_encounters_notebook.getData())
        return FieldEncount(**fieldEncount)
    
    def updateData(self, fieldEncount: FieldEncount):
        self.fieldEncount = fieldEncount
        self.time_encounters_notebook.updateData(fieldEncount)
        self.enc_rate_frame.updateData(fieldEncount)
        self.swayGrass_frame.updateData(fieldEncount.swayGrass)
        self.water_mons_frame.updateData(fieldEncount.water_mons)
        self.rod_encounters_notebook.updateData(fieldEncount)

class WildPokemonEditorFrame(ttk.Frame):
    def __init__(self, master, padding=1):
        super().__init__(master, padding=padding)
        menubar = Menu(master)
        master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Save", command=self.onSave)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
    
        self.fieldEncountTable = GDataManager.getFieldEncountTable()
        self.currIdx = 1
        
        self.treeViewFrame = ttk.Frame(self, borderwidth=3, relief='groove')
        self.containerFrame = ttk.Frame(self)
        self.treeView = ttk.Treeview(self.treeViewFrame, show='tree')
        self.ybar = Scrollbar(self.treeViewFrame, orient=VERTICAL, command=self.treeView.yview)
        self.treeView.configure(yscrollcommand=self.ybar.set)
        self.treeView.heading('#0', text='Zones', anchor='w')
        self.treeView.bind('<ButtonRelease-1>', self.onTreeSelect)
        self.treeView.bind('<KeyRelease>', self.onTreeSelect)
        for i, fieldEncount in enumerate(self.fieldEncountTable.table):
            zoneID = ZoneID(fieldEncount.zoneID)
            # if zoneID == zoneID.UNKNOWN:
            #     continue
            nodeText = '{} - {}'.format(i, zoneID.name)
            self.treeView.insert('', 'end', text=nodeText, open=False)
        # GRID
        self.wildPokemonFrame = WildPokemonFrame(self, self.fieldEncountTable.table[self.currIdx])

        # TreeView Frame Layout
        self.ybar.pack(side=RIGHT, fill=Y, expand=True)
        self.treeView.pack(fill=Y, expand=True)

        # 
        self.wildPokemonFrame.pack(side=RIGHT, fill=BOTH)
        self.treeViewFrame.pack(fill=Y, expand=True)
   
    def onSave(self):
        with open("AssetFolder/gamesettings_Export/FieldEncountTable_d.json", "w", encoding='utf-8') as ofobj:
            rapidjson.dump(FieldEncountTable.Schema().dump(self.fieldEncountTable), ofobj, indent=4)

    def onTreeSelect(self, event):
        curItem = self.treeView.focus()
        newIdx = self.treeView.index(curItem)
        # Serialize updated TrainerParty into the map
        fieldEncount = self.wildPokemonFrame.getData()
        self.fieldEncountTable.table[self.currIdx] = fieldEncount
        # trainerData = self.trainerDataFrame.getTrainerData()
        # trainerParty = self.trainerPartyNotebook.getTrainerParty()
        # self.trainerTable["TrainerData"][self.currIdx] = trainerData
        # self.trainerTable["TrainerPoke"][self.currIdx] = trainerParty
        # Set frames to use the new data
        self.currIdx = newIdx
        self.wildPokemonFrame.updateData(self.fieldEncountTable.table[self.currIdx])
        # self.trainerDataFrame.updateTrainerData(self.trainerTable["TrainerData"][self.currIdx])
        # self.trainerPartyNotebook.updateTrainerParty(self.trainerTable["TrainerPoke"][self.currIdx])
        