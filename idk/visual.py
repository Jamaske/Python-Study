from copy import deepcopy

class Logger:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

    def __init__(self, arr, colors):
        size = len(arr)
        out_w = len(str(max(size-1, *arr)))
        self.iterations = 0

        self.colors = colors
        self.positions = [None] * len(colors)

        self.clean_idxs = list(map(lambda  i: f"{ i:0{out_w}}", range(size)))
        self.clean_vals = list(map(lambda el: f"{el:{out_w}}", arr))

        self.colored_idxs = deepcopy(self.clean_idxs)
        self.colored_vals = deepcopy(self.clean_vals)
    
    def move_colors(self, positions):
        for cur_pos, new_pos, color  in zip(self.positions, positions, self.colors):
            if cur_pos == new_pos:# color didn't chenged
                continue
            if cur_pos is not None and cur_pos not in positions:#clear old colorization
                self.colored_idxs[cur_pos] = self.clean_idxs[cur_pos]
                self.colored_vals[cur_pos] = self.clean_vals[cur_pos]
            if new_pos is not None:#colore new positions
                self.colored_idxs[new_pos] = f"{color}{self.clean_idxs[new_pos]}{self.END}"
                self.colored_vals[new_pos] = f"{color}{self.clean_vals[new_pos]}{self.END}"
        self.positions = positions

    def print(self):
        print(f"{' '.join(self.colored_idxs)}\n{' '.join(self.colored_vals)}\n")

    def __call__(self, move = None):
        if move is not None:
            self.move_colors(move)

        print(f"iter: {self.iterations}")
        self.print()
        self.iterations += 1


class EmptyLogger:
    def __init__(self):
        self.iterations = 0
    
    def __call__(self, *_):
        self.iterations += 1

def preaty(search):
    
    def wrapper(arr:list, value:int) -> int:
        if len(arr) <= 32:
            logger = Logger(arr, (Logger.RED, Logger.BLUE, Logger.GREEN))
        else:
            logger = EmptyLogger()

        print(f"=============== {search.__name__}({value}) ========\n")
        idx = search(arr, value, logger)
        logger((None,None, idx))
        print(f"found {arr[idx]}\nat index {idx}\nin {logger.iterations-1} iterations")

        return idx
    return wrapper