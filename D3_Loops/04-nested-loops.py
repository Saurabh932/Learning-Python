nums = [1, 2, 3, 4, 5, 6]

for i in range(0, len(nums)):
    for j in range(1, len(nums)-1):
        print(f"i={nums[i]}, j={nums[j]}")