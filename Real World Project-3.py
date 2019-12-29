passed = int(input("Enter the number of passed students:"))
failed = int(input("Enter the number of failed students:"))
total = passed + failed
print("The percentage of passed students :", format((passed/total)*100, ".2f"))
print("The percentage of failed students :", format((failed/total)*100, ".2f"))