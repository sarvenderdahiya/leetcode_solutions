nums = [1,2,4,6,5,3,7,8,2,9]

n, d = nums[nums[0]], nums[nums[nums[0]]]

while n != d:
    print("now at", n, d)
    n = nums[n]
    d = nums[nums[d]]
print(nums[n], nums[d])
