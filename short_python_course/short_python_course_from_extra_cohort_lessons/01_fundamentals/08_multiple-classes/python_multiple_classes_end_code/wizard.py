class Wizard:
    def __init__(self, name, wand):
        self.name = name
        self.wand = wand

    def cast_spell(self, spell):
        return self.wand.cast_spell(spell)
