//27.07 review offer05 replace space

class Solution {
public:
    string replaceSpace(string s) {
    int count = 0, len = s.size();
    for(char c : s){
        if (c == ' ') count++;
    }
    s.resize(len + 2 * count);
    for(int i = len -1, j = s.size() - 1; i < j;i--, j--){
        if (s[i] != ' ')
            s[j] = s[i];
        else {
            s[j - 2] = '%';
            s[j - 1] = '2';
            s[j] = '0';
            j -= 2;
        }
    }
    return s;
    }
};


class Solution {
public:
    string replaceSpace(string s) {
        string res;
        for(int i = 0; i < s.size(); ++i){
            if(s[i] != ' ')
                res += s[i];
            else{
                res += '%';
                res += '2';
                res += '0';
            }
        }
        return res;
    }
};

//02.08 offer06 print linked list from end to start, reversePrint
//recursion
class Solution {
public:
    vector<int> reversePrint(ListNode* head){
        recur(head);
        return res;
    }
private:
    vector<int> res;
    void recur(ListNode* head) {
        if(head == nullptr) return;
        recur(head->next);
        res.push_back(head->val);
    }
};
//stack
class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        stack<int> stk;
        while(head != nullptr) {
            stk.push(head->val);
            head = head->next;
        }
        vector<int> res;
        while(!stk.empty()) {
            res.push_back(stk.top());
            stk.pop();
        }
        return res;
    }
};

