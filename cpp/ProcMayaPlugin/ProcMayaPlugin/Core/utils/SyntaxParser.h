#pragma once

#include <maya/MArgDatabase.h>

class SyntaxParser {

public:
	static void ParseDouble(MArgDatabase argData, const char* flag, double* value);
	static void ParseMString(MArgDatabase argData, const char* flag, MString* value);
	static void ParseUnsigned(MArgDatabase argData, const char* flag, unsigned int* value);
};