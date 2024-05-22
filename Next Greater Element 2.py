def nextGreaterEle(nums):
    n = len(nums)
    stack = []
    for i in range(n-1, -1, -1):
        stack.append(nums[i])
    result = [-1] * n
    
    for i in range(n-1, -1, -1):
        while len(stack)>0 and stack[-1] <= nums[i]:
            stack.pop()
        
        if len(stack) > 0:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result

nums = [12, 10, 4, 15, 9, 200, 121, 154, 12]
result = nextGreaterEle(nums)
print(result)