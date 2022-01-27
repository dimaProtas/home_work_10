class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


    # def func(self):
    #     for i in self.matrix:
    #         for j in i:
    #             print("{:4d}".format(j), end = "")
    #         print()


    def __add__(self, other):
        mat = []
        for i in range(len(self.matrix)):
            itr= []
            for j in range(len(self.matrix[0])):
                x = self.matrix[i][j] + other.matrix[i][j]
                itr.append(x)
            mat.append(itr)
            result = str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))
        return result



m_1 = Matrix([[1, 2, 3], [5, 6, 6], [7, 9, 4]])
m_2 = Matrix([[1, 8, 4], [5, 6, 2], [5, 8, 4]])
m_3 = Matrix([[56, 64, 234, 45], [987, 745, 4, 76], [87, 13, 65, 65]])
m_4 = Matrix([[6, 4, 4, 5], [9, 5, 4, 6], [8, 1, 6, 5]])
# m_1.func()
# basket = m_1 + m_2
# print(basket)
# print(type(m_1))
print(m_2)
# basket_2 = m_3 + m_4
# print(basket_2)