class country:
    def __init__(self,country,language,continent):
        self.country=country
        self.language=language
        self.continent=continent
    def welcome(self):
        print("Welcome")
Ken=country("Kenya","Swahili","Africa")
print(Ken.welcome)


