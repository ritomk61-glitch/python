import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [2000, 3000, 2500, 4000]
}

df = pd.DataFrame(data)

# Total sales
print("Total Sales:", df['Sales'].sum())

# Highest selling month
print(df[df['Sales'] == df['Sales'].max()])

# Pie chart
df.set_index('Month')['Sales'].plot(kind='pie')
plt.show()