n = int(input())

arr = list(map(int, input().split()))

remainder_freq = [0] * 200
for num in arr:
    remainder = num % 200
    remainder_freq[remainder] += 1

result = 0
for freq in remainder_freq:
    result += freq * (freq - 1) // 2

print(result)

