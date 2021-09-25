x = '32269 29088 19779 26613'
y = '10792 16295 23484 17463'

def xor(a, b):
    c = 0
    for i in a:
        for j in b:
            x = i^j
            if x in a or x in b:
                c += 1
    if c%2==0:
        return 'Yes'
    else:
        return 'No'

x = list(map(int, x.split()))
y = list(map(int, y.split()))
print(xor(x, y))
