
class RowReduction:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def getLongest(self):
        large = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                test = str(int(self.matrix[i][j]))
                numTest = len(test)
                large = max(large, numTest)
        return (large + 6)
    
    def printMatrix(self):
        largest = self.getLongest()
        result = ""
        format = "{:" + str(largest) + ".3f}"
        for i in range(len(self.matrix)):
            result += "|"
            for j in range(len(self.matrix[i])):
                result += format.format(self.matrix[i][j])
            result += "| \n"
        return result

    def partialPivoting(self, index):
        large = abs(self.matrix[index][index])
        largeIndex = index
        for i in range(index, len(self.matrix)):
            if abs(self.matrix[i][index]) > large:
                large = abs(self.matrix[i][index])
                largeIndex = i 
        temp = []
        for i in range(len(self.matrix[index])):
            temp.append(self.matrix[index][i])
        self.matrix[index] = self.matrix[largeIndex]
        self.matrix[largeIndex] = temp
        return self.matrix

    def singleRowReduction(self, colLocator, rowLocator):
        for i in range(rowLocator + 1, len(self.matrix)):
            ratio = self.matrix[i][colLocator] / self.matrix[rowLocator][colLocator]
            for j in range(len(self.matrix[0])):
                current = self.matrix[i][j]
                self.matrix[i][j] = (current - (ratio * self.matrix[rowLocator][j]))
        return self.matrix

    def checkZero(self, colLocator, rowLocator):
        return(self.matrix[rowLocator][colLocator] == 0)

    def rowReduction(self):
        rowLocator = 0
        colLocator = 0
        while (rowLocator < len(self.matrix)) & (colLocator < len(self.matrix[0])):
            self.partialPivoting(colLocator)
            if not self.checkZero(colLocator, rowLocator):
                self.singleRowReduction(colLocator, rowLocator)
            rowLocator += 1
            colLocator += 1
        return self.matrix

    # def partialPivoting(self):
    #     # largest in magnitude, need to change!!
    #     colLocator = 0
    #     for i in range(len(matrix)):
    #         if colLocator < len(matrix[0]):
    #             max = abs(matrix[i][colLocator])
    #             rowIndex = i
    #             for j in range(i, len(matrix)):
    #                 if abs(matrix[j][colLocator]) > max:
    #                     max = abs(matrix[j][colLocator])
    #                     rowIndex = j
    #             temp = matrix[i]
    #             matrix[i] = matrix[rowIndex]
    #             matrix[rowIndex] = temp
    #             colLocator += 1
    #         else:
    #             break
    #     print("partial")
    #     print(a.printMatrix())
    #     print()
    #     return matrix

    # def partialPivoting(self):
    #     # largest in magnitude, need to change!!
    #     pivot = 0
    #     while pivot < len(matrix) and pivot < len(matrix[0]):
    #         max = abs(matrix[pivot][pivot])
    #         rowIndex = pivot
    #         for i in range(pivot, len(matrix)):
    #             if abs(matrix[i][pivot]) > max:
    #                 max = abs(matrix[i][pivot])
    #                 rowIndex = i
    #         temp = matrix[rowIndex]
    #         matrix[rowIndex] = matrix[pivot]
    #         matrix[pivot] = temp
    #         pivot += 1
    #     print("partial")
    #     print(self.printMatrix())
    #     print()
    #     return matrix


    # def checkZero(self, colLocator, rowLocator):
    #     if (rowLocator < len(matrix)) & (colLocator < len(matrix[0])):
    #         return(matrix[rowLocator][colLocator] == 0)
    #     else:
    #         return False

            # self.singleRowReduction(colLocator, rowLocator)
            # print("reduce")
            # print(a.printMatrix())
            # print()
            # rowLocator += 1
            # colLocator += 1
            # while rowLocator < len(matrix) & colLocator < len(matrix[0]) & self.checkZero(colLocator, rowLocator):
            #     rowLocator += 1
            #     colLocator += 1





# matrix = [[1,3,3,9],[4,9,3,4], [2,6,1,2], [2,5,2,1], [9,5,2,1],[2,3,4,5]]
# matrix = [[0,0,0],[0,0,0],[0,0,0]]
matrix = [[3,2,1],[3,1,2],[3,0,1],[5,0,1]]


# a = RowReduction(matrix)
# print(a.printMatrix())
# print()
# a.rowReduction()
# print(a.printMatrix())
# from numpy import random
# matrix = random.uniform(size=(11, 10))

a = RowReduction(matrix)
print("Initial")
print(a.printMatrix())
print()
a.rowReduction()
print("Result")
print(a.printMatrix())