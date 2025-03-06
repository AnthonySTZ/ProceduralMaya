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
    return MS::kSuccess;
}
