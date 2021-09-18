import copy


class MatrixSizeError(Exception):
    def __init__(self):
        pass


class Matrix:
    # Part 1
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)
        self.__len__ = len(matrix)
        self.determinant = 0

    def __str__(self):
        matrix_str = ''
        for line_index, line in enumerate(self.matrix):
            for elem_index, elem in enumerate(line):
                if elem_index == len(line) - 1:
                    matrix_str = matrix_str + str(elem)
                else:
                    matrix_str = matrix_str + str(elem) + '\t'

            if line_index != len(self.matrix) - 1:
                matrix_str = matrix_str + '\n'

        return matrix_str

    # Part 2
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError
        else:
            return self.matrix == other.matrix

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    # Part 3
    def __add__(self, other):
        # return self + other
        if not isinstance(other, self.__class__):
            raise TypeError
        else:
            if len(self.matrix) != len(other.matrix):
                raise MatrixSizeError
            else:
                result = []
                for i in range(len(self.matrix)):
                    if len(self.matrix[i]) != len(other.matrix[i]):
                        raise MatrixSizeError
                    else:
                        result.append([])
                        for j in range(len(self.matrix[0])):
                            result[i].append(
                                self.matrix[i][j] + other.matrix[i][j]
                            )
                return self.__class__(result)

    def __sub__(self, other):
        # return self - other
        if not isinstance(other, self.__class__):
            raise TypeError
        else:
            if len(self.matrix) != len(other.matrix):
                raise MatrixSizeError
            else:
                result = []
                for i in range(len(self.matrix)):
                    if len(self.matrix[i]) != len(other.matrix[i]):
                        raise MatrixSizeError
                    else:
                        result.append([])
                        for j in range(len(self.matrix[0])):
                            result[i].append(
                                self.matrix[i][j] - other.matrix[i][j]
                            )
                return self.__class__(result)

    # Part 4
    def __mul__(self, other):
        # return self * other
        if not isinstance(other, self.__class__):
            raise TypeError
        else:
            if len(self.matrix[0]) != len(other.matrix):
                raise MatrixSizeError
            else:
                result = []
                other_transposed = other.transpose()
                for i in range(len(self.matrix)):
                    result.append([])
                    for k in range(len(other_transposed.matrix)):
                        result[i].append(sum([
                            a*b for a, b in zip(
                                self.matrix[i], other_transposed.matrix[k]
                            )
                        ]))
                return self.__class__(result)

    # Part 5
    def transpose(self):
        str_len = len(self.matrix[0])
        result = []
        for i in range(len(self.matrix)):
            for k in range(str_len):
                if len(result) <= k:
                    result.append([])
                result[k].append(self.matrix[i][k])
        return self.__class__(result)

    # Part 6
    def tr(self):
        if len(self.matrix[0]) != len(self.matrix):
            raise MatrixSizeError
        else:
            result = 0
            for i in range(len(self.matrix)):
                result += self.matrix[i][i]
        return result

    def det(self):
        if len(self.matrix[0]) != len(self.matrix):
            raise MatrixSizeError
        else:
            indices = list(range(len(self.matrix)))

            if len(self.matrix) == 1 and len(self.matrix[0]) == 1:
                return self.matrix[0][0]

            if len(self.matrix) == 2 and len(self.matrix[0]) == 2:
                val = (
                    self.matrix[0][0] * self.matrix[1][1]
                ) - self.matrix[1][0] * self.matrix[0][1]
                return val

            for fc in indices:
                As = copy.deepcopy(self.matrix)
                As = As[1:]
                height = len(As)

                for i in range(height):
                    As[i] = As[i][0:fc] + As[i][fc+1:]

                sign = (-1) ** (fc % 2)
                new_matrix = self.__class__(As)
                sub_det = new_matrix.det()
                self.determinant += sign * self.matrix[0][fc] * sub_det

            return self.determinant


# a = Matrix([[9]])
# b = Matrix([[-8, 9, 12], [-7, 5, 6]])
# c = Matrix([[6, 3, 9], [4, 2, 6], [5, 9, 3]])
# print(a * b)
# print(c.det())
