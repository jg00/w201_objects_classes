# 1 Basics
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

        self.friends = []

        self.greeting_count = 0

        # self.num_unique_people_greeted = 0
        self.unique_people_greeted_count = 0

        self.maintain_unique_list_of_people_greeted = []
    
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

        # Maintain list of unique people a person has greeted
        if (other_person not in self.maintain_unique_list_of_people_greeted):
            self.maintain_unique_list_of_people_greeted.append(other_person)
            self.unique_people_greeted_count += 1

    def num_unique_people_greeted(self):
        print("Number of unique peope greeted: " + str(self.unique_people_greeted_count))

    def print_contact_info(self):
        print('{0}\'s email: {1}, {0}\'s phone number: {2}'.format(self.name, self.email, self.phone))

    def add_friend(self, person):
        self.friends.append(person)

    def num_friends(self):
        print(len(self.friends))

    def __repr__(self):
        return "{} {} {}".format(self.name, self.email, self.phone)
    
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
dee_ann = Person('Dee_Ann', 'dee@gmail.com', '476-276-0987')


sonny.greet(jordan)
jordan.greet(sonny)

print("{} - email: {}, phone: {}".format(sonny.name, sonny.email, sonny.phone))
print("{} - email: {}, phone: {}".format(jordan.name, jordan.email, jordan.phone))


print()
# 2 Make your own class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(self.year, self.make, self.model)
    

car = Vehicle('Nissan', 'Leaf', 2015)


print()
# 3 Add a method
car.print_info()


print()
# 4 Add a method 2
sonny.print_contact_info()
jordan.print_contact_info()


print()
# 5 Add an instance variable (attribute)
jordan.friends.append(sonny)
sonny.friends.append(jordan)

print(len(jordan.friends))


print()
# 6 Add a add_friend method
jordan.add_friend(sonny)
# print(len(jordan.friends))


print()
# 7 Add a num_friends method
jordan.num_friends()


print()
# 8 Count number of greetings
print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)


print()
# 9 __repr__
print(jordan)   # Without __repr__ <__main__.Person object at 0x10f615358>


print()
# 10 Bonus Challenge

sonny.num_unique_people_greeted()

sonny.greet(jordan)
sonny.num_unique_people_greeted()

sonny.greet(jordan)
sonny.num_unique_people_greeted()

sonny.greet(dee_ann)
sonny.num_unique_people_greeted()

print()