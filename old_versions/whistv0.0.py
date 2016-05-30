p1 = input('P1 name: ')
print(p1)
p2 = input('P2 name: ')
print(p2)
p3 = input('P3 name: ')
print(p3)
p4 = input('P4 name: ')
print(p4)
p5 = input('P5 name: ')
print(p5)

def round1():
    while True:
        try:
            p1f = int(input(p1 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p1f > 1:
            print("Nu poate face mai multe de 1.")
            continue
        else:
            print(p1 + ' face: ' + str(p1f))
            break
    while True:
        try:
            p2f = int(input(p2 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p2f > 1:
            print("Nu poate face mai multe de 1.")
            continue
        else:
            print(p2 + ' face: ' + str(p2f))
            break
    while True:
        try:
            p3f = int(input(p3 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p3f > 1:
            print("Nu poate face mai multe de 1.")
            continue
        else:
            print(p3 + ' face: ' + str(p3f))
            break
    while True:
        try:
            p4f = int(input(p4 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p4f > 1:
            print("Nu poate face mai multe de 1.")
            continue
        else:
            print(p4 + ' face: ' + str(p4f))
            break
        if (p1f + p2f + p3f + p4f) == 0:
            p5f = 0
            print(p5 + ' face: ' + str(p5f))
        elif int(p1f + p2f + p3f + p4f) == 1:
            p5f = 1
            print(p5 + ' face: ' + str(p5f))
        else:
            while True:
                try:
                    p5f = int(input(p5 + ': '))
                except ValueError:
                    print("Introdu un numar.")
                    continue
                if p5f > 1:
                    print("Nu poate face mai multe de 1.")
                    continue
                else:
                    print(p5 + ' face: ' + str(p5f))
                    break

round1()
