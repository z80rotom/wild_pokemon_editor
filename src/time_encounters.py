import copy

from tkinter import *
from tkinter import ttk
from typing import List, Dict
from combobox import SpeciesOptionMenu

from core import EncEntry, FieldEncount
from gdatamanger import GDataManager
from spinbox import LevelSpinbox

class TimeEncountersFrame(ttk.Frame):
    def __init__(self, root, ground_mons: List[EncEntry], time_encounters: List[EncEntry], padding=3):
        super().__init__(root, padding=padding)
        self.ground_mons = copy.copy(ground_mons)
        self.ground_mons[2] = time_encounters[0]
        self.ground_mons[3] = time_encounters[1]

        self.speciesLabel = ttk.Label(self, text="Species")
        self.minLvlLabel = ttk.Label(self, text="Min Lvl")
        self.maxLvlLabel = ttk.Label(self, text="Max Lvl")

        self.speciesLabel.grid(column=1, row=0, padx=3, pady=3)
        self.minLvlLabel.grid(column=2, row=0, padx=3, pady=3)
        self.maxLvlLabel.grid(column=3, row=0, padx=3, pady=3)

        self.ground_mon_vars = []
        for i, ground_mon in enumerate(self.ground_mons):
            # Use the same var name because these should have the same information across tabs
            if i not in [2, 3]:
                species = StringVar(self, GDataManager.getPokemonById(ground_mon.monsNo), "groundMonSpecies{}".format(i))
                minLvl = StringVar(self, ground_mon.minlv, "groundMonMinLvl{}".format(i))
                maxLvl = StringVar(self, ground_mon.maxlv, "groundMonMaxLvl{}".format(i))
            else:
                # These are the unique entries
                species = StringVar(self, GDataManager.getPokemonById(ground_mon.monsNo))
                minLvl = StringVar(self, ground_mon.minlv)
                maxLvl = StringVar(self, ground_mon.maxlv)
            self.ground_mon_vars.append({
                "species" : species,
                "minLvl" : minLvl,
                "maxLvl" : maxLvl
            })
            
            speciesOptionMenu = SpeciesOptionMenu(self, species)
            minLvlSpinBox = LevelSpinbox(self, minLvl)
            maxLvlSpinBox = LevelSpinbox(self, maxLvl)
            speciesOptionMenu.set(GDataManager.getPokemonById(ground_mon.monsNo))
            minLvlSpinBox.set(str(ground_mon.minlv))
            maxLvlSpinBox.set(str(ground_mon.maxlv))
            
            speciesOptionMenu.grid(column=1, row=i+1, padx=3, pady=3)
            minLvlSpinBox.grid(column=2, row=i+1, padx=3, pady=3)
            maxLvlSpinBox.grid(column=3, row=i+1, padx=3, pady=3)

    def updateData(self, ground_mons: List[EncEntry], time_encounters: List[EncEntry]):
        self.ground_mons = copy.copy(ground_mons)
        self.ground_mons[2] = time_encounters[0]
        self.ground_mons[3] = time_encounters[1]

        for i, ground_mon in enumerate(ground_mons):
            ground_mon_var = self.ground_mon_vars[i]
            ground_mon_var["species"].set(GDataManager.getPokemonById(ground_mon.monsNo))
            ground_mon_var["minLvl"].set(ground_mon.minlv)
            ground_mon_var["maxLvl"].set(ground_mon.maxlv)

    def getGroundMons(self):
        ground_mons = []
        for ground_mon_var in self.ground_mon_vars:
            ground_mons.append(EncEntry(**{
                "maxlv" : int(ground_mon_var["maxLvl"].get()),
                "minlv" : int(ground_mon_var["minLvl"].get()),
                "monsNo" : GDataManager.getPokemonList().index(ground_mon_var["species"].get())
            }))
        
        return ground_mons

    def getTimeEncounters(self):
        time_encounters = []
        for i in range(2):
            time_enc_var = self.ground_mon_vars[2+i]
            time_encounters.append(EncEntry(**{
                "maxlv" : int(time_enc_var["maxLvl"].get()),
                "minlv" : int(time_enc_var["minLvl"].get()),
                "monsNo" : GDataManager.getPokemonList().index(time_enc_var["species"].get())
            }))
        return time_encounters
        

class TimeEncountersNotebook(ttk.Notebook):
    def __init__(self, master, fieldencount: FieldEncount, padding=3):
        super().__init__(master, padding=padding)

        self.morning = TimeEncountersFrame(self, fieldencount.ground_mons, fieldencount.tairyo)
        self.day = TimeEncountersFrame(self, fieldencount.ground_mons, fieldencount.day)
        self.night = TimeEncountersFrame(self, fieldencount.ground_mons, fieldencount.night)

        self.add(self.morning, text="Morning")
        self.add(self.day, text="Day")
        self.add(self.night, text="Night")
    
    def updateData(self, fieldencount: FieldEncount):
        self.morning.updateData(fieldencount.ground_mons, fieldencount.tairyo)
        self.day.updateData(fieldencount.ground_mons, fieldencount.day)
        self.night.updateData(fieldencount.ground_mons, fieldencount.night)
    
    def getData(self):
        ground_mons = self.day.getGroundMons()
        tairyo = self.morning.getTimeEncounters()
        day = self.day.getTimeEncounters()
        night = self.night.getTimeEncounters()
        return {
            "ground_mons" : ground_mons,
            "tairyo" : tairyo,
            "day" : day,
            "night" : night
        }