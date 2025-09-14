from src.protein.protein import Protein


def len_sort(protein_code_in: str, proteins: list[Protein]) -> list[Protein]:
    code_in_len = len(protein_code_in)
    min_len = int(code_in_len * 0.7)
    max_len = int(code_in_len * 1.3)

    new_proteins: list[Protein] = []
    for protein in proteins:
        cur_len = len(protein.code)
        if cur_len > max_len or cur_len < min_len:
            continue
        new_proteins.append(protein)

    return new_proteins
