#include <maya/MFnPlugin.h>
#include <maya/MGlobal.h>

#include "Command.h"

const MString RenderCmd = "renderGraph";

MStatus initializePlugin(MObject obj) {
	
	const char* pluginVendor = "AnthonySTZ";
	const char* pluginVersion = "0.0.1";

	MFnPlugin fnPlugin(obj, pluginVendor, pluginVersion);
	MGlobal::displayInfo("Plugin has been initialized!");

	MStatus status = fnPlugin.registerCommand(RenderCmd, Command::creator);

	return MS::kSuccess;

}

MStatus uninitializePlugin(MObject obj) {

	MFnPlugin plugin(obj);
	CHECK_MSTATUS(plugin.deregisterCommand(RenderCmd));
	MGlobal::displayInfo("Plugin has been uninitialize!");

	return MS::kSuccess;

}