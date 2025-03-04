#include "Command.h"

void* Command::creator()
{
    return new Command();
}

MStatus Command::doIt(const MArgList& args) {

    MStatus status = ProcMaya::Render();
    return status;
}