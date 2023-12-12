def wrap_paper() -> int:
    total: int = 0
    with open("input.txt", "r") as f:
        for line in f:
            dim_string = line.strip().split("x")
            dim_int = [int(x) for x in dim_string]
            l, w, h = dim_int
            sides = [l * w, w * h, h * l]
            total += 2 * sides[0] + 2 * sides[1] + 2 * sides[2]
            sides.sort()
            total += sides[0]
    return total


def ribbon() -> int:
    total: int = 0
    with open("input.txt", "r") as f:
        for line in f:
            dim_string = line.strip().split("x")
            dim_int = [int(x) for x in dim_string]
            dim_int.sort()
            total += 2 * dim_int[0] + 2 * dim_int[1]
            total += dim_int[0] * dim_int[1] * dim_int[2]
    return total


def main() -> None:
    print(wrap_paper())
    print(ribbon())


if __name__ == "__main__":
    main()
