import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = "NanumGothic"
mpl.rcParams['font.size'] = 10

# Read in the data from a CSV file
df = pd.read_csv('dt.csv', encoding='cp949')

# Categorize the brand column
df['categorized_brand'] = df['brand'].apply(lambda x: 'CGV' if 'CGV' in x else ('메가박스' if '메가박스' in x else ('롯데시네마' if '롯데시네마' in x else '기타')))

# Count the number of occurrences of each categorized brand
brand_counts = df['categorized_brand'].value_counts()

# Plot the pie chart
fig, ax = plt.subplots(figsize=(8, 6))
brand_counts.plot(kind='pie', autopct='%1.1f%%', startangle=0, labels=None, ax=ax)
plt.ylabel('')
plt.legend(labels=brand_counts.index, loc='upper right')
plt.axis('equal')
plt.title('상영관 비율', loc='left', fontsize=20, fontweight='bold')
plt.show()