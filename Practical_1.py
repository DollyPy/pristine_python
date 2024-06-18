#Employee payroll
from faker import Faker
import random
Name = []
Staff_ID = []
Salary = []
Employee_Level = []
gender = []
print("Name", "Staff_ID", "Sal", "Level", "gender")
fake = Faker()
for i in range(10):
    gender.append(random.choice(["Male", "Female"]))
    if gender[i] == "Male":
        Name.append(fake.name_male())
    else:
        Name.append(fake.name_female())

    Staff_ID.append(random.randint(1, 500))
    gender.append(random.choice(["Male", "Female"]))
    Salary.append(random.randint(5000, 35000))

    if (Salary[i] > 10000) and (Salary[i] < 20000):
        Employee_Level.append("A1")
    else:
        Employee_Level.append("Nil")

    if ((Salary[i] > 7500) and (Salary[i] < 30000)) and (gender[i] == "Female"):
        Employee_Level[i] = ("A5-F")

    print(Name[i], Staff_ID[i], Salary[i], Employee_Level[i], gender[i], sep=" | ")
