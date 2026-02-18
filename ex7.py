from itertools import permutations

def all_permutations():
    numbers_set = set(map(int, input().split()))
    numbers = sorted(numbers_set)
    perms = permutations(numbers)
    for p in perms:
        print(*p)


if __name__ == "__main__":
    all_permutations()
