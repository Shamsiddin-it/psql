from connection import conn

cur = conn.cursor()

cur.execute("""create table if not exists students(
            id serial primary key,
            name varchar(100) not null,
            surname varchar(100) not null,
            addres varchar(255),
            phone varchar(13),
            email varchar(255));
            """)

conn.commit()




class Student:
    def __init__(self,name,surname,addres,phone,email):
        self.name=name
        self.surname = surname
        self.addres = addres
        self.phone = phone
        self.email = email
    
class StudentManager:
    def create():
        student = Student(input("name: "),input("surname: "),input("addres: "),input("phone: "),input("eamil: "))
        cur.execute(f"""insert into students(name,surname,addres,phone,email) values
                    ('{student.name}','{student.surname}','{student.addres}','{student.phone}','{student.email}');
                    """)
        conn.commit()
    def show():
        cur.execute("select * from students")
        rows = cur.fetchall()
        for i in rows:
            print(i)

    def update():
        id = int(input("Enter id to update: "))
        cur.execute(f"""update students
                    set addres = '{input("Enter new addres: ")}' where id = {id}""")
        conn.commit()
        
    def dele():
        id=int(input("Enter id to del: "))
        cur.execute(f"""delete from students where id = {id}""")
        conn.commit()
        
student = StudentManager
while True:
    a=int(input("-> "))
    if a==1:
        student.create()
    elif a==2:
        student.show()
    elif a==3:
        student.update()
    elif a==4:
        student.dele()
    else:
        break


cur.close()
conn.close()