#include "Commands.h"


MStatus initializePlugin(MObject obj) {
	
	const char* pluginVendor = "AnthonySTZ";
	const char* pluginVersion = "0.0.1";

	MFnPlugin fnPlugin(obj, pluginVendor, pluginVersion);
	MGlobal::displayInfo("Plugin has been initialized!");

	Commands::registerAllCommands(fnPlugin);

	return MS::kSuccess;

}

MStatus uninitializePlugin(MObject obj) {

	MFnPlugin plugin(obj);
	Commands::deregisterAllCommands(plugin);
	MGlobal::displayInfo("Plugin has been uninitialize!");

	return MS::kSuccess;

}