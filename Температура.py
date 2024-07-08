class Температура:
    def __init__(self, значение):
        self.значение = max(значение, -273)

    def __str__(self):
        return f"{self.значение}°"

    def __float__(self):
        return float(self.значение)

    def __add__(self, other):
        return self.__class__(self.значение + other.значение)

    def __sub__(self, other):
        return self.__class__(self.значение - other.значение)

    def __eq__(self, other):
        return self.значение == other.значение

    def __lt__(self, other):
        return self.значение < other.значение

    def __le__(self, other):
        return self.значение <= other.значение

    def в_фаренгейты(self):
        return Фаренгейт(self.значение * 9/5 + 32)

    def в_кельвины(self):
        return Кельвин(self.значение + 273.15)


class Цельсий(Температура):
    pass


class Фаренгейт(Температура):
    def __init__(self, значение):
        self.значение = max((значение - 32) * 5/9, -273)

    def в_цельсии(self):
        return Цельсий((self.значение - 32) * 5/9)

    def в_кельвины(self):
        return Кельвин(self.в_цельсии().значение + 273.15)


class Кельвин(Температура):
    def __init__(self, значение):
        self.значение = max(значение, 0)

    def в_цельсии(self):
        return Цельсий(self.значение - 273.15)

    def в_фаренгейты(self):
        return Фаренгейт(self.в_цельсии().значение * 9/5 + 32)
