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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        // First Lets calculate the number of nodes in the ll

        ListNode* temp = head;
        ListNode* prev = nullptr;
        
        // to calculate the total len
        int len = 0;
        for (;temp != nullptr; temp = temp->next) {
            len++;
        }
        
        // have to remove the 
        int index = len - n + 1;

        if (index - 1 == 0) {
            head = head->next;
            return head;
        }
        
        temp = head;

        for (int i = 0; i < (index - 1); i++) {
            prev = temp;
            temp = temp->next;
        }

        cout << "The node to be removed is: " << temp->val << endl;
        cout << "The prev node is: " << prev->val << endl;


        prev->next = temp->next;
        delete temp;
        temp = nullptr;

        return head;
    
    }
};
