#Print numbers from 1 to 50, Skip multiples of 5 and Stop at 37

for i in range(1, 51):

    if i % 5 == 0:
        continue

    if i == 37:
        break

    print(i)

