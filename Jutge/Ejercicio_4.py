nums = []
while len(nums) < 3:
    nums += list(map(int, input().split()))
print(sum(nums))
