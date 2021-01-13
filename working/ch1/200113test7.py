class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕!" + to_name +" 나는" + self.name)


    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")

class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다." + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음에 뭘 만들지? 아 이걸만들어야겠다 : " + to_program)




wonie = Person("워니", 21)
jenny = Police("제니", 25)
michale = Programmer("마이클", 33)


wonie.introduce()
jenny.introduce()
michale.introduce()

michale.arrest("워니")
michale.program("이메일 클라이언트를 만들어야겠다")

