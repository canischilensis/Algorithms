def main():
    n=int(input('Ingrese un número: '))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('*',end='5')
        print()

if __name__ == '__main__':
    main()