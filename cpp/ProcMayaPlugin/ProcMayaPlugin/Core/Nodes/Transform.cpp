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
    MFloatVector rotate(0.0f, 0.0f, 0.0f);
    MFloatVector scale(1.0f, 1.0f, 1.0f);

    SyntaxParser::ParseMString(argData, "-obj", &nodeName);

    SyntaxParser::ParseFloat(argData, "-tx", &translate.x);
    SyntaxParser::ParseFloat(argData, "-ty", &translate.y);
    SyntaxParser::ParseFloat(argData, "-tz", &translate.z);

    SyntaxParser::ParseFloat(argData, "-rx", &rotate.x);
    SyntaxParser::ParseFloat(argData, "-ry", &rotate.y);
    SyntaxParser::ParseFloat(argData, "-rz", &rotate.z);

    SyntaxParser::ParseFloat(argData, "-sx", &scale.x);
    SyntaxParser::ParseFloat(argData, "-sy", &scale.y);
    SyntaxParser::ParseFloat(argData, "-sz", &scale.z);

    MSelectionList sel;
    CHECK_MSTATUS(sel.add(nodeName));
    MObject nodeObj;
    CHECK_MSTATUS(sel.getDependNode(0, nodeObj));
    if (nodeObj.isNull()) {
        MGlobal::displayError("Invalid object name: " + nodeName);
        return MS::kFailure;
    }

    transformMesh(nodeObj, translate, rotate, scale);
    MFnDependencyNode depNode(nodeObj);
    setResult(depNode.name());

    return MS::kSuccess;
}



void TransformNode::transformMesh(MObject obj, MFloatVector translate, MFloatVector rotate, MFloatVector scale)
{
    MFnDependencyNode depNode(obj);
    MGlobal::displayInfo(MString("Transform Obj : ") + depNode.name());

    MGlobal::displayInfo(MString("Translate : ") + translate.x + MString(" ") + translate.y + MString(" ") + translate.z);
    MGlobal::displayInfo(MString("Rotate : ") + rotate.x + MString(" ") + rotate.y + MString(" ") + rotate.z);
    MGlobal::displayInfo(MString("Scale : ") + scale.x + MString(" ") + scale.y + MString(" ") + scale.z);

    MItMeshVertex vert_it(obj);
    for (; !vert_it.isDone(); vert_it.next()) {
        MPoint position = vert_it.position(MSpace::kWorld);
        position += translate;
        vert_it.setPosition(position, MSpace::kObject);
    }

    return;
}
