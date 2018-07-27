'''
Created on Feb 26, 2018

@author: j3ff1
'''

displayName = "Remove Natural Plants"

def perform(level, box, options):
    for x in xrange(box.minx,box.maxx):
        for y in xrange(box.miny,box.maxy):
            for z in xrange(box.minz,box.maxz):
                if testIfNatureBlock(level, (x,y,z)):
                    level.setBlockAt(x,y,z,0)

def testIfNatureBlock(level, position):
    (x,y,z) = position
    blockID = level.blockAt(x,y,z)
    return blockID == 17 \
        or blockID == 18 \
        or blockID == 31 \
        or blockID == 32 \
        or blockID == 37 \
        or blockID == 38 \
        or blockID == 39 \
        or blockID == 40 \
        or blockID == 83 \
        or blockID == 83 \
        or blockID == 86 \
        or blockID == 99 \
        or blockID == 100 \
        or blockID == 103 \
        or blockID == 104 \
        or blockID == 105 \
        or blockID == 106 \
        or blockID == 111 \
        or blockID == 161 \
        or blockID == 162 \
        or blockID == 175 \
        