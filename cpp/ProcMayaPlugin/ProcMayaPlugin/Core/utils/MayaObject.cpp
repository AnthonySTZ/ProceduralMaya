#include "MayaObject.h"

MStatus MayaObject::FromName(MString name, MObject* obj)
{
    MSelectionList sel;
    CHECK_MSTATUS(sel.add(name));
    CHECK_MSTATUS(sel.getDependNode(0, *obj));
    if ((*obj).isNull()) {
        MGlobal::displayError("Invalid object name: " + name);
        return MS::kFailure;
    }
    return MS::kSuccess;
}

MObject MayaObject::getChildOf(MObject obj) {
    MFnDagNode dagNode1(obj);
    if (dagNode1.childCount() > 0) {
        MObject shapeObj1 = dagNode1.child(0);
        return shapeObj1;
    }
    return obj;
}