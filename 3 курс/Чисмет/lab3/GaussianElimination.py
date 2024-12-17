

class GaussianElimination():

    @classmethod
    def sub(cls, iterable, start=0):
        for val in iterable:
            start -= val
        return start


    def __init__(self, hight:int, width:int, source=None, ans = None, chose:bool = True):
        '''
        hight, width - размеры матрицы состоящей из обьединения матрицы A и набора правых векторов-стлбцов
        source - матрица в виде списка из списков-строк
        ans - матрица из заведомо верных ответов. В виде списка списков - столбцов - векторов
        chose - производить ли выбор главного элемента
        '''
        self.h = hight
        self.w = width
        self.m = min(hight, width)
        self.M = max(hight, width)
        self.data = source
        self.ans = ans
        self.chose = chose
        self.row_map = list(range(hight))
        self.col_map = list(range(width))


    def forward(self):
        print("forward step")
        self.print_state()
        for diag in range(self.m):
            if self.chose:
                # Find the maximum element in the remaining submatrix
                max_element = abs(self.data[self.row_map[diag]][self.col_map[diag]])
                max_row = diag
                max_col = diag
                for i in range(diag, self.h):
                    for j in range(diag, self.h):
                        if abs(self.data[self.row_map[i]][self.col_map[j]]) > max_element:
                            max_element = abs(self.data[self.row_map[i]][self.col_map[j]])
                            max_row = i
                            max_col = j
                
                # Update row and column maps
                self.row_map[diag], self.row_map[max_row] = self.row_map[max_row], self.row_map[diag]
                self.col_map[diag], self.col_map[max_col] = self.col_map[max_col], self.col_map[diag]
                print(f"max el {max_row},{max_col} is swaped")
                self.print_state()

            # Column calculations b_ij
            j = diag
            for i in range(diag, self.h):
                exp = self.sub((self.data[self.row_map[i]][self.col_map[k]] * self.data[self.row_map[k]][self.col_map[j]] for k in range(j)), start=self.data[self.row_map[i]][self.col_map[j]])
                print(f'b_{i}{j} = {exp.steps()}')
                exp.flush()
                self.data[self.row_map[i]][self.col_map[j]] = exp

            # Row calculations c_ij
            i = diag
            for j in range(diag + 1, self.w):
                exp = self.sub((self.data[self.row_map[i]][self.col_map[k]] * self.data[self.row_map[k]][self.col_map[j]] for k in range(i)), start=self.data[self.row_map[i]][self.col_map[j]])
                exp = exp / self.data[self.row_map[i]][self.col_map[i]]
                print(f'c_{i}{j} = {exp.steps()}')
                exp.flush()
                self.data[self.row_map[i]][self.col_map[j]] = exp

    def backward(self):
        print("\nbackward step\n")
        last_col = self.w - 1
        for i in range(self.h-1, -1, -1):
            exp = self.sub((self.data[self.row_map[i]][self.col_map[j]] * self.data[self.row_map[j]][self.col_map[last_col]] for j in range(self.h-1, i, -1)), start=self.data[self.row_map[i]][self.col_map[last_col]])
            print(f'x_{i} = {exp.steps()}')
            exp.flush()
            self.data[self.row_map[i]][self.col_map[last_col]] = exp
        self.print_state()
    
    def err(self):
        """
        for each rhs column-vector return its norm2 error from correct value
        """
        return [sum(( (float(self.data[self.row_map[i]][self.col_map[j]] - float(self.ans[j - self.h][i])))**2 for i in range(self.h)))**0.5   for j in range(self.h, self.w)]


    def solve(self):
        try:
            self.forward()
        except ZeroDivisionError:
            print("Devision by Zero. Skip rest of the algo")
            return
        self.backward()
        if self.ans is not None:
            print(f"errors: {', '.join(map(lambda err:  f'{err:.7f}',self.err()))}")
            


    def print_state(self):
        print()
        for i in range(self.h):
            print('|' , end = '')
            for j in range(self.w):
                print(self.data[self.row_map[i]][self.col_map[j]], end = '\t')
            print('|')
        print()

    