#pragma once

#include <maya/MGlobal.h>
#include <maya/MSyntax.h>
#include <maya/MPxCommand.h>

class Merge : public MPxCommand{

private:
	static void* creator();
	static MSyntax syntax();
	MStatus doIt(const MArgList& args) override;

};