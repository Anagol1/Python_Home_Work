
# 5. Реализуйте алгоритм перемешивания списка.
import random
num_N = int (input ("Input number: ")) 
my_list = list(range(0, num_N))
print(f"List {my_list}")
for n in range(0, num_N - 1):
    i = random.randint(0, num_N - 1)
    my_list[n] = my_list[i]
    my_list[i] = my_list[n]
print(f"Mixed list {my_list}")