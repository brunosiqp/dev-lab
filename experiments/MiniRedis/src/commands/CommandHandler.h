#pragma once

#include vector
#include string
#include ..storeKeyValueStore.h

class CommandHandler {

public
    static stdstring handle(const stdvectorstdstring& tokens, KeyValueStore store);
};