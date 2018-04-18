import random
import sys
import os

# Objects and Classes

'''

    Objects allow a programmer to model real world stuff from everyday life. Real
world objects have attributes: color, height, weight, sound, and more. Real world
objects have abilities like walk, talk, eat, and more. Objects are a way to
copy real world objects into a computer setting using classes.

    Classes are blueprints for creating an object

'''

class Animal:
    # None is NULL
    # __ denotes a private variable inside of python
    # if we want to change the values, we will have to use
    # a function defined within the class Animal, and to get
    # those values we will need to define that function within
    # our Animal class as well
    __name = None
    __height = 0
    __weight = 0
    __sound = 0


    '''
    Constructors are called to create or initialize an object
        inside the constructor you initialize the values for
        each object from the parameters being passed in
    '''
    def __init__(self, n, h, w, s):
        self.__name = n
        self.__height = h
        self.__weight = w
        self.__sound = s

    # self means it can refer to itself
    # self is like using this
    # the follow eight functions are just getters/setters
    # set self->name = n
    def set_name(self, n):
        self.__name = n

    def set_height(self, h):
        self.__height = h

    def set_weight(self, w):
        self.__weight = w

    def set_sound(self, s):
        self.__sound = s


    # the follow just returns the name, height, etc you request
    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_sound(self):
        return self.__sound


    # used to show polymorphism closer
    def get_type(self):
        print("Superclass : Animal")


    # create a to_string function to print out our information
    def to_string(self):
        return "{} is {} inches tall and {} lbs, whom also likes to {} all day.".format(self.__name,
                                                                                self.__height,
                                                                                self.__weight,
                                                                                self.__sound)


# Lets create three animals

cat = Animal("PurrPurr", 13, 10, "meow meow")

dog = Animal("Marlow", 15, 8, "bark bark")

bird = Animal("Pooper", 6, 0.5, "chirp chirp")

print(cat.to_string())

print(dog.to_string())

print(bird.to_string())

'''
Let us show some inheritance, we will create another class
called Dog that will inherit from the super class Animal
'''

# passing in Animal to Dog ensures that all of the variables and functions of Animal
# will be shared with Dog
class Dog(Animal):
    __owner = None

    # We need to overwrite the constructor
    def __init__(self, n, h, w, s, o):
        self.__owner = o
        self.__animal_type = None
        #to make Animal handle the other 4 parameters
        super(Dog, self).__init__(n, h, w, s)


    # we need to get/set the owner
    def set_owner(self, o):
        self.__owner = o

    def get_owner(self):
        return self.__owner

    # we will use this to show polymorphism
    def get_type(self):
        print("Subclass : Dog")

    # We need to override the to_string function to add the changes
    def to_string(self):
        return "{} owns {}, who is {} inches tall and {} lbs, and also likes to {} all day.".format(self.__owner,
                                                                                                        self.get_name(),
                                                                                                        self.get_height(),
                                                                                                        self.get_weight(),
                                                                                                        self.get_sound(),)

    # Overloading
    # the ability to perform different tasks based on the attributes that
    # are sent as parameters

    # this function defines how many times our Animal will make a sound
    # (self, variable=None) means that they can pass in None
    def multipl_sounds(self, how_many_sounds=None):
        if how_many_sounds is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many_sounds)


buster = Dog("Buster", 48, 75, "Ruff Ruff", "James")

print(buster.to_string())
