def myfunc():
    print("Yasss")
    return 1

print(myfunc())

#===================================

def myrange():
    yield "wow"
    yield "is"
    yield "great"

for wowowowo in myrange():
    print(wowowowo)

#===================================

def squaredrange(sqr):
    for i in range(sqr):
        yield i * i
        
for i in squaredrange(500):
    print(i)
    
#===================================

#===================================