#pragma once

#include <maya/MGlobal.h>
#include <maya/MSelectionList.h>
#include <maya/MFnDagNode.h>
#include <maya/MFnMesh.h>
#include <maya/MDagPath.h>

class MayaObject {

public:
	static MStatus FromName(MString name, MObject* obj);
	static MObject getChildOf(MObject obj);
	static MFnMesh getMeshFrom(MObject obj);
};