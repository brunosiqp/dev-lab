#include "KeyValueStore.h"

void KeyValueStore::set(const std::string& key, const std::string& value) {
    store[key] = value;
}

std::string KeyValueStore::get(const std::string& key) {

    if (store.find(key) == store.end()) {
        return "(nil)\n";
    }

    return store[key] + "\n";
}

bool KeyValueStore::del(const std::string& key) {

    if (store.find(key) == store.end()) {
        return false;
    }

    store.erase(key);
    return true;
}