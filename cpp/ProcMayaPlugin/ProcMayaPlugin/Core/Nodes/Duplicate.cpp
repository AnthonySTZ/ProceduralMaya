#include "Duplicate.h"

void* Duplicate::creator()
{
    return new Duplicate;
}

MSyntax Duplicate::syntax()
{
    MSyntax syntax;
    syntax.addFlag("-obj", "-object", MSyntax::kString);
    syntax.addFlag("-a", "-amount", MSyntax::kUnsigned);

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
    unsigned int amount = 0;
    MVector translate(0.0f, 0.0f, 0.0f);
    double rotate[3] = { 0.0, 0.0, 0.0 };
    double scale[3] = { 1.0, 1.0, 1.0 };

    SyntaxParser::ParseMString(argData, "-obj", &nodeName);
    SyntaxParser::ParseUnsigned(argData, "-a", &amount);

    SyntaxParser::ParseDouble(argData, "-tx", &translate.x);
    SyntaxParser::ParseDouble(argData, "-ty", &translate.y);
    SyntaxParser::ParseDouble(argData, "-tz", &translate.z);

    SyntaxParser::ParseDouble(argData, "-rx", &rotate[0]);
    SyntaxParser::ParseDouble(argData, "-ry", &rotate[1]);
    SyntaxParser::ParseDouble(argData, "-rz", &rotate[2]);

    SyntaxParser::ParseDouble(argData, "-sx", &scale[0]);
    SyntaxParser::ParseDouble(argData, "-sy", &scale[1]);
    SyntaxParser::ParseDouble(argData, "-sz", &scale[2]);
}