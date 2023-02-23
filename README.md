#Part 1:
###TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

###TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

###TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 



# Part 2:
###TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

###TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"


###TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.


# Part 3:
###TODO-7: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
###TODO-8: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.


# Part 4:
### TODO-9: Import and print the logo from art.py when the program starts.
### TODO-10: What if the user enters a shift that is greater than the number of letters in the alphabet?
### TODO-11: What happens if the user enters a number/symbol/space?
    # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    # e.g. start_text = "meet me at 3"
    # end_text = "•••• •• •• 3"
### TODO-12: Can you figure out a way to ask the user if they want to restart the cipher program?