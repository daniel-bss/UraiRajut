def urai(kata):
    x = list()
    for i in range(len(kata)):
        for j in range(i+1):
            x.append(kata[j])

    a = ''
    for i in x:
        a += i
    return a

def rajut(kata):
    g = list()
    for i in kata:
        g.append(i)

    x = 0
    y = 0
    z = list()

    while y < len(kata):
        x += 1
        y += x
        z.append(x)

    for i in z[:-1]:
        for j in range(i):
            g.pop(0)
    k = ''
    for i in g:
        k += i

    return k



print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))
print()
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))


