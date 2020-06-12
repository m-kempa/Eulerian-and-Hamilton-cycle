from pathlib import Path
def dfs_lista_nast(lista, start=0,ret = [], path = [],first = True):
    if first:
        path = []
        ret = []
    path += [start]
    if lista.get(start) is None:
        return ret

    for i in lista.get(start):
        if i is not None and i not in path:
            ret = dfs_lista_nast(lista, i, ret, path,False)
            ret.insert(0,i)

    if first:
        ret.insert(0, start)
    return ret


def euler_skier(lista_nast, start = 0,sciezka=[], first = True, liczba_krawedzi = 0):
    if first:
        zrobione = 0
        sciezka=[]
        wierzholki_in_out= {}
        liczba_wie = 0

        for key, value in lista_nast.items():
            #stopnie wyjsciowe wierzchołków
            if key not in wierzholki_in_out:
                wierzholki_in_out[key] = [0,len(lista_nast[key])]
                liczba_wie+=1
            else:
                wierzholki_in_out[key][1] = len(lista_nast[key])

            #stopnie wejsciowe wierzchołkow
            for i in value:
                if i not in wierzholki_in_out:
                    wierzholki_in_out[i] = [1,0]
                    liczba_wie += 1
                else:
                    wierzholki_in_out[i][0] +=1

        #print(wierzholki_in_out)
        for j in wierzholki_in_out:
            if wierzholki_in_out[j][0] != wierzholki_in_out[j][1] and zrobione==0:
                print( "Brak cyklu Eulera\n")
                zrobione = zrobione + 1
        if len(dfs_lista_nast(lista_nast))!= liczba_wie and zrobione==0:   #graf nie jest spójny
            print( "Brak cyklu Eulera\n")
            zrobione = zrobione + 1
        liczba_krawedzi = 0
        for i in wierzholki_in_out:
            liczba_krawedzi += wierzholki_in_out[i][0]

    n = 1
    while n<=len(lista_nast[start]):
        #procedura generowanie ścieżki eulera
        if [start,lista_nast[start][n-1]] not in sciezka:
            sciezka.append([start,lista_nast[start][n-1]])
            #print(sciezka)
            euler_skier(lista_nast,lista_nast[start][n-1],sciezka,False,liczba_krawedzi)
            if liczba_krawedzi == len(sciezka):
                if first:
                    print("Cykl Eulera")
                    for i in range(len(sciezka)):
                        print(sciezka[i][0], "->", sciezka[i][1])

            else:
                #jeżeli dana ścieżka nie utworzyła cyklu przechodzącego przez wszystkie krawędzie
                sciezka.remove([start,lista_nast[start][n - 1]])
                #print(sciezka)
                if n == len(lista_nast[start]) and first and zrobione==0:
                    print ("Brak cyklu Eulera\n")
                    zrobione = zrobione + 1
        n += 1




mypath = Path("dane_c.txt")
czy_pusty = mypath.stat().st_size
if(czy_pusty == 0):
    print("Plik jest pusty")

else:
    with open('dane_c.txt') as f:
        first_line = f.readline()
        V_and_E = first_line.split()
        v = int(V_and_E[0])
        e = int(V_and_E[1])



    lista =[]

    with open("dane_c.txt", 'r') as f:
        licznik = 0
        for i, x in enumerate(f):
            ilosc = x.split()
            ilosc = len(ilosc)
            if ilosc != 2:
                print("niepoprawnie wprowadzone dane!")
                break
            if 1 <= i:
                word = x.split()
                if word[1].isdigit() and word[0].isdigit():
                    nword = list(map(int, word))
                    lista.append(nword)
                    licznik += 1
                else:
                    print("Można wprowadzać tylko cyfry")
                    break

    max_value = max(max(a) for a in lista)

    connections = {i: [] for i in range(max_value+1)} #podstawa do listy nastepników

    for i in connections:
        for a in lista:
            if i == a[0]:
                # if not e == i:
                connections[i].append(a[1])

    #print(connections)
    if e != licznik:
        print("Dane są wprowadzone niepoprawnie")

    else:
        euler_skier(connections)



