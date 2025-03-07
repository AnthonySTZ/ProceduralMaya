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

    SyntaxParser::ParseDouble(argData, "-w", &width);
    SyntaxParser::ParseDouble(argData, "-h", &height);
    SyntaxParser::ParseDouble(argData, "-d", &depth);

    MObject mesh = CreateCube(width, height, depth);
    MFnDependencyNode depNode(mesh);
	setResult(depNode.name());

	return MS::kSuccess;
}



MObject CubeNode::CreateCube(double width, double height, double depth)
{
    double xOffset = width / 2.0f;
    double yOffset = height / 2.0f;
    double zOffset = depth / 2.0f;

    MPointArray vertices;
    vertices.append(MPoint(-xOffset, -yOffset, -zOffset));  // 0
    vertices.append(MPoint(xOffset, -yOffset, -zOffset));  // 1
    vertices.append(MPoint(xOffset, yOffset, -zOffset));  // 2
    vertices.append(MPoint(-xOffset, yOffset, -zOffset));  // 3
    vertices.append(MPoint(-xOffset, -yOffset, zOffset));  // 4
    vertices.append(MPoint(xOffset, -yOffset, zOffset));  // 5
    vertices.append(MPoint(xOffset, yOffset, zOffset));  // 6
    vertices.append(MPoint(-xOffset, yOffset, zOffset));  // 7

    MIntArray polygonCounts;
    polygonCounts.append(4);  // First face
    polygonCounts.append(4);  // Second face
    polygonCounts.append(4);  // Third face
    polygonCounts.append(4);  // Fourth face
    polygonCounts.append(4);  // Fifth face
    polygonCounts.append(4);  // Sixth face

    MIntArray polygonConnects;
    polygonConnects.append(0); polygonConnects.append(1); polygonConnects.append(2); polygonConnects.append(3);  // First face
    polygonConnects.append(4); polygonConnects.append(5); polygonConnects.append(6); polygonConnects.append(7);  // Second face
    polygonConnects.append(0); polygonConnects.append(1); polygonConnects.append(5); polygonConnects.append(4);  // Third face
    polygonConnects.append(1); polygonConnects.append(2); polygonConnects.append(6); polygonConnects.append(5);  // Fourth face
    polygonConnects.append(2); polygonConnects.append(3); polygonConnects.append(7); polygonConnects.append(6);  // Fifth face
    polygonConnects.append(3); polygonConnects.append(0); polygonConnects.append(4); polygonConnects.append(7);  // Sixth face

    MFnMesh fnMesh;
    MObject cubeObj = fnMesh.create(vertices.length(), polygonCounts.length(), vertices, polygonCounts, polygonConnects, MObject::kNullObj);

    StandardSurface::AssignShaderTo(cubeObj);

	return cubeObj;
}
