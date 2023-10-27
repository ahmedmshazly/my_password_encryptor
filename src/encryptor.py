# encryptor.py

import random
import string

def encrypt(password, keyword):
    try:
        encrypted_password = ''
        keyword_length = len(keyword)

        for i, char in enumerate(password):
            keyword_char = keyword[i % keyword_length]  # Repeating keyword characters
            encrypted_char = chr((ord(char) + ord(keyword_char)) % 256)
            encrypted_password += encrypted_char

        if len(encrypted_password) >= 15:
            return "C" + encrypted_password[:12] + ">"
        else:
            encrypted_password = "C" + encrypted_password + ">"
            # Add padding to make sure length is 15
            padding = add_chars(15 - len(encrypted_password))
            encrypted_password += padding

            return encrypted_password

    except Exception as e:
        raise ValueError(f"An error occurred during encryption: {e}")

def decrypt(encrypted_password, keyword):
    try:
        def cut_string(input_string, target_char):
            # Use split to separate the string at the target character
            split_string = input_string.split(target_char)

            # Return the first part of the split
            return split_string[0]

        if encrypted_password.startswith("C") and ">" in encrypted_password:

            if encrypted_password.startswith("C") and encrypted_password.endswith(">"):
                encrypted_password = encrypted_password[1:-1]  # Remove padding markers
                keyword_length = len(keyword)

                decrypted_password = ''
                for i, char in enumerate(encrypted_password):
                    keyword_char = keyword[i % keyword_length]  # Repeating keyword characters
                    decrypted_char = chr((ord(char) - ord(keyword_char)) % 256)
                    decrypted_password += decrypted_char

                return decrypted_password

            elif encrypted_password.startswith("C"):
                encrypted_password = cut_string(encrypted_password, ">")[1:]
                keyword_length = len(keyword)

                decrypted_password = ''
                for i, char in enumerate(encrypted_password):
                    keyword_char = keyword[i % keyword_length]  # Repeating keyword characters
                    decrypted_char = chr((ord(char) - ord(keyword_char)) % 256)
                    decrypted_password += decrypted_char

                return decrypted_password

            else:
                raise ValueError("Invalid encrypted password format")

        else:
            raise ValueError("Invalid encrypted password format")

    except Exception as e:
        raise ValueError(f"An error occurred during decryption: {e}")

def add_chars(length):
    try:
        chars = string.ascii_letters + string.punctuation
        chars_length = len(chars)

        generated_chars = ""
        for i in range(length):
            generated_chars += chars[i % chars_length]

        return generated_chars

    except Exception as e:
        raise ValueError(f"An error occurred during character addition: {e}")

