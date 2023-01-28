


def obome(x, InT, ExT):
    if InT == ExT: return x
    a = oboms(x, InT)
    if ExT == 'm^3': return a / (100 ** 3)
    if ExT == 'cm^3': return a
    if ExT == 'dm^3': return a / (10 ** 3)
    if ExT == 'liters': return a / (10 ** 3)


def oboms(x, InT):
    if InT == 'm^3': return x * (100 ** 3)
    if InT == 'cm^3': return x
    if InT == 'dm^3': return x * (10 ** 3)
    if InT == 'liters': return x * (10 ** 3)





def mass(x, InT, ExT):
    if InT == ExT: return x
    a = massa(x, InT)
    if ExT == 'g': return a * 1000
    if ExT == 'kg': return a
    if ExT == 'mg': return a * 1000000
    if ExT == 't': return a * 0.001


def massa(x, InT):
    if InT == 'g': return x * 0.001
    if InT == 'kg': return x
    if InT == 'mg': return x * 0.000001
    if InT == 't': return x * 1000





def kal():
    print('Введите простое алгебравическое выражение обособляя знаки препинания пробелами')
    print('Если вы хотите возвести число в стевень используйте" ^ "')
    print('Если вы хотите разделить число нацело используйте" // "')
    sp = input().split()
    sim = sp[1]
    if sim == '+': return int(sp[0]) + int(sp[2])
    if sim == '-': return int(sp[0]) - int(sp[2])
    if sim == '*': return int(sp[0]) * int(sp[2])
    if sim == '/': return int(sp[0]) / int(sp[2])
    if sim == '//': return int(sp[0]) / int(sp[2])
    if sim == '^': return int(sp[0]) ** int(sp[2])


print(kal())