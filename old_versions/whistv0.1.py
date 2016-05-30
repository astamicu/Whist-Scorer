##p1 = input('P1 name: ')
##print(p1)
##p2 = input('P2 name: ')
##print(p2)
##p3 = input('P3 name: ')
##print(p3)
##p4 = input('P4 name: ')
##print(p4)
##p5 = input('P5 name: ')
##print(p5)

p1 = 'a'
p2 = 'b'
p3 = 'c'
p4 = 'd'
p5 = 'e'

scor = 5

def round1():
    global p1f, p2f, p3f, p4f, p5f
    print('Round 1. Bid.')
    while True:
        try:
            p1f = int(input(p1 + ': '))
        except ValueError:
            print("Insert a number")
            continue
        if p1f > 1:
            print("You can't bid more than 1.")
            continue
        else:
            break
    while True:
        try:
            p2f = int(input(p2 + ': '))
        except ValueError:
            print("Insert a number")
            continue
        if p2f > 1:
            print("Nu poate face mai multe de 1.")
            continue
        else:
            break
    while True:
        try:
            p3f = int(input(p3 + ': '))
        except ValueError:
            print("Insert a number")
            continue
        if p3f > 1:
            print("Nu poate face mai multe de 1.")
            continue
        else:
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
            break
    while True:
        if (p1f + p2f + p3f + p4f) == 0:
            p5f = 0
            break
        elif int(p1f + p2f + p3f + p4f) == 1:
            p5f = 1
            break
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
                    break
        break
    print(p1 + ' face: ' + str(p1f))
    print(p2 + ' face: ' + str(p2f))
    print(p3 + ' face: ' + str(p3f))
    print(p4 + ' face: ' + str(p4f))
    print(p5 + ' face: ' + str(p5f))

def round2():
    global p1f, p2f, p3f, p4f, p5f
    print('Runda 2. Cate face fiecare.')
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
            break
    while True:
        if (p1f + p2f + p3f + p4f) == 0:
            p5f = 0
            break
        elif int(p1f + p2f + p3f + p4f) == 1:
            p5f = 1
            break
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
                    break
        break
    print(p1 + ' face: ' + str(p1f))
    print(p2 + ' face: ' + str(p2f))
    print(p3 + ' face: ' + str(p3f))
    print(p4 + ' face: ' + str(p4f))
    print(p5 + ' face: ' + str(p5f))

def score1():
    global p1scor, p2scor, p3scor, p4scor, p5scor
    print('Runda 1. Cate a facut fiecare.')
    while True:
        try:
            p1s = int(input(p1 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p1s > 1:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p1s == p1f:
            p1scor = scor + p1s
            break
        else:
            p1scor = -1
            break
    while True:
        try:
            p2s = int(input(p2 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p2s > 1:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p2s == p2f:
            p2scor = scor + p2s
            break
        else:
            p2scor = -1
            break
    while True:
        try:
            p3s = int(input(p3 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p3s > 1:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p3s == p3f:
            p3scor = scor + p3s
            break
        else:
            p3scor = -1
            break
    while True:
        try:
            p4s = int(input(p4 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p4s > 4:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p4s == p4f:
            p4scor = scor + p4s
            break
        else:
            p4scor = -1
            break
    while True:
        try:
            p5s = int(input(p5 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p5s > 1:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p5s == p5f:
            p5scor = scor + p5s
            break
        else:
            p5scor = -1
            break
    print('Scorul dupa runda 1')
    print(p1 + ": " + str(p1scor))
    print(p2 + ": " + str(p2scor))
    print(p3 + ": " + str(p3scor))
    print(p4 + ": " + str(p4scor))
    print(p5 + ": " + str(p5scor))

def score2():
    global p1scor, p2scor, p3scor, p4scor, p5scor
    print('Runda 2. Cate a facut fiecare.')
    while True:
        try:
            p1s = int(input(p1 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p1s > 1:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p1s == p1f:
            p1scor = p1scor + scor + p1s
            break
        elif p1s < p1f:
            p1scor = p1scor - (p1f - p1s)
            break
        else:
            p1scor = p1scor - (p1s - p1f)
            break
    while True:
        try:
            p2s = int(input(p2 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p2s > 1:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p2s == p2f:
            p2scor = p2scor + scor + p2s
            break
        elif p2s < p2f:
            p2scor = p2scor - (p2f - p2s)
            break
        else:
            p2scor = p2scor - (p2s - p2f)
            break
    while True:
        try:
            p3s = int(input(p3 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p3s > 1:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p3s == p3f:
            p3scor = p3scor + scor + p3s
            break
        elif p3s < p3f:
            p3scor = p3scor - (p3f - p3s)
            break
        else:
            p3scor = p3scor - (p3s - p3f)
            break
    while True:
        try:
            p4s = int(input(p4 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p4s > 4:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p4s == p4f:
            p4scor = p4scor + scor + p4s
            break
        elif p4s < p4f:
            p1scor = p4scor - (p4f - p4s)
            break
        else:
            p4scor = p4scor - (p4s - p4f)
            break
    while True:
        try:
            p5s = int(input(p5 + ': '))
        except ValueError:
            print("Introdu un numar.")
            continue
        if p5s > 1:
            print("Nu a putut face mai multe de 1.")
            continue
        elif p5s == p5f:
            p5scor = p5scor + scor + p5s
            break
        elif p5s < p5f:
            p5scor = p5scor - (p5f - p5s)
            break
        else:
            p5scor = p5scor - (p5s - p5f)
            break
    print('Scorul dupa runda 2')
    print(p1 + ": " + str(p1scor))
    print(p2 + ": " + str(p2scor))
    print(p3 + ": " + str(p3scor))
    print(p4 + ": " + str(p4scor))
    print(p5 + ": " + str(p5scor))

round1()
score1()
round2()
score2()
