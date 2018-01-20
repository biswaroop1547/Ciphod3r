import string
import time


def load_words(file_name):
    """
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.

    """
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    in_file.close()
    return word_list


def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        """
        Initializes a Message object
                
        text (string): the message's text

        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        """
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        """
        return self.message_text

    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        """
        return self.valid_words[:]

    @staticmethod
    def build_shift_dict(shift):
        
        """
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.
    
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        """
        all_lower_list = string.ascii_lowercase
        all_upper_list = string.ascii_uppercase
        the_dict = {}
        if shift > 26:
            while True:
                shift -= 26
                if shift < 26:
                    break
    
        for i in all_lower_list:
    
            sums = ord(i) + shift
            if sums > 122:
                sums -= 26
            the_dict[i] = chr(sums)
    
        for i in all_upper_list:
            sums = ord(i) + shift
            if sums > 90:
                sums -= 26
            the_dict[i] = chr(sums)
    
        return the_dict


    def apply_shift(self, shift):
        """
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        """

        the_msg = self.get_message_text()

        the_shift_dict = self.build_shift_dict(shift)

        new_msg = ''

        for i in the_msg:
            if i not in list(string.punctuation + ' ' + string.digits):
                new_msg += the_shift_dict[i]

            else:
                new_msg += i

        return new_msg


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        """
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        """
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        """
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        """
        return self.shift

    def get_encrypting_dict(self):
        """
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        """
        return self.encrypting_dict.copy()

    def dict_setter(self, shift):
        self.encrypting_dict = self.build_shift_dict(shift)

    def get_message_text_encrypted(self):
        """
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        """
        return self.message_text_encrypted

    def text_msg_setter(self, shift):
        self.message_text_encrypted = self.apply_shift(shift)

    def change_shift(self, shift):
        """
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).

        Returns: nothing
        """
        if shift > 26:
            while True:
                shift -= 26
                if shift < 26:
                    break
                    
        self.dict_setter(shift)
        self.text_msg_setter(shift)
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        """
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        """
        Message.__init__(self, text)

    def decrypt_message(self):
        """
        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        """

        a_list = []
        for shift in range(26):
            i = 0
            puzzled_msg = self.apply_shift(shift)
            word_list = puzzled_msg.split(' ')

            for j in word_list:
                if is_word(self.get_valid_words(), j):
                    i += 1

            a_list.append(i)
        the_max = max(a_list)
        req_shift = a_list.index(the_max)

        return req_shift, self.apply_shift(req_shift)

def intro():
    from time import sleep

    print('\t\t', end="")
    for i in range(85):
        print('=', end="", flush=True)
        sleep(0.01)

    print('')
    print('\t\t', end="")
    print('||                                                                                 ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||       # #                                                                       ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||     #                                                                           ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||    #                                                                            ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||    #         #            #     #       #  #      ## #     ## ##                ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||    #                      #     #     #      #    #    #         #              ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||    #         #  # # #     #     #    #         #  #     #         #  #  ## #    ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||    #         #  #     #   #######   #           # #      #        #  # #    #   ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||     #        #  #      #  #     #   #           # #      #  ######   ##         ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||      #       #  #      #  #     #    #          # #      #        #  #          ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||        ###   #  # # # #   #     #     #        #  #     #         #  #          ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||                 #         #     #        # # #     ### #   ## ###    #          ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||                 #                                                               ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||                 #                                                               ||', flush=True)
    print('\t\t', end="")
    sleep(0.08)
    print('||                                                                                 ||')
    print('\t\t', end="")

    for i in range(85):
        print('=', end="", flush=True)
        sleep(0.01)
    for i in '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    ~ by biswaroop08':
        print(i, end="", flush=True)
        sleep(0.05)
    print('')
    

def main():
    intro()
    print('\n\n')
    print('\t\t\t\tWould you like to encrypt a text or decrypt a text ?')
    time.sleep(2)

    while True:
        print('')
        user_input_1 = input("\t\t\t\tPlease Enter encrypt or decrypt or Q to exit: ")

        if user_input_1.lower() == 'encrypt':
            while True:
                print('')
                user_input_2 = input("\t\t\t\tPlease Enter your text! : ")
                if user_input_2:
                    break

            while True:
                user_input_3 = int(input("\t\t\t\tEnter by how many places you want to shift the letters ? : "))
                if type(user_input_3) == int:
                    break

            plaintext = PlaintextMessage(user_input_2, user_input_3)
            encrypted_msg = plaintext.get_message_text_encrypted()
            text_shift = user_input_3
            
            print('\n\n')
            print('\t\t\t\tEncrypting......Please wait!')
            print('\t\t\t\t', end= "")
            for i in range(50):
                time.sleep(0.04)
                print("█", end="", flush=True)
            time.sleep(2)
            print('')
            print('\t\t\t\tYour message has been successfully encrypted!!\n')
            print(f'\t\t\t\tYour Encrypted text with shift --> {text_shift} is : {encrypted_msg}\n')
            user_input_4 = input("\t\t\t\tPress Q to exit or press any key to continue using: ")
            if user_input_4.lower() == 'q':
                break

        elif user_input_1.lower() == 'decrypt':
            while True:
                print()
                user_input_2 = input("\t\t\t\tPlease Enter your secret text! : ")
                if user_input_2:
                    break

            ciphertext = CiphertextMessage(user_input_2)
            decrypted_msg_with_shift = ciphertext.decrypt_message()
            decrypted_msg = decrypted_msg_with_shift[1]
            shifted = decrypted_msg_with_shift[0]
            print('\n\n')
            print('\t\t\t\tDecrypting......Please wait!\n')
            time.sleep(2)
            print('\t\t\t\tBreaking the code....', end="")
            time.sleep(3)
            print('..little more..')
            time.sleep(1)
            print('\t\t\t\t', end= "")
            for i in range(50):
                time.sleep(0.1)
                print("█", end="", flush=True)
            time.sleep(1)
            print('')
            print('\t\t\t\tSuccess!!!!\n')
            print(f'\t\t\t\tYour decoded text is : "{decrypted_msg}"\n')
            print(f'\t\t\t\there the texts shifted {shifted} places')
            time.sleep(2)
            print('')
            user_input_4 = input("\t\t\t\tPress Q to exit or press any key to continue using: ")
            if user_input_4.lower() == 'q':
                break
        
        elif user_input_1.lower() == 'q':
            exit()

        else:
            time.sleep(2)
            print('\n\n')
            print('\t\tSorry something went wrong please try again!! ')
            time.sleep(2)

    time.sleep(1)
    print('\t\t\t\tThank you for using!! :D')
    time.sleep(2)


main()
