#pragma once
#define MNoVersionString
#include <maya/MFnPlugin.h>
#include <maya/MGlobal.h>
#include "Core/Nodes/CubeNode.h"

class Commands{

public:
	static MStatus registerAllCommands(MFnPlugin& fnPlugin);
	static MStatus deregisterAllCommands(MFnPlugin& fnPlugin);
};