'''
Created on Mar 20, 2018

@author: j3ff1
'''

from pymclevel import TAG_String, TAG_List, TAG_Compound, TAG_Float, TAG_Double, TAG_Byte, TAG_Short
from pymclevel import TileEntity

displayName = "Fill with Rel Coords"

x=0
y= 0
z=0
x2=0
y2=0
z2=0
xs=""
ys=""
zs=""
demo = "demo"
cmd = ""

def perform(level, box, options):
    
    
    
    
    corners = {'SET': (box.maxx-1,box.maxy-1,box.maxz-1), 'SEB': (box.maxx-1,box.miny,box.maxz-1), 
               'SWT': (box.minx,box.maxy-1,box.maxz-1), 'SWB':(box.minx,box.miny,box.maxz-1),
               'NET': (box.maxx-1,box.maxy-1,box.minz), 'NEB': (box.maxx-1,box.miny,box.minz),
               'NWT': (box.minx,box.maxy-1,box.minz), 'NWB': (box.minx,box.miny,box.minz)}
    
    
    
    if checkIfCommandBlock(level.blockAt(corners['SET'][0],corners['SET'][1],corners['SET'][2])):
        doCornerStuff(corners['SET'],corners['NWB'])
    elif checkIfCommandBlock(level.blockAt(corners['SEB'][0],corners['SEB'][1],corners['SEB'][2])):
        doCornerStuff(corners['SEB'],corners['NWT'])
    elif checkIfCommandBlock(level.blockAt(corners['SWT'][0],corners['SWT'][1],corners['SWT'][2])):
        doCornerStuff(corners['SWT'],corners['NEB']) 
    elif checkIfCommandBlock(level.blockAt(corners['SWB'][0],corners['SWB'][1],corners['SWB'][2])):
        doCornerStuff(corners['SWB'],corners['NET'])  
    elif checkIfCommandBlock(level.blockAt(corners['NET'][0],corners['NET'][1],corners['NET'][2])):
        doCornerStuff(corners['NET'],corners['SWB'])
    elif checkIfCommandBlock(level.blockAt(corners['NEB'][0],corners['NEB'][1],corners['NEB'][2])):
        doCornerStuff(corners['NEB'],corners['SWB'])
    elif checkIfCommandBlock(level.blockAt(corners['NWT'][0],corners['NWT'][1],corners['NWT'][2])):
        doCornerStuff(corners['NWT'],corners['SEB'])
    elif checkIfCommandBlock(level.blockAt(corners['NWB'][0],corners['NWB'][1],corners['NWB'][2])):
        doCornerStuff(corners['NWB'],corners['SET'])   
    
    global x,y,z
    
    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:  
            if x == t["x"].value and y == t["y"].value and z == t["z"].value:
                oldcmd = t["Command"].value
                chunk.dirty = True
                t["Command"] = TAG_String(oldcmd + " " + cmd)   
                
    
    
def doCornerStuff(coordTuple,coordTuple2):    
    global x,y,z
    global x2,y2,z2
    global xs,ys,zs
    global cmd
    
    x,y,z = coordTuple
    x2,y2,z2 = coordTuple2
    xs = str(x2-x)
    ys = str(y2-y)
    zs = str(z2-z)
    cmd = "~"+xs+" ~"+ys+" ~"+zs 
    
def checkIfCommandBlock(id):
    if(id == 137 or id == 210 or id ==211):
        return True
    else:
        return False
    
    
    
    