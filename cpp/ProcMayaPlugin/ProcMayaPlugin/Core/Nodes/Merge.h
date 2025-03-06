#pragma once

#include <maya/MGlobal.h>
#include <maya/MSyntax.h>
#include <maya/MPxCommand.h>
#include <maya/MArgDatabase.h>

#include "../utils/SyntaxParser.h"

class Merge : public MPxCommand{

public:
	static void* creator();
	static MSyntax syntax();
	MStatus doIt(const MArgList& args) override;
	static void MergeObjs(MObject obj1, MObject obj2);
};