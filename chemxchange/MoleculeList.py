class MoleculeList(object):
    def __init__(self,molecules):
        self.molecules = molecules
        return

    def __getitem__(self,*args,**kwds):
        return self.molecules.__getitem__(*args,**kwds
