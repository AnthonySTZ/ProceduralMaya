#pragma once
#define MNoVersionString
#include <maya/MFnPlugin.h>
#include <maya/MGlobal.h>

#include <vector>
#include "Core/Nodes/CubeNode.h"
#include "Core/Nodes/Transform.h"
#include "Core/Nodes/Merge.h"

struct CommandEntry {
	const char* command;
	MCreatorFunction creator;
	MCreateSyntaxFunction syntax;
};

class Commands{

public:
	static MStatus registerAllCommands(MFnPlugin& fnPlugin);
	static MStatus deregisterAllCommands(MFnPlugin& fnPlugin);
};

extern const std::vector<CommandEntry> commands;