def hamming_distance(x : list , y: list):
    """Distance de Hammer

    Args:
        x (list): Gène 1
        y (list): Gène 2

    Returns:
        _type_: Distance de Hammer
    """
        
    if len(x) != len(y):
        raise ValueError("Les deux gènes ne sont pas de la même longeur.")

    indices= []
    
    for i in range(len(x)):
        if x[i] != y[i]:
            indices.append(i)
    print("Les différences sont sur les indices :", {i for i in indices})       
    
    return len(indices)

