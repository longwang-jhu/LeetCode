// https://leetcode.com/problems/course-schedule-ii/

// There are a total of numCourses courses you have to take, labeled from 0 to
// numCourses - 1. You are given an array prerequisites where prerequisites[i] =
// [ai, bi] indicates that you must take course bi first if you want to take course
// ai.

// Return the ordering of courses you should take to finish all courses. If there
// are many valid answers, return any of them. If it is impossible to finish all
// courses, return an empty array.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses); // graph[pre] = {courses}
        vector<int> indegrees(numCourses, 0);
        for (auto& edge : prerequisites) {
            graph[edge[1]].push_back(edge[0]);
            ++indegrees[edge[0]];
        }
        
        queue<int> todo;
        for (int course = 0; course < numCourses; ++course) {
            if (indegrees[course] == 0) todo.push(course);
        }
        vector<int> ans;
        while (!todo.empty()) {
            int course = todo.front(); todo.pop();
            ans.push_back(course);
            for (auto& child : graph[course]) {
                --indegrees[child];
                if (indegrees[child] == 0) todo.push(child);
            }
        }
        if (ans.size() < numCourses) return {};
        return ans;
    }
};
