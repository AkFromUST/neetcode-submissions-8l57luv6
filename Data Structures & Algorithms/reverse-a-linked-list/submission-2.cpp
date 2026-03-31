/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        if (!head) {
            return nullptr;
        }
        
        ListNode* curr = head;

        vector<ListNode*> all_nodes = {};

        while (curr != nullptr) {
            cout << "The current node value is: " << curr->val <<endl;
            all_nodes.push_back(curr);
            curr = curr->next;
        }

        // Now curr is pointing to the last element
        for (int i = all_nodes.size() - 1; i > 0; i--) {
            cout << "The nodes are: " << all_nodes[i]->val <<endl;
            all_nodes[i]->next = all_nodes[i-1];
        }

        // Making the 'new' last node next to nullptr
        all_nodes[0]->next = nullptr;

        return all_nodes[all_nodes.size()-1];
    }
};
