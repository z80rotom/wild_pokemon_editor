from tkinter import *
from tkinter import ttk
import copy

from core import TrainerPokemon
from combobox import SpeciesOptionMenu, SexOptionMenu, ItemOptionMenu, AbilityOptionMenu, NatureOptionMenu, MoveOptionMenu
from gdatamanger import GDataManager
from spinbox import LevelSpinbox, IVSpinbox, EVSpinbox

class TrainerPokemonFrame(ttk.Frame):
    def __init__(self, root, pokeIndex, trainerPokemon, padding=3):
        super().__init__(root, padding=padding)
        self.pokeIndex = pokeIndex
        self.trainerPokemon = trainerPokemon
        self.effortHp = StringVar(self, self.trainerPokemon.EffortHp, "P{}EffortHp".format(self.pokeIndex))
        self.effortAtk = StringVar(self, self.trainerPokemon.EffortAtk, "P{}EffortAtk".format(self.pokeIndex))
        self.effortDef = StringVar(self, self.trainerPokemon.EffortDef, "P{}EffortDef".format(self.pokeIndex))
        self.effortSpAtk = StringVar(self, self.trainerPokemon.EffortSpAtk, "P{}EffortSpAtk".format(self.pokeIndex))
        self.effortSpDef = StringVar(self, self.trainerPokemon.EffortSpDef, "P{}EffortSpDef".format(self.pokeIndex))
        self.effortAgi = StringVar(self, self.trainerPokemon.EffortAgi, "P{}EffortAgi".format(self.pokeIndex))
        # self.effortHp.trace_add("write")

        self.evs = [{
            "name" : "Hp",
            "stringVar" : self.effortHp
        }, {
            "name" : "Atk",
            "stringVar" : self.effortAtk
        }, {
            "name" : "Def",
            "stringVar" : self.effortDef
        }, {
            "name" : "SpAtk",
            "stringVar" : self.effortSpAtk
        }, {
            "name" : "SpDef",
            "stringVar" : self.effortSpDef
        }, {
            "name" : "Agi",
            "stringVar" : self.effortAgi
        }]

        self.talentHp = StringVar(self, self.trainerPokemon.TalentHp, "P{}TalentHp".format(self.pokeIndex))
        self.talentAtk = StringVar(self, self.trainerPokemon.TalentAtk, "P{}TalentAtk".format(self.pokeIndex))
        self.talentDef = StringVar(self, self.trainerPokemon.TalentDef, "P{}TalentDef".format(self.pokeIndex))
        self.talentSpAtk = StringVar(self, self.trainerPokemon.TalentSpAtk, "P{}TalentSpAtk".format(self.pokeIndex))
        self.talentSpDef = StringVar(self, self.trainerPokemon.TalentSpDef, "P{}TalentSpDef".format(self.pokeIndex))
        self.talentAgi = StringVar(self, self.trainerPokemon.TalentAgi, "P{}TalentAgi".format(self.pokeIndex))
        self.ivs = [{
            "name" : "Hp",
            "stringVar" : self.talentHp
        }, {
            "name" : "Atk",
            "stringVar" : self.talentAtk
        }, {
            "name" : "Def",
            "stringVar" : self.talentDef
        }, {
            "name" : "SpAtk",
            "stringVar" : self.talentSpAtk
        }, {
            "name" : "SpDef",
            "stringVar" : self.talentSpDef
        }, {
            "name" : "Agi",
            "stringVar" : self.talentAgi
        }]


        self.move1 = StringVar(self, GDataManager.getMoveById(self.trainerPokemon.Waza1), "P{}Waza1".format(self.pokeIndex))
        self.move2 = StringVar(self, GDataManager.getMoveById(self.trainerPokemon.Waza2), "P{}Waza2".format(self.pokeIndex))
        self.move3 = StringVar(self, GDataManager.getMoveById(self.trainerPokemon.Waza3), "P{}Waza3".format(self.pokeIndex))
        self.move4 = StringVar(self, GDataManager.getMoveById(self.trainerPokemon.Waza4), "P{}Waza4".format(self.pokeIndex))
        self.moves = [[{
            "name" : "Move 1",
            "stringVar" : self.move1
        }, {
            "name" : "Move 2",
            "stringVar" : self.move2
        }], [{
            "name" : "Move 3",
            "stringVar" : self.move3
        }, {
            "name" : "Move 4",
            "stringVar" : self.move4
        }]]

        self.miscFrame = ttk.Frame(self)
        # Row 0
        self.species = StringVar(self, GDataManager.getPokemonById(self.trainerPokemon.MonsNo), "P{}MonsNo".format(self.pokeIndex))
        self.formNo = StringVar(self, self.trainerPokemon.FormNo, "P{}FormNo".format(self.pokeIndex))
        self.speciesLabel = ttk.Label(self.miscFrame, text="Species")
        self.formNoLabel = ttk.Label(self.miscFrame, text="Form No.")
        self.speciesOptionMenu = SpeciesOptionMenu(self.miscFrame, self.species)
        self.formNoSpinBox = ttk.Spinbox(self.miscFrame, textvariable=self.formNo)

        # Row 1
        self.isRare = IntVar(self, self.trainerPokemon.IsRare, "P{}IsRare".format(self.pokeIndex))
        self.level = StringVar(self, self.trainerPokemon.Level, "P{}Level".format(self.pokeIndex))
        self.isRareLabel = ttk.Label(self.miscFrame, text="Shiny")
        self.levelLabel = ttk.Label(self.miscFrame, text="Level")
        self.isRareCheckbox = Checkbutton(self.miscFrame, variable=self.isRare)
        self.levelSpinBox = LevelSpinbox(self.miscFrame, self.level)

        # Row 2
        self.sex = StringVar(self, SexOptionMenu.SEX_LIST[self.trainerPokemon.Sex], "P{}Sex".format(self.pokeIndex))
        self.item = StringVar(self, GDataManager.getItemById(self.trainerPokemon.Item), "P{}Item".format(self.pokeIndex))
        self.sexLabel = ttk.Label(self.miscFrame, text="Sex")
        self.itemLabel = ttk.Label(self.miscFrame, text="Item")
        self.sexOptionMenu = SexOptionMenu(self.miscFrame, self.sex)
        self.itemOptionMenu = ItemOptionMenu(self.miscFrame, self.item)

        # Row 3
        self.ability = StringVar(self, GDataManager.getAbilityById(self.trainerPokemon.Tokusei), "P{}Tokusei".format(self.pokeIndex))
        self.nature = StringVar(self, GDataManager.getNatureById(self.trainerPokemon.Seikaku), "P{}Seikaku".format(self.pokeIndex))
        self.abilityLabel = ttk.Label(self.miscFrame, text="Ability")
        self.natureLabel = ttk.Label(self.miscFrame, text="Nature")
        self.abilityOptionMenu = AbilityOptionMenu(self.miscFrame, self.ability)
        self.natureOptionMenu = NatureOptionMenu(self.miscFrame, self.nature)

        # Row 4
        self.ball = StringVar(self, self.trainerPokemon.Ball, "P{}Ball".format(self.pokeIndex))
        self.seal = StringVar(self, self.trainerPokemon.Seal, "P{}Seal".format(self.pokeIndex))
        self.ballLabel = ttk.Label(self.miscFrame, text="Ball")
        self.sealLabel = ttk.Label(self.miscFrame, text="Seal")
        self.ballSpinBox = ttk.Spinbox(self.miscFrame, textvariable=self.ball)
        self.sealSpinBox = ttk.Spinbox(self.miscFrame, textvariable=self.seal)

        # Row 0
        self.speciesLabel.grid(column=0, row=0, padx=3, pady=3)
        self.speciesOptionMenu.grid(column=1, row=0, padx=3, pady=3)
        self.formNoLabel.grid(column=2, row=0, padx=3, pady=3)
        self.formNoSpinBox.grid(column=3, row=0, padx=3, pady=3)

        # Row 1
        self.isRareLabel.grid(column=0, row=1, padx=3, pady=3)
        self.isRareCheckbox.grid(column=1, row=1, padx=3, pady=3, sticky = 'w')
        self.levelLabel.grid(column=2, row=1, padx=3, pady=3)
        self.levelSpinBox.grid(column=3, row=1, padx=3, pady=3)

        # Row 2 
        self.sexLabel.grid(column=0, row=2, padx=3, pady=3)
        self.sexOptionMenu.grid(column=1, row=2, padx=3, pady=3)
        self.itemLabel.grid(column=2, row=2, padx=3, pady=3)
        self.itemOptionMenu.grid(column=3, row=2, padx=3, pady=3)

        # Row 3
        self.abilityLabel.grid(column=0, row=3, padx=3, pady=3)
        self.abilityOptionMenu.grid(column=1, row=3, padx=3, pady=3)
        self.natureLabel.grid(column=2, row=3, padx=3, pady=3)
        self.natureOptionMenu.grid(column=3, row=3, padx=3, pady=3)

        # Row 4
        self.ballLabel.grid(column=0, row=4, padx=3, pady=3)
        self.ballSpinBox.grid(column=1, row=4, padx=3, pady=3)
        self.sealLabel.grid(column=2, row=4, padx=3, pady=3)
        self.sealSpinBox.grid(column=3, row=4, padx=3, pady=3)

        self.miscFrame.grid(column=0, row=0, padx=3, pady=3, rowspan=5)

        # self.miscFrame = ttk.Frame(self)
        self.movesFrameLabel = ttk.Label(self, text="Moves")
        self.movesFrame = ttk.Frame(self, borderwidth=3, relief='sunken')
        for i, row in enumerate(self.moves):
            for j, col in enumerate(row):
                moveOptionMenu = MoveOptionMenu(self.movesFrame, col["stringVar"], 
                            validate="focusout", validatecommand=lambda: self.validateMoveOption(col["stringVar"]))
                moveOptionMenu.grid(column=j, row=i)
                 
        self.movesFrameLabel.grid(column=0, row=5, padx=3, pady=3, rowspan=1)
        self.movesFrame.grid(column=0, row=6, padx=3, pady=3, rowspan=2)
        self.grid_rowconfigure(6, weight=2, uniform="foo")

        self.evFrameLabel = ttk.Label(self, text="Effort Values")
        self.evFrame = ttk.Frame(self, borderwidth=3, relief='sunken')
        for i, ev in enumerate(self.evs):
            name = ev["name"]
            stringVar = ev["stringVar"]
            label = ttk.Label(self.evFrame, text=name)
            spinBox = EVSpinbox(self.evFrame, stringVar)
            label.grid(column=0, row=i, padx=3, pady=3)
            spinBox.grid(column=1, row=i, padx=3, pady=3)
        self.evFrameLabel.grid(column=1, row=0, padx=3, pady=3, rowspan=1)
        self.evFrame.grid(column=1, row=1, padx=3, pady=3, rowspan=7)


        self.ivFrameLabel = ttk.Label(self, text="Individual Values")
        self.ivFrame = ttk.Frame(self, borderwidth=3, relief='sunken')
        for i, iv in enumerate(self.ivs):
            name = iv["name"]
            stringVar = iv["stringVar"]
            label = ttk.Label(self.ivFrame, text=name)
            spinBox = IVSpinbox(self.ivFrame, stringVar)
            label.grid(column=0, row=i, padx=3, pady=3)
            spinBox.grid(column=1, row=i, padx=3, pady=3)
        # self.ivFrame.pack()
        self.ivFrameLabel.grid(column=2, row=0, padx=3, pady=3, rowspan=1)
        self.ivFrame.grid(column=2, row=1, padx=3, pady=3, rowspan=7)

        self.pack()

    def updateTrainerPokemon(self, trainerPokemon):
        self.trainerPokemon = trainerPokemon
        self.effortHp.set(self.trainerPokemon.EffortHp)
        self.effortAtk.set(self.trainerPokemon.EffortAtk)
        self.effortDef.set(self.trainerPokemon.EffortDef)
        self.effortSpAtk.set(self.trainerPokemon.EffortSpAtk)
        self.effortSpDef.set(self.trainerPokemon.EffortSpDef)
        self.effortAgi.set(self.trainerPokemon.EffortAgi)

        self.talentHp.set(self.trainerPokemon.TalentHp)
        self.talentAtk.set(self.trainerPokemon.TalentAtk)
        self.talentDef.set(self.trainerPokemon.TalentDef)
        self.talentSpAtk.set(self.trainerPokemon.TalentSpAtk)
        self.talentSpDef.set(self.trainerPokemon.TalentSpDef)
        self.talentAgi.set(self.trainerPokemon.TalentAgi)

        self.move1.set(GDataManager.getMoveById(self.trainerPokemon.Waza1))
        self.move2.set(GDataManager.getMoveById(self.trainerPokemon.Waza2))
        self.move3.set(GDataManager.getMoveById(self.trainerPokemon.Waza3))
        self.move4.set(GDataManager.getMoveById(self.trainerPokemon.Waza4))

        self.species.set(GDataManager.getPokemonById(self.trainerPokemon.MonsNo))
        self.formNo.set(self.trainerPokemon.FormNo)
        self.isRare.set(self.trainerPokemon.IsRare)
        self.level.set(self.trainerPokemon.Level)
        self.sex.set(SexOptionMenu.SEX_LIST[self.trainerPokemon.Sex])
        self.item.set(GDataManager.getItemById(self.trainerPokemon.Item))
        self.ability.set(GDataManager.getAbilityById(self.trainerPokemon.Tokusei))
        self.nature.set(GDataManager.getNatureById(self.trainerPokemon.Seikaku))
        self.ball.set(self.trainerPokemon.Ball)
        self.seal.set(self.trainerPokemon.Seal)

    def getTrainerPokemon(self):
        trainerPokemon = {
            "EffortHp" : int(self.effortHp.get()),
            "EffortAtk" : int(self.effortAtk.get()),
            "EffortDef" : int(self.effortDef.get()),
            "EffortSpAtk" : int(self.effortSpAtk.get()),
            "EffortSpDef" : int(self.effortSpDef.get()),
            "EffortAgi" : int(self.effortAgi.get()),

            "TalentHp" : int(self.talentHp.get()),
            "TalentAtk" : int(self.talentAtk.get()),
            "TalentDef" : int(self.talentDef.get()),
            "TalentSpAtk" : int(self.talentSpAtk.get()),
            "TalentSpDef" : int(self.talentSpDef.get()),
            "TalentAgi" : int(self.talentAgi.get()),
            "Waza1" : GDataManager.getMoveList().index(self.move1.get()),
            "Waza2" : GDataManager.getMoveList().index(self.move2.get()),
            "Waza3" : GDataManager.getMoveList().index(self.move3.get()),
            "Waza4" : GDataManager.getMoveList().index(self.move4.get()),
            "FormNo" : int(self.formNo.get()),
            "IsRare" : int(self.isRare.get()),
            "Level" : int(self.level.get()),
            "Sex" : SexOptionMenu.SEX_LIST.index(self.sex.get()),
            "Item" : GDataManager.getItemList().index(self.item.get()),
            "Seikaku" : GDataManager.getNatureList().index(self.nature.get()),
            "Tokusei" : GDataManager.getAbilityList().index(self.ability.get()),
            "MonsNo" : GDataManager.getPokemonList().index(self.species.get()),
            "Ball" : int(self.ball.get()),
            "Seal" : int(self.seal.get())
        }

        return TrainerPokemon(**trainerPokemon)

class TrainerPartyNotebook(ttk.Notebook):
    def __init__(self, master, trainerParty, padding=3):
        super().__init__(master, padding=padding)
        self.trainerParty = trainerParty
        self.p1 = TrainerPokemonFrame(self, 1, self.trainerParty.party[0])
        self.p2 = TrainerPokemonFrame(self, 2, self.trainerParty.party[1])
        self.p3 = TrainerPokemonFrame(self, 3, self.trainerParty.party[2])
        self.p4 = TrainerPokemonFrame(self, 4, self.trainerParty.party[3])
        self.p5 = TrainerPokemonFrame(self, 5, self.trainerParty.party[4])
        self.p6 = TrainerPokemonFrame(self, 6, self.trainerParty.party[5])
        
        self.add(self.p1, text="Pokemon 1")
        self.add(self.p2, text="Pokemon 2")
        self.add(self.p3, text="Pokemon 3")
        self.add(self.p4, text="Pokemon 4")
        self.add(self.p5, text="Pokemon 5")
        self.add(self.p6, text="Pokemon 6")

    def updateTrainerParty(self, trainerParty):
        self.trainerParty = trainerParty
        self.p1.updateTrainerPokemon(self.trainerParty.party[0])
        self.p2.updateTrainerPokemon(self.trainerParty.party[1])
        self.p3.updateTrainerPokemon(self.trainerParty.party[2])
        self.p4.updateTrainerPokemon(self.trainerParty.party[3])
        self.p5.updateTrainerPokemon(self.trainerParty.party[4])
        self.p6.updateTrainerPokemon(self.trainerParty.party[5])

    def getTrainerParty(self):
        trainerParty = copy.copy(self.trainerParty)
        trainerParty.party[0] = self.p1.getTrainerPokemon()
        trainerParty.party[1] = self.p2.getTrainerPokemon()
        trainerParty.party[2] = self.p3.getTrainerPokemon()
        trainerParty.party[3] = self.p4.getTrainerPokemon()
        trainerParty.party[4] = self.p5.getTrainerPokemon()
        trainerParty.party[5] = self.p6.getTrainerPokemon()
        return trainerParty