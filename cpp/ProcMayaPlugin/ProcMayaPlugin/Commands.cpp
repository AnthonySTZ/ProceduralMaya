#include "Commands.h"

MStatus Commands::registerAllCommands(MFnPlugin& fnPlugin)
{   
    CHECK_MSTATUS(fnPlugin.registerCommand("cubeNode", CubeNode::creator, CubeNode::syntax));

    return MS::kSuccess;
}

MStatus Commands::deregisterAllCommands(MFnPlugin& fnPlugin)
{
    CHECK_MSTATUS(fnPlugin.deregisterCommand("cubeNode"));

    return MS::kSuccess;
}
