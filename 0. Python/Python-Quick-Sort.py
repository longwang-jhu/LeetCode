import random
nums = list(range(10))

### Quick Sort ###
# Time comp: O(n logn) average, O(n^2) worst
# Space: O(1) in place

# pick first ele as pivot
def quick_sort_first(nums, start, end):
    if start >= end: return

    piv_val = nums[start]
    left, right = start + 1, end   

    while left <= right: # stop when left > right
        while left <= right and nums[left] <= piv_val: # search for larger value
            left += 1
        while left <= right and piv_val <= nums[right]: # search for smaller value
            right -= 1
        if left < right: # swap
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # swap piv_val with smaller value at right
    nums[start], nums[right] = nums[right], nums[start]

    # divide
    quick_sort_first(nums, start, right - 1)
    quick_sort_first(nums, right + 1, end)

random.shuffle(nums)
quick_sort_first(nums, 0, len(nums) - 1)
print('Quick Sort (first):', nums)

# pick last ele as pivot
def quick_sort_last(nums, start, end):
    if start >= end: return

    piv_val = nums[end]
    left, right = start, end - 1
    
    while left <= right: # stop when left > right
        while left <= right and nums[left] <= piv_val: # search for larger value
            left += 1
        while left <= right and piv_val <= nums[right]: # search for smaller value
            right -= 1
        if left < right: # swap
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # swap piv_val with larger value at left
    nums[end], nums[left] = nums[left], nums[end]

    # divide
    quick_sort_last(nums, start, left - 1)
    quick_sort_last(nums, left + 1, end)

random.shuffle(nums)
quick_sort_last(nums, 0, len(nums) - 1)
print('Quick Sort (last):', nums)

# pick mid ele as pivot
def quick_sort_mid(nums, start, end):
    if start >= end: return

    left, right = start, end
    mid = left + (right - left) // 2
    piv_val = nums[mid]

    while left <= right: # stop when left > right
        while left <= right and nums[left] <= piv_val: # search for larger value
            left += 1
        while left <= right and piv_val <= nums[right]: # search for smaller value
            right -= 1
        if left < right: # swap
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # determine piv position and swap
    if right > mid:
        nums[mid], nums[right] = nums[right], nums[mid]
        piv = right
    elif left < mid:
        nums[mid], nums[left] = nums[left], nums[mid]
        piv = left
    else:
        piv = mid

    quick_sort_mid(nums, start, piv - 1)
    quick_sort_mid(nums, piv + 1, end)

random.shuffle(nums)
quick_sort_mid(nums, 0, len(nums) - 1)
print('Quick Sort (mid):', nums)