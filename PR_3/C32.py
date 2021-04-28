class C32:
    def __init__(self):
        self.state = 'A'

    def erase(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'E':
            self.state = 'E'
            return 7
        elif self.state == 'F':
            self.state = 'F'
            return 8
        else:
            raise RuntimeError

    def share(self):
        if self.state == 'B':
            return 2
        else:
            raise RuntimeError

    def make(self):
        if self.state == 'B':
            self.state = 'E'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise RuntimeError
