

class GaussianElimination():

    @classmethod
    def sub(cls, iterable, start=0):
        for val in iterable:
            start -= val
        return start


    def __init__(self, hight:int, width:int, source=None, correct = None, chose:bool = True):
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
        self.correct = correct
        self.chose = chose
        self.row = list(range(hight))
        self.col = list(range(width))


    def forward(self):
        print("forward step")

        if not self.chose: self.print_state()
        for diag in range(self.m):
            if self.chose:
                self.print_state()
                # Find the maximum element in the remaining submatrix
                max_element = abs(self.data[self.row[diag]][self.col[diag]])
                i_max = diag
                j_max = diag
                for i in range(diag, self.h):
                    cur_row = self.row[i]
                    for j in range(diag, self.h):
                        cur_col = self.col[j]
                        if (el := abs(self.data[cur_row][cur_col]) > max_element):
                            max_element = el
                            i_max = i
                            j_max = j
                            
                
                # swap cur diaganal element with max via row, col permutation (maps values swaps)
                
                main_row = self.row[i_max]
                main_col = self.col[j_max]
                self.row[i_max] = self.row[diag]
                self.col[j_max] = self.col[diag]
                self.row[diag] = main_row
                self.col[diag] = main_col
                print(f"max el {i_max + 1},{j_max + 1} is swaped")
                self.print_state()

            # Column calculations b_ij
            j = diag
            for i in range(diag, self.h):
                cur_row = self.row[i]
                exp = self.sub((self.data[cur_row][self.col[k]] * self.data[self.row[k]][main_col] for k in range(j)), start=self.data[cur_row][main_col])
                print(f'b_{i + 1}{j + 1} = {exp.steps()}')
                exp.flush()
                self.data[cur_row][main_col] = exp

            # Row calculations c_ij
            i = diag
            for j in range(diag + 1, self.w):
                cur_col = self.col[j]
                exp = self.sub((self.data[main_row][self.col[k]] * self.data[self.row[k]][cur_col] for k in range(i)), start=self.data[main_row][cur_col])
                exp = exp / self.data[self.row[i]][self.col[i]]
                print(f'c_{i + 1}{j + 1} = {exp.steps()}')
                exp.flush()
                self.data[main_row][cur_col] = exp

    def backward(self):
        print("\nbackward ste p\n")
        self.print_state()
        last_col = self.w - 1
        for i in range(self.h-1, -1, -1):
            exp = self.sub((self.data[self.row[i]][self.col[j]] * self.data[self.row[j]][self.col[last_col]] for j in range(self.h-1, i, -1)), start=self.data[self.row[i]][self.col[last_col]])
            print(f"x'_{i + 1} = {exp.steps()}")
            exp.flush()
            self.data[self.row[i]][self.col[last_col]] = exp
        self.print_state()
    
    def answer(self):
        print('answer')
        ans = []
        for j in range(self.h, self.w):
            vect = []
            for i in range(self.h):
                # Да-да двойное отобрпжение через таблицы перестановок.
                # Почему? Я не имею ни малейшего понятия.
                # Как я это вывел? Больно... очень больно.
                x = self.data[self.row[self.col[i]]][self.col[j]]
                vect.append(x)
                print(x, end = '\t')
            ans.append(vect)
            print()
        self.ans = ans
        print()

    def err(self):
        """
        for each rhs column-vector return its norm2 error from correct value
        """
        return [sum(( (float(self.ans[j][i]) - float(self.correct[j][i])))**2 for i in range(self.h))**0.5   for j in range(self.w - self.h)]


    def solve(self):
        try:
            self.forward()
        except ZeroDivisionError:
            print("Devision by Zero. Skip rest of the algo")
            return
        self.backward()
        self.answer()
        if self.correct is not None:
            print(f"errors: {', '.join(map(lambda err:  f'{err:.7f}',self.err()))}")
            


    def print_state(self):
        print()
        for i in range(self.h):
            print('|' , end = '')
            for j in range(self.w):
                print(self.data[self.row[i]][self.col[j]], end = '\t')
            print('|')
        print()

    