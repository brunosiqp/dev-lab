#pragma once

#include "../store/KeyValueStore.h"

class TcpServer {
private:
    int port;
    KeyValueStore* store;

public:
    TcpServer(int port, KeyValueStore* store);
    void start();
};