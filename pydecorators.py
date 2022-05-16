
class employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@gmail.com'

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        if self.first or self.last == None:
            return "Employees firstname and lastname is not set "
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('delete name')


emp1 = employee('vandana', 'dubey')
emp1.fullname = 'Arun Dubey'

print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)

print()
del emp1.fullname
print(emp1.fullname)
