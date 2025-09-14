from src.parser.parser import parse_file
from src.sorter.len_sort import len_sort


def main():
    proteins = parse_file("insulin.fasta")
    for protein in proteins:
        print(str(protein))

    protein_code_in = input("Код белка: ")
    proteins = len_sort(protein_code_in, proteins)
    print(len(proteins))


if __name__ == '__main__':
    main()
