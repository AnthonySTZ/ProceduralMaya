#include "Duplicate.h"

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
    setResult(nodeName);

    return MS::kSuccess;
}

MObject Duplicate::DuplicateMesh(MObject obj, int amount, MTransformationMatrix transformMatrix)
{

    MObject shapeObj = MayaObject::getChildOf(obj);
    MFnMesh meshFn1(shapeObj);

    return MObject();
}
