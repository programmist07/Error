class NolgaKopaytirma1(Exception):

    def __init__(self, message):
        self.a = message

    def __str__(self):
        return self.a