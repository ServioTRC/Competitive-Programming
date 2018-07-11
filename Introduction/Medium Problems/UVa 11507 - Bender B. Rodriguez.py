def main():
    while True:
        size = int(input())
        if size == 0:
            break
        coordi = input().split(" ")
        # +x = 0, -x = 1, +y = 2, -y = 3, +z = 4, -z = 5
        last = 0
        for element in coordi:                
            if element == "+z":
                if last == 0:
                    last = 4    #+x -> +z
                elif last == 1:
                    last = 5    #-x -> -z
                elif last == 2:
                    last = 2     #+y -> +y
                elif last == 3:
                    last = 3     #-y -> -y
                elif last == 4:
                    last = 1    #+z -> -x
                elif last == 5:
                    last = 0     #-z -> +x
            elif element == "-z":
                if last == 0:
                    last = 5    #+x -> -z
                elif last == 1:
                    last =  4   #-x -> +z
                elif last == 2:
                    last = 2     #+y -> +y
                elif last == 3:
                    last = 3     #-y -> -y
                elif last == 4:
                    last = 0    #+z -> +x
                elif last == 5:
                    last = 1     #-z -> -x                   
            elif element == "+y":
                if last == 0:
                    last = 2    #+x -> +y
                elif last == 1:
                    last = 3    #-x -> -y
                elif last == 2:
                    last = 1     #+y -> -x
                elif last == 3:
                    last = 0     #-y -> +x
                elif last == 4:
                    last = 4    #+z -> +z
                elif last == 5:
                    last = 5     #-z -> -z
            elif element == "-y":
                if last == 0:
                    last = 3    #+x -> -y
                elif last == 1:
                    last = 2    #-x -> +y
                elif last == 2:
                    last = 0     #+y -> +x
                elif last == 3:
                    last = 1     #-y -> -x
                elif last == 4:
                    last = 4    #+z -> +z
                elif last == 5:
                    last = 5     #-z -> -z
        if last == 0:
            print("+x")
        elif last == 1:
            print("-x")
        elif last == 2:
            print("+y")
        elif last == 3:
            print("-y")
        elif last == 4:
            print("+z")
        elif last == 5:
            print("-z")

if __name__ == "__main__":
    main()