class Complex:
    def __checker(self, value):
        if (
            not isinstance(value, int) and
            not isinstance(value, float) and
            not isinstance(value, self.__class__)
        ):
            return False
        else:
            return True

    # Part 1
    def __init__(self, re=0, im=0):
        if (
            (
                not isinstance(re, int) and
                not isinstance(re, float)
            ) or (
                not isinstance(im, int) and
                not isinstance(im, float)
            )
        ):
            raise TypeError
        else:
            self.re = re
            self.im = im

    def __str__(self):
        string = str(self.re)
        if self.im >= 0:
            string = string + '+'
        string = string + str(self.im) + 'i'
        return string

    # Part 2
    def __add__(self, other):
        if not self.__checker(other):
            raise TypeError
        else:
            result = self.__class__()
            if isinstance(other, self.__class__):
                result.re = self.re + other.re
                result.im = self.im + other.im
            else:
                result.re = self.re + other
                result.im = self.im

            return result

    def __sub__(self, other):
        if not self.__checker(other):
            raise TypeError
        else:
            result = self.__class__()
            if isinstance(other, self.__class__):
                result.re = self.re - other.re
                result.im = self.im - other.im
            else:
                result.re = self.re - other
                result.im = self.im

            return result

    # Part 3
    def __mul__(self, other):
        if not self.__checker(other):
            raise TypeError
        else:
            result = self.__class__()
            complex_other = other
            if not isinstance(complex_other, self.__class__):
                complex_other = self.__class__(other)

            result.re = self.re*complex_other.re - self.im*complex_other.im
            result.im = self.re*complex_other.im + self.im*complex_other.re

            return result

    def __truediv__(self, other):
        if not self.__checker(other):
            raise TypeError
        else:
            result = self.__class__()
            complex_other = other
            if not isinstance(complex_other, self.__class__):
                complex_other = self.__class__(other)

            result.re = (
                self.re*complex_other.re + self.im*complex_other.im
            )/(complex_other.re**2 + complex_other.im**2)
            result.im = (
                self.im*complex_other.re - self.re*complex_other.im
            )/(complex_other.re**2 + complex_other.im**2)

            return result

    # Part 4
    def __eq__(self, other):
        if not self.__checker(other):
            raise TypeError
        else:
            complex_other = other
            if not isinstance(complex_other, self.__class__):
                complex_other = self.__class__(other)

            return self.re == complex_other.re and self.im == complex_other.im

    def __abs__(self):
        return (self.re**2 + self.im**2)**(1/2)


# a = Complex(3, -9)
# b = 11
# c = Complex(-5, 1)

# print(a.__abs__())
# print(a.__mul__(b))
# print(a.__mul__(c))

# print(a.__truediv__(a))
# print(a.__truediv__(b))
# print(a.__truediv__(c))
