#include "SyntaxParser.h"

void SyntaxParser::ParseDouble(MArgDatabase argData, const char* flag, double* value)
{
    if (argData.isFlagSet(flag)) {
        CHECK_MSTATUS(argData.getFlagArgument(flag, 0, *value));
    }
}

void SyntaxParser::ParseMString(MArgDatabase argData, const char* flag, MString* value)
{
    if (argData.isFlagSet(flag)) {
        CHECK_MSTATUS(argData.getFlagArgument(flag, 0, *value));
    }
}

void SyntaxParser::ParseInt(MArgDatabase argData, const char* flag, int* value)
{
    if (argData.isFlagSet(flag)) {
        CHECK_MSTATUS(argData.getFlagArgument(flag, 0, *value));
    }
}