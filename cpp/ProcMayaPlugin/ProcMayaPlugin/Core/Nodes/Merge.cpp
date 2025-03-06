#include "Merge.h"

#include <chrono>
using namespace std::chrono;

void* Merge::creator()
{
    return new Merge;
}

MSyntax Merge::syntax()
{
    MSyntax syntax;
    syntax.addFlag("-f", "-first", MSyntax::kString);
    syntax.addFlag("-s", "-second", MSyntax::kString);
    return syntax;
}

MStatus Merge::doIt(const MArgList& args)
{
    MArgDatabase argData(syntax(), args);

    MString node1Name;
    MString node2Name;

    SyntaxParser::ParseMString(argData, "-f", &node1Name);
    SyntaxParser::ParseMString(argData, "-s", &node2Name);

    if (node1Name.isEmpty() || node2Name.isEmpty()) return MS::kFailure;


    MObject node1Obj;
    MObject node2Obj;
    CHECK_MSTATUS(MayaObject::FromName(node1Name, &node1Obj));
    CHECK_MSTATUS(MayaObject::FromName(node2Name, &node2Obj));

    MObject mergedObj = MergeObjs(node1Obj, node2Obj);
    MFnDependencyNode depNode(mergedObj);
    setResult(depNode.name());

    return MS::kSuccess;
}

MObject Merge::MergeObjs(MObject obj1, MObject obj2)
{
    MFnMesh meshFn1 = MayaObject::getMeshFrom(obj1);
    MFnMesh meshFn2 = MayaObject::getMeshFrom(obj2);

    MPointArray vertices1, vertices2;
    meshFn1.getPoints(vertices1);
    meshFn2.getPoints(vertices2);

    MPointArray combinedVertices = vertices1;
    for (unsigned int i = 0; i < (unsigned int)vertices2.length(); i++) {
        combinedVertices.append(vertices2[i]);
    }    

    auto start = high_resolution_clock::now();

    MIntArray polygonCounts, polygonConnects;
    meshFn1.getVertices(polygonCounts, polygonConnects);

    MIntArray polygonCounts2, polygonConnects2;
    meshFn2.getVertices(polygonCounts2, polygonConnects2);

    for (unsigned int i = 0; i < polygonCounts2.length(); i++) {
        polygonCounts.append(polygonCounts2[i]);
    }
    unsigned int vertexOffset = vertices1.length();
    for (unsigned int i = 0; i < polygonConnects2.length(); i++) {
        polygonConnects.append(polygonConnects2[i] + vertexOffset);
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    MGlobal::displayInfo(MString("Merge in ") + duration.count() + MString("ms."));

    int numPolygons = polygonCounts.length();

    // Create new mesh
    MFnMesh newMeshFn;
    MObject newObj = newMeshFn.create(combinedVertices.length(), numPolygons, combinedVertices, polygonCounts, polygonConnects, MObject::kNullObj);
    StandardSurface::AssignShaderTo(newObj);

    // Delete old meshes
    MFnDependencyNode dep1Node(obj1);
    MFnDependencyNode dep2Node(obj2);
    MGlobal::executeCommand(MString("delete ") + dep1Node.name() + ";");
    MGlobal::executeCommand(MString("delete ") + dep2Node.name() + ";");

    return newObj;

}

// command mergeNode -f "pCube1" -s "pCube2"
// Merge in 22944ms.
// Merge in 14684ms.