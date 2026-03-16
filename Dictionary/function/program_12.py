# How to use zip() function
days=['sunday','monday','tuesday','Wednesday','Thursday','Friday','Saturday']
temp=[30.5,30,29.5,32.5,31,28.5,30]
a={i:j for (i,j) in zip (days,temp)}
print(a)