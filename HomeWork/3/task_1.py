def main(seq1, seq2):
    print(len(set(seq1) & set(seq2)))

if __name__ == '__main__':
    seq1 = [int(digit) for digit in input().split()]
    seq2 = [int(digit) for digit in input().split()]
    main(seq1, seq2)