"""
На стол в ряд выложены карточки, на каждой карточке написано натуральное число. За один ход разрешается взять карточку либо с левого, либо с правого конца ряда. Всего можно сделать 
k ходов. Итоговый счет равен сумме чисел на выбранных карточках. Определите, какой максимальный счет можно получить по итогам игры.

input:
7
4
1 1 9 2 2 2 6

output:
17

"""


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
