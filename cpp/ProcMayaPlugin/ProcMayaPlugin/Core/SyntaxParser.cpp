#include "SyntaxParser.h"

void SyntaxParser::ParseDouble(MArgDatabase argData, const char* flag, double* value)
{
    if (argData.isFlagSet(flag)) {
        double tmp_value;
        CHECK_MSTATUS(argData.getFlagArgument(flag, 0, tmp_value));
        *value = tmp_value;
    }
}

void SyntaxParser::ParseMString(MArgDatabase argData, const char* flag, MString* value)
{
    if (argData.isFlagSet(flag)) {
        CHECK_MSTATUS(argData.getFlagArgument(flag, 0, *value));
    }
}