INPUT = [1721, 979, 366, 299, 675, 1456]

def product_two(nums: list) -> int:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == 2020:
                return nums[i] * nums[j]
    return -1

assert product_two(INPUT) == 514579

def product_three(nums: list) -> int:
    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) == 2020:
                    return (nums[i] * nums[j] * nums[k])
    return -1

assert product_three(INPUT) == 241861950

with open('../inputs/day01.txt', 'r') as f:
    data = [int(l) for l in f]
    assert product_two(data) == 786811
    assert product_three(data) == 199068980  