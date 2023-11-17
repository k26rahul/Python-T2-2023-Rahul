class Signal:
    def __init__(self, T):
        self.state = 'red'
        self.v = 0
        self.T = T

    def sense(self, v):
        self.v = v

    def update(self):
        self.state = 'red' if self.v < self.T else 'green'
