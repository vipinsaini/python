
employee_file = open("employees.txt", "a")
employee_file.write("\nVipin Saini - CFO")
employee_file.close()

employee_file1 = open("employees1.txt", "w")
employee_file1.write("\nVipin Saini - CFO")
employee_file1.close()

html_file = open("index.html", "w")
html_file.write("<p>This is index html page</p>")
html_file.close()