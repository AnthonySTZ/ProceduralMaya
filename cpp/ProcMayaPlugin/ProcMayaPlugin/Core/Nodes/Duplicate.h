#pragma once

#include <maya/MGlobal.h>
#include <maya/MSyntax.h>
#include <maya/MPxCommand.h>
#include <maya/MArgDatabase.h>
#include <maya/MtransformationMatrix.h>
#include <maya/MMatrix.h>
#include <maya/MPointArray.h>
#include <tbb/parallel_for.h>

#include "../utils/SyntaxParser.h"
#include "../Shaders/StandardSurface.h"
#include "../utils/MayaObject.h"

class Duplicate : public MPxCommand {

public:
	static void* creator();
	static MSyntax syntax();
	MStatus doIt(const MArgList& args) override;
	static MObject DuplicateMesh(MObject obj, int amount, MTransformationMatrix transformMatrix);

};