# teszt listák

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]       # sorrendbe van
lista2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]       # visszefele sorrendbe van
lista3 = [4, -5, 1, 9, -7, 2, 3, 8, 6]     # minusz szám van benne
lista4 = [4, 5.0, 1, 9, 7.4, 2, 3, 8, 6]   # nem egész szám van benne
lista5 = [4, 5, 1, 9, 7, 2, 3, 8, 6, 5]    # egy szám 2x szerepel benne
lista6 = [4, 4, 4, 4, 4]                   # csak ugyanaz a szám van benne


def tesztelesek():
    egyszeruteszteles()
    buborekteszteles()
    tovabbfejlesztettbuborekteszteles()
    beszuroteszteles()
    tovabbfejlesztettbeszuroteszteles()
    minimumkivalasztasteszteles()
    maximumkivalasztasteszteles()
    kertitorpeteszteles()
    leszamoloteszteles()
    ladateszteles()
    shellteszteles()
    kupacteszteles()
    versenyteszteles()
    kozvetlenteszteles()


def egyszeruteszteles():
    egyszeru(lista1)
    egyszeru(lista2)
    egyszeru(lista3)
    egyszeru(lista4)
    egyszeru(lista5)
    egyszeru(lista6)


def buborekteszteles():
    buborek(lista1)
    buborek(lista2)
    buborek(lista3)
    buborek(lista4)
    buborek(lista5)
    buborek(lista6)


def tovabbfejlesztettbuborekteszteles():
    tovabbfejlesztettbuborek(lista1)
    tovabbfejlesztettbuborek(lista2)
    tovabbfejlesztettbuborek(lista3)
    tovabbfejlesztettbuborek(lista4)
    tovabbfejlesztettbuborek(lista5)
    tovabbfejlesztettbuborek(lista6)


def beszuroteszteles():
    beszuro(lista1)
    beszuro(lista2)
    beszuro(lista3)
    beszuro(lista4)
    beszuro(lista5)
    beszuro(lista6)


def tovabbfejlesztettbeszuroteszteles():
    tovabbfejlesztettbeszuro(lista1)
    tovabbfejlesztettbeszuro(lista2)
    tovabbfejlesztettbeszuro(lista3)
    tovabbfejlesztettbeszuro(lista4)
    tovabbfejlesztettbeszuro(lista5)
    tovabbfejlesztettbeszuro(lista6)


def minimumkivalasztasteszteles():
    minimumkivalasztas(lista1)
    minimumkivalasztas(lista2)
    minimumkivalasztas(lista3)
    minimumkivalasztas(lista4)
    minimumkivalasztas(lista5)
    minimumkivalasztas(lista6)


def maximumkivalasztasteszteles():
    maximumkivalasztas(lista1)
    maximumkivalasztas(lista2)
    maximumkivalasztas(lista3)
    maximumkivalasztas(lista4)
    maximumkivalasztas(lista5)
    maximumkivalasztas(lista6)


def kertitorpeteszteles():
    kertitorpe(lista1)
    kertitorpe(lista2)
    kertitorpe(lista3)
    kertitorpe(lista4)
    kertitorpe(lista5)
    kertitorpe(lista6)


def leszamoloteszteles():
    leszamolo(lista1)
    leszamolo(lista2)
    leszamolo(lista3)
    # leszamolo(lista4) # a leszámoló és a láda tesztelés nem bírja a tört számokat
    leszamolo(lista5)
    leszamolo(lista6)


def ladateszteles():
    lada(lista1)
    lada(lista2)
    lada(lista3)
    # lada(lista4)
    lada(lista5)
    lada(lista6)


def shellteszteles():
    shell(lista1)
    shell(lista2)
    shell(lista3)
    shell(lista4)
    shell(lista5)
    shell(lista6)


def kupacteszteles():
    kupac(lista1)
    kupac(lista2)
    kupac(lista3)
    kupac(lista4)
    kupac(lista5)
    kupac(lista6)


def versenyteszteles():
    verseny(lista1)
    verseny(lista2)
    verseny(lista3)
    verseny(lista4)
    verseny(lista5)
    verseny(lista6)


def kozvetlenteszteles():
    kozvetlen(lista1)
    kozvetlen(lista2)
    kozvetlen(lista3)
    kozvetlen(lista4)
    kozvetlen(lista5)
    kozvetlen(lista6)

# rendezési tételek1


def egyszeru(lista):
    print("Egyszerű rendezés")
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            print(i, j, lista, end='')
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                print('!', lista[i], lista[j])
                print('   ', lista)
            else:
                print('')


def buborek(lista):
    print("Buborék rendezés")
    ellenorzesekszama = 0
    cserekszama = 0
    for i in range(len(lista) - 1, 0, -1):
        ellenorzesekszama = ellenorzesekszama + 1
        for j in range(0, i):
            if lista[j + 1] < lista[j]:
                cserekszama =+ 1
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama+ellenorzesekszama)


def tovabbfejlesztettbuborek(lista):
    print("Továbbfejlesztett buborék rendezés")
    cserekszama = 0
    ellenorzesekszama = 0
    n = len(lista)
    for i in range(n):
        swapped = False  # figyeljük, hogy történt-e csere
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        # ha nem történt csere, akkor a tömb már rendezett, kész vagyunk
        if not swapped:
            break
    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def beszuro(lista):
    print("Beszúró rendezés")
    ellenorzesekszama = 0
    cserekszama = 0
    n = len(lista)
    for i in range(1, n):
        ellenorzesekszama += 1
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            cserekszama += 1
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def tovabbfejlesztettbeszuro(lista):
    print("Továbbfejlesztett beszúró rendezés")
    ellenorzesekszama = 0
    cserekszama = 0
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def minimumkivalasztas(lista):
    print("Minimumkiválasztásos rendezés")
    ellenorzesekszama = 0
    cserekszama = 0
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def maximumkivalasztas(lista):
    print("Maximumkiválasztásos rendezés")
    ellenorzesekszama = 0
    cserekszama = 0
    n = len(lista)
    for i in range(n - 1, -1, -1):
        max_index = i
        for j in range(i):
            if lista[j] > lista[max_index]:
                max_index = j
        lista[i], lista[max_index] = lista[max_index], lista[i]
    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)

# rendezési tételek2


def kertitorpe(lista):
    print("Kertitörpe rendeezés")
    cserekszama = 0
    ellenorzesekszama = 0
    i = 0
    while i < len(lista):
        if i == 0 or lista[i - 1] <= lista[i]:  # jó sorrend?
            i += 1  # előre
        else:
            temp = lista[i]  # csere
            lista[i] = lista[i - 1]
            lista[i - 1] = temp
            i -= 1
    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def leszamolo(lista):
    print("Leszámoló rendezés")
    cserekszama = 0
    ellenorzesekszama = 0
    n = len(lista)
    max_element = max(lista)
    count = [0] * (max_element + 1)
    output = [0] * n

    # elemek számlálása
    for i in range(n):
        count[lista[i]] += 1

    # összegzés
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]

    # rendezés
    for i in range(n - 1, -1, -1):
        output[count[lista[i]] - 1] = lista[i]
        count[lista[i]] -= 1

    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def lada(lista):
    print("Ládarendezés")
    ellenorzesekszama = 0
    cserekszama = 0
    legkisebb = min(lista)
    legnagyobb = max(lista)
    darab = [0] * (legnagyobb - legkisebb + 1)
    for szam in lista:
        darab[szam - legkisebb] += 1

    rendezett = []
    for szam in range(legkisebb, legnagyobb + 1):
        hanyszor = darab[szam - legkisebb]
        rendezett.extend([szam] * hanyszor)

    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def shell(lista):
    print("Shell-féle rendezés")
    cserekszama = 0
    ellenorzesekszama = 0
    # Az intervallumok meghatározása
    intervallumok = [len(lista) // 2]
    while intervallumok[-1] > 0:
        intervallum = intervallumok[-1] // 2
        intervallumok.append(intervallum)

    # Shell rendezés az intervallumokra
    for intervallum in intervallumok:
        for i in range(intervallum, len(lista)):
            temp = lista[i]
            j = i
            while j >= intervallum and lista[j - intervallum] > temp:
                lista[j] = lista[j - intervallum]
                j -= intervallum
            lista[j] = temp

    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def kupac(lista):
    print("Kupacrendezés")
    cserekszama = 0
    ellenorzesekszama = 0
    def kupac_epit(i, n):
        while 2 * i + 1 < n:
            j = 2 * i + 1
            if j + 1 < n and lista[j] < lista[j + 1]:
                j += 1
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                i = j
            else:
                break

    n = len(lista)

    # Kupac építése
    for i in range(n // 2 - 1, -1, -1):
        kupac_epit(i, n)

    # Kupacból kiemelés és rendezés
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        kupac_epit(0, i)

    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def verseny(lista):
    print("Verseny rendezés")
    cserekszama = 0
    ellenorzesekszama = 0
    n = len(lista)
    temp = [None] * n
    for i in range(n):
        temp[i] = [lista[i], i]

    while n > 1:
        m = (n + 1) // 2
        for i in range(m):
            if 2 * i + 1 < n:
                if temp[2 * i][0] < temp[2 * i + 1][0]:
                    j = 2 * i + 1
                else:
                    j = 2 * i
            else:
                j = 2 * i
            temp[i] = temp[j]

        n = m
    for i in range(1, len(temp)):
        key = temp[i][0]
        j = i - 1
        while j >= 0 and temp[j][0] > key:
            temp[j + 1] = temp[j]
            j -= 1
        temp[j + 1] = [key, temp[j + 1][1]]

    result = [None] * len(lista)
    for i in range(len(temp)):
        result[i] = lista[temp[i][1]]

    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


def kozvetlen(lista):
    print("Közvetlen kiválasztás")
    ellenorzesekszama = 0
    cserekszama = 0
    for i in range(0, len(lista) - 1):
        minidx = i  # minimum keresése
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minidx]:
                minidx = j

        if minidx != i:
            temp = lista[minidx]  # csere
            lista[minidx] = lista[i]
            lista[i] = temp
    print("Sorrendbe rakott lista:", lista)
    print("Ellenörzések száma:", ellenorzesekszama)
    print("Cserék száma:", cserekszama)
    print("Összes művelet száma:", cserekszama + ellenorzesekszama)


tesztelesek()
