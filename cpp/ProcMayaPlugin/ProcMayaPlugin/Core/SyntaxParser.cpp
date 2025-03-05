#include "SyntaxParser.h"

void SyntaxParser::ParseFloat(MArgDatabase argData, const char* flag, float* value)
{
    if (argData.isFlagSet(flag)) {
        double tmp_value;
        CHECK_MSTATUS(argData.getFlagArgument(flag, 0, tmp_value));
        *value = float(tmp_value);
    }
}

void SyntaxParser::ParseMString(MArgDatabase argData, const char* flag, MString* value)
{
    if (argData.isFlagSet(flag)) {
        CHECK_MSTATUS(argData.getFlagArgument(flag, 0, *value));
    }
}