class CoffeeBase:
    
    @staticmethod
    def from_dict(source):
        pass

    def to_dict(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}/\n{self.to_dict()}'