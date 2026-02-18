def intersection() -> bool:

    """
    Finds out whether a given number exists in the intersection of two sets or not.
    Args:
        None
    Returns:
        bool
    """
  
    fst_set = set(input().split())
    snd_set = set(input().split())
    value = input().strip()
    inter = fst_set & snd_set
    return value in inter


if __name__ == "__main__":
    print(intersection())
