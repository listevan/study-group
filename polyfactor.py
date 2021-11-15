print('Ax^2+Bx+C')
a = int(input('Give A: '))
b = int(input('Give B: '))
c = int(input('Give C: '))

def factors(num) -> list:
    fin = []
    for i in range(1, num+1):
        if (num%i==0):
            fin.append(i)
            fin.append(-i)
    return fin

afactors = factors(a)
cfactors = factors(c)

def factor(afactor, cfactor, a, b, c):
    for i in (afactor):
        for j in (cfactor):
            if (c-(b*j/i)+(a*((j/i)**2))==0):
                if (i%j != 0):
                    return ("(ax+b)(cx+d) a: " + str(i) + " b: " + str(j) + " c: " + str(int(a/i)) + " d: " + str(int((b-a*(j/i))/i)))
                return ("(ax+b)(cx+d) a: 1" + " b: " + str(j/i) + " c: " + str(int(a)) + " d: " + str(int(b-a*(j/i))))
    return("unfactorable")
print(factor(afactors, cfactors, a, b, c))            
