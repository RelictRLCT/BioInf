from src.parser.parser import parse_file


def main():
    proteins = parse_file("insulin.fasta")
    for protein in proteins:
        print(str(protein))


if __name__ == '__main__':
    main()
