class VerificateurPalindrome:
    @staticmethod
    def est_palindrome(chaine):
        return chaine == chaine[::-1]
