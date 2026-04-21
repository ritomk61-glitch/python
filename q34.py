import pandas as pd
import matplotlib.pyplot as plt

# a
df = pd.read_csv("student.csv")

# b
print(df.shape)

# c
print(df.tail(5))

# d
print(df[df['Marks'] == df['Marks'].min()])

# e
print(df[df['Gender'] == 'F']['Marks'].sum())

# f
print(df[df['Gender'] == 'M']['Name'])

# g
print(df['Age'].mean())

# h
df['Marks'].plot(kind='line')
plt.show()

# i
print(df['Age'].idxmax())

# j
male_avg = df[df['Gender']=='M']['Marks'].mean()
female_avg = df[df['Gender']=='F']['Marks'].mean()

if male_avg > female_avg:
    print("Males are better")
else:
    print("Females are better")