#include "server/TcpServer.h"
#include "store/KeyValueStore.h"

int main() {
    KeyValueStore store;
    TcpServer server(6379, &store);

    server.start();
}