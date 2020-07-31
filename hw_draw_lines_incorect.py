def drawLine(length=0, direction="v"):
    try:
        length = float(input("Indicati lungimea (ex: 10): "))
    except:
        print("Indicati doar numere intregi!")
    direction = input("Indicati orientarea (ex: v - verticala/ h - orizontala): ")

    if length == int(length) and length != str(length) and direction == "h":
        while length >= 0:
            print("-"*int(length))
            length -= 1
            break
    elif length == int(length) and direction == "v":
            while length >= 0:
                print("|\n"*int(length))
                length -= 1
                break
    else:
        print("Indicati doar numere intregi / alegeti directia orizontala sau verticala")

drawLine()
