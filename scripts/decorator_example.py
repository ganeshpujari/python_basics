# Q write a decorator to calculate time required for complete execution of a fu
# nction
import time


def time_logger(func):
    def timmer(*args, **kwrgs):
        start_time = time.time()
        result = func(*args, **kwrgs)
        print("Result is {result}".format(result=result))
        end_time = time.time()
        print("Excecution time: {tm}".format(tm=end_time-start_time))
    return timmer


@time_logger
def sum(*args, **kwrgs):
    result = 0
    for no in args:
        with open("a.txt", 'a') as fw:
            result += no
            fw.write(str(result) + "  ")
    return result

sum(10, 10)
