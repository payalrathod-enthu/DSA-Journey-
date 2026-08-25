class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Taking input from user
nums = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target: "))

# Creating object
solution = Solution()

# Getting answer
result = solution.twoSum(nums, target)

# Printing answer
print("Indices:", result)