__author__ = "OR"
__year__ = 2026

from bio_info.classification_hierarchique import HierarchicalClustering


def main():
    etiquettes = ["A", "B", "C", "D", "E", "F", "G"]

    matrice_exo = [
        [0,  4,  2,  7,  6,  8, 15],  # A
        [4,  0,  5,  6,  3, 12,  4],  # B
        [2,  5,  0, 10, 13, 17,  9],  # C
        [7,  6, 10,  0, 18, 20, 10],  # D
        [6,  3, 13, 18,  0,  1, 12],  # E
        [8, 12, 17, 20,  1,  0, 20],  # F
        [15, 4,  9, 10, 12, 20,  0],  # G
    ]

    # On initialise avec des séquences de même taille (pour que Hamming ne plante pas à l'init)
    hc = HierarchicalClustering(etiquettes)
    # On remplace la matrice calculée par la matrice de ton exercice
    hc.matrice = [ligne[:] for ligne in matrice_exo]

    print("=== ÉTAT INITIAL ===")
    print("Clusters :", [[etiquettes[i] for i in c.indices] for c in hc.clusters])
    for ligne in hc.matrice:
        print(" ", ligne)

    etape = 1
    while len(hc.clusters) > 1:
        nouveau = hc.fusion_cluster()
        noms_fusionnes = [etiquettes[i] for i in nouveau.indices]
        
        print(f"\n=== ÉTAPE {etape} : Fusion -> {noms_fusionnes} (distance = {nouveau.distance_fusion}) ===")
        print("Clusters actuels :", [[etiquettes[i] for i in c.indices] for c in hc.clusters])
        print("Nouvelle matrice :")
        for ligne in hc.matrice:
            print(" ", ligne)
        etape += 1


if __name__ == "__main__":
    main()