#Лабораторна робота №2. Розробка програм на Python з використанням
#функцій. Словники. Обробка виняткових ситуацій, робота з файлами.
#Варіант 1

def all_eq(lst):
    max_length = max(len(s) for s in lst)
    new_lst = [s.ljust(max_length, '_') for s in lst]
    return new_lst

# Приклад використання
input_list = ["apple", "banana", "orange", "kiwi"]
result_list = all_eq(input_list)

print(result_list)

