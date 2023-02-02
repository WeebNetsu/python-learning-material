# a list that contains statements


nums1 = [i ** 5 for i in range(3)]
print(nums1)  # [0, 1, 32]
# 32 = 2 * 2 * 2 * 2 * 2

# get all multiples of 3 (up to 15)
nums2 = [i for i in range(15) if i % 3 == 0]
print(nums2)

# get multiples of 10
nums3 = [i * 10 for i in range(1, 10)]
print(nums3)

# 0, 4, 16, 36, 64
nums = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(nums)
