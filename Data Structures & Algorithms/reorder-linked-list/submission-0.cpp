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
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* cut = head;

        if(slow == nullptr){
            return;
        }
        if(slow->next == nullptr){
            return;
        }



        while(fast != nullptr && fast->next != nullptr){
            cut = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        cut->next = nullptr;

        ListNode* prev = nullptr;
        ListNode* curr = slow;

        while(curr!= nullptr){
            ListNode* forward = curr->next;
            curr->next = prev;
            prev = curr;
            curr = forward;
        }
        // prev is head of reverse second half

        while(head != nullptr && prev != nullptr){
    ListNode* next1 = head->next;
    ListNode* next2 = prev->next;
    head->next = prev;
    prev->next = next1;
    ListNode* prevtrack = prev;
    prev = next2;
    head = next1;
    if(head == nullptr){
        prevtrack->next = prev;
    }
}

    }
};
