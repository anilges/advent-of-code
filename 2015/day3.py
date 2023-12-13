def one_present() -> int:
    pos = (0, 0)
    delivered = []
    delivered.append(pos)
    house = 1
    with open("input.txt", "r") as f:
        for line in f:
            for char in line:
                if char == "^":
                    pos = (pos[0], pos[1] + 1)
                elif char == "v":
                    pos = (pos[0], pos[1] - 1)
                elif char == ">":
                    pos = (pos[0] + 1, pos[1])
                else:
                    pos = (pos[0] - 1, pos[1])
                if pos not in delivered:
                    house += 1
                    delivered.append(pos)
    return house


def robo_helps() -> int:
    pos_santa = (0, 0)
    pos_robo = (0, 0)
    delivered = []
    delivered.append(pos_santa)
    house = 1
    who = True
    with open("input.txt", "r") as f:
        for line in f:
            for char in line:
                if who == True:
                    who = False
                    if char == "^":
                        pos_santa = (pos_santa[0], pos_santa[1] + 1)
                    elif char == "v":
                        pos_santa = (pos_santa[0], pos_santa[1] - 1)
                    elif char == ">":
                        pos_santa = (pos_santa[0] + 1, pos_santa[1])
                    else:
                        pos_santa = (pos_santa[0] - 1, pos_santa[1])
                    if pos_santa not in delivered:
                        house += 1
                        delivered.append(pos_santa)
                else:
                    who = True
                    if char == "^":
                        pos_robo = (pos_robo[0], pos_robo[1] + 1)
                    elif char == "v":
                        pos_robo = (pos_robo[0], pos_robo[1] - 1)
                    elif char == ">":
                        pos_robo = (pos_robo[0] + 1, pos_robo[1])
                    else:
                        pos_robo = (pos_robo[0] - 1, pos_robo[1])
                    if pos_robo not in delivered:
                        house += 1
                        delivered.append(pos_robo)
    return house


def main() -> None:
    print(one_present())
    print(robo_helps())


if __name__ == "__main__":
    main()
