class Molecule(object):
    def __init__(self,atoms=[],charge=0,spin=0):
        self.atoms = atoms
        self.charge = charge
        self.spin = spin
        return

    def __getitem__(self,*args,**kwds):
        return self.atoms.__getitem__(*args,**kwds)
