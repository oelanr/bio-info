__author__ = "OR"
__year__ = 2026

from .distances import levenshtein_distance, hamming_distance
from .cluster import Cluster

class HierarchicalClustering:
    
    def __init__(self, sequences, mesure = hamming_distance ):
        
        self.sequences = sequences
        self.mesure = mesure
        self.matrice = None
        self.clusters = []
        
        self.matrice_distance()
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
        self.clusters =  []
        
        for i in range(len(self.sequences)):
            self.clusters.append(Cluster([i]))        
        
    def calcul_distance_clusters(self, cluster1:Cluster, cluster2: Cluster):
        # La matrice est réduite après chaque fusion : ses indices désignent
        # donc les clusters courants, et non plus les séquences originales.
        i = self.clusters.index(cluster1)
        j = self.clusters.index(cluster2)
        return self.matrice[i][j]
    
    def trouver_clusters_proches(self):
        
        cluster1_proche:Cluster = None
        cluster2_proche:Cluster = None
        distance_min = distance = float("inf")
        n = len(self.clusters)
        
        for i in range(n):
            for j in range(i+1, n):
                
                distance = self.calcul_distance_clusters(self.clusters[i], self.clusters[j])
                
                if distance < distance_min : 
                    distance_min = distance
                    cluster1_proche = self.clusters[i] ; cluster2_proche = self.clusters[j]
                
        return cluster1_proche, cluster2_proche,  distance_min  
    
    def fusion_cluster(self):
        
        if len(self.clusters) < 2:
            return None
        
        
        cluster1, cluster2, distance_min = self.trouver_clusters_proches()
        
        i = self.clusters.index(cluster1)
        j = self.clusters.index(cluster2)
        
        if i > j:
            i, j = j, i
            cluster1, cluster2 = cluster2, cluster1
        
        nouvelles_distances = []
        
        for k in range(len(self.clusters)):
            
            if k == i or k == j:
                continue
            distance = min(self.matrice[i][k], self.matrice[j][k])
            nouvelles_distances.append(distance)
            
        self.matrice.pop(j)
        self.matrice.pop(i)
        
        for ligne in self.matrice:
            ligne.pop(j)
            ligne.pop(i)
            
        self.matrice = [[dist] + ligne for dist, ligne in zip(nouvelles_distances, self.matrice)]
        
        self.matrice.insert(0, [0] + nouvelles_distances)
        
        self.clusters.pop(j)
        self.clusters.pop(i)
        
        nouveau_cluster = Cluster(
            indices=cluster1.indices + cluster2.indices,
            gauche=cluster1,
            droite=cluster2,
            distance_fusion=distance_min
        )
        self.clusters.insert(0, nouveau_cluster)
        
        return nouveau_cluster

    def fit(self):
        """Exécute le clustering jusqu'à obtenir la racine unique du dendrogramme."""
        while len(self.clusters) > 1:
            self.fusion_cluster()
        return self.clusters[0] if self.clusters else None