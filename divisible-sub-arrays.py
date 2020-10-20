import math
f = math.factorial
arr = []
new_arr = [0]
total_subarrays = 0
l = list(map(int, input().split()))
k = 5
for i in range(len(l)):
    new_arr.append(sum(l[:i+1])%k)
    
for i in set(new_arr):
    if new_arr.count(i)>1:
        n = new_arr.count(i)
        total_subarrays+=(f(n)//f(2)//f(n-2))
print(total_subarrays)
