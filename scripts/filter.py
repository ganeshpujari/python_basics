# Filter taks function as first argument nad sequence as second argument.
# Filter return iterator with element those function returns true.

def is_even(number):
    if number % 2==0:
        return True
    else:
        return False

even_number_list=filter(is_even,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(even_number_list)
print(type(even_number_list))
for no in even_number_list:
    print(no)