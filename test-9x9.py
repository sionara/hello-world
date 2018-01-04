x = 0
y = 1

while x < 9:
    x += 1
    print('======== ',x,' =============')

    while y <= 9:
        result = x * y
        print(x, '*', y, '=', result)
        y += 1

    y = 1

for table in range(0,10):
    print('======', table, '======')
    for num in range(0,10):
        result = table * num 
        print(table, '*', num, '=', result)


        