from pathlib import Path

class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)] \
                      for row in range(vertices)]
        self.V = vertices



    def bezpieczny(self, v, pos, sciezka):

        #sprawdzamy czy bierzący wierzchołek i wcześniej dodany wierzchołek w ścieżce sąsiadują ze sobą
        if self.graph[sciezka[pos - 1]][v] == 0:
            return False


        #sprawdzamy czy bierzchący wierzchołek nie jest już w uwzgledniony w ścieżce
        for wierzcholek in sciezka:
            if wierzcholek == v:
                return False

        return True



    def CyklHamWGlab(self, sciezka, pos):



        if pos == self.V:
           #ostatni wierzchołek musi być połączony z pierwszym wierzchołkiem w ścieżce inaczej
           # nie może być to cykl Hamiltona co najwyżej Ścieżka Hamiltona
            if self.graph[sciezka[pos - 1]][sciezka[0]] == 1:
                return True
            else:
                return False

       #sprawdzamy inne wierzchołki w grafie do Cyklu Hamiltona, oprocz wirzchołka 0 poniewaz jest on poczatkowy
        for v in range(1, self.V):

            if self.bezpieczny(v, pos, sciezka) == True:

                sciezka[pos] = v

                if self.CyklHamWGlab(sciezka, pos + 1) == True:
                    return True

                #usuwamy bierzący wierzchołek ze ścieżki jeśli nie prowadzi do rozwiązania
                sciezka[pos] = -1

        return False

    def CyklHam(self):
        sciezka = [-1] * self.V


        #ustawiamy wierzchołek 0 jako pierwszy w ścieżce.
        sciezka[0] = 0

        if self.CyklHamWGlab(sciezka, 1) == False:
            print("W tym grafie nie ma Cyklu Hamiltona\n")
            return False
        else:
            self.wypisanie(sciezka)
            return True

    def wypisanie(self, sciezka):
        print("Istnieje Cykl Hamiltona: ")
        for wierzcholek in sciezka:
            print (wierzcholek)
        print(sciezka[0], "\n")

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
                    licznik+=1
                else:
                    print("Można wprowadzać tylko cyfry")
                    break

    if e != licznik:
        print("Dane są wprowadzone niepoprawnie")

    else:
        graf = Graph(v)
        graf.graph = matrix
        graf.CyklHam()

