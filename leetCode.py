nums = list(map(int, input().split()))
hasil = []
for i in nums:
    count = sum(1 for j in nums if j < i)
    hasil.append(count)
print(hasil)