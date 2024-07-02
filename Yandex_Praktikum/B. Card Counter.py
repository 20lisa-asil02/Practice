n = int(input())
k = int(input())

arr = list(map(int, input().split()))

left = [arr[0]]
right = [arr[-1]]

cur_sum = sum(arr[0:(n-k)])
min_sum = cur_sum


for i in range(k):

    cur_sum = cur_sum - arr[i] + arr[i +(n-k)]
    min_sum = min(min_sum, cur_sum)

print(sum(arr) - min_sum)