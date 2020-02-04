class Secret():
    def visible(self):
        print("Je suis VISIBLE")
    def _invisible(self):
        print("Pas vraiment visible...")
    def __invisible(self):
        print("Discret mais pas absolument invisible !")

secret = Secret()

secret.visible()
secret._invisible()
secret.__invisible()

secret.__Secret__invisible()