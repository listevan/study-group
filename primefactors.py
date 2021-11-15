num = int(input('enter a number: '))
fin = []
def factor(num, fin):
    if num == 1:
        fin.append(1)
        fin.sort()
        return(fin)
    for i in range(2, int(num)+1):
        prime = True
        for j in (fin):
            if (i%j == 0 and i != j):
                prime = False
        if (num%i == 0 and prime):
            fin.append(i)
            print(fin)
            return(factor(num/i, fin))
print(factor(num, fin))
