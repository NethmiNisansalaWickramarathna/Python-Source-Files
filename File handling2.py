age = 12
name = "Nethu"
print(f"""
 👾👾Student marks report
      student name: {name}
      age : {age}
      💙💙💙💙💙
      marks  43
      total = 430
      average = 23.43
    """)


#Student Marks Report

name = input("Enter Your Name:")

subject1 = input("Enter Subject 1 name : ")
mark1 = int(input(f"Enter marks{subject1} :"))

subject2 = input("Enter Subject 2 name : ")
mark2 = int(input(f"Enter marks{subject2} :"))

subject3 = input("Enter Subject 3 name : ")
mark3 = int(input(f"Enter marks{subject3} :"))

total = mark1 + mark2 + mark3
average = total / 3

report =f"""
============================
👾👾Student marks report
============================
Student name : {name}

{subject1} : {mark1}
{subject2} : {mark2}
{subject3} : {mark3}
=============================
Total marks = {total}
average = {average:.2f}
"""
with open("report.txt","a",encoding="utf-8") as file:
   file.write(report)
print("Report is saved")   
print(report)



