
def drawLine(length, direction):
    if direction == "h":
        while length >= 0:
            print("-"*int(length))
            length -= 1
            break
    if direction == "v":
        while length >= 0:
            print("|\n"*int(length))
            length -= 1
            break

drawLine(5, "v")