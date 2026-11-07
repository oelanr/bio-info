def hamming_distance(x, y):
    """Distance de Hamming : nombre de positions où x et y diffèrent.

    Args:
        x (str | list): première séquence
        y (str | list): deuxième séquence (même longueur que x)

    Returns:
        int: nombre de positions différentes

    Raises:
        ValueError: si x et y n'ont pas la même longueur
    """
    
    
    if len(x) != len(y):
        raise ValueError("Les deux gènes ne sont pas de la même longueur.")

    indices = []                      # positions où les lettres diffèrent
    for i in range(len(x)):
        if x[i] != y[i]:
            indices.append(i)

    print("Les différences sont sur les indices :", indices)
    return len(indices)


def levenshtein_distance(x, y):
    """Distance de Levenshtein : nombre minimal d'insertions,
    suppressions et substitutions pour transformer x en y.

    D[i][j] = distance entre les i premières lettres de x
              et les j premières lettres de y.

    Returns:
        int: D[n][m], la distance entre x et y
    """
    
    n, m = len(x), len(y)

    # Tableau de (n+1) lignes et (m+1) colonnes (+1 pour le mot vide)
    D = [[0] * (m + 1) for _ in range(n + 1)]

    # Étape 1 : mot vide -> mot vide
    D[0][0] = 0

    # Étape 2 : bords (suppressions / insertions successives)
    for i in range(1, n + 1):
        D[i][0] = D[i - 1][0] + 1
    for j in range(1, m + 1):
        D[0][j] = D[0][j - 1] + 1

    # Étape 3 : remplissage case par case
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # e1 : diagonale (garder ou substituer)
            if x[i - 1] == y[j - 1]:
                e1 = D[i - 1][j - 1]
            else:
                e1 = D[i - 1][j - 1] + 1
            e2 = D[i - 1][j] + 1      # haut : suppression
            e3 = D[i][j - 1] + 1      # gauche : insertion
            D[i][j] = min(e1, e2, e3)

    # Étape 4 : coin en bas à droite
    return D[n][m]