#!/usr/bin/env python

def getext(fname):
    """\
    Get the file extension.
    >>> getext('file.xyz')
    'xyz'
    >>> getext('file')
    ''
    >>> getext('file.')
    ''
    """
    wds = fname.split('.')
    if len(wds) > 1: return wds[-1]
    return ''

def getconverter(converters,fname,format,default_format):
    """\
    Get a converter (a reader or a writer) based on either a specified
    format or a format from the filename. Ultimately, fall back to a
    converter we know exists.
    
    >>> converters=dict(xyz='xyz',abc='abc',ijk='ijk')
    >>> getconverter(converters,'file.xyz',None,'abc')
    'xyz'
    >>> getconverter(converters,'file.xyz0',None,'abc')
    'abc'
    >>> getconverter(converters,'file.xyz0','ijk','abc')
    'ijk'
    """
    if format:
        converter = converters.get(format)
        assert converter
    else:
        ext = getext(fname)
        converter = converters.get(ext,default_format)
        assert converter
    return converter
