
class A(object):

	def __init__(self, name):
		self.name = name
	def f(self):
		print("public")
	def __g(self):
		print("private")
	def iden(self):
		print("class by self:", id(self.__g))

	def iden2(cls):
		print("class by cls :", id(cls.__g))

a = A("a")
a.f()
a._A__g()
print("object : ", id(a._A__g))
print("class  : ", id(A._A__g))
print()
A.iden(a)
A.iden2(A)
# print(A.__mro__)
# print(dir(A))
# print(dir(a))
# print(A.__dict__)


# A.__dict__["f"].__get__(a, A)()
# print(A.__dict__["f"](a))