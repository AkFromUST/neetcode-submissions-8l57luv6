/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        
        if (!head) {
            return nullptr;
        }
        
        // two pass?
        Node* pass1 = new Node(head->val); Node* temp = head;
        Node* res = pass1;
        unordered_map<Node*, Node*> hashmap = {};
        
        while (head->next != nullptr) {
            hashmap[head] = pass1;
            // next doesnt exist yet
            Node* newNode = new Node(head->next->val); pass1->next = newNode;
            
            // iterating
            head = head->next; 
            pass1 = pass1->next;
        }
        hashmap[head] = pass1;

        Node* pass2 = res;
        while (temp->next != nullptr) {
            
            if (temp->random != nullptr) {
                Node* val = temp->random;
                if (hashmap.contains(val)) {
                    pass2->random = hashmap[val];
                }
            } else {
                pass2->random = nullptr;
            }
            
            temp = temp->next; 
            pass2 = pass2->next;
        }

        if (temp->random != nullptr) {
            Node* val = temp->random;
            if (hashmap.contains(val)) {
                pass2->random = hashmap[val];
            }
        } else {
            pass2->random = nullptr;
        }

        return res;
    }
};
