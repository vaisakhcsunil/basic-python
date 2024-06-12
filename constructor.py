# class Employee:
#     def __init__(self):
#         self.name="BHAVANA"
#         self.age=24
# el=Employee()
# print("NAME:{}",format(el.name))
# print("AGE:{}".format(el.age))


# class student:
    # def __init__(self):
        # self.name="VAISAKH"
        # self.mark=100
# el=student()
# print("NAME:{}".format(el.name))
# print("MARK:{}".format(el.mark))

class triangle:
    base=0
    height=0
    area=0
    def __init__(self,b,h):
        self.base=b
        self.height=h
    def areaoftriangle(self):
        self.area=self.base*self.height*0.5
        print("area of triangle:"+str(self.area))
obj=triangle(5,14)
obj.areaoftriangle()
    