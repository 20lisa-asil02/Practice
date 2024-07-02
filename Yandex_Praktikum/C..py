n = int(input())

arr = list(map(int, input().split()))
# counter = 0
#
# hash_arr = [arr[i] % 200 for i in range(n)]
#
# unic_num = dict()
#
# for i in range(n):
#     if hash_arr[i] not in unic_num:
#         unic_num[hash_arr[i]] = 0
#
#     else:
#         unic_num[hash_arr[i]] = unic_num[hash_arr[i]] * 2 + 1
#
# counter = sum(unic_num.values())
#
# print(counter)

remainder_freq = [0] * 200
for num in arr:
    remainder = num % 200
    remainder_freq[remainder] += 1

result = 0
for freq in remainder_freq:
    result += freq * (freq - 1) // 2

print(result)

