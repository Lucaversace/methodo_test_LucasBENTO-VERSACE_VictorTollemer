from languefrancaise import LangueFrancaise
from langueanglaise import LangueAnglaise
from momentdelajournee import MomentDeLaJournee
from verificateur_palindrome import VerificateurPalindrome

def main():
    langue = LangueFrancaise()  # ou LangueAnglaise()
    moment = MomentDeLaJournee.obtenir_moment()

    print(langue.saluer(moment))

    try:
        while True:
            texte = input("Entrez un texte (ou 'quitter' pour arrêter) : ")
            if texte.lower() == 'quitter':
                print(langue.acquitter(moment))
                break

            print(f"Écho : {texte[::-1]}")
            if VerificateurPalindrome.est_palindrome(texte.replace(" ", "").lower()):
                print(langue.feliciter())
    except KeyboardInterrupt:
        print(langue.acquitter(moment))

if __name__ == "__main__":
    main()
