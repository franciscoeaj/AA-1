n = int(raw_input())
 
unique_nums = []
nums = []
for i in range(n):
    x = int(raw_input())
    nums.append(x)
 
    if (x not in unique_nums):
        unique_nums.append(x)
 
unique_nums = sorted(unique_nums)
for i in range(len(unique_nums)):
    counted = nums.count(unique_nums[i])
 
    print "%i aparece %i vez(es)" % (unique_nums[i], counted)