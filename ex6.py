def solve_puzzle() -> None:
    """
    Solves the equation HOD + HOD + HOD = MAT.
    Each letter represents a unique digit from 0 to 9.
    H and M cannot be zero as they are leading digits.
    """
    digits = range(10)

    for h in range(1, 10):
        for o in digits:
            if o == h:
                continue
            for d in digits:
                if d in (h, o):
                    continue

                hod_value = h * 100 + o * 10 + d
                mat_value = 3 * hod_value

                if mat_value > 999:
                    break

                m = mat_value // 100
                a = (mat_value // 10) % 10
                t = mat_value % 10

                if m == 0:
                    continue

                used_digits = {h, o, d, m, a, t}

                if len(used_digits) == 6:
                    print(f"{hod_value}+{hod_value}+{hod_value}={mat_value}")


if __name__ == "__main__":
    solve_puzzle()
