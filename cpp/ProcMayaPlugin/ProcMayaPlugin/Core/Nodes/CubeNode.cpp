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

	if (argData.isFlagSet("-w")) {
		argData.getFlagArgument("-w", 0, width);
	}
	if (argData.isFlagSet("-h")) {
		argData.getFlagArgument("-h", 0, height);
	}
	if (argData.isFlagSet("-d")) {
		argData.getFlagArgument("-d", 0, depth);
	}

    MObject mesh = CreateCube(width, height, depth);
    MFnDependencyNode depNode(mesh);
	setResult(depNode.name());

	return MS::kSuccess;
}



MObject CubeNode::CreateCube(double width, double height, double depth)
{
    MFloatPointArray vertices;
    vertices.append(MFloatPoint(-1.0f, -1.0f, -1.0f));  // 0
    vertices.append(MFloatPoint(1.0f, -1.0f, -1.0f));  // 1
    vertices.append(MFloatPoint(1.0f, 1.0f, -1.0f));  // 2
    vertices.append(MFloatPoint(-1.0f, 1.0f, -1.0f));  // 3
    vertices.append(MFloatPoint(-1.0f, -1.0f, 1.0f));  // 4
    vertices.append(MFloatPoint(1.0f, -1.0f, 1.0f));  // 5
    vertices.append(MFloatPoint(1.0f, 1.0f, 1.0f));  // 6
    vertices.append(MFloatPoint(-1.0f, 1.0f, 1.0f));  // 7

    // Define the 6 faces of the cube (each face is a quad with 4 vertices)
    MIntArray polygonCounts;
    polygonCounts.append(4);  // First face
    polygonCounts.append(4);  // Second face
    polygonCounts.append(4);  // Third face
    polygonCounts.append(4);  // Fourth face
    polygonCounts.append(4);  // Fifth face
    polygonCounts.append(4);  // Sixth face

    // Define the connectivity (vertex indices) for each face
    MIntArray polygonConnects;
    polygonConnects.append(0); polygonConnects.append(1); polygonConnects.append(2); polygonConnects.append(3);  // First face
    polygonConnects.append(4); polygonConnects.append(5); polygonConnects.append(6); polygonConnects.append(7);  // Second face
    polygonConnects.append(0); polygonConnects.append(1); polygonConnects.append(5); polygonConnects.append(4);  // Third face
    polygonConnects.append(1); polygonConnects.append(2); polygonConnects.append(6); polygonConnects.append(5);  // Fourth face
    polygonConnects.append(2); polygonConnects.append(3); polygonConnects.append(7); polygonConnects.append(6);  // Fifth face
    polygonConnects.append(3); polygonConnects.append(0); polygonConnects.append(4); polygonConnects.append(7);  // Sixth face

    // Create the cube using MFnMesh
    MFnMesh fnMesh;
    MObject parent = MObject::kNullObj; // No parent for this example
    MObject cubeObj = fnMesh.create(vertices.length(), polygonCounts.length(), vertices, polygonCounts, polygonConnects, parent);

    StandardSurface::AssignShaderTo(cubeObj);

	return cubeObj;
}
