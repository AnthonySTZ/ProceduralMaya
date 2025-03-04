#pragma once

#include <maya/MpxCommand.h>
#include <maya/MGlobal.h>
#include <maya/MArgDatabase.h>
#include <maya/MSyntax.h>
#include <maya/MCommandResult.h>
#include <maya/MFloatPointArray.h>
#include <maya/MIntArray.h>
#include <maya/MFnMesh.h>
#include <maya/MObject.h>

#include "../Shaders/Lambert.h"

class CubeNode : public MPxCommand {

public:
	static void* creator();
	static MSyntax syntax();
	MStatus doIt(const MArgList& args) override;
	static MObject CreateCube(double width, double height, double depth);

};