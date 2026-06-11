class MyHashSet {
public:
    unordered_set<int> hashset;

    MyHashSet() {}
    
    void add(int key) {
        hashset.insert(key);
    }
    
    void remove(int key) {
        if (hashset.contains(key)) hashset.erase(key);
    }
    
    bool contains(int key) {
        return hashset.contains(key);
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */