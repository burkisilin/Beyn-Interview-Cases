import inspect
class MatchDetail:
    def __init__(self):
        self.id = None
        self.name = None
        self.date = None

    def props(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        return [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]