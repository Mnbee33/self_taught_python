def sequential_search(number_list, n):
    found = False
    for i in number_list:
        if i in number_list:
            if i == n:
                found = True
                break
    return found

numbers = range(0, 100)
s1 = sequential_search(numbers, 2)
print(s1)

s2 = sequential_search(numbers, 202)
print(s2)
