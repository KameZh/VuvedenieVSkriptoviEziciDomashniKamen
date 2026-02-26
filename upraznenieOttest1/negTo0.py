nums = [-47, 3, -89, 62, -15, 94, -28, 71, 56, -8]
for i, n in enumerate(nums):
    if int(n) < 0:
        nums[i] = 0
print(nums)