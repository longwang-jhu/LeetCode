// https://leetcode.com/problems/course-schedule/

// There are a total of numCourses courses you have to take, labeled from 0 to
// numCourses - 1. You are given an array prerequisites where prerequisites[i] =
// [ai, bi] indicates that you must take course bi first if you want to take course
// ai.

// Return true if you can finish all courses. Otherwise, return false.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
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
        int numTaken = 0;
        while (!todo.empty()) {
            int course = todo.front(); todo.pop();
            ++numTaken;
            for (auto& child : graph[course]) {
                --indegrees[child];
                if (indegrees[child] == 0) todo.push(child);
            }
        }
        return numTaken == numCourses;
    }
};
