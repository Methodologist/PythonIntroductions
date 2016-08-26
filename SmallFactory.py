BaseClass = type("BaseClass",(object,),{})

@classmethod
def Check1(self,myStr):
    return myStr == "ham"

@classmethod
def Check2(self,myStr):
    return myStr == "sandwhich"

C1 = type("C1",(BaseClass,),{"x":1, "Check":Check1})
C2 = type("C2",(BaseClass,),{"x":30, "Check":Check2})

def MyFactory(myStr):
    for cls in BaseClass.__subclasses__():
        if cls.Check(myStr):
            return cls()

m = MyFactory("ham")
v = MyFactory("sandwhich")
print(m.x,v.x)
