// https://leetcode.com/problems/employee-importance/

// You have a data structure of employee information, which includes the employee's
// unique id, their importance value, and their direct subordinates' id.

// You are given an array of employees employees where:

// Given an integer id that represents the ID of an employee, return the total
// importance value of this employee and all their subordinates.

////////////////////////////////////////////////////////////////////////////////

/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, Employee*> idMap;
        for (auto& emp : employees) idMap[emp->id] = emp;
        return dfs(idMap, id);
    }
    
    int dfs(const unordered_map<int, Employee*>& idMap, int id) {
        Employee* emp = idMap.at(id);
        int val = emp->importance;
        for (int idSub : emp->subordinates) {
            val += dfs(idMap, idSub);
        }
        
        return val;
    }
};
