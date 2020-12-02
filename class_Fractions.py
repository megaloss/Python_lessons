class Fraction:
    def __init__(self, u, d):
        self.u = u
        self.d = d

    def __str__(self):
        return f'{self.u} / {self.d}'

    def simplify(self):
        if self.d == 0:
            return False
        elif self.u/self.d > 0:
            positive = True
        else:
            positive = False

        for i in range(int(min(abs(self.d), abs(self.u))), 1, -1):
            if self.d % i == 0 and self.u % i == 0:

                return Fraction(int(self.u / i), int(self.d / i))
        return Fraction(self.u, self.d)

    def __mul__(self, other):
        return Fraction(self.u * other.u, self.d * other.d).simplify()

    def __truediv__(self, other):
        return Fraction(self.u * other.d, self.d * other.u).simplify()

    def __add__(self, other):
        return Fraction(self.u * other.d + self.d * other.u, self.d * other.d).simplify()

    def __sub__(self, other):
        if self.u * other.d - self.d * other.u == 0:
            return Fraction (0,0)
        return Fraction(self.u * other.d - self.d * other.u, self.d * other.d).simplify()


fraction1 = Fraction(3, 21)
fraction2 = Fraction(13, 27)
print("1-st fraction is: ", fraction1, "simplified is: ", fraction1.simplify())
print("2-nd fraction is: ", fraction2, "simplified is: ", fraction2.simplify())
print('\n_____Calculations_____\n')
print("Multiplied: ", (fraction1 * fraction2))
print("Divided: ", (fraction1 / fraction2))
print("Sum: ", (fraction1 + fraction2))
print("Sub: ", (fraction1 - fraction2))

