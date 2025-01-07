#day3
a=int(input("Enter the first subject Marks: "))
b=int(input("Enter the second subject Marks: "))
c=int(input("Enter the third subject Marks: "))
d=(a+b+c)/3
if d>=90:
  print("Grade: A")
elif 80<=d<90:
  print("Grade: B")
elif 70<=d<80:
  print("Grade: C")
else:
  print("Grade: Fail")
