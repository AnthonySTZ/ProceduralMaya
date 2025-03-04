#include "CubeNode.h"

#include <string>

void* CubeNode::creator() {
	return new CubeNode;
}

MSyntax CubeNode::syntax()
{
	MSyntax syntax;
	syntax.addFlag("-w", "-width", MSyntax::kDouble);
	syntax.addFlag("-h", "-height", MSyntax::kDouble);
	syntax.addFlag("-d", "-depth", MSyntax::kDouble);
	return syntax;
}

MStatus CubeNode::doIt(const MArgList& args)
{
	MArgDatabase argData(syntax(), args);
	double width = 1.0;
	double height = 1.0;
	double depth = 1.0;

	if (argData.isFlagSet("-w"))
		argData.getFlagArgument("-w", 0, width);
	if (argData.isFlagSet("-h"))
		argData.getFlagArgument("-h", 0, height);
	if (argData.isFlagSet("-d"))
		argData.getFlagArgument("-d", 0, depth);

	return CreateCube(width, height, depth);
}



MStatus CubeNode::CreateCube(double width, double height, double depth)
{
	MGlobal::displayInfo(MString("Create cube : width=") + MString().set(width, 2) + 
								MString(" height=") + MString().set(height, 2) + 
								MString(" depth=") + MString().set(depth, 2));

	return MS::kSuccess;
}
