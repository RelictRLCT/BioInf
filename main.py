import sys

from src.parser.parser import parse_file
from src.sorter.bigram_sort import bigram_sort
from src.sorter.len_sort import len_sort


def main():
    mode = int(input('Ввод названия файла с клавиатуры или использовать uniprot_sprot.fasta? (1/2): '))
    if mode == 2:
        print('Загрузка файла...')
        proteins = parse_file("uniprot_sprot.fasta")
    else:
        file = input('Название файла из папки data: ').strip()
        print('Загрузка файла...')
        proteins = parse_file(file)

    print("Код белка (в конце два раза enter): ")

    lines = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        lines.append(line)

    protein_code_in = "".join(lines)

    proteins = len_sort(protein_code_in, proteins)
    print(f'\nПосле отсеивания по длине осталось {len(proteins)}\n')

    top100 = bigram_sort(protein_code_in, proteins)

    print(f'Всего результатов: {len(top100)}\n')
    for score, protein in top100:
        print(f'Сходство: {100*score:.1f}%: {str(protein)}\n')


if __name__ == '__main__':
    main()
