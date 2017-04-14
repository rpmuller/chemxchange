"""\
Main io dispatch of chemxchange
"""
import XYZ,CML,NWC

# Table of converters:
#  (shorthand, extension, reader, writer):
converters = [
    ('xyz', 'xyz', XYZ.read, XYZ.write),
    ('cml', 'cml', CML.read, CML.write),
    ('nwo', 'out', NWC.reado, None),
    ('nw', 'nw', NWC.read, NWC.write),
   ]

readers={}
writers={}
for (sh,ext,rd,wr) in converters:
    if rd:
        if ext not in readers:
            readers[ext] = rd
        if sh not in readers:
            readers[sh] = rd
    if wr:
        if ext not in writers:
            writers[ext] = wr
        if sh not in writers:
            writers[sh] = wr

def read_molecules(fname,format=None,default_format='xyz'):
    reader = getconverter(readers,fname,format,default_format)
    return reader(fname)

def write_molecules(geos,fname,format=None,default_format='xyz'):
    writer = getconverter(writers,fname,format,default_format)
    writer(geos,fname)
    return
