from lib.test_lib import Person

class Person2(Person):
    def __str__(self):
        return 'Info: Name: {}'.format(self.name)

P = Person(20, 'John')
p = Person2(23, 'Boris')

print(P, '\n', p)

Sam = Person2(21, 'Sam')
print(Sam)