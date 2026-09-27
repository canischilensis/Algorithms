def main(high, width):
    for i in range(high):
        for j in range(width):
            print("*", end="")
        print()

if __name__ == '__main__':
    ancho=int(input("Ingrese el ancho de su figura: "))
    alto=int(input("Ingrese el alto de su figura: "))
    main(alto, ancho)