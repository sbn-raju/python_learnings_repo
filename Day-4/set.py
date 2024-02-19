# Set is the collection of the unordered  items 
# Eacj element in the set must be unique & immutable
# *** Set is mutable but the element in the set is immutable**
nums = {1,2,3,4,5}
print(nums)
#to make a null set
null_set = set()
print(type(null_set))
# Sets have a nique values 
#set methods
nums.add(6)
print(nums)
# add it will add the element into the set 
nums.remove(6)
print(nums)
# remove the random element from the set
poped = nums.pop()
print(poped)
# pop it will remove the last element from the set
nums2 = {6,7,8,9,1}
set = nums2.union(nums)
print(set)
#combines both the sets
set_common = nums.intersection(nums2)
print(set_common)
# print only the common element 
nums.clear()
print(nums)
#it will clear the set

