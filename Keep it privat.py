#Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.


class myclass:
    __privatvar= 25
    def __privMeth(self):
        print("This is Jaddua and his teacher in a private universe")
    def hello(self):
        print("the private variable is ", myclass.__privatvar)
object=myclass()
object.hello()
object.__privMeth