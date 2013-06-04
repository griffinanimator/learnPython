from maya import cmds, OpenMaya

center =  'center'
vtx = cmds.ls(sl=1, fl=1)

for v in vtx:
    cmds.select(cl=1)
    jnt =  cmds.joint()
    pos =  cmds.xform(v, q=1, ws=1, t=1)
    cmds.xform(jnt, ws=1, t=pos)
    posC =  cmds.xform(center, q=1, ws=1, t=1)
    cmds.select(cl=1)
    jntC =  cmds.joint()
    cmds.xform(jntC, ws=1, t=posC)
    cmds.parent(jnt, jntC)
    cmds.joint(jntC, e=1, oj="xyz", secondaryAxisOrient="yup", ch=1)
    
    
    
sel = cmds.ls(sl=True)

for s in sel:
    loc =  cmds.spaceLocator()[0]
    pos = cmds.xform(s, q=1, ws=1, t=1)
    cmds.xform(loc, ws=1, t=pos)
    par = cmds.listRelatives(s, p=1)[0]
    cmds.aimConstraint(loc, par, mo=True, weight=1, aimVector = (1,0,0), upVector = (0,1,0), worldUpType = "object", worldUpObject = 'r_eye_up_loc')



#########################################

from maya import cmds , OpenMaya

curveM = getMObject ("curveShape1")
print curveM

curveFn = OpenMaya.MFnNurbsCurve(curveM)
print curveFn

pos = cmds.xform("locator1", q=1, ws=1, t=1)
mPos = OpenMaya.MPoint(pos[0], pos[1], pos[2])

scriptU = OpenMaya.MScriptUtil()
paramPt = scriptU.asDoublePtr()

curveFn.getParamAtPoint(mPos, paramPt, OpenMaya.MSpace.kObject)

param = scriptU.getDouble(paramPt)

del(paramPt)

def getMObject(objectName):
    print objectName
    if isinstance(objectName, list)==True:
        print "True"
        oNodeList=[]
        for o in objectName:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(o)
            oNode = OpenMaya.MObject()
            selectionList.getDependNode(0, oNode)
            oNodeList.append(oNode)
        return oNodeList
        
    else:
        selectionList = OpenMaya.MSelectionList()
        selectionList.add(objectName)
        oNode = OpenMaya.MObject()
        selectionList.getDependNode(0, oNode)
        
        return oNode