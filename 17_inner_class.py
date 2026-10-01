# Python program to demonstrate inner class

class Outer:

    def display_outer(self):
        print("This is the Outer class.")

    class Inner:

        def display_inner(self):
            print("This is the Inner class.")


outer = Outer()
outer.display_outer()

inner = Outer.Inner()
inner.display_inner()
