#include "Transform.h"

#include <string>

void* TransformNode::creator() {
    return new TransformNode;
}

MSyntax TransformNode::syntax()
{
    MSyntax syntax;
    syntax.addFlag("-t", "-translate", MSyntax::kDouble);
    syntax.addFlag("-r", "-rotate", MSyntax::kDouble);
    syntax.addFlag("-s", "-scale", MSyntax::kDouble);
    return syntax;
}

MStatus TransformNode::doIt(const MArgList& args)
{
    MArgDatabase argData(syntax(), args);
    MFloatVector translate(0.0f, 0.0f, 0.0f);
    MFloatVector rotate(0.0f, 0.0f, 0.0f);
    MFloatVector scale(1.0f, 1.0f, 1.0f);

    if (argData.isFlagSet("-t")) {
        double tx, ty, tz;
        CHECK_MSTATUS(argData.getFlagArgument("-t", 0, tx));
        CHECK_MSTATUS(argData.getFlagArgument("-t", 1, ty));
        CHECK_MSTATUS(argData.getFlagArgument("-t", 2, tz));
        translate.x = tx;
        translate.y = ty;
        translate.z = tz;
    }

    MObject mesh = transformMesh(translate, rotate, scale);
    MFnDependencyNode depNode(mesh);
    setResult(depNode.name());

    return MS::kSuccess;
}



MObject TransformNode::transformMesh(MFloatVector translate, MFloatVector rotate, MFloatVector scale)
{
    MGlobal::displayInfo(MString("Translate : ") + translate.x + MString(" ") + translate.y + MString(" ") + translate.z);
    MGlobal::displayInfo(MString("Rotate : ") + rotate.x + MString(" ") + rotate.y + MString(" ") + rotate.z);
    MGlobal::displayInfo(MString("Scale : ") + scale.x + MString(" ") + scale.y + MString(" ") + scale.z);

    return MObject();
}
