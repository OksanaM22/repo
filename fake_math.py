#fake_divide
def divide(first, second):
    if  second != 0:
        return first / second
    return 'ошибка'
if __name__== "__main__":
    result1 = divide(69, 3)
    print(result1)
    result2 = divide(3, 0)
    print(result2)






