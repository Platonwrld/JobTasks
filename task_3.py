# одна из моих любимых сортировок - быстрая сортировка, также известная как сортировка Хоара
# асимптотическая сложность алгоритма - O(N log N), поэтому алгоритм считается одним из самых эффективных и быстрых, так как логарифмиская сложность считается лучшим временем

def quick_sort(array):

    if len(array) <= 1:
        return 
    
  
    barrier = array[0]

    l = []
    m = []
    r = []

    for x in array:
            
        if x < barrier:
            l.append(x)
            
        elif x == barrier: 
            m.append(x)
            
        else:
            r.append(x)

    k = 0

    for x in l + m + r:
        array[k] = x
        k += 1

    return array

print(quick_sort([2, 1, 6, 5]))
