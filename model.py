#PER AGGIUNGERE UN INSIEME DI ARCHI A TUTTI I NODI --> UTILIZZARE ITERTOOL
myedges = list(itertools.combinations(self._allTeams, 2))
alternativaaaaaa
def addEdgePesati(self, year):
    salary = DAO.getAllSalaries(year)
    self.grafo.clear_edges()
    for n1 in self.grafo.nodes:
        for n2 in self.grafo.nodes:
            if n1.ID != n2.ID:
                self.grafo.add_edge(n1, n2, peso=(salary[n1.ID] + salary[n2.ID]))

#PER VEDERE I VICINI IN UN GRAFO UTILIZZO
self.grafo.neighbors(nodo_partenza)

#PER VEDERE GLI ARCHI ENTRANTI ED USCENTI
def creaDizionarioBilancio(self):
    self.bilancio = {}
    for n in self._grafo.nodes:
        self.bilancio[n.AlbumId] = 0
        for bil in self._grafo.predecessors(n):
            self.bilancio[n.AlbumId] += float(self._grafo[bil][n]['weight'])
        for bil2 in self._grafo.successors(n):
            self.bilancio[n.AlbumId] -= float(self._grafo[n][bil2]['weight'])
#OPPURE
    def bilancio(self, nodo):
        entranti = 0
        uscenti = 0
        for archientranti in self.grafo.in_edges(nodo):
            entranti += self.grafo[archientranti[0]][archientranti[1]]["weight"]
        for archiuscenti in self.grafo.out_edges(nodo):
            uscenti += self.grafo[archiuscenti[0]][archiuscenti[1]]["weight"]
        return entranti - uscenti

#suggerimenti esame
Suggerimento.
In un grafo orientato, è possibile utilizzare i seguenti metodi:
• outDegreeOf: restituisce il numero di archi uscenti da un determinato vertice;
• inDegreeOf: restituisce il numero di archi entranti in un determinato vertice;
• outgoingEdgesOf: restituisce il set di archi uscenti da un determinato vertice;
• incomingEdgesOf: restituisce il set di archi entranti in un determinato vertice;
• Graphs.successorListOf: restituisce la lista di vertici raggiunti dagli outgoingEdges;
• Graphs.predecessorListOf: restituisce la lista di vertici raggiunti dagli incomingEdges.