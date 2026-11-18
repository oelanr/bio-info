__author__ = "OR"
__year__ = 2026

from bio_info.distances import levenshtein_distance
from bio_info.classification_hierarchique import HierarchicalClustering
 
def main():

    sequences = ["CGAT", "CATG", "CGTT", "GGAT"]
    hc = HierarchicalClustering(sequences)
    
    print(hc.matrice_distance())
    print(hc.matrice)

if __name__ == "__main__":
    main()
