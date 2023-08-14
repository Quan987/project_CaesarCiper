from art import *
def caesar(u_dir):
    if u_dir == "encode" or u_dir == "decode":
        u_text = input("\nType your message: ")
        u_shift = int(input("\nType the shift number: "))
        char_list = []
        for i in range(len(u_text)):
            # if user want to encode
            if u_dir == "encode":
                char_list.append(alphabet.index(u_text[i]) + u_shift)
                if char_list[i] > len(alphabet):
                    char_list[i] %= len(alphabet)
            # user want to decode
            else:
                char_list.append(alphabet.index(u_text[i]) - u_shift)
            char_list[i] = alphabet[char_list[i]]
        print(f"\nThe {u_dir} text is: {''.join(char_list)}")
        char_list.clear()
    else:
        print("Please enter 'encode' or 'decode'!")
# main
stopper = False
print(logo + "\nWelcome to the Caesar Cipher Program!\n")
while not stopper:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    caesar(u_dir=direction)
    if input("\nDo you want to go again? Type 'y' or 'n': ") == "y":
        print()
    else:
        stopper = True
        print("\nProgram End!")
