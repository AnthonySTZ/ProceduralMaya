#pragma once

#include <maya/MArgDatabase.h>

class SyntaxParser {

public:
	static void ParseFloat(MArgDatabase argData, const char* flag, float* value);
};