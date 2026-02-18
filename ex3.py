def only_sladkoezhkin() -> int:

    '''
    Finds how many products are liked only by Sladkoezhkin.
    Args: None
    Return: set: None
    '''

    sladkoezhkin = set(input().split())
    n = int(input())
    friends_products = set()

    for _ in range(n):
        friend = set(input().split())
        friends_products |= friend

    only_sladko = sladkoezhkin - friends_products
    return len(only_sladko)

if __name__ == "__main__":
    print(only_sladkoezhkin())
