class MyHashMap {
private:

    unordered_map<int, int> hashmap;

public:
    MyHashMap() {}
    
    void put(int key, int value) {
        hashmap[key] = value;
    }
    
    int get(int key) {
        if (hashmap.contains(key)) return hashmap[key];
        return -1;
    }
    
    void remove(int key) {
        hashmap[key] = -1;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */