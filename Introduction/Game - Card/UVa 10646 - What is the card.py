def card_value(card):
    if card[0] == "2":
        return 2
    elif card[0] == "3":
        return 3
    elif card[0] == "4":
        return 4
    elif card[0] == "5":
        return 5
    elif card[0] == "6":
        return 6
    elif card[0] == "7":
        return 7
    elif card[0] == "8":
        return 8
    elif card[0] == "9":
        return 9
    elif card[0] == "K" or card[0] == "Q" or card[0] == "J" or card[0] == "A" or card[0] == "T":
        return 10

def main():
    n = int(input())
    for i in range(1, n+1):
        cards = input().split(" ")
        cards.reverse()
        y = 0
        for _ in range(3):
            x = card_value(cards.pop())
            y += x
            if (10-x) > 0:
                cards = cards[:(-1*(10-x))]
        cards.reverse()
        print("Case %d: %s" % (i, cards[y-1]))


if __name__ == "__main__":
    main()