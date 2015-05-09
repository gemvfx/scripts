import c4d
from c4d import gui
import os
import xml.etree.ElementTree as xml
#Welcome to the world of Python

def ProcessBrick(brick):
    print("processing brick")
    print brick.items()
    for a in brick.findall('Part'):
        print a


def ProcessPart(part):
    print part
    
def ProcessBone(bone):
    print bone
    

def main():
    #gui.MessageDialog('Hello World!')
    FILENAME = 'C:\\tmp\\lego\\IMAGE100.LXFML'
    o = FILENAME + " " + str(os.stat(FILENAME).st_size)
    #s = open(FILENAME).read()
    #print str(len(s))
    tree = xml.parse(FILENAME)
    rootElement = tree.getroot()
    print rootElement
    # process all bricks
    for a in rootElement.findall('Bricks/Brick'):
        ProcessBrick(a)
        
        
    

if __name__=='__main__':
    main()
