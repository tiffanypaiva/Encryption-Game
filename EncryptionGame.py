def Encrypt(Message, Key):
    #Encrypt Message with a Key.
    Result_ = ''



    for Letter_ in Message:
        if Letter_.isalpha():


            Num = ord(Letter_)

            if Letter_.isupper():
                Base = ord('A')
            elif Letter_.islower():
                Base = ord('a')

            # This is the Encryption equation:

            Num = (Num - Base + Key) % 26 + Base

            Result_ += chr(Num)

        elif Letter_.isdigit():

            # This will encrpt
            Result_ += Letter_

        else:
            Result_ += Letter_

    return Result_

def Decrypt(Message, Key):
    #Decrypt Message with a Key.
    return Encrypt(Message, -Key)

def Decode(Message):
    #Decode Message without a Key.
    pass

def get_Key():
    #Get a Key from the user.
    try:
        text = input('Please Enter a Key (1 - 25): ')
        Key = int(text)
        return Key
    except:
        print('That is an Invalid Key. Using Key: 0.')
        return 0

print('Do you want me to Encrypt, Decrypt, or Decode a Message for this occasion?')
Choice = input()

if Choice == 'Encrypt':
    Phrase = input('Message: ')
    Code = get_Key()
    print('Encrypted Message:', Encrypt(Phrase, Code))
elif Choice == 'Decrypt':
    Phrase = input('Message: ')
    Code = get_Key()
    print('Decrypted Message:', Decrypt(Phrase, Code))
elif Choice == 'Decode':
    Phrase = input('Message: ')
    print('Decoding Message:')
    Decode(Phrase)
else:
    print('There Has Been An Error: Unrecognized Command')
