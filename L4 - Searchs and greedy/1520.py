while True:
    def binary_search(seq, search):
        right = len(seq)
        left = 0
        previous_center = -1
        if search < seq[0]:
            return -1
        while 1:
            center = (left + right) / 2
            candidate = seq[center]
            if search == candidate:
                center = seq.index(search)
                return center
            if center == previous_center:
                return - 2 - center
            elif search < candidate:
                right = center
            else:
                left = center
            previous_center = center
    
    try:
        N = raw_input()
    except EOFError: break
    
    if N == '': continue
    
    list = []
    for i in range(int(N)):
        a, b = map(int, raw_input().split())
        for j in range(a, b + 1):
            list.append(j)
    list2 = sorted(list)
    buscado = int(raw_input())
    result = binary_search(list2, buscado) + 1
    if result - 1 >= 0:
        inicio = list2.index(buscado)
        fim = list2.index(buscado)
        for i in range(list2.index(buscado) + 1, len(list2)):
            if list2[i] == buscado:
                fim = i
            else: break
        print str(buscado) + ' found from ' + str(inicio) + ' to ' + str(fim)
    else:
        print str(buscado) + ' not found'