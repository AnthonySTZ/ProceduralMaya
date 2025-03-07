#include "Transform.h"

#include <string>

#include <chrono>
using namespace std::chrono;

void* TransformNode::creator() {
    return new TransformNode;
}

MSyntax TransformNode::syntax()
{
    MSyntax syntax;
    syntax.addFlag("-obj", "-object", MSyntax::kString);

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

MStatus TransformNode::doIt(const MArgList& args)
{
    MArgDatabase argData(syntax(), args);

    MString nodeName;
    MVector translate(0.0f, 0.0f, 0.0f);
    double rotate[3] = { 0.0, 0.0, 0.0 };
    double scale[3] = { 1.0, 1.0, 1.0 };

    SyntaxParser::ParseMString(argData, "-obj", &nodeName);

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

    rotate[0] = Math::toRadians(rotate[0]);
    rotate[1] = Math::toRadians(rotate[1]);
    rotate[2] = Math::toRadians(rotate[2]);

    MTransformationMatrix transformMatrix;
    transformMatrix.setTranslation(translate, MSpace::kWorld);
    transformMatrix.setRotation(rotate, MTransformationMatrix::RotationOrder::kXYZ);
    transformMatrix.setScale(scale, MSpace::kWorld);
    

    MGlobal::displayInfo(MString("Translate : ") + translate.x + " " + translate.y + " " + translate.z);
    MGlobal::displayInfo(MString("Rotate : ") + rotate[0] + " " + rotate[1] + " " + rotate[2]);
    MGlobal::displayInfo(MString("Scale : ") + scale[0] + " " + scale[1] + " " + scale[2]);

    transformMesh(nodeObj, transformMatrix);
    setResult(nodeName);

    return MS::kSuccess;
}


void TransformNode::transformMesh(MObject obj, MTransformationMatrix transformMatrix)
{
    MMatrix fullTransformMatrix = transformMatrix.asMatrix();

    MFnMesh fnMesh = MayaObject::getMeshFrom(obj);
    MPointArray points;

    fnMesh.getPoints(points, MSpace::kWorld);

    auto start = high_resolution_clock::now();

    tbb::parallel_for(tbb::blocked_range<size_t>(0, points.length()), [&](const tbb::blocked_range<size_t>& range) {
            for (size_t i = range.begin(); i < range.end(); i++) {
                points[i] *= fullTransformMatrix;
            }
        });

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);


    fnMesh.setPoints(points, MSpace::kWorld);
    MGlobal::displayInfo(MString("Mesh transformed successfully in ") + duration.count() + MString("ms."));

    return;
}

// command transformNode -obj "pCube1" -tx 1.0