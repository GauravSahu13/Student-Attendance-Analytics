import pandas as pd
# from pandas_profiling import ProfileReport
#
# df = pd.read_csv('C:\\Users\\Gaurav\\Desktop\\FYND\\Final Project\\Final Project\\student.csv')
# print(df)
#
#
# profile = ProfileReport(df)
# profile.to_file(output_file = "attendance.html")


# to read csv file named "samplee"
a = pd.read_csv("E:/FYND/Final Project/Data Creation /it.csv")

# to save as html file
# named as "Table"
a.to_html("IT.html")

# assign it to a
# variable (string)
html_file = a.to_html()