#pragma once

#include <maya/MObject.h>
#include <maya/MFnMesh.h>
#include <maya/MFnDagNode.h>
#include <maya/MGlobal.h>

class StandardSurface {

public:
	static void AssignShaderTo(MObject fnObj);

};