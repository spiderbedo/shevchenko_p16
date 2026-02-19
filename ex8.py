from itertools import combinations

def get_subsets() -> list:
    """
    Reads a line of space-separated natural numbers from input,
    converts them to integers, and generates all possible subsets.
    Returns:
        list
    """
    stroka = input().strip()
    if not stroka:
        return []
    elem = stroka.split()
    subsets = []
    for r in range(len(elem) + 1):
        for combo in combinations(elem, r):
            subsets.append(list(combo))
    return subsets


if __name__ == "__main__":
    print(len(get_subsets()))
    for sbset in get_subsets():
        print(sbset)
