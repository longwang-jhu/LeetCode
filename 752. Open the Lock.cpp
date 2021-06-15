// https://leetcode.com/problems/open-the-lock/

// You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
// '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely
// and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each
// move consists of turning one wheel one slot.

// The lock initially starts at '0000', a string representing the state of the 4
// wheels.

// You are given a list of deadends dead ends, meaning if the lock displays any of
// these codes, the wheels of the lock will stop turning and you will be unable to
// open it.

// Given a target representing the value of the wheels that will unlock the lock,
// return the minimum total number of turns required to open the lock, or -1 if it
// is impossible.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        return openLockBiBfs(deadends, target);
        if (target == "0000") return 0;
        unordered_set<string> bads(deadends.begin(), deadends.end());
        if (bads.find("0000") != bads.end()) return -1;
        
        // bfs
        queue<string> q; q.push("0000");
        unordered_set<string> visited; visited.insert("0000");
        int ans = 0;
        while (!q.empty()) {
            int nThisLayer = q.size();
            while (nThisLayer--) {
                string wheel = q.front(); q.pop();
                // generate wheelNext
                for (int i : {0, 1, 2, 3}) {
                    for (int incr : {1, 9}) {
                        string wheelNext = wheel;
                        wheelNext[i] = (wheel[i] - '0' + incr) % 10 + '0';
                        if (wheelNext == target) return ++ans;
                        if (bads.find(wheelNext) == bads.end()
                            and visited.find(wheelNext) == visited.end()) {
                            q.push(wheelNext);
                            visited.insert(wheelNext);
                        }
                    }
                }
            }
            ++ans;
        }
        return -1;
    }
    
    int openLockBiBfs(vector<string>& deadends, string target) {
        if (target == "0000") return 0;
        unordered_set<string> bads(deadends.begin(), deadends.end());
        if (bads.find("0000") != bads.end()) return -1;
        
        // bi-dfs
        queue<string> q1; q1.push("0000");
        queue<string> q2; q2.push(target);
        unordered_set<string> q1Set; q1Set.insert("0000");
        unordered_set<string> q2Set; q2Set.insert(target);
        unordered_set<string> visited; visited.insert("0000"); visited.insert(target);
        int ans = 0;
        while (!q1.empty() and !q2.empty()) {
            if (q1.size() > q2.size()) { swap(q1, q2); swap(q1Set, q2Set); q1Set.clear(); }
            
            int nThisLayer = q1.size();
            while (nThisLayer--) {
                string wheel = q1.front(); q1.pop();
                // generate wheelNext
                for (int i : {0, 1, 2, 3}) {
                    for (int incr : {1, 9}) {
                        string wheelNext = wheel;
                        wheelNext[i] = (wheel[i] - '0' + incr) % 10 + '0';
                        if (q2Set.find(wheelNext) != q2Set.end()) return ++ans;
                        if (bads.find(wheelNext) == bads.end()
                            and visited.find(wheelNext) == visited.end()) {
                            q1.push(wheelNext);
                            q1Set.insert(wheelNext);
                            visited.insert(wheelNext);
                        }
                    }
                }
            }
            ++ans;
        }
        return -1;
    }
};
