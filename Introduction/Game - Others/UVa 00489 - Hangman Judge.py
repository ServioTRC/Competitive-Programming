def main():
    while True:
        case = int(input())
        if case == -1:
            break
        print("Round %d" % (case))
        word = input()
        guess = input()
        letters_cor = set()
        letters_guess = set()
        for le in word:
            letters_cor.add(le)
        corrects_size = len(letters_cor)
        done = False
        count_pos = 0
        count_neg = 0
        for le in guess:
            if le not in letters_guess:
                letters_guess.add(le)
                if le in letters_cor:
                    count_pos += 1
                else:
                    count_neg += 1
            if count_neg >= 7:
                print("You lose.")
                done = True
                break
            elif count_pos == corrects_size:
                print("You win.")
                done = True
                break
        if not done:
            print("You chickened out.")

if __name__ == "__main__":
    main()