from tkinter import *
from tkinter import ttk

from gdatamanger import GDataManager

class MoveOptionMenu(ttk.Combobox):
    def __init__(self, master, textvariable, **kwargs):
        move_list = sorted(set(GDataManager.getMoveList()))
        super().__init__(master, textvariable=textvariable, values=move_list, **kwargs)
        self.bind('<KeyRelease>', self.filterList)
    
    def filterList(self, event):
        value = event.widget.get()
        if value == '':
            return
        move_list = sorted(set(GDataManager.getMoveList()))
        self['values'] = list(filter(lambda move: move.lower().startswith(value.lower()), move_list))

class SpeciesOptionMenu(ttk.Combobox):
    def __init__(self, master, textvariable, **kwargs):
        pokemon_list = sorted(set(GDataManager.getPokemonList()))
        super().__init__(master, textvariable=textvariable, values=pokemon_list, **kwargs)
        self.bind('<KeyRelease>', self.filterList)
    
    def filterList(self, event):
        value = event.widget.get()
        if value == '':
            return
        pokemon_list = sorted(set(GDataManager.getPokemonList()))
        self['values'] = list(filter(lambda pokemon: pokemon.lower().startswith(value.lower()), pokemon_list))

class SexOptionMenu(ttk.OptionMenu):
    SEX_LIST = ["Default", "Male", "Female", "Agender"]
    def __init__(self, master, textvariable, **kwargs):
        super().__init__(master, textvariable, "Default", *self.SEX_LIST, **kwargs)
    #     self.bind('<KeyRelease>', self.filterList)
    
    # def filterList(self, event):
    #     value = event.widget.get()
    #     if value == '':
    #         return
    #     sex_list = ["Agender", "Male", "Female"]
    #     self['values'] = list(filter(lambda pokemon: pokemon.lower().startswith(value.lower()), pokemon_list))


class ItemOptionMenu(ttk.Combobox):
    def __init__(self, master, textvariable, **kwargs):
        item_list = sorted(set(GDataManager.getItemList()))
        super().__init__(master, textvariable=textvariable, values=item_list, **kwargs)
        self.bind('<KeyRelease>', self.filterList)
    
    def filterList(self, event):
        value = event.widget.get()
        if value == '':
            return
        item_list = sorted(set(GDataManager.getItemList()))
        self['values'] = list(filter(lambda item: item.lower().startswith(value.lower()), item_list))

class AbilityOptionMenu(ttk.Combobox):
    def __init__(self, master, textvariable, **kwargs):
        ability_list = sorted(set(GDataManager.getAbilityList()))
        super().__init__(master, textvariable=textvariable, values=ability_list, **kwargs)
        self.bind('<KeyRelease>', self.filterList)
    
    def filterList(self, event):
        value = event.widget.get()
        if value == '':
            return
        ability_list = sorted(set(GDataManager.getAbilityList()))
        self['values'] = list(filter(lambda ability: ability.lower().startswith(value.lower()), ability_list))

class NatureOptionMenu(ttk.Combobox):
    def __init__(self, master, textvariable, **kwargs):
        nature_list = sorted(set(GDataManager.getNatureList()))
        super().__init__(master, textvariable=textvariable, values=nature_list, **kwargs)
        self.bind('<KeyRelease>', self.filterList)
    
    def filterList(self, event):
        value = event.widget.get()
        if value == '':
            return
        nature_list = sorted(set(GDataManager.getNatureList()))
        self['values'] = list(filter(lambda nature: nature.lower().startswith(value.lower()), nature_list))

class TrainerNameOptionMenu(ttk.Combobox):
    def __init__(self, master, textvariable, **kwargs):
        trainer_names = sorted(set(GDataManager.getTrainerNames().keys()))
        super().__init__(master, textvariable=textvariable, values=trainer_names, **kwargs)
        self.bind('<KeyRelease>', self.filterList)
    
    def filterList(self, event):
        value = event.widget.get()
        if value == '':
            return
        trainer_names = sorted(set(GDataManager.getTrainerNames().keys()))
        self['values'] = list(filter(lambda name: name.lower().startswith(value.lower()), trainer_names))

class TrainerMessageOptionMenu(ttk.Combobox):
    def __init__(self, master, textvariable, **kwargs):
        trainer_msgs = sorted(set(GDataManager.getTrainerMessageList()))
        super().__init__(master, textvariable=textvariable, values=trainer_msgs, width=50, **kwargs)
        self.bind('<KeyRelease>', self.filterList)
    
    def filterList(self, event):
        value = event.widget.get()
        if value == '':
            return
        trainer_msgs = sorted(set(GDataManager.getTrainerMessageList()))
        self['values'] = list(filter(lambda trainer_msg: trainer_msg.lower().startswith(value.lower()), trainer_msgs))
