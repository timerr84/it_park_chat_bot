def sum_list(a):
    s = 0 #сумма чисел
    s1 = 0 #длина символов в строке
    for x in a:
        if type(x) == int or type(x) == float:
            s += x
        elif isinstance(x, str):
            s1 += len(x)
        elif type(x) == list:
            ss, ss1 = sum_list(x)
            s += ss
            s1 += ss1
    return s, s1
a = [1.2,3,True, 5,7,[12,3, [2,1], 'q'], 'sdfs']
print(sum_list(a))