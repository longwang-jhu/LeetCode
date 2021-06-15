// https://leetcode.com/problems/walking-robot-simulation/

// A robot on an infinite XY-plane starts at point (0, 0) and faces north. The
// robot can receive one of three possible types of commands:

// Some of the grid squares are obstacles. The ith obstacle is at grid point
// obstacles[i] = (xi, yi).

// If the robot would try to move onto them, the robot stays on the previous grid
// square instead (but still continues following the rest of the route.)

// Return the maximum Euclidean distance that the robot will be from the origin
// squared (i.e. if the distance is 5, return 25).

// Note:

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        struct PairHash {
            size_t operator()(const pair<int, int>& point) const {
                return hash<int>{}(point.first) * 99 + hash<int>{}(point.second);
            }
        };
        
        vector<pair<int, int>> dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}}; // N, E, S, W
        // make obstacles a hashSet
        unordered_set<pair<int, int>, PairHash> obsSet;
        for (auto& obs : obstacles) obsSet.insert(make_pair(obs[0], obs[1]));
        
        int x = 0, y = 0, dirIdx = 0, ans = 0;
        for (int& cmd : commands) {
            if (cmd == -1) dirIdx = (dirIdx + 1) % 4;
            else if (cmd == -2) dirIdx = (dirIdx + 3) % 4;
            else {
                for (int i = 0; i < cmd; ++i) {
                    int xNext = x + dirs[dirIdx].first;
                    int yNext = y + dirs[dirIdx].second;
                    if (obsSet.find(make_pair(xNext, yNext)) != obsSet.end()) break;
                    else {
                        x = xNext; y = yNext;
                        ans = max(ans, x * x + y * y);
                    }
                }
            }
        }
        return ans;
    }
};
