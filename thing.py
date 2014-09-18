class thing:
        def __init__(self, name, parent = None):
            self.name = name
            if (parent):
                self.parent = parent
        def comosellama (self, p = 0):
            if p == True:
                print(self.name)
            return self.name

