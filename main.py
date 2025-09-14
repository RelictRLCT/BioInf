from src.parser.parser import parse_file
from src.sorter.bigram_sort import bigram_sort
from src.sorter.len_sort import len_sort


def main():
    # TODO: добавить ввод файла с клавиатуры
    proteins = parse_file("uniprot_sprot.fasta")
    for protein in proteins:
        print(str(protein))

    protein_code_in = input("Код белка: ").strip().upper()

    proteins = len_sort(protein_code_in, proteins)
    print(f'\nПосле отсеивания по длине осталось {len(proteins)}\n')

    top100 = bigram_sort(protein_code_in, proteins)

    print(f'Всего результатов: {len(top100)}\n')
    for score, protein in top100:
        print(f'Сходство: {100*score:.3f}%: {str(protein)}\n')


if __name__ == '__main__':
    main()
