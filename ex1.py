def find_repeated(numbers: str, needed_str: str) -> bool:
  
    '''
    Checks whether the target number is among the repeating elements
    in the sequence.
    Args:
        numbers
        needed_str
    Return: True if the number is repeated in the sequence, otherwise False.
    '''

    spisok = list(map(int, numbers.split()))
    needed_num = int(needed_str)

    seen = set()
    duplicates = set()

    for num in spisok:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return needed_num in duplicates


if __name__ == "__main__":
    input_nums = input()
    input_needed = input()
    result = find_repeated(input_nums, input_needed)
    print(result)
