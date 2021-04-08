def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left + 1 < right: # stop at (left, right)
        mid = left + (right - left) // 2 # avoid overflow
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    else:
        return -1

nums = range(100)
target = 99
print(binary_search(nums, target))