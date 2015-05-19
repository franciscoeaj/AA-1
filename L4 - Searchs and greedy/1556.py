while True:    
    try:
        entrada = raw_input()
    except EOFError:
        break
    def pd(i):
        if i == len(entrada):
            array.append('')
            return
        pd(i + 1)
        aux = array[:]
        for x in aux:
            if not dic.has_key(entrada[i] + x):
                dic[entrada[i] + x] = True
                array.append(entrada[i] + x)

    array = []
    dic = {}
    pd(0)
    array.pop(0)

    for i in sorted(array):
        print i
    print