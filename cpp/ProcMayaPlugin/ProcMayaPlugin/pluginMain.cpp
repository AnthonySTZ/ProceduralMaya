#include <maya/MFnPlugin.h>
#include <maya/MGlobal.h>

MStatus initializePlugin(MObject obj) {
	
	const char* pluginVendor = "AnthonySTZ";
	const char* pluginVersion = "0.0.1";

	MFnPlugin fnPlugin(obj, pluginVendor, pluginVersion);

	MGlobal::displayInfo("Plugin has been initialized!");

	return MS::kSuccess;

}

MStatus uninitializePlugin(MObject obj) {

	MGlobal::displayInfo("Plugin has been uninitialize!");

	return MS::kSuccess;

}