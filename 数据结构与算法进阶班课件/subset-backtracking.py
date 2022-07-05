def subsets_recursive(nums):
    lst = []
    result = []
    subsets_recursive_helper(result, lst, nums, 0);
    return result;

def subsets_recursive_helper(result, lst, nums, pos):
    result.append(lst[:])
    for i in range(pos, len(nums)): # 这里是递归的出口
        lst.append(nums[i]) #
        subsets_recursive_helper(result, lst, nums, i+1)
        lst.pop() # 从这里开始回溯


nums = ['a', 'b', 'c']
print(subsets_recursive(nums))