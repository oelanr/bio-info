from bio_info.distances import hamming_distance


def main():
    seq1 = "ACTGATG"
    seq2 = "ACGGTTG"
    d_h = hamming_distance(seq1, seq2)

    print(d_h)


if __name__ == "__main__":
    main()
