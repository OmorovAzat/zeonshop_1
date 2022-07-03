def azat(func):
    def wrapper():
        print('Yasuo')
        func()
        print('zed')
        return wrapper()

def ddd():
    print("legeu")

    ddd = azat(ddd())