y = "90052"


def foo(y: str) -> str:
    with open("channel/" + y + ".txt") as f:
        return str(f.read())


a = "Next nothing is "
prev_y = []
while True:
    z = foo(y)
    if "Divide by two and keep going" in z:
        y = z[z.find(a) + len(a) :].rstrip("'")
        y = int(prev_y[-1]) / 2
        y = str(y)
        print("Dividing by two", y)
    if "Collect the comments." in z:
        print("Comments", y, prev_y)
        break
    if a in z:
        y = z[z.find(a) + len(a) :].rstrip("'")
        print("y", y)
    else:
        print(z)
    prev_y.append(y)
