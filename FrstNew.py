Num = str([+375296631274, +375296630940, +375296628268, +375296623912, +375296623085])
with open('text3.txt', 'w+', encoding="utf8") as file:
    print(file.write(Num))


def Anysumm(x: int, y: int) -> float:
    return x + y


f = str(Anysumm(3, 4))
with open('text4.txt', 'w+', encoding="utf8") as file:
    print(file.write(f))