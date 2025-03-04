#include "ProcMaya.h"

MStatus ProcMaya::Render()
{
	MGlobal::displayInfo("Render!");

	return MS::kSuccess;
}
