if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second_lowest = sorted(set([s for _, s in records]))[1]
    names = [n for n, s in records if s == second_lowest]

    for n in sorted(names):
        print(n)
