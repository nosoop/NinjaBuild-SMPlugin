#include <sourcemod>

#pragma semicolon 1
#pragma newdecls required

public Plugin myinfo = {
    name        = "",
    author      = "",
    description = "",
    version     = "0.0.0",
    url         = ""
};

public void OnPluginStart()
{
    PrintToServer("Hello, World!");
}
