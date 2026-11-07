from bio_info.distances import levenshtein_distance


def main():
    seq1 = "CGAT"
    seq2 = "CATG"
    d_h = levenshtein_distance(seq1, seq2)

    print(d_h)


if __name__ == "__main__":
    main()
