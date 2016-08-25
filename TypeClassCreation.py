class MyClass(object):
    def __init__(self):
        self.x = 5

def printHam(self):
        print("ham")

TypeClass = type("TypeClass",(object,),{"x":5,
                                        "pH":printHam})

m = MyClass()
t = TypeClass()

t.pH()
