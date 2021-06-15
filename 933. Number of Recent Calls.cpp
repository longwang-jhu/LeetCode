// https://leetcode.com/problems/number-of-recent-calls/

// You have a RecentCounter class which counts the number of recent requests within
// a certain time frame.

// Implement the RecentCounter class:

// It is guaranteed that every call to ping uses a strictly larger value of t than
// the previous call.

////////////////////////////////////////////////////////////////////////////////

class RecentCounter {
public:
    deque<int> window;
    RecentCounter() {}
    
    int ping(int t) {
        window.push_back(t);
        while (window.front() < t - 3000) {
            window.pop_front();
        }
        return window.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
