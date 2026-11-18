from .distances import levenshtein_distance, hamming_distance

from .cluster import Cluster

class HierarchicalClustering:
    
    def __init__(self, sequences, mesure = hamming_distance ):
        
        self.sequences = sequences
        self.mesure = mesure
        self.matrice = None
        self.clusters = []
        
        self.init_clusters()
        
    def matrice_distance(self):
        
        n = len(self.sequences)
        
        D = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                    D[i][j] = self.mesure(self.sequences[i], self.sequences[j])
                    D[j][i] = D[i][j]
        
        self.matrice = D
                    
        return D
    
    def init_clusters(self):
        for i in range(len(self.sequences)):
            self.clusters.append(Cluster([i]))        
        
    def calcul_distance_clusters(self, cluster1:Cluster, cluster2: Cluster):
        
        distance = []
        
        for i in cluster1.indices:
            for j in cluster2.indices:
                distance.append(self.matrice[i][j])
                
                
        return min(distance)