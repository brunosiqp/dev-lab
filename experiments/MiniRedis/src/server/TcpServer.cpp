#include "TcpServer.h"
#include "../protocol/CommandParser.h"
#include "../commands/CommandHandler.h"

#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>

TcpServer::TcpServer(int port, KeyValueStore* store) {
    this->port = port;
    this->store = store;
}

void TcpServer::start() {

    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);

    server_fd = socket(AF_INET, SOCK_STREAM, 0);

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(port);

    bind(server_fd, (struct sockaddr*)&address, sizeof(address));
    listen(server_fd, 3);

    std::cout << "MiniRedis rodando na porta " << port << std::endl;

    while (true) {

        new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen);

        char buffer[1024] = {0};
        read(new_socket, buffer, 1024);

        std::string request(buffer);

        auto tokens = CommandParser::parse(request);
        std::string response = CommandHandler::handle(tokens, store);

        send(new_socket, response.c_str(), response.size(), 0);
        close(new_socket);
    }
}