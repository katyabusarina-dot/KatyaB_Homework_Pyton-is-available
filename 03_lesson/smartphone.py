class Smartphone:
    def __init__(self, marka, model, phone_number):
        self.marka = marka
        self.model = model
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.marka}-{self.model}.{self.phone_number}"
