import matplotlib.pyplot as plt

#BASIC PLOT (by default:line)
days=[1,2,3,4,5]
temp=[30,45,49,25.6,69]
plt.plot(days,temp)
plt.show()

#SAME AS ABOVE
days=[1,2,3,4,5]
temp=[30,45,49,25.6,69]
plt.plot(days,temp)
plt.title("TEMP OVER 5 DAYS")
plt.xlabel("DAYS")
plt.ylabel("TEMP in CELCIUS")
plt.show()

#BAR GRAPH/PLOT
stu=["A","B","C","D","D"]
marks=[10,30,80,100,45]
plt.bar(stu,marks)
plt.title("MARKS OF DIFF STUDENTS")
plt.xlabel("STUDENTS NAMES")
plt.ylabel("MARKS")
plt.show()

#SCATTER GRAPH/PLOT
hrs=[1,2,3,4,5,6,7,8,9,10]
marks=[10,2,30,45,63,45,75,78,99,100]
plt.scatter(hrs,marks)
plt.title("STUDY HRS VS MARKS")
plt.xlabel("STUDY HRS")
plt.ylabel("MARKS")
plt.show()

#PIE CHART
act=["Study","Game","Code","Sleep","Doomscrolling"]
hrs=[5,4,7,3,12]
plt.pie(hrs,labels=act)
plt.title("HRS SPEND PER ACTIVITY")
plt.show()

#HISTOGRAM
marks=[10,99,30,78,78,60,45,63,45,75,78,99,100]
plt.hist(marks)
plt.title("DISTRIBUTION OF STU MARKS")
plt.ylabel("FREQUENCY")
plt.xlabel("MARKS")
plt.show()

