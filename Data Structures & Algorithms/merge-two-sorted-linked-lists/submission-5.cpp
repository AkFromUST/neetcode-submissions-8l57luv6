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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Idea is to have temp pointers to clean up the memory

        if ((list1 == nullptr) && (list2 == nullptr)) {
            return nullptr;
        }
        else if (list1 == nullptr) {
            return list2;
        } else if (list2 == nullptr) {
            return list1;
        }

        ListNode* l = list1;
        ListNode* r = list2;

        int first = 0;

        //whichever ends first
        while ((l != nullptr) &&  (r != nullptr)) {

            cout << "Pointers at: " << endl;
            cout << "\tLeft pointer at: " << l->val << endl;
            cout << "\tRight pointer at: " << r->val << endl;

            //lol, wrong logic




            if (l->val <= r->val) {

                while ((l->next != nullptr) && (l->next->val <= r->val)) {
                    l = l->next;
                }

                ListNode* temp = l->next; 
                l->next = r;
                l = temp;

                if (first == 0) {
                    first = 1;
                }

            } else {

                while ((r->next != nullptr) && (r->next->val <= l->val)) {
                    r = r->next;
                }

                ListNode* temp = r->next;
                r->next = l;
                r = temp;

                if (first == 0) {
                    first = 2;
                }
            }

        }

        // Which is head?
        if (first == 1) {
            return list1;
        } else {
            return list2;
        }
    }
};
