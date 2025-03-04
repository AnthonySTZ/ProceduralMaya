#pragma once

#include <maya/MpxCommand.h>
#include <maya/MGlobal.h>
#include <maya/MArgDatabase.h>
#include <maya/MSyntax.h>

class CubeNode : public MPxCommand {

public:
	static void* creator();
	static MSyntax syntax();
	MStatus doIt(const MArgList& args) override;
	static MStatus CreateCube(double width, double height, double depth);

};