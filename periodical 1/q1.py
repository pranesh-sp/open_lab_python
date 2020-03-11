class printt:
    def pattern(self, row, col):
        for i in range(0, row):
            l1 = (col - (3 * (2 * i + 1))) // 2
            for j in range(0, l1):
                print("#", end="")
            for j in range(0, (2 * i) + 1):
                print("_|_", end="")
            for j in range(0, l1):
                print("#", end="")
            print()
        l2 = (col - 5) // 2
        for j in range(0, l2):
            print("#", end="")
        print("AABAA", end="")
        for j in range(0, l2):
            print("#", end="")
        print()
        for i in range(row - 1, -1, -1):
            l1 = (col - (3 * (2 * i + 1))) // 2
            for j in range(0, l1):
                print("#", end="")
            for j in range(0, (2 * i) + 1):
                print("_|_", end="")
            for j in range(0, l1):
                print("#", end="")
            print()


i = input().split(" ")
row = (int(i[0]) - 1) // 2
col = int(i[1])
p = printt()
p.pattern(row, col)
