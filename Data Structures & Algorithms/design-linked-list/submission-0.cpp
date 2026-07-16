#include <unordered_map>
using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* prev;

    Node(): val(0), next(nullptr), prev(nullptr) {}
    Node(int val, Node* next, Node* prev): val(val), next(next), prev(prev) {}
};

class MyLinkedList {
public:
    // index, Node*
    unordered_map<int, Node*> linkedList = {};
    int currIndex = -1; // Set to -1 when empty so tail index aligns perfectly with size - 1
    
    MyLinkedList() {}
    
    int get(int index) {
        if (linkedList.find(index) != linkedList.end()) {
            return linkedList[index]->val;
        }
        return -1;
    }
    
    void addAtHead(int val) {
        if (linkedList.size() == 0) {
            linkedList[0] = new Node(val, nullptr, nullptr);
            currIndex = 0;
            return;
        }

        Node* head = linkedList[0];
        Node* newNode = new Node(val, head, nullptr);
        head->prev = newNode;
        currIndex++;

        // Shift all existing keys up by 1
        unordered_map<int, Node*> temp = {};
        temp[0] = newNode;
        for (const auto& [key, node] : linkedList) {
            temp[key + 1] = node;
        }
        linkedList = temp;
    }
    
    void addAtTail(int val) {
        if (linkedList.size() == 0) {
            linkedList[0] = new Node(val, nullptr, nullptr); 
            currIndex = 0;
            return;
        }

        Node* tail = linkedList[currIndex];
        Node* newNode = new Node(val, nullptr, tail);
        tail->next = newNode;
        currIndex++;
        linkedList[currIndex] = newNode;
    }
    
    void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
            return;
        }

        if (index == currIndex + 1) {
            addAtTail(val);
            return;
        }

        if (index > currIndex + 1 || index < 0) { return; }

        Node* at_index = linkedList[index];
        Node* prevNode = at_index->prev;

        Node* newNode = new Node(val, at_index, prevNode);
        prevNode->next = newNode;
        at_index->prev = newNode;

        // Shift subsequent map elements properly without overwriting keys
        unordered_map<int, Node*> temp = {};
        for (const auto& [key, node] : linkedList) {
            if (key < index) {
                temp[key] = node;
            } else {
                temp[key + 1] = node;
            }
        }
        temp[index] = newNode;
        
        linkedList = temp;
        currIndex++;
    }
    
    void deleteAtIndex(int index) {
        if (index < 0 || index > currIndex || linkedList.size() == 0) return;

        if (index == 0) {
            Node* head = linkedList[0];
            Node* nextNode = head->next;
            if (nextNode) {
                nextNode->prev = nullptr;
            }
            delete head;

            unordered_map<int, Node*> temp = {};
            for (const auto& [key, node] : linkedList) {
                if (key == 0) continue;
                temp[key - 1] = node;
            }
            linkedList = temp;
            currIndex--;
            return;
        }

        if (index == currIndex) {
            Node* tail = linkedList[currIndex];
            if (tail->prev) {
                tail->prev->next = nullptr;
            }
            delete tail;

            unordered_map<int, Node*> temp = {};
            for (const auto& [key, node] : linkedList) {
                if (key == currIndex) continue;
                temp[key] = node;
            }
            linkedList = temp;
            currIndex--;
            return;
        }

        // Middle node deletion
        Node* at_index = linkedList[index];
        Node* prevNode = at_index->prev;
        Node* afterNode = at_index->next;

        prevNode->next = afterNode;
        if (afterNode) {
            afterNode->prev = prevNode;
        }
        delete at_index;

        unordered_map<int, Node*> temp = {};
        for (const auto& [key, node] : linkedList) {
            if (key < index) {
                temp[key] = node;
            } else if (key > index) {
                temp[key - 1] = node;
            }
        }
        linkedList = temp;
        currIndex--;
    }
};