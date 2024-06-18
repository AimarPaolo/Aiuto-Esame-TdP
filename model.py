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