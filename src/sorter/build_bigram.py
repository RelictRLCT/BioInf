def build_bigram(seq: str) -> list[int]:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pos = {c: i for i, c in enumerate(letters)}
    n = len(letters)

    vec = [0] * (n * n)  # длина 676

    for i in range(len(seq) - 1):
        a, b = seq[i], seq[i+1]
        if a in pos and b in pos:
            idx = pos[a] * n + pos[b]
            vec[idx] += 1

    return vec
