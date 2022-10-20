print("Caesar Cypher")

alpha = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
alphabets = alpha.split(",")

def encode(message, shift_amount):
    messages = list(message)
    encoded_msg = []
    for char in message:
        if char not in alphabets:
            encoded_msg.append(char)
        else:
            position = alphabets.index(char)
            new_position = position + shift_amount
            encoded_msg.append(alphabets[new_position])


    # Print encoded msg
    print(encoded_msg)

def decode(encoded_msg, shift_amount):
    decoded_msg = []
    for char in encoded_msg:
        if char not in alphabets:
            decoded_msg.append(char)
        else:
            position = alphabets.index(char)
            new_position = position - shift_amount
            decoded_msg.append(alphabets[new_position])

    print(decoded_msg)



def caesar(text, shit_amount, direction):
    end_text = []
    if direction == "decode":
        shit_amount *= -1
    for char in text:
        if char not in alphabets:
            end_text.append(char)
        else:
            position = alphabets.index(char)
            new_position = position + shit_amount
            #print(f"current position : {position} - new position : {position + shit_amount}")
            end_text.append(alphabets[new_position])
            shit_amount = shit_amount

    for x in end_text:
        print(x, end="")
    print("\n")


go_again = 'yes'

print(go_again)

direction_tab = ['encode', 'decode']

while go_again == 'yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt ").lower()

    if direction not in direction_tab:
        print("You should type 'encode' to encrypt and type 'decode' to decrypt.")
        go_again = input("Type 'yes' if you want to go again, Otherwise type 'no'.")
    else:
        text = input("Type the text here : ")
        shift = int(input("Type the shift number : "))
        if shift < 0 or shift > 45:
            print("You cannot use this shift")
        else:
            caesar(text, shift, direction)
            go_again = input("Type 'yes' if you want to go again, Otherwise type 'no'.")


#text = input("Type text : ").lower()
#caesar(text, 5, direction)




#direction = input("Direction : (encode | decode)").lower()
#text = input("Type text : ").lower()
#caesar(text, 5, direction)





#encode("hello world!", 5)

#decode("mjqqt btwqi!", 5)