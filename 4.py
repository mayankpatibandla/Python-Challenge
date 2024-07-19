import urllib
import urllib.request

x = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
y = "12345"


def foo(y: str) -> str:
    with urllib.request.urlopen(x + y) as f:
        return str(f.read())


a = "and the next nothing is "
prev_y = ""
while True:
    z = foo(y)
    if "Divide by two and keep going" in z:
        y = z[z.find(a) + len(a) :].rstrip("'")
        y = int(prev_y) / 2
        y = str(y)
        print("Dividing by two", y)
    if a in z:
        y = z[z.find(a) + len(a) :].rstrip("'")
        print("y", y)
    else:
        print(z)
    prev_y = y
