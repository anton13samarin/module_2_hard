def generator_parolia(chislo):
    parol_chisla = ('')
    for i in range (1, chislo):
        for j in range (2, chislo):
            if j <= i:
                continue
            if chislo % (i + j) == 0:
                parol_chisla += str(i) + str(j)
    return parol_chisla
for i in range(3, 21):
    result = generator_parolia(i)
    print(i, result, sep=" - ")
