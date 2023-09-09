from read import Read
import sys


class Function(Read):
    def __init__(self):
        super().__init__()

    def close(self):
        sys.exit()

    def setting(self):
        pass