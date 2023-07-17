print("Spy Code Machine")
# User enters a message and it returns a secret code in encode mode
# User enters the secret message and the machine decrypts the message for the user

def enigma():

    # create keys string
    keys = "abcdefghijklmnopqrstuvwxyz !"
    # autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0 : -1]

    # print(keys)
    # print(values)

    # create 2 dictionaries
    dict_encode = dict(zip(keys, values))
    dict_decode = dict(zip(values, keys))

    # user input: 'the message' and mode
    msg = input("Enter your secret message: ")
    mode = input("Crypto modes- encode (e) /decode (d): ")

    # run encode or decode
    if mode.lower() == 'e':
        new_msg = ''.join([dict_encode[letter] for letter in msg])
    elif mode.lower() == 'd':
        new_msg = ''.join([dict_decode[letter] for letter in msg])
    else:
        print("Invalid input")
        return None

    return new_msg


print(enigma())


