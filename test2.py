# import subprocess
# print("inside python")

# subprocess.call("./demoscript.sh", shell=True)


def is_odd_deco(actual_function):
    def inner(num):
        if num % 2 == 0:
            raise Exception("value must be odd")
        else:
            return actual_function(num)
        
    return inner

@is_odd_deco
def func(num):
    return num


print(func(2))