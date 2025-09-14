from src.protein.protein import Protein


def parse_file(file_name: str) -> list[Protein]:
    try:
        with open(f"data/{file_name}", 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f'Файла {file_name} нет в папке data')
        exit(1)

    proteins: list[Protein] = []
    desc = None
    sequence = ""

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith(">"):
            if desc is not None:
                proteins.append(Protein(desc, sequence))
            desc = line
            sequence = ""
        else:
            sequence += line

    # последний
    if desc is not None:
        proteins.append(Protein(desc, sequence))

    return proteins
