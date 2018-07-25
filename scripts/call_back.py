
def even_numver_list(limit,cb):
    even_numbers=[]
    for i in range(limit):
        ret_data=cb(i)
        if ret_data[0]:
            even_numbers.append(ret_data[1])
    return even_numbers


def is_even(number):
    if number % 2 == 0:
        return (True, number)
    else:
        return (False, None)

if __name__ == '__main__':
    result=even_numver_list(10,is_even)
    print(result)