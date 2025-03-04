#include <maya/MFnPlugin.h>
#include <maya/MGlobal.h>

#include "Command.h"

const MString GraphCmd = "nodeGraph";

MStatus initializePlugin(MObject obj) {
	
	const char* pluginVendor = "AnthonySTZ";
	const char* pluginVersion = "0.0.1";

	MFnPlugin fnPlugin(obj, pluginVendor, pluginVersion);
	MGlobal::displayInfo("Plugin has been initialized!");

	MStatus status = fnPlugin.registerCommand(GraphCmd, Command::creator);

	return MS::kSuccess;

}

MStatus uninitializePlugin(MObject obj) {

	MFnPlugin plugin(obj);
	CHECK_MSTATUS(plugin.deregisterCommand(GraphCmd));
	MGlobal::displayInfo("Plugin has been uninitialize!");

	return MS::kSuccess;

}