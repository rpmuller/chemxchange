import numpy as np

class Atom(object):
    def __init__(self,atno,x,y,z):
        self.atno = atno
        self.xyz = np.array((x,y,z),'d')
        return

