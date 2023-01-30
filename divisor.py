num = int(input("Enter a number: "))

list_range = list(range(1, num+1))

Divisor_list = []

for number in list_range:
    if num % number == 0:
        Divisor_list.append(number)
print(Divisor_list)
