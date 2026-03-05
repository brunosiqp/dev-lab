cmake_minimum_required(VERSION 3.10)
project(mini_redis)

set(CMAKE_CXX_STANDARD 17)

add_executable(mini_redis
    src/main.cpp
    src/server/TcpServer.cpp
    src/store/KeyValueStore.cpp
    src/protocol/CommandParser.cpp
    src/commands/CommandHandler.cpp
)