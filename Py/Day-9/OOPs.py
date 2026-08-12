'''OOPs'''
#Classes and Objects
class Myclass:
    x = 5
    y = 10
    z = 15
p1 = Myclass()
print(p1.x)
print(p1.y)
print(p1.z)
 
#Small Code (__init__ used)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello my name is", self.name, "and I am", self.age, "years old")

p1 = Person("Harry", 22)
p1.greet()


'''Create a class Student with an __init__ that takes name and grade, and stores them as properties
Create an object s1 with name "Anna" and grade "A"
Print the grade of s1
Change the grade of s1 to "B"
Print the updated grade'''

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Anna", "A")
print(s1.grade)

s1.grade = "B"
print(s1.grade)

'''Creating a Playlist'''

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print("Added:", song)

    def del_song(self, song):
        self.songs.remove(song)
        print("Removed:", song)

    def show_song(self):
        print("Playlist", self.name)
        for song in self.songs:
            print("-", song)

my_playlist = Playlist("Favs: ")
my_playlist.add_song("Harleys in Hawaii")
my_playlist.add_song("Strangers")
my_playlist.show_song()    

'''Calling a function'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r1 = Rectangle(3,5)
print(r1.area())