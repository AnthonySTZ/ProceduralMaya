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
	float width = 1.0;
	float height = 1.0;
	float depth = 1.0;

    SyntaxParser::ParseFloat(argData, "-w", &width);
    SyntaxParser::ParseFloat(argData, "-h", &height);
    SyntaxParser::ParseFloat(argData, "-d", &depth);

    MObject mesh = CreateCube(width, height, depth);
    MFnDependencyNode depNode(mesh);
	setResult(depNode.name());

	return MS::kSuccess;
}



MObject CubeNode::CreateCube(float width, float height, float depth)
{
    double xOffset = width / 2.0f;
    double yOffset = height / 2.0f;
    double zOffset = depth / 2.0f;

    MFloatPointArray vertices;
    vertices.append(MFloatPoint(-xOffset, -yOffset, -zOffset));  // 0
    vertices.append(MFloatPoint(xOffset, -yOffset, -zOffset));  // 1
    vertices.append(MFloatPoint(xOffset, yOffset, -zOffset));  // 2
    vertices.append(MFloatPoint(-xOffset, yOffset, -zOffset));  // 3
    vertices.append(MFloatPoint(-xOffset, -yOffset, zOffset));  // 4
    vertices.append(MFloatPoint(xOffset, -yOffset, zOffset));  // 5
    vertices.append(MFloatPoint(xOffset, yOffset, zOffset));  // 6
    vertices.append(MFloatPoint(-xOffset, yOffset, zOffset));  // 7

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
