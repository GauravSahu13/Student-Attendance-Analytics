# -*- coding: utf-8 -*-
"""IT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JxNwWH_18qnbYgsw8Lv5jy007AQeA3lQ
"""

from google.colab import drive
drive.mount('/content/gdrive')

import os
os.listdir('/content')

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

''' Reading CSV file'''
student_df = pd.read_csv('/content/gdrive/MyDrive/Student Attendance System/student.csv')
# print(student_df.head())

student_df = student_df.fillna(0)
# print(student_df)

student_df['Month'] = pd.DatetimeIndex(student_df['Date']).month
# print(student_df)





''' Filtering Data'''

# selecting rows based on condition
secondMonth = student_df.loc[(student_df['Month'] == 2) &
			student_df['Branch']]
# print(secondMonth)

secondMonth = secondMonth.loc[:, (secondMonth != 0).any(axis=0)]
secondMonth = secondMonth.loc[(secondMonth['Branch'] == 'IT')]
# print(secondMonth)

''' Grouping data on basis of Name ,Month'''

finalsecondMonth = secondMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),M3= ('M3','sum'),Logic_Design= ('Logic_Design','sum'),DMS= ('DMS','sum'),
                                                           DS= ('DS','sum'),DBA= ('DBA','sum'),OS= ('OS','sum'),OOPs= ('OOPs','sum'),
                                                           M4= ('M4','sum'),LMS= ('LMS','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].reset_index()
# finalsecondMonth = secondMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].nsmallest(20)
print(finalsecondMonth)

temp_df = finalsecondMonth[finalsecondMonth['Lec_Attended_Percentage'] < 40] 

temp_df.plot(x='Name', y=['Lec_Attended_Percentage'], kind='bar',figsize=(15,10),width =0.25) 

plt.yticks(np.arange(0, 100, 5))


plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

plt.title("Monthly Defaulter of IT ",fontdict = {'family':'serif','color':'blue','size':20})
plt.xlabel("Student Name", fontdict = {'family':'serif','color':'darkred','size':15})
plt.ylabel("Attendance(%)", fontdict = {'family':'serif','color':'darkred','size':15})
plt.legend(loc ="upper left")
plt.show()







''' Filtering Data'''

# selecting rows based on condition
thirdMonth = student_df.loc[(student_df['Month'] == 3) &
			student_df['Branch']]
# print(thirdMonth)

thirdMonth = thirdMonth.loc[:, (thirdMonth != 0).any(axis=0)]
thirdMonth = thirdMonth.loc[(thirdMonth['Branch'] == 'IT')]
# print(thirdMonth)

''' Grouping data on basis of Name ,Month'''

# finalthirdMonth = thirdMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),M3= ('M3','sum'),Logic_Design= ('Logic_Design','sum'),DMS= ('DMS','sum'),
#                                                            DS= ('DS','sum'),DBA= ('DBA','sum'),OS= ('OS','sum'),OOPs= ('OOPs','sum'),
#                                                            M4= ('M4','sum'),LMS= ('LMS','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].nsmallest(16)
finalthirdMonth = thirdMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),M3= ('M3','sum'),Logic_Design= ('Logic_Design','sum'),DMS= ('DMS','sum'),
                                                           DS= ('DS','sum'),DBA= ('DBA','sum'),OS= ('OS','sum'),OOPs= ('OOPs','sum'),
                                                           M4= ('M4','sum'),LMS= ('LMS','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].reset_index()
print(finalthirdMonth)

temp_df = finalthirdMonth[finalthirdMonth['Lec_Attended_Percentage'] < 40] 

temp_df.plot(x='Name', y=['Lec_Attended_Percentage'], kind='bar',figsize=(15,10),width =0.25) 

plt.yticks(np.arange(0, 100, 5))


plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

plt.title("Monthly Defaulter of IT ",fontdict = {'family':'serif','color':'blue','size':20})
plt.xlabel("Student Name", fontdict = {'family':'serif','color':'darkred','size':15})
plt.ylabel("Attendance(%)", fontdict = {'family':'serif','color':'darkred','size':15})
plt.legend(loc ="upper left")
plt.show()





''' Filtering Data'''

# selecting rows based on condition
fourthMonth = student_df.loc[(student_df['Month'] == 4) &
			student_df['Branch']]
# print(fourthMonth)

fourthMonth = fourthMonth.loc[:, (fourthMonth != 0).any(axis=0)]
fourthMonth = fourthMonth.loc[(fourthMonth['Branch'] == 'IT')]
# print(fourthMonth)

''' Grouping data on basis of Name ,Month'''
# finalfourthMonth = fourthMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),M3= ('M3','sum'),Logic_Design= ('Logic_Design','sum'),DMS= ('DMS','sum'),
#                                                            DS= ('DS','sum'),DBA= ('DBA','sum'),OS= ('OS','sum'),OOPs= ('OOPs','sum'),
#                                                            M4= ('M4','sum'),LMS= ('LMS','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].nsmallest(11)
finalfourthMonth = fourthMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),M3= ('M3','sum'),Logic_Design= ('Logic_Design','sum'),DMS= ('DMS','sum'),
                                                           DS= ('DS','sum'),DBA= ('DBA','sum'),OS= ('OS','sum'),OOPs= ('OOPs','sum'),
                                                           M4= ('M4','sum'),LMS= ('LMS','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].reset_index()

print(finalfourthMonth)

temp_df = finalfourthMonth[finalfourthMonth['Lec_Attended_Percentage'] < 40] 

temp_df.plot(x='Name', y=['Lec_Attended_Percentage'], kind='bar',figsize=(15,10),width =0.25) 

plt.yticks(np.arange(0, 100, 5))


plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

plt.title("Monthly Defaulter of IT ",fontdict = {'family':'serif','color':'blue','size':20})
plt.xlabel("Student Name", fontdict = {'family':'serif','color':'darkred','size':15})
plt.ylabel("Attendance(%)", fontdict = {'family':'serif','color':'darkred','size':15})
plt.legend(loc ="upper left")
plt.show()







''' Filtering Data'''

# selecting rows based on condition
fifthMonth = student_df.loc[(student_df['Month'] == 5) &
			student_df['Branch']]
# print(fifthMonth)

fifthMonth = fifthMonth.loc[:, (fifthMonth != 0).any(axis=0)]
fifthMonth = fifthMonth.loc[(fifthMonth['Branch'] == 'IT')]
# print(fifthMonth)

''' Grouping data on basis of Name ,Month'''

# finalfifthMonth = fifthMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),M3= ('M3','sum'),Logic_Design= ('Logic_Design','sum'),DMS= ('DMS','sum'),
#                                                            DS= ('DS','sum'),DBA= ('DBA','sum'),OS= ('OS','sum'),OOPs= ('OOPs','sum'),
#                                                            M4= ('M4','sum'),LMS= ('LMS','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].nsmallest(16)

finalfifthMonth = fifthMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),M3= ('M3','sum'),Logic_Design= ('Logic_Design','sum'),DMS= ('DMS','sum'),
                                                           DS= ('DS','sum'),DBA= ('DBA','sum'),OS= ('OS','sum'),OOPs= ('OOPs','sum'),
                                                           M4= ('M4','sum'),LMS= ('LMS','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].reset_index()
print(finalfifthMonth)

temp_df = finalfifthMonth[finalfifthMonth['Lec_Attended_Percentage'] < 40] 

temp_df.plot(x='Name', y=['Lec_Attended_Percentage'], kind='bar',figsize=(15,10),width =0.25) 

plt.yticks(np.arange(0, 100, 5))


plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

plt.title("Monthly Defaulter of IT ",fontdict = {'family':'serif','color':'blue','size':20})
plt.xlabel("Student Name", fontdict = {'family':'serif','color':'darkred','size':15})
plt.ylabel("Attendance(%)", fontdict = {'family':'serif','color':'darkred','size':15})
plt.legend(loc ="upper left")
plt.show()







'''Filtering Data'''

# selecting rows based on condition
sixthMonth = student_df.loc[(student_df['Month'] == 6) &
			student_df['Branch']]
# print(sixthMonth)

sixthMonth = sixthMonth.loc[:, (sixthMonth != 0).any(axis=0)]
sixthMonth = sixthMonth.loc[(sixthMonth['Branch'] == 'IT')]
# print(sixthMonth)

''' Grouping data on basis of Name ,Month'''

# finalsixthMonth = sixthMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),M3= ('M3','sum'),Logic_Design= ('Logic_Design','sum'),DMS= ('DMS','sum'),
                                                          #  DS= ('DS','sum'),DBA= ('DBA','sum'),OS= ('OS','sum'),OOPs= ('OOPs','sum'),
                                                          #  M4= ('M4','sum'),LMS= ('LMS','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].nsmallest(30)
finalsixthMonth = sixthMonth.groupby(['Name','Enrolled_ID']).agg(M1= ('M1','sum'),CP= ('CP','sum'),BEE= ('BEE','sum'),M3= ('M3','sum'),Logic_Design= ('Logic_Design','sum'),DMS= ('DMS','sum'),
                                                           DS= ('DS','sum'),DBA= ('DBA','sum'),OS= ('OS','sum'),OOPs= ('OOPs','sum'),
                                                           M4= ('M4','sum'),LMS= ('LMS','sum'),Lec_Attended_Percentage= ('Lec_Attended(%)','mean'))["Lec_Attended_Percentage"].reset_index()
print(finalsixthMonth)

temp_df = finalsixthMonth[finalsixthMonth['Lec_Attended_Percentage'] < 30] 

temp_df.plot(x='Name', y=['Lec_Attended_Percentage'], kind='bar',figsize=(15,10),width =0.25) 

plt.yticks(np.arange(0, 100, 5))


plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

plt.title("Monthly Defaulter of IT ",fontdict = {'family':'serif','color':'blue','size':20})
plt.xlabel("Student Name", fontdict = {'family':'serif','color':'darkred','size':15})
plt.ylabel("Attendance(%)", fontdict = {'family':'serif','color':'darkred','size':15})
plt.legend(loc ="upper left")
plt.show()





