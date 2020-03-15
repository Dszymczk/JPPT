x = 1
number_list = []
while x != 0:
    x = float(input(" Podaj liczbe: "))
    number_list.append(x)

even_number_list = []
for num in number_list: 
    if num % 2 == 0:
        even_number_list.append(num)
print(sum(even_number_list))
