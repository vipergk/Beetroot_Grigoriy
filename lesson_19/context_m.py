class Myclass:
    def __init__(self, *args):
        self.args = args
        self.res = None

    def __enter__(self):
        self.res = Res()
        self.res.open(*self.args)
        return self.res

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.res:
            self.res.close()

if __name__ == '__main__':
    with Myclass() as res:
        res.sumething()
        raise ValueError('Value_Error')

