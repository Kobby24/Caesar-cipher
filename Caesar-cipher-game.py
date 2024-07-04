import Day_eight           
print(Day_eight.logo)
run_again = True
while run_again:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")   
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceaser(coded_text, shif_num, direction):

        final_text = ""
        for letter in coded_text:
            if letter in alphabet:
                
                if direction == "encode":
                    position = alphabet.index(letter) + shif_num
                    if position > 25:
                        new_position = position % 26
                        final_text += alphabet[new_position]
                    else:
                        final_text += alphabet[position]
            
                elif direction == "decode":
                    position = alphabet.index(letter) - shif_num
                    
                    if position < 0:
                        new_position = position % 26
                        final_text += alphabet[new_position]
                    else:
                        final_text += alphabet[position]
            else:
                final_text += letter
        print(f"The {direction}d message is {final_text}")
    ceaser(text, shift, direction)
    restart = input("Do you want to restart the cypher if yes type 'yes' if no type 'no'\n").lower()
    if restart == "yes":
        run_again = True
    else:
        run_again = False
print("Goodbye")