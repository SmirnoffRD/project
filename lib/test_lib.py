class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return 'Name: {}, Age: {}'.format(self.age, self.name)
