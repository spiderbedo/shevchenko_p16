from itertools import combinations

def get_k_subsets() -> None:
    """
    Reads a set of natural numbers from input and a number K,
    then prints subsets of len(k).
    """
    stroka = input().strip()
    k_str = input().strip()
    if not stroka or not k_str:
        return None
    elem = stroka.split()
    k = int(k_str)
    k_sub = list(combinations(elem, k))
    for subset in k_sub:
        print(list(subset))


if __name__ == "__main__":
    get_k_subsets()
