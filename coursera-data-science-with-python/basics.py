import sys

#tuple, immutable
x = (1, 'a')
print type(x)
print len(x)

#list, mutable
y = [1, 'a']
print type(y)
print len(y)
print 1 in y

#looping
for i in y:
    print i

#slices, similar to ruby ranges
x = "Chandan Jog"
print x[0]
print x[-3:len(x)]
splits = x.split(' ')
for i in splits:
    print i

x = True
print x
x = None #nulls, nils
print x

x = {'a': 'Hello', 'b' : 'dear'} #dictionary, hash, map
print x
print x['b']
for i in x:
    print i
for i in x.values():
    print i
print x.items()
for name, value in x.items():
    print name + " " + value

#unpacking
firstname, lastname = ['Chandan', 'Jog']
print firstname
print lastname

# list append
x = []
i = 1
while i <= 10:
    x.append(i)
    i=i+1
print x

# list extend
x.append(['a', 'b'])
print x
x.extend(['a', 'b'])
print x

print range(1,10)

def add_numbers(x, y):
    return x + y
print add_numbers(4, 10)
x = add_numbers
print type(add_numbers)
print type(x)


#exception handling, indentation matters
try:
    1/0
    # x = "hello" + 1
    # x = 1
except IOError:
    print 'IOError'
except ValueError:
    print 'Value error'
except:
    print 'Some error', sys.exc_info()
else:
    print 'always happens on success'
finally:
    print 'finally always happens, error or success'

#string formatting
x = "Fill {} in {}"
print x.format("me", "here")

#with as statment http://effbot.org/zone/python-with-statement.htm

#reading writing csv files

#date time lib

#classes, objects https://www.tutorialspoint.com/python/python_classes_objects.htm
class Person:
    department = "Mathematics" #class variable
    def __init__(self, name): # Not mandatory
        self.name = name
    def set_name(self, new_name):
        self.name = new_name
    def get_name(self): # self is necessary
        return self.name
    def set_department(self):
        Person.department = "FOOBAR"
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"
class Child(Person):
    def plays(self):
        print 'I am a child. I play!!'

p = Person("p") #instantiate
print p
print p.department
print p.set_name('Chandan')
print p.name
print p.get_name()
q = Person("q")
print Person.department
print p.department
print q.department
q.set_department
# q.set_department()
# Person.department = "HMM"
print p.department
print q.department
print Person.department
print "Person.__dict__:", Person.__dict__
c = Child('child')
c.plays()

# map function. Functional programming, chaining, immutable
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
def split_title_and_name(person):
    splits = person.split(" ")
    return splits[0] + splits[2]
print list(map(split_title_and_name, people))

store1 = [1.0, 5.0, 3.4]
store2 = [2.0, 6.0, 1.4]
cheapest = map(min, store1, store2)
cheapest #lazy evaluation
print list(cheapest)
