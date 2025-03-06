#pragma once

#include <maya/MGlobal.h>
#include <maya/MSelectionList.h>
#include <maya/MFnDagNode.h>

class MayaObject {

public:
	static MStatus FromName(MString name, MObject* obj);
	static MObject getChildOf(MObject obj);
};