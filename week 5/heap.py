import heapq

N = int(input())
rating = []
top_rating = []
count = 0
while (N >= 1):
    n1 = input()
    n2 = n1.split(" ")
    if (int(n2[0]) == 1):
        rating.append(int(n2[1]))
        heapq.heapify(rating)
        count = count + 1
    if (int(n2[0]) == 2):
        if (int(count / 3) > 0):
            top_rating.append(heapq.nlargest(int(count / 3), rating))
            c = int(count / 3) - 1
            print(top_rating[0][c])
        else:
            print("No Reviews Available")
    N = N - 1