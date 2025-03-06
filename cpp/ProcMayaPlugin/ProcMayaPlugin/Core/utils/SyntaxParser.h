#pragma once

#include <maya/MArgDatabase.h>

class SyntaxParser {

public:
	static void ParseFloat(MArgDatabase argData, const char* flag, float* value);
	static void ParseDouble(MArgDatabase argData, const char* flag, double* value);
	static void ParseMString(MArgDatabase argData, const char* flag, MString* value);
};