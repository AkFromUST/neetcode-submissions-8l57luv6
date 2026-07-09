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
    ListNode* middleNode(ListNode* head) {
        ListNode* temp = head;
        int count = 0;
        while (temp) {
            count++;
            temp = temp->next;
        }
        int middle = -1;
        if (count % 2 == 0) {
            middle = (count)/2 + 1;
        } else {
            middle = (count+1)/2;
        }

        cout << middle;
        
        int count2 = 1;
        ListNode* res = head;

        while (count2 != middle) {
            res = res->next;
            count2++;
        }
        return res;
    }
};