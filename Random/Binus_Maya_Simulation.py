'''
class BinusMaya:
    def __init__(self, student, major, batch, gpa):
        self.student = student
        self.major = major
        self.batch = batch
        self.gpa = gpa
    def Add_student(self, name, major, batch, gpa):
        self.student += name
        self.major += major
        self.batch += batch
        self.gpa += gpa
    def DO_student(self, do):
        self.student -= do
    def Updatestudent(self, update_name, update_major, update_batch, update_gpa):
        self.student = update_name
        self.major = update_major
        self.batch = update_batch
        self.gpa = update_gpa
    def Search(self, search, question):
        if search == self.student:
            print(search,"is registered as our Student!")
            if question == "yes":
                print("Name: %s" %self.student)
                print("Major: %s" %self.major)
                print("Batch: %s" %self.batch)
                print("GPA: %s" %self.gpa)
        else:
            print("There is no student that goes by the name of",search)

a1 = BinusMaya("Excelino Noveda Alfa Fernando","Computer Science","2021","11/10")
a1.Search("Excelino Noveda Alfa Fernando","yes")
#a1.DO_student("Excelino Noveda Alfa Fernando")
#a1.Search("Excelino Noveda Alfa Fernando","no")
'''
class BinusMaya:
    def __init__(self):
        self.datas = {"ids":"","students":"","majors":"","batches":"","gpas":""}
    def Add_student(self, id, student, major, batch, gpa):
        self.datas["ids"].__add__(id)
        self.datas["students"].__add__(student)
        self.datas["majors"].__add__(major)
        self.datas["batches"].__add__(batch)
        self.datas["gpas"].__add__(gpa)
    def DO_student(self, do): #[do] = Drop_Out, input student_id or student_name to [do]
        if do in self.datas["ids"]:
            self.datas["ids"].__delattr__(do)
            self.datas["students"].__delattr__(do)
            self.datas["majors"].__delattr__(do)
            self.datas["batches"].__delattr__(do)
            self.datas["gpas"].__delattr__(do)
        elif do in self.datas["students"]:
            self.datas["ids"].__delattr__(do)
            self.datas["students"].__delattr__(do)
            self.datas["majors"].__delattr__(do)
            self.datas["batches"].__delattr__(do)
            self.datas["gpas"].__delattr__(do)
        else:
            False
    def Updatestudent(self, updating):
        if updating in self.datas["ids"]:
    def Search(self, search, question):
         for i in range (len(self.students)):
            if search == self.students:
            print(search,"is registered as our Student!")
            if question == "yes":
                print("Name: %s" %self.student)
                print("Major: %s" %self.major)
                print("Batch: %s" %self.batch)
                print("GPA: %s" %self.gpa)
        else:
            print("There is no student that goes by the name of",search)

a1 = BinusMaya("Excelino Noveda Alfa Fernando","Computer Science","2021","11/10")
a1.Search("Excelino Noveda Alfa Fernando","yes")
#a1.DO_student("Excelino Noveda Alfa Fernando")
#a1.Search("Excelino Noveda Alfa Fernando","no")
