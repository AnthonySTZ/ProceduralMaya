#pragma once

#include <maya/MpxCommand.h>
#include <maya/MGlobal.h>
#include <maya/MArgDatabase.h>
#include <maya/MSyntax.h>
#include <maya/MCommandResult.h>
#include <maya/MFloatVector.h>
#include <maya/MObject.h>
#include <maya/MSelectionList.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MItMeshVertex.h>
#include <maya/MTransformationMatrix.h>
#include <maya/MMatrix.h>
#include <maya/MFnMesh.h>
#include <maya/MPointArray.h>
#include <maya/MDagPath.h>
#include <tbb/parallel_for.h>

#include "../utils/SyntaxParser.h"

class TransformNode : public MPxCommand {

public:
	static void* creator();
	static MSyntax syntax();
	MStatus doIt(const MArgList& args) override;
	static void transformMesh(MObject obj, MTransformationMatrix transformMatrix);

};