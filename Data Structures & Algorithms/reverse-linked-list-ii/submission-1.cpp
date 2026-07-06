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
    
    
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        int count = 1; ListNode* prev = nullptr; ListNode* curr = head; ListNode* prev_prev = nullptr;
        
        while (count != left) { 
            prev = curr; curr = curr->next; 
            if (count == (left - 1)) {
                prev_prev = prev;
            }
            count++;
        }

        //now take note of this pos
        ListNode* start = curr;
        
        // now we have reached left
        while (count != right) { prev = curr; curr = curr->next; count++; }

        ListNode* end = curr;
        //now just reverse it

        // make the start->next as curr->next
        ListNode* after = end->next;
        // make the end->next as the prev_prev
        

        prev = start; curr = start->next;

        while (curr != after) {
            // cout << prev->val << "\tcurr: " << curr->val << endl;
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr; curr = nxt;
        }
        
        if (prev_prev == nullptr) {
            head = end;
        } else {
            prev_prev->next = end;
        }

        start->next = after;

        return head;
    }
};