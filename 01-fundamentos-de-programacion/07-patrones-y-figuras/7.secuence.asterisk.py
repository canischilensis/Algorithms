def main():
    for i in range(high):
        for j in range(width):
            print("*", end="")
        print()

if __name__ == '__main__':
    width=int(input("Ingrese el ancho de su figura: "))
    high=int(input("Ingrese el alto de su figura: "))
    main()