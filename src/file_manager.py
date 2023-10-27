# file_manager.py

def write_to_file(password):
    try:
        with open('./data/passwords.txt', 'r', encoding='utf-8') as file:
            passwords = file.read().splitlines()

        if password not in passwords:  # Check if the password already exists
            with open('./data/passwords.txt', 'a', encoding='utf-8') as file:
                file.write(password + '\n')
        else:
            print(f"The password '{password}' already exists. Skipping write operation.")
    except FileNotFoundError as e:
        print(f"Error: {e}. 'data/passwords.txt' file not found.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_from_file():
    try:
        with open('./data/passwords.txt', 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except FileNotFoundError as e:
        print(f"Error: {e}. 'data/passwords.txt' file not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading from the file: {e}")
        return []

