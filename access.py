# public

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
# s=student("john",20)
# s.display()


# protect

# class person:
    # def __init__(self,name,age):
        # self._name=name
        # self._age=age
    # def _display(self):
        # print("name",self._name)
        # print("age",self._age)
# class student(person):
    # def __init__(self,name,age,roll_no):
        # super().__init__(name,age)
        # self._roll_no=roll_no
    # def display(self):
        # self._display()
        # print("roll",self._roll_no)
# s=student("vaisakh",24,3)
# s.display()


# private

# class bank_account:
    # def __init__(self,account_no,balance):
        #   self.__account_no=account_no
        #   self.__balance=balance
        #   def display(self):
            # print("account_no",self.__account_no)
            # print("balance",self.__balance)
# b=bank_account(12345678,5000)
# b.display()


# class hr:
    # def __init__(self,name,salary):
        # self._name=name
        # self._salary=salary
    # def _display(self):
        # print("name",self._name)
        # print("salary",self._salary)
# class account(hr):
        # def __init__ (self,name,salary,account_no):
            # super(). __init__(name,salary)
            # self._account_no=account_no
        # def display(self):
            #  self._display()
            #  print("account_no",self._account_no)
# 
# a=account("vaisakh",25000,1234566)
# a.display()

# class mynumbers:
    # def __iter__(self):
        # self.a=1
        # return self
    # def __next__ (self):
        # x=self.a
        # self.a+=1
        # return x
# myclass=mynumbers()
# myit=iter(myclass)
# print(next(myit))
# print(next(myit))

# class mynumbers:
    # def __iter__(self):
        # self.a=1
        # return self
    # def __next__(self):
        # if self.a<=20:
            # x=self.a
            # self.a+=1
            # return x
        # else:
            # raise StopIteration
# myclass=mynumbers()
# 
# myiter=iter(myclass)

# for x in myclass:
    # print(x)

