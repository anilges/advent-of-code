import hashlib


def mine_five() -> int:
    i: int = 0
    while True:
        ans = "ckczppom" + str(i)
        hash = hashlib.md5(ans.encode()).hexdigest()
        if hash.startswith("00000"):
            return i
        i += 1


def mine_six() -> int:
    i: int = 0
    while True:
        ans = "ckczppom" + str(i)
        hash = hashlib.md5(ans.encode()).hexdigest()
        if hash.startswith("000000"):
            return i
        i += 1


def main() -> None:
    print(mine_five())
    print(mine_six())


if __name__ == "__main__":
    main()
