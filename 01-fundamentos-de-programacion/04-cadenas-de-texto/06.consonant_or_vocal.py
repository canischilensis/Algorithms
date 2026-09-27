def consonant():
    letter=input("Hi Hooman, enter you consonant ").lower()
    if letter=="a":
        print("stupid hooman, i say 'enter your consonant'")
        return consonant()
    if letter=="e":
        print("stupid hooman, i say 'enter your consonant'")
        return consonant()
    if letter=="i": 
        print("stupid hooman, i say 'enter your consonant'")
        return consonant()
    if letter=="o":
        print("stupid hooman, i say 'enter your consonant'")
        return consonant()
    if letter=="u":
        print("stupid hooman, i say 'enter your consonant'")
        return consonant()
    else:
        print('Excelent, no bad!')

if __name__=="__main__":
    consonant()
