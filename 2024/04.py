from problem import *
from statistics import median

nums = [int(x) for x in get_input(1).split('\n') if x]

#clip(sum(nums) - min(nums)*len(nums))

nums = [int(x) for x in get_input(2).split('\n') if x]

#print(sum(nums) - min(nums)*len(nums))

nums = [int(x) for x in get_input(3).split('\n') if x]

median = int(median(nums))
clip(sum(abs(x - median) for x in nums))
