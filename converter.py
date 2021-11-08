import pandas as pd

# reading csv file
readIT = pd.read_csv("E:/FYND/Final Project/Attendance Portal.csv")

# csv file to save as table in html file
readIT.to_html("view.html")

# assign it to a
# variable (string)
html_file = readIT.to_html()
