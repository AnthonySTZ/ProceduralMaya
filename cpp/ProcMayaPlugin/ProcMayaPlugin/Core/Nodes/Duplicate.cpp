#include "Duplicate.h"

#include <chrono>
using namespace std::chrono;

void* Duplicate::creator()
{
    return new Duplicate;
}

MSyntax Duplicate::syntax()
{
    MSyntax syntax;
    syntax.addFlag("-obj", "-object", MSyntax::kString);
    syntax.addFlag("-a", "-amount", MSyntax::kLong);

    syntax.addFlag("-tx", "-translateX", MSyntax::kDouble);
    syntax.addFlag("-ty", "-translateY", MSyntax::kDouble);
    syntax.addFlag("-tz", "-translateZ", MSyntax::kDouble);

    syntax.addFlag("-rx", "-rotateX", MSyntax::kDouble);
    syntax.addFlag("-ry", "-rotateY", MSyntax::kDouble);
    syntax.addFlag("-rz", "-rotateZ", MSyntax::kDouble);

    syntax.addFlag("-sx", "-scaleX", MSyntax::kDouble);
    syntax.addFlag("-sy", "-scaleY", MSyntax::kDouble);
    syntax.addFlag("-sz", "-scaleZ", MSyntax::kDouble);
    return syntax;
}

MStatus Duplicate::doIt(const MArgList& args)
{
    MArgDatabase argData(syntax(), args);

    MString nodeName;
    int amount = 0;
    MVector translate(0.0f, 0.0f, 0.0f);
    double rotate[3] = { 0.0, 0.0, 0.0 };
    double scale[3] = { 1.0, 1.0, 1.0 };

    SyntaxParser::ParseMString(argData, "-obj", &nodeName);
    SyntaxParser::ParseInt(argData, "-a", &amount);

    SyntaxParser::ParseDouble(argData, "-tx", &translate.x);
    SyntaxParser::ParseDouble(argData, "-ty", &translate.y);
    SyntaxParser::ParseDouble(argData, "-tz", &translate.z);

    SyntaxParser::ParseDouble(argData, "-rx", &rotate[0]);
    SyntaxParser::ParseDouble(argData, "-ry", &rotate[1]);
    SyntaxParser::ParseDouble(argData, "-rz", &rotate[2]);

    SyntaxParser::ParseDouble(argData, "-sx", &scale[0]);
    SyntaxParser::ParseDouble(argData, "-sy", &scale[1]);
    SyntaxParser::ParseDouble(argData, "-sz", &scale[2]);

    MObject nodeObj;
    CHECK_MSTATUS(MayaObject::FromName(nodeName, &nodeObj));    

    MTransformationMatrix transformMatrix;
    transformMatrix.setTranslation(translate, MSpace::kWorld);
    transformMatrix.setRotation(rotate, MTransformationMatrix::RotationOrder::kXYZ);
    transformMatrix.setScale(scale, MSpace::kWorld);

    MObject new_obj = DuplicateMesh(nodeObj, amount, transformMatrix);
    MFnDependencyNode depNode(new_obj);
    setResult(depNode.name());

    return MS::kSuccess;
}

MObject Duplicate::DuplicateMesh(MObject obj, int amount, MTransformationMatrix transformMatrix)
{
    MMatrix fullTransformMatrix = transformMatrix.asMatrix();

    MFnMesh meshFn = MayaObject::getMeshFrom(obj);

    MPointArray baseVertices;
    meshFn.getPoints(baseVertices, MSpace::kWorld);

    MPointArray combinedVertices;

    MIntArray basePolygonCounts, basePolygonConnects, combinedPolygonCounts, combinedPolygonConnects;
    meshFn.getVertices(basePolygonCounts, basePolygonConnects);   

    auto start = high_resolution_clock::now();

    for (unsigned int i = 0; i < amount; i++) {
        for (unsigned int j = 0; j < (unsigned int)baseVertices.length(); j++) {
            combinedVertices.append(baseVertices[j]);
        }
        for (unsigned int j = 0; j < basePolygonCounts.length(); j++) {
            combinedPolygonCounts.append(basePolygonCounts[j]);
        }
        unsigned int vertexOffset = baseVertices.length() * i;
        for (unsigned int j = 0; j < basePolygonConnects.length(); j++) {
            combinedPolygonConnects.append(basePolygonConnects[j] + vertexOffset);
        }
        for (unsigned int k = 0; k < baseVertices.length(); k++) {
            baseVertices[k] *= fullTransformMatrix;
        }
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    MGlobal::displayInfo(MString("Duplicate in ") + duration.count() + MString("ms."));

    int numPolygons = combinedPolygonCounts.length();

    MFnMesh newMeshFn;
    MObject newObj = newMeshFn.create(combinedVertices.length(), numPolygons, combinedVertices, combinedPolygonCounts, combinedPolygonConnects, MObject::kNullObj);
    StandardSurface::AssignShaderTo(newObj);

    // delete old obj
    MFnDependencyNode depNode(obj);
    MGlobal::executeCommand(MString("delete ") + depNode.name() + ";");

    return newObj;
}

// command duplicateNode -obj "pCube1" -a 200 -tx 1.2 -ry 45
// Duplicate in 138740ms with 6146 vertices.