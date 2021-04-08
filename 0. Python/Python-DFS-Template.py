# get all combs: aaa, aab, ...

def dfs(ans, holder, nums):
    if len(holder) == len(nums):
        ans.append(''.join(holder))
        return

    for num in nums: # generate children
        holder.append(num) # save child into holder
        dfs(ans, holder, nums) # move to child
        holder.pop() # move back to parent, pop the latest child

nums = ['a', 'b', 'c']
ans = []

dfs(ans, [], nums)
print(ans)