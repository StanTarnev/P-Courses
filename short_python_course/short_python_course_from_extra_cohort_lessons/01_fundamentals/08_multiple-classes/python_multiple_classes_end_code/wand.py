class Wand:
    def __init__(self, wood, core):
        self.wood = wood
        self.core = core

    def cast_spell(self, spell):
        if(self.wood == "holly" and self.core == "phoenix feather"):
            return spell.upper()
        else:
            return spell
