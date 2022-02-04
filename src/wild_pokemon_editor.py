from tkinter import *
from tkinter import ttk

from wild_pokemon_frame import WildPokemonFrame, WildPokemonEditorFrame

def gui_main():
    root = Tk()
    root.title("BDSP Wild Pokemon Editor")
    frm = WildPokemonEditorFrame(root)
    frm.pack(expand=1, fill='both')
    root.mainloop()

if __name__ == "__main__":
    gui_main()