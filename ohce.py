def is_palindrome(s):
    return s == s[::-1]

def main():
    print("Bonjour")

    while True:
        user_input = input("Entrez un texte (ou 'quitter' pour arrêter) : ")

        if user_input.lower() == 'quitter':
            print("Au revoir")
            break

        print(f"Vous avez écrit : {user_input}")

        if is_palindrome(user_input.replace(" ", "").lower()):
            print("Bien dit")

if __name__ == "__main__":
    main()
