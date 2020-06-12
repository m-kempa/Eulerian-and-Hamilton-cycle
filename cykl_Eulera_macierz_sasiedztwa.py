from pathlib import Path
def findpath(graph):
    n = len(graph)
    numofadj = list()

    #Liczba krawędzi jakie ma dany wierzchołek
    for i in range(n):
        numofadj.append(sum(graph[i]))

        #ile krawędzi ma nieprzysty stopien
    startpoint = 0
    numofodd = 0
    for i in range(n - 1, -1, -1):
        if (numofadj[i] % 2 == 1):
            numofodd += 1
            startpoint = i

    #jeżeli liczba wierzchołków z stopniami nieparzystymi jest !=0 nie jest to Graf Eulerowski
    if (numofodd != 0):
        print("Graf nie ma cyklu Eulera")
        return


    stack = list()
    path = list()
    cur = startpoint


    while (stack != [] or sum(graph[cur]) != 0):

       #jeżeli bierzący węzeł nie ma żadnego sąsiada
        if (sum(graph[cur]) == 0):
            path.append(cur)
            cur = stack.pop(-1)


        #Jeżeli bierz element ma conajmniej 1
        else:
            for i in range(n):
                if graph[cur][i] == 1:
                    stack.append(cur)
                    graph[cur][i] = 0
                    graph[i][cur] = 0
                    cur = i
                    break

    # wypisujemy ścieżkę
    for ele in path:
        print(ele, "-> ", end = '')
    print(cur )







mypath = Path("dane_b.txt")
czy_pusty = mypath.stat().st_size
if(czy_pusty == 0):
    print("Plik jest pusty")

else:
    with open('dane_b.txt') as f:
        first_line = f.readline()
        V_and_E = first_line.split()
        v = int(V_and_E[0])
        e = int(V_and_E[1])

    #print("v",v, "e", e)

    matrix= [[0]*v for _ in range(v)]

    with open("dane_b.txt", 'r') as f:
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
                    w1=0
                    w2=0
                    w1 = int(word[0])
                    w2 = int(word[1])
                    matrix[w1][w2] = 1
                    matrix[w2][w1] = 1
                    licznik += 1
                else:
                    print("Można wprowadzać tylko cyfry")
                    break


    if e != licznik:
        print("Dane są wprowadzone niepoprawnie")

    else:
        findpath(matrix)



