def arrayPairSum(nums):
    # Solution 1
    # nums.sort(reverse=True)
    # s = 0
    # n = len(nums) // 2
    # for i in range(n):
    #     min_val = min(nums[2*i], nums[2*i+1])
    #     s += min_val
    # return s

    # Solution 2
    nums.sort()
    print(nums)
    # [::2] 表示每个两位去一个数
    # [::-1] 表示从后往前每隔一位取一个数
    print(nums[::2])
    # 相加可以直接用sum
    return sum(nums[::2])



nums = [6,2,6,5,1,2]
print(arrayPairSum(nums))