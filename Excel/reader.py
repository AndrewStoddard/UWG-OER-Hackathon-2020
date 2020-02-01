import pandas as pd

excel_file = (r"C:\Users\csuser\Desktop\UWGcoursematerial.xlsx")
entries = pd.read_excel(excel_file)

subject = entries[['Subject']]

course = entries[['Course']]

isbn = entries[['ISBN']]

author = entries[['Author']]

title = entries[['Title']]

edition = entries[['Ed.']]

year = entries[['Year']]


print(subject)

print(course)

print(isbn)

print(author)

print(title)

print(edition)

print(year)
