__author__ = "OR"
__year__ = 2026

from .classification_hierarchique import HierarchicalClustering

class Cluster:
    def __init__(self, indices, gauche =None, droite =None, distance_fusion =None):
        self.indices = indices
        self.gauche = gauche
        self.droite =droite
        self.distance_fusion =distance_fusion
        