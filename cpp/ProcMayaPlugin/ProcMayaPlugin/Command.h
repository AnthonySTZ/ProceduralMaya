#pragma once

#include <maya/MpxCommand.h>
#include "Core/ProcMaya.h"

class Command : public MPxCommand {

public:
	static void* creator();
	MStatus doIt(const MArgList& args) override;
};