#pragma once

#include <maya/MGlobal.h>
#include <maya/MSyntax.h>
#include <maya/MPxCommand.h>
#include <maya/MArgDatabase.h>
#include <maya/MFnMesh.h>
#include <maya/MPointArray.h>
#include <maya/MIntArray.h>

#include "../utils/SyntaxParser.h"
#include "../utils/MayaObject.h"
#include "../Shaders/StandardSurface.h"

class Merge : public MPxCommand{

public:
	static void* creator();
	static MSyntax syntax();
	MStatus doIt(const MArgList& args) override;
	static MObject MergeObjs(MObject obj1, MObject obj2);
};