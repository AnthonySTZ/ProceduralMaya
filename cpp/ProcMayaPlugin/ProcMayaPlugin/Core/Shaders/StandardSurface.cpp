#include "StandardSurface.h"

void StandardSurface::AssignShaderTo(MObject fnObj)
{
    MFnDagNode dagNode(fnObj);
    MString objName = dagNode.fullPathName();

    MString selectCommand = "select -r " + objName + ";";
    MGlobal::executeCommand(selectCommand, true);

    MString command = "hyperShade -assign standardSurface1 " + objName + ";";
    MGlobal::executeCommand(command, true);

    MString conformNormalCommand = "polyNormal -normalMode 2 -userNormalMode 0 " + objName + ";";
    MGlobal::executeCommand(conformNormalCommand, true);
    MGlobal::executeCommand("expandPolyGroupSelection; polySetToFaceNormal;", true);

    MGlobal::executeCommand("select -cl", true);
    MGlobal::executeCommand("refresh;", true);
}
