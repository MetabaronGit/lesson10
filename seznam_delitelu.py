import pprint as pp

def test_divisor(divisor: int, range: range) -> list:
    result = []
    for i in range:
        if i % divisor == 0:
            result.append(str(i))
    return result


def get_tab_width(divisors: dict) -> int:
    """
    Zjistí délku nejdelšího sloupce tabulky.
    """
    line = " " + ", ".join(divisors.get(2)) + " |"
    return len(line)


def draw_tab(divisors: dict, range: range, tab_width: int) -> None:
    first_col = "| Divisor |"
    print(first_col + "Numbers Divided".center(tab_width) + " |")
    print("=" * (len(first_col) + tab_width + 2))
    x = 2
    for i in range:

        line = ", ".join(divisors.get(x)).center(tab_width)
        print("|" + str(i).center(9) + "|" + line + " |")
        x += 1


def main():
    divisors = dict()

    START_POINT = int(input("START_POINT: "))
    END_POINT = int(input("END_POINT: "))

    # testujeme pro dělitele 2 až 9
    DIVISOR = range(2, 10)

    for i in DIVISOR:
        divisors[i] = test_divisor(i, range(START_POINT, END_POINT + 1))

    # pp.pprint(divisors)
    draw_tab(divisors, DIVISOR, get_tab_width(divisors))


main()
