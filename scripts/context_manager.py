class NumberCheck(object):
    def __init__(self, number):
        self.number=number
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.number=0
        return True

number_check=NumberCheck(2)
print(number_check.number)

with NumberCheck(5) as number_check:
    1/0
    print(number_check.number)

print("works like finally id __exit__() returns True")
print(number_check.number)
