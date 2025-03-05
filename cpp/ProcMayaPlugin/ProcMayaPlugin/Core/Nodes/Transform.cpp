#include "Transform.h"

#include <string>

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
    MFloatVector translate(0.0f, 0.0f, 0.0f);
    double rotate[3] = { 0.0, 0.0, 0.0 };
    double scale[3] = { 1.0, 1.0, 1.0 };

    SyntaxParser::ParseMString(argData, "-obj", &nodeName);

    SyntaxParser::ParseFloat(argData, "-tx", &translate.x);
    SyntaxParser::ParseFloat(argData, "-ty", &translate.y);
    SyntaxParser::ParseFloat(argData, "-tz", &translate.z);

    SyntaxParser::ParseDouble(argData, "-rx", &rotate[0]);
    SyntaxParser::ParseDouble(argData, "-ry", &rotate[1]);
    SyntaxParser::ParseDouble(argData, "-rz", &rotate[2]);

    SyntaxParser::ParseDouble(argData, "-sx", &scale[0]);
    SyntaxParser::ParseDouble(argData, "-sy", &scale[1]);
    SyntaxParser::ParseDouble(argData, "-sz", &scale[2]);

    MSelectionList sel;
    CHECK_MSTATUS(sel.add(nodeName));
    MObject nodeObj;
    CHECK_MSTATUS(sel.getDependNode(0, nodeObj));
    if (nodeObj.isNull()) {
        MGlobal::displayError("Invalid object name: " + nodeName);
        return MS::kFailure;
    }

    MTransformationMatrix transformMatrix;
    transformMatrix.setTranslation(translate, MSpace::kWorld);
    transformMatrix.setRotation(rotate, MTransformationMatrix::RotationOrder::kXYZ);
    transformMatrix.setScale(scale, MSpace::kWorld);

    transformMesh(nodeObj, transformMatrix);
    MFnDependencyNode depNode(nodeObj);
    setResult(depNode.name());

    return MS::kSuccess;
}



void TransformNode::transformMesh(MObject obj, MTransformationMatrix transformMatrix)
{
    MFnDependencyNode depNode(obj);
    MGlobal::displayInfo(MString("Transform Obj : ") + depNode.name());

    MItMeshVertex vert_it(obj);
    for (; !vert_it.isDone(); vert_it.next()) {
        MPoint position = vert_it.position(MSpace::kWorld);
        position *= transformMatrix.asScaleMatrix();
        position *= transformMatrix.asRotateMatrix();
        position += transformMatrix.getTranslation(MSpace::kWorld);
        vert_it.setPosition(position, MSpace::kObject);
    }

    return;
}
