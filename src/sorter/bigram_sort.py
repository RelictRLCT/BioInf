from math import sqrt

from src.protein.protein import Protein
from src.sorter.build_bigram import build_bigram


def cosine_sim(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    norm1 = sqrt(sum(a*a for a in v1))
    norm2 = sqrt(sum(b*b for b in v2))
    return dot / (norm1 * norm2) if norm1 and norm2 else 0.0


def bigram_sort(code_in:str, proteins: list[Protein]) -> list[(float, Protein)]:
    bigram_in = build_bigram(code_in)

    bigrams: list[list[int]]= []

    for protein in proteins:
        bigrams.append(build_bigram(protein.code))

    scores: list[(float, Protein)] = []
    for protein, vec in zip(proteins, bigrams):
        score = cosine_sim(bigram_in, vec)
        scores.append((score, protein))

    scores.sort(key=lambda x: x[0], reverse=True)

    top100 = scores[:100]

    return top100
