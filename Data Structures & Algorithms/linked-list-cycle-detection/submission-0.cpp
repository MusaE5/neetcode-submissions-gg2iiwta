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
    bool hasCycle(ListNode* head) {
        unordered_set<ListNode*> visited;
        
        if(head == nullptr  || head->next == nullptr){
            return false;
        }
        else{
            ListNode* tmp = head;
            visited.insert(head);
            while(tmp->next != nullptr){
                if(visited.contains(tmp->next)){
                    return true;
                }
                visited.insert(tmp->next);
                tmp = tmp->next;
            }

        }
        return false;
    }
};
