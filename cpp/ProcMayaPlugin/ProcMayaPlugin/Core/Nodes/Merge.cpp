#include "Merge.h"

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

static MObject getChildOf(MObject obj) {
    MFnDagNode dagNode1(obj);
    if (dagNode1.childCount() > 0) {
        MObject shapeObj1 = dagNode1.child(0);
        return shapeObj1;
    }
    return obj;
}

MObject Merge::MergeObjs(MObject obj1, MObject obj2)
{
    MObject shapeObj1 = getChildOf(obj1);
    MObject shapeObj2 = getChildOf(obj2);

    // Now use MFnMesh on the shape nodes
    MFnMesh meshFn1(shapeObj1);
    MFnMesh meshFn2(shapeObj2);

    MPointArray vertices1, vertices2;
    meshFn1.getPoints(vertices1);
    meshFn2.getPoints(vertices2);

    MPointArray combinedVertices = vertices1;
    for (unsigned int i = 0; i < (unsigned int)vertices2.length(); i++) {
        combinedVertices.append(vertices2[i]);
    }

    MIntArray polygonCounts;
    MIntArray polygonConnects;

    MIntArray tmpVertices;

    for (unsigned int i = 0; i < (unsigned int)meshFn1.numPolygons(); i++) {
        meshFn1.getPolygonVertices(i, tmpVertices);

        for (unsigned int j = 0; j < (unsigned int)tmpVertices.length(); j++) {
            polygonConnects.append(tmpVertices[j]);
        }

        polygonCounts.append(tmpVertices.length());
    }

    unsigned int vertexOffset = vertices1.length(); 

    for (unsigned int i = 0; i < (unsigned int)meshFn2.numPolygons(); i++) { 
        meshFn2.getPolygonVertices(i, tmpVertices);

        for (unsigned int j = 0; j < (unsigned int)tmpVertices.length(); j++) {
            polygonConnects.append(tmpVertices[j] + vertexOffset);
        }

        polygonCounts.append(tmpVertices.length());
    }

    
    int numPolygons = polygonCounts.length();
    
    MGlobal::displayInfo(MString("Num Polygons : ") + numPolygons);
    MGlobal::displayInfo(MString("Num Vertices1 : ") + vertices1.length());
    MGlobal::displayInfo(MString("Num Vertices2: ") + vertices2.length());
    MGlobal::displayInfo(MString("Polygon Counts: ") + polygonCounts.length());
    MGlobal::displayInfo(MString("Polygon Connects: ") + polygonConnects.length());

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
