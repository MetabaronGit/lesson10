def make_table(start, stop, header=['Divisor', 'Numbers Divided']):
    rng = range(start, stop + 1)
    table = [header]

    for i in range(2, 10):
        numbers_divisible = get_numbers_divisible(i, rng)
        table.append([i, numbers_divisible])
    return table


def get_numbers_divisible(divisor, rng):
    numbers = []

    for num in rng:
        if num % divisor == 0:
            numbers.append(str(num))
    return ', '.join(numbers)


def print_table(table):
    widths = column_widths(table)

    for i, row in enumerate(table):
        print('| {:^{w1}} | {:^{w2}} |'.format(*row, **widths))
        if i == 0:
            row_width = len('| {:^{w1}} | {:^{w2}} |'.format(*row, **widths))
            print("=" * row_width)


def column_widths(table):
    num_cols = len(table[0])
    widths = {}

    for row in table:
        for col_num, col in enumerate(row):
            key = 'w%d' % (col_num + 1)
            widths[key] = widths.setdefault(key, 0)
            width = len(str(col))
            if widths[key] < width:
                widths[key] = width
    return widths


def main():
    print()
    start = int(input('START POINT: '))
    stop = int(input('END POINT: '))
    print()
    table = make_table(start, stop)
    print_table(table)


main()
