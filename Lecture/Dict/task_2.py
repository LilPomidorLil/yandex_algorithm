# дано 2 числа Х и Y без ведущих нулей, необходимо проверить, можно ли получить первое из второго перестановкой цифр

def main(digit1, digit2):
    def countdigit(digit):
        dlist = list(digit)

        hash_digit = [0] * 10
        for i in range(len(dlist)):
            hash_digit[int(dlist[i])] += 1

        return  hash_digit

    digit1_after = countdigit(digit1)
    digit2_after = countdigit(digit2)

    for digit in range(10):
        if digit2_after[digit] != digit1_after[digit]:
            return False
    return True


if __name__ == '__main__':

    digit1 = str(input())
    digit2 = str(input())
    print(main(digit1, digit2))

