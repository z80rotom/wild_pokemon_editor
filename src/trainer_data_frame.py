
from tkinter import *
from tkinter import ttk
import copy

from core import TrainerData
from combobox import ItemOptionMenu, TrainerNameOptionMenu, TrainerMessageOptionMenu
from gdatamanger import GDataManager

class TrainerDataFrame(ttk.Frame):
    def __init__(self, master, trainerData, padding=10):
        super().__init__(master)
        self.trainerData = trainerData

        self.coreDataFrame = Frame(self, borderwidth=3, relief='groove')
        self.messageFrame = Frame(self, borderwidth=3, relief='groove')

        self.msgFieldPokeOne = StringVar(self, self.trainerData.MsgFieldPokeOne, "MsgFieldPokeOne")
        self.msgFieldBefore = StringVar(self, self.trainerData.MsgFieldBefore, "MsgFieldBefore")
        self.msgFieldRevenge = StringVar(self, self.trainerData.MsgFieldRevenge, "MsgFieldRevenge")
        self.msgFieldAfter = StringVar(self, self.trainerData.MsgFieldAfter, "MsgFieldAfter")

        
        self.msgFightFirstDamage = StringVar(self, self.trainerData.MsgBattle[0], "MsgFightFirstDamage")
        self.msgFightPokeLast = StringVar(self, self.trainerData.MsgBattle[2], "MsgFightPokeLast")
        self.msgFightPokeLastHalfHp = StringVar(self, self.trainerData.MsgBattle[4], "MsgFightPokeLastHalfHp")
        self.msgFightLose = StringVar(self, self.trainerData.MsgBattle[6], "msgFightLose")

        self.msgs = [{
            "name" : "PokeOne",
            "stringVar" : self.msgFieldPokeOne
        }, {
            "name" : "Before",
            "stringVar" :  self.msgFieldBefore
        }, {
            "name" : "Revenge",
            "stringVar" : self.msgFieldRevenge
        }, {
            "name" : "After",
            "stringVar" : self.msgFieldAfter
        }, {
            "name" : "FightDamage",
            "stringVar" : self.msgFightFirstDamage
        }, {
            "name" : "PokeLast",
            "stringVar" : self.msgFightPokeLast
        }, {
            "name" : "PokeLastHalfHp",
            "stringVar" : self.msgFightPokeLastHalfHp
        }, {
            "name" : "Lose",
            "stringVar" : self.msgFightLose
        }]

        self.typeID = StringVar(self, self.trainerData.TypeID, "TypeID")
        self.trainerName = StringVar(self, self.trainerData.NameLabel.replace('DP_Trainers_Name_TR_', ''), "NameLabel")
        self.hpRecoverFlag = IntVar(self, self.trainerData.HpRecoverFlag, "HpRecoverFlag")
        self.bossBattleFlag = IntVar(self, self.trainerData.SeqBattle == ['ee630'], "SeqBattle")
        self.gold = StringVar(self, self.trainerData.Gold, "Gold")
        self.aiBit = StringVar(self, self.trainerData.AIBit, "AIBit")
        self.colorID = StringVar(self, self.trainerData.ColorID, "ColorID")
        self.fightType = StringVar(self, self.trainerData.FightType, "FightType")
        self.arenaID = StringVar(self, self.trainerData.ArenaID, "ArenaID")
        self.effectID = StringVar(self, self.trainerData.EffectID, "EffectID")

        # Item Group
        self.useItem1 = StringVar(self, GDataManager.getItemById(self.trainerData.UseItem1), "UseItem1")
        self.useItem2 = StringVar(self, GDataManager.getItemById(self.trainerData.UseItem2), "UseItem2")
        self.useItem3 = StringVar(self, GDataManager.getItemById(self.trainerData.UseItem3), "UseItem3")
        self.useItem4 = StringVar(self, GDataManager.getItemById(self.trainerData.UseItem4), "UseItem4")
        self.giftItem = StringVar(self, GDataManager.getItemById(self.trainerData.GiftItem), "GiftItem")
        self.useItems = [{
            "name" : "Use Item 1",
            "stringVar" : self.useItem1
        }, {
            "name" : "Use Item 2",
            "stringVar" : self.useItem2
        }, {
            "name" : "Use Item 3",
            "stringVar" : self.useItem3
        }, {
            "name" : "Use Item 4",
            "stringVar" : self.useItem4
        }, {
            "name" : "Gift Item",
            "stringVar" : self.giftItem
        }]

        self.spinboxes = [{
            "name" : "AIBit",
            "stringVar" : self.aiBit
        }, {
            "name" : "Color ID",
            "stringVar" : self.colorID
        }, {
            "name" : "Fight Type",
            "stringVar" : self.fightType
        }, {
            "name" : "Arena ID",
            "stringVar" : self.arenaID
        }, {
            "name" : "Effect ID",
            "stringVar" : self.effectID
        }]

        self.typeIDLabel = ttk.Label(self.coreDataFrame, text="Type ID")
        self.typeIDSpinbox = ttk.Spinbox(self.coreDataFrame, textvariable=self.typeID)
        self.nameLabel = ttk.Label(self.coreDataFrame, text="Name")
        self.nameOptionMenu = TrainerNameOptionMenu(self.coreDataFrame, self.trainerName)

        self.hpRecoverFlagLabel = ttk.Label(self.coreDataFrame, text="HP Recover Flag")
        self.hpRecoverFlagCheckbox = Checkbutton(self.coreDataFrame, variable=self.hpRecoverFlag)
        self.bossBattleFlagLabel = ttk.Label(self.coreDataFrame, text="Boss Battle")
        self.bossBattleFlagCheckbox = Checkbutton(self.coreDataFrame, variable=self.bossBattleFlag)
        self.goldLabel = ttk.Label(self.coreDataFrame, text="Gold")
        self.goldSpinBox = ttk.Spinbox(self.coreDataFrame, textvariable=self.gold)

        for i, spinbox in enumerate(self.spinboxes):
            name = spinbox["name"]
            stringVar = spinbox["stringVar"]
            label = ttk.Label(self.coreDataFrame, text=name)
            spinbox = ttk.Spinbox(self.coreDataFrame, textvariable=stringVar)
            label.grid(column=0, row=i+1, padx=3, pady=3)
            spinbox.grid(column=1, row=i+1, padx=3, pady=3)

        for i, useItem in enumerate(self.useItems):
            name = useItem["name"]
            stringVar = useItem["stringVar"]
            label = ttk.Label(self.coreDataFrame, text=name)
            itemOptionMenu = ItemOptionMenu(self.coreDataFrame, stringVar)
            label.grid(column=2, row=i+2, padx=3, pady=3)
            itemOptionMenu.grid(column=3, row=i+2, padx=3, pady=3)

        for i, msg in enumerate(self.msgs):
            name = msg["name"]
            stringVar = msg["stringVar"]
            msgLabel = ttk.Label(self.messageFrame, text=name)
            msgOptionMenu = TrainerMessageOptionMenu(self.messageFrame, stringVar)     
            msgLabel.grid(column=0, row=i, padx=3, pady=3)
            msgOptionMenu.grid(column=1, row=i, padx=3, pady=3)
        self.messageFrame.grid_columnconfigure(0, weight=1, uniform="foo")
        self.messageFrame.grid_columnconfigure(1, weight=3, uniform="foo")

        # Row 0
        self.typeIDLabel.grid(column=0, row=0, padx=3, pady=3)
        self.typeIDSpinbox.grid(column=1, row=0, padx=3, pady=3)
        self.nameLabel.grid(column=2, row=0, padx=3, pady=3)
        self.nameOptionMenu.grid(column=3, row=0, padx=3, pady=3)

        # Row 1
        self.goldLabel.grid(column=2, row=1, padx=3, pady=3)
        self.goldSpinBox.grid(column=3, row=1, padx=3, pady=3)

        # Row 8
        self.hpRecoverFlagLabel.grid(column=0, row=8, padx=3, pady=3)
        self.hpRecoverFlagCheckbox.grid(column=1, row=8, padx=3, pady=3, sticky = 'w')
        self.bossBattleFlagLabel.grid(column=2, row=8, padx=3, pady=3)
        self.bossBattleFlagCheckbox.grid(column=3, row=8, padx=3, pady=3, sticky = 'w')

        # Internal Frames
        self.coreDataFrame.grid(column=0, row=0, padx=3, pady=3, columnspan=8)
        self.messageFrame.grid(column=8, row=0, padx=3, pady=3, columnspan=8)

    def getTrainerData(self):
        # self.trainerName.set(GDataManager.getTrainerNameByLabel(self.trainerData.NameLabel))
        msgBattle = []
        seqBattle = []
        if self.bossBattleFlag.get():
            seqBattle = ['ee630']
        
        if self.msgFightFirstDamage.get():
            msgBattle.append(self.msgFightFirstDamage.get())
            msgBattle.append('bk002')
        else:
            msgBattle.extend(['', ''])
        
        if self.msgFightPokeLast.get():
            msgBattle.append(self.msgFightPokeLast.get())
            msgBattle.append('bk002')
        else:
            msgBattle.extend(['', ''])
        
        if self.msgFightPokeLastHalfHp.get():
            msgBattle.append(self.msgFightPokeLastHalfHp.get())
            msgBattle.append('bk002')
        else:
            msgBattle.extend(['', ''])
                
        if self.msgFightLose.get():
            msgBattle.append(self.msgFightLose.get())
        else:
            msgBattle.append('')
                
        msgBattle.append('ee501')

        trainerData = {
            "NameLabel" : 'DP_Trainers_Name_TR_{}'.format(self.trainerName.get()),
            "TypeID" : int(self.typeID.get()),
            "HpRecoverFlag" : int(self.hpRecoverFlag.get()),
            "Gold" : int(self.gold.get()),
            "AIBit" : int(self.aiBit.get()),
            "ColorID" : int(self.colorID.get()),
            "FightType" : int(self.fightType.get()),
            "ArenaID" : int(self.arenaID.get()),
            "EffectID" : int(self.effectID.get()),
            "MsgFieldPokeOne" : self.msgFieldPokeOne.get(),
            "MsgFieldBefore" : self.msgFieldBefore.get(),
            "MsgFieldRevenge" : self.msgFieldRevenge.get(),
            "MsgFieldAfter" : self.msgFieldAfter.get(),
            "MsgBattle" : msgBattle,
            "SeqBattle" : seqBattle,
            "UseItem1" : GDataManager.getItemList().index(self.useItem1.get()),
            "UseItem2" : GDataManager.getItemList().index(self.useItem2.get()),
            "UseItem3" : GDataManager.getItemList().index(self.useItem3.get()),
            "UseItem4" : GDataManager.getItemList().index(self.useItem4.get()),
            "GiftItem" : GDataManager.getItemList().index(self.giftItem.get()),
        }

        return TrainerData(**trainerData)

    def updateTrainerData(self, trainerData):
        self.trainerData = trainerData
        self.msgFieldPokeOne.set(self.trainerData.MsgFieldPokeOne)
        self.msgFieldBefore.set(self.trainerData.MsgFieldBefore)
        self.msgFieldRevenge.set(self.trainerData.MsgFieldRevenge)
        self.msgFieldAfter.set(self.trainerData.MsgFieldAfter)

        self.msgFightFirstDamage.set(self.trainerData.MsgBattle[0])
        self.msgFightPokeLast.set(self.trainerData.MsgBattle[2])
        self.msgFightPokeLastHalfHp.set(self.trainerData.MsgBattle[4])
        self.msgFightLose.set(self.trainerData.MsgBattle[6])

        self.typeID.set(self.trainerData.TypeID)
        self.trainerName.set(self.trainerData.NameLabel.replace('DP_Trainers_Name_TR_', ''))
        self.hpRecoverFlag.set(self.trainerData.HpRecoverFlag)
        self.bossBattleFlag.set(self.trainerData.SeqBattle == ['ee630'])
        self.gold.set(self.trainerData.Gold)
        self.aiBit.set(self.trainerData.AIBit)
        self.colorID.set(self.trainerData.ColorID)
        self.fightType.set(self.trainerData.FightType)
        self.arenaID.set(self.trainerData.ArenaID)
        self.effectID.set(self.trainerData.EffectID)

        # Item Group
        self.useItem1.set(GDataManager.getItemById(self.trainerData.UseItem1))
        self.useItem2.set(GDataManager.getItemById(self.trainerData.UseItem2))
        self.useItem3.set(GDataManager.getItemById(self.trainerData.UseItem3))
        self.useItem4.set(GDataManager.getItemById(self.trainerData.UseItem4))
        self.giftItem.set(GDataManager.getItemById(self.trainerData.GiftItem))
