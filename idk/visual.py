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

        self.colors = colors
        self.positions = [None] * len(colors)

        self.clean_idxs = list(map(lambda  i: f"{ i:0{out_w}}", range(size)))
        self.clean_vals = list(map(lambda el: f"{el: {out_w}}", arr))

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

    
    def __call__(self, move = None):
        if move is not None:
            self.move_colors(move)
        print(f"{' '.join(self.colored_idxs)}\n{' '.join(self.colored_vals)}\n")


def preaty(search):
    
    def wrapper(arr:list, value:int) -> int:
        logger = Logger(arr, (Logger.RED, Logger.BLUE, Logger.GREEN))
        print(f"=============== {search.__name__}({value}) ========\n")
        idx = search(arr, value, logger)
        print("result:")
        logger((None,None, idx))
        return idx
    return wrapper