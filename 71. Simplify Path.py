# https://leetcode.com/problems/simplify-path/

# Given a string path, which is an absolute path (starting with a slash '/') to a
# file or directory in a Unix-style file system, convert it to the simplified
# canonical path.

# In a Unix-style file system, a period '.' refers to the current directory, a
# double period '..' refers to the directory up a level, and any multiple
# consecutive slashes (i.e. '//') are treated as a single slash '/'. For this
# problem, any other format of periods such as '...' are treated as file/directory
# names.

# The canonical path should have the following format:

# Return the simplified canonical path.

################################################################################

# split by "/" -> append dir_name if necessary and pop ans if dir_name == ".."

class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        path = path.split('/')
        
        for dir_name in path:
            if not dir_name or dir_name == ".":
                continue
            elif dir_name == "..":
                if ans:
                    ans.pop() # pop the most recent directory
            else:
                ans.append(dir_name)
        
        return '/' + '/'.join(ans)
