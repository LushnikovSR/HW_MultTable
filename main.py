def get_multiplication_table(n, s=""):
    if n == 1:
        return "1 * " + str(n) + " = " + str(1 * n) + s
    s = "\n" + "1 * " + str(n) + " = " + str(1 * n) + s
    return get_multiplication_table(n-1, s)


if __name__ == '__main__':
    print(get_multiplication_table(997)) #997 maximum recursion depth

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
