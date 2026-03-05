#include "CommandHandler.h"

std::string CommandHandler::handle(const std::vector<std::string>& tokens, KeyValueStore* store) {

    if (tokens.empty()) {
        return "ERR empty command\n";
    }

    std::string cmd = tokens[0];

    if (cmd == "PING") {
        return "PONG\n";
    }

    if (cmd == "SET") {

        if (tokens.size() < 3) {
            return "ERR wrong arguments\n";
        }

        store->set(tokens[1], tokens[2]);
        return "OK\n";
    }

    if (cmd == "GET") {

        if (tokens.size() < 2) {
            return "ERR wrong arguments\n";
        }

        return store->get(tokens[1]);
    }

    if (cmd == "DEL") {

        if (tokens.size() < 2) {
            return "ERR wrong arguments\n";
        }

        bool removed = store->del(tokens[1]);

        return removed ? "1\n" : "0\n";
    }

    return "ERR unknown command\n";
}