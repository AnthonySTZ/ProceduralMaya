#include "Commands.h"

const std::vector<CommandEntry> commands = {
        {"cubeNode", CubeNode::creator, CubeNode::syntax},
        {"transformNode", TransformNode::creator, TransformNode::syntax}
};

MStatus Commands::registerAllCommands(MFnPlugin& fnPlugin)
{   
    for (const CommandEntry& cmd : commands) {
        CHECK_MSTATUS(fnPlugin.registerCommand(cmd.command, cmd.creator, cmd.syntax));
    }
    return MS::kSuccess;
}

MStatus Commands::deregisterAllCommands(MFnPlugin& fnPlugin)
{
    for (const CommandEntry& cmd : commands) {
        CHECK_MSTATUS(fnPlugin.deregisterCommand(cmd.command));
    }

    return MS::kSuccess;
}
