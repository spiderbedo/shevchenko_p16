def find_courses(students_courses) -> set:
    '''
    Finds the number of courses that every student chose
    Args:
        students_courses (list): A list of sets of every student
    Return: set: A set of common courses
    '''

    if not students_courses:
        return set()

    common = students_courses[0].copy()
    for courses in students_courses[1:]:
        common &= courses
    return common


if __name__ == "__main__":
    n = int(input())
    all_courses = [set(input().split()) for _ in range(n)]
    print(len(find_courses(all_courses)))
