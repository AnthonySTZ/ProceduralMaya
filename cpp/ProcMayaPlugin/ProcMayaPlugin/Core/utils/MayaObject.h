#pragma once

#include <maya/MGlobal.h>
#include <maya/MSelectionList.h>

class MayaObject {

public:
	static MStatus FromName(MString name, MObject* obj);
};