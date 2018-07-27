'''
Created on Mar 23, 2018

@author: j3ff1
'''

from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_String

displayName = "Cmd Block Coord Rotater"

inputs = (
    ("flip X", False),
    ("flip Z", False),
    ("swap XZ", False),
)




def perform(level,box,options):
    print("starting")

    flipX = options["flip X"]
    flipZ = options["flip Z"]
    swapXZ = options["swap XZ"]
    
    for (chunk, slices, point) in level.getChunkSlices(box):
        for t in chunk.TileEntities:
            x = t["x"].value
            y = t["y"].value
            z = t["z"].value
            
            if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz and t["id"].value == "minecraft:command_block": 
                
                oldCommand = t["Command"].value
                t["Command"].value = converter(oldCommand,flipX,flipZ,swapXZ)
                chunk.dirty = True
            ##else:
                ##print("else executed once")
                ##raise Exception("Else being executed")
                
def converter(oldCommand,flipX,flipZ,swapXZ):
    if isStringNull(oldCommand)==False and oldCommand!="":
        commandType = cutCommandType(oldCommand)
        
        if(numberOfCoordinates(oldCommand)==0):
            return oldCommand
        elif(numberOfCoordinates(oldCommand)== 3):
            allCoords=cutOutCoord(oldCommand)
            cmdX=allCoords[0]
            cmdY=allCoords[1]
            cmdZ=allCoords[2]
            commandTail = cutOutTail(oldCommand)
            if swapXZ == True:
                holder = cmdX
                cmdX = cmdZ
                cmdZ = holder
            if flipX == True:
                cmdX *= (-1)
            if flipZ == True:
                cmdZ *= (-1)
                
            return combiner(commandType,commandTail,cmdX,cmdY,cmdZ)
        elif(numberOfCoordinates(oldCommand)==6):
            allCoords=cutOutCoord(oldCommand)
            cmdX=allCoords[0]
            cmdY=allCoords[1]
            cmdZ=allCoords[2]
            cmdX2=allCoords[3]
            cmdY2=allCoords[4]
            cmdZ2=allCoords[5]
            commandTail = cutOutTail(oldCommand)
            if swapXZ == True:
                holder = cmdX
                holder2 = cmdX2
                cmdX = cmdZ
                cmdX2 = cmdZ2
                cmdZ = holder
                cmdZ2=holder2
            if flipX == True:
                cmdX *= (-1)
                cmdX2 *= (-1)
            if flipZ == True:
                cmdZ *= (-1)
                cmdZ2 *= (-1)
            return combiner(commandType,commandTail,cmdX,cmdY,cmdZ,cmdX2,cmdY2,cmdZ2)
        elif(numberOfCoordinates(oldCommand)==9):
            allCoords=cutOutCoord(oldCommand)
            cmdX=allCoords[0]
            cmdY=allCoords[1]
            cmdZ=allCoords[2]
            cmdX2=allCoords[3]
            cmdY2=allCoords[4]
            cmdZ2=allCoords[5]
            cmdX3=allCoords[6]
            cmdY3=allCoords[7]
            cmdZ3=allCoords[8]
            commandTail = cutOutTail(oldCommand)
            if swapXZ == True:
                holder = cmdX
                holder2 = cmdX2
                holder3 = cmdX3
                cmdX = cmdZ
                cmdX2 = cmdZ2
                cmdX3 = cmdZ3
                cmdZ = holder
                cmdZ2=holder2
                cmdZ3 = holder3
            if flipX == True:
                cmdX *= (-1)
                cmdX2 *= (-1)
                cmdX3 *= (-1)
            if flipZ == True:
                cmdZ *= (-1)
                cmdZ2 *= (-1)
                cmdZ3 *= (-1)
            return combiner(commandType,commandTail,cmdX,cmdY,cmdZ,cmdX2,cmdY2,cmdZ2,cmdX3,cmdY3,cmdZ3)
    else:
        return oldCommand    


def numberOfCoordinates(string):
        
    number = 0
    for letter in string:
        if(letter== '~'):
            number+=1
    return number

def isStringNull(String):
    isNull = True
    if(len(String)>=1):
        isNull = False

    return isNull


##leaves space after if there are coordds
##if no coords returns the whole thing back
def cutCommandType(string):
        
    if(numberOfCoordinates(string)>0):
        export = string[0:string.find("~")]
    else:
        export = string
    
    return export

##can handle no coords
##but only takes precut commands
def isFirstCoordNeg(string):
    neg = False
    ##check null
    if(len(string)>=1):
        if(string[0:1]=='~'):
            if(string[1:2]=='-'):
                neg = True

    return neg
    
##Cut out methods, parses the coordinate into integer
##make sure there are coordinates to be processed 
##otherwise would return error

##cuts and parses every coordinate in range into a list of ints
##can take tails so long as tails don't have ~
def slowCut(temp, howMany):
    
    exportCoord = []
    ## "~ ~2 ~" "~ ~2 ~ "
    for iteration in range(howMany):
        
        if(temp!=""):        
            temp = temp[temp.find("~")+1:]
        ###
            if(temp.find("~")==-1):
                if(temp==""):
                    exportCoord.append(0)
                elif(temp==" "):
                    exportCoord.append(0)
                elif(temp[0]=="-"):
                    exportCoord.append(int(temp[0:2]))
                elif(temp[0]==" "):
                    exportCoord.append(0)
                else:
                    exportCoord.append(int(temp[0]))
            else:
                if(temp[0]=="-"):
                    exportCoord.append(int(temp[0:2]))
                elif(temp[0]==" "):
                    exportCoord.append(0)
                else:
                    exportCoord.append(int(temp[0]))    
                temp = temp[temp.find("~"):]      
        ###
        else:
            exportCoord.append(0)
                
    return exportCoord

##returns all coordinates orderly in a list of integers
def cutOutCoord(string):
    
    if(numberOfCoordinates(string)> 0):
        temp = string[string.find("~"):]
        
        if(numberOfCoordinates(string)==3):
            exportCoord = slowCut(temp, 3)
        elif(numberOfCoordinates(string)==6):
            exportCoord = slowCut(temp, 6)
        elif(numberOfCoordinates(string)==9):
            exportCoord = slowCut(temp, 9)
            
    return exportCoord




    ##regardless whether there is a tail, this method can execute without a problem
    ##if there is no tail, the method would simply return an empty string
    ##leaves a space before the tail
def cutOutTail(string):
    
    ##checks if there are coordinates
    ##if there are, cut to first tilde
    ##if not, exports an empty string
    if(numberOfCoordinates(string)> 0):
        temp = string[string.find("~"):]
        ##"~1 ~2 ~3"
        ##"~ ~ ~ k"
        
        while(numberOfCoordinates(temp)>=2):
            temp = temp[temp.find("~")+1:]
            temp = temp[temp.find("~"):]

            
            
        if temp ==  "~":
            exportTail = ""
        elif temp == "~ ":
            exportTail = ""
        else:
            if(temp.find(' ')==-1):
                exportTail = ""
            else:
                temp = temp[temp.find(' '):]
                exportTail = temp
        
    else:
        exportTail = ""
    
    print(exportTail+"exported tail")    
    return exportTail


def combiner(commandType, commandTail, x=None, y=None, z=None, x2=None,y2=None,z2=None, x3=None,y3=None,z3=None):
    
    if(x==None):
        export = commandType
    elif(x2 == None):
        export = commandType + "~" + str(x)+ " ~" + str(y) + " ~" + str(z)  + commandTail
    elif(x3==None):
        export = commandType + "~" + str(x)+ " ~" + str(y) + " ~" + str(z) \
        + " ~" + str(x2) + " ~" + str(y2) + " ~" + str(z2)  + commandTail
    else:
        export = commandType + "~" + str(x)+ " ~" + str(y) + " ~" + str(z) + " ~" \
        + str(x2) + " ~" + str(y2) + " ~" + str(z2) + " ~" \
        + str(x3) + " ~" + str(y3) + " ~" + str(z3) + commandTail
    return export
