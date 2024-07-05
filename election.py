import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="besantmoviebooking_db"
)
mycursor = mydb.cursor()
def register_student(name, age, grade):
    sql="INSERT INTO students (name, age, grade) values (%s, %s, %s)"
    values=(name, age, grade)
    mycursor.execute(sql,values)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("Student registered successfully!")

def view_students():
    sql="SELECT * FROM students"
    mycursor.execute(sql)
    students = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return students

def search_student(name):
    sql="SELECT * FROM students WHERE name LIKE %s", (f"%{name}%",)
    mycursor.execute(sql)
    students = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return students

def main():
    while True:
        print("\n--- Student Registration System ---")
        print("1. Register a new student")
        print("2. View all students")
        print("3. Search for a student by name")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            register_student(name, age, grade)
        elif choice == '2':
            students = view_students()
            print("\nRegistered Students:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        elif choice == '3':
            name = input("Enter student name to search: ")
            students = search_student(name)
            print("\nSearch Results:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
