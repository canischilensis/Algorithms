def palindrome(word):
    word=word.lower()
    word=word.replace(' ','')
    if word==word[::-1]:
        return True
    else:
        return False

def run():
    word=input("Please, enter yor phrase or word:")
    if palindrome(word):
        print("this is palindrome")
    else:
        print("this is not palindrome")

if __name__ == "__main__":
    run()