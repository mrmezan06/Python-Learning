passed = int(input("Enter the number of passed students:"))
failed = int(input("Enter the number of failed students:"))
total = passed + failed
print("The percentage of passed students :", format((passed/total)*100, ".3f"), "%")
print("The percentage of failed students :", format((failed/total)*100, ".3f"), "%")

# Auto percentage formatting
print(format((passed/total), "%"), " of passed students.")
print(format((failed/total), "%"), " of failed students.")