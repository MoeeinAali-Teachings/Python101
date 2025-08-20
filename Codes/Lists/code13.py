nums = [1,10,5,7]
nums2 = [1,10,5,7]

nums.reverse()
print(nums)

print(reversed(nums2)) # we should cast it from list_reverseiterator to list
print(list(reversed(nums2)))
print(nums2)