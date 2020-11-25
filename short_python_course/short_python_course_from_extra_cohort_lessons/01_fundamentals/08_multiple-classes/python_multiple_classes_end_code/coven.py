class Coven:
    def __init__(self, wizards):
        self.wizards = wizards

    def cast_spell(self, spell):
        mass_spell = []

        for wizard in self.wizards:
            mass_spell.append(wizard.cast_spell(spell))

        return mass_spell
