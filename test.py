def find_even():
    
    result = []

    for num in range(1,51):
        if num % 2 == 0:
            result.append(num)
    print(result)

find_even()