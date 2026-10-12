class PSHS_Galaxy:
    def __init__(self):
        self.__name = "a"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        print("Name has been set to:", value)


class Nationality(PSHS_Galaxy):
    def __init__(self):
        super().__init__()
        self.__nationality = "Filipino"

    @property
    def nationality(self):
        return self.__nationality

    @nationality.setter
    def nationality(self, value):
        self.__nationality = value
        print("Nationality has been set to:", value)


class Alien(PSHS_Galaxy):
    def __init__(self):
        super().__init__()
        self.__species = "Kree"

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__species = value
        print("Species has been set to:", value)


class Filipino(Nationality):
    def __init__(self):
        super().__init__()
        self.__food = "adobo"

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, value):
        self.__food = value
        print("Food has been set to:", value)


class Indonesian(Nationality):
    def __init__(self):
        super().__init__()
        self.__food = "nasi goreng"

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, value):
        self.__food = value
        print("Food has been set to:", value)


class Spaniards(Nationality):
    def __init__(self):
        super().__init__()
        self.__food = "paella"

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, value):
        self.__food = value
        print("Food has been set to:", value)


class Marvel(Alien):
    def __init__(self):
        super().__init__()
        self.__weapon = "shield"
        self.__character = "Captain America"

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, value):
        self.__weapon = value
        print("Weapon has been set to:", value)

    @property
    def character(self):
        return self.__character

    @character.setter
    def character(self, value):
        self.__character = value
        print("Character has been set to:", value)


class Avengers(Alien):
    def __init__(self):
        super().__init__()
        self.__weapon = "hammer"
        self.__character = "Thor"

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, value):
        self.__weapon = value
        print("Weapon has been set to:", value)

    @property
    def character(self):
        return self.__character

    @character.setter
    def character(self, value):
        self.__character = value
        print("Character has been set to:", value)

