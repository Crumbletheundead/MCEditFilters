'''
Created on Mar 21, 2018

@author: j3ff1
'''
from pymclevel import alphaMaterials

displayName = "Side Coat Filter"

inputs = (
            ("Pick block", "label"),
            ("Pick", alphaMaterials.CobblestoneWall),
        )

blocksToReplace = []

def perform(level, box, options):
    
    global blocksToReplace
    
    for x in xrange(box.minx,box.maxx):
        for y in xrange(box.miny,box.maxy):
            for z in xrange(box.minz,box.maxz):
                if testIfSide(level,x,y,z):
                    blocksToReplace.append((x,y,z))
    
    for tuple in blocksToReplace:
        xr = tuple[0]
        yr = tuple[1]
        zr = tuple[2]
        chosenMat = getBlockFromOptions(options,"Pick")
        level.setBlockAt(xr,yr,zr,chosenMat[0])
        level.setBlockDataAt(xr,yr,zr,chosenMat[1])
        
    level.markDirtyBox(box)    

def getBlockFromOptions(options, block):
    return (options[block].ID, options[block].blockData)
             
def testIfSide(level,x,y,z):
    if level.blockAt(x,y,z)==0:
        return False
    elif level.blockAt(x+1,y,z)==0 or level.blockAt(x-1,y,z)==0 or \
    level.blockAt(x,y,z+1)==0 or level.blockAt(x,y,z-1)==0:
        return True
    else:
        return False
    
    
    
    