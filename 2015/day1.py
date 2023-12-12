def what_floor() -> int:
    floor: int = 0
    with open("1.in", "r") as f:
        for line in f:
            for char in line:
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1
                else:
                    print(f"Wrong input.")
        return floor


def char_pos() -> int:
    floor: int = 0
    pos: int = -1
    with open("1.in", "r") as f:
        for line in f:
            for char in line:
                pos += 1
                if floor == -1:
                    break
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1
                else:
                    print(f"Wrong input.")
        return pos


def main() -> None:
    print(what_floor())
    print(char_pos())


if __name__ == "__main__":
    main()
