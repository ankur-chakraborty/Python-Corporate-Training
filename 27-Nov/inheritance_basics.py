class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d= Dog()
d.speak()  #inherited
d.bark()   #child's own method

#Inheritance is the expanding on parent's methods into a new own class

