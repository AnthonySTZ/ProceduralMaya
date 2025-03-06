#include "Merge.h"

void* Merge::creator()
{
    return new Merge;
}

MSyntax Merge::syntax()
{
    MSyntax syntax;
    syntax.addFlag("-obj1", "-object1", MSyntax::kString);
    syntax.addFlag("-obj2", "-object2", MSyntax::kString);
    return syntax;
}

MStatus Merge::doIt(const MArgList& args)
{
    MArgDatabase argData(syntax(), args);

    MString node1Name;
    MString node2Name;

    SyntaxParser::ParseMString(argData, "-obj1", &node1Name);
    SyntaxParser::ParseMString(argData, "-obj2", &node2Name);

    if (node1Name.isEmpty() || node2Name.isEmpty()) return MS::kFailure;

    

    return MS::kSuccess;
}

void Merge::MergeObjs(MObject obj1, MObject obj2) 
{

}
