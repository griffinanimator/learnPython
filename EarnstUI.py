import maya.cmds as cmds


def UI():
    # Check to see if the window exists
    if cmds.window("testUI", exists=True):
        cmds.deleteUI("testUI")
        
    # Create a window 
    windowA = cmds.window("testUI", title="ExampleUI", w=300, h=300,  mnb=False, mxb=False, sizeable=False)
    
    # Create a main layout
    mainLayout = cmds.columnLayout(w=300, h=300)
    # Banner Image
    #imagePath = cmds.internalVar
    imagePath = "C:/Users/rgriffin/Google Drive/RG_ARTTOOLS/learnPython/exbanner.png"
    cmds.image(h=300, w=300, image=imagePath)
    
    # Show window
    cmds.showWindow(windowA)
    