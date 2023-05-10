import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = "NanumGothic"
mpl.rcParams['font.size'] = 10

# Read in the data from a CSV file
df = pd.read_csv('dt2.csv', encoding='cp949')

# Categorize the brand column
df['categorized_brand'] = df['brand'].apply(lambda x: 'CGV' if 'CGV' in x else ('메가박스' if '메가박스' in x else ('롯데시네마' if '롯데시네마' in x else '기타')))

# Group the dataframe by the categorized brand and sum the number of seats and screens separately
screens_df = df.groupby('categorized_brand', sort=False).agg({'screens': 'sum'}).sort_values(by='screens')
seats_df = df.groupby('categorized_brand', sort=False).agg({'seats': 'sum'}).sort_values(by='seats')

# Plot the bar chart for screens and seats
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
ax[0].bar(screens_df.index, screens_df['screens'])
ax[0].set_title('스크린수')
ax[0].set_ylabel('개')

ax[1].bar(seats_df.index, seats_df['seats'])
ax[1].set_title('좌석수')
ax[1].set_ylabel('개')

plt.tight_layout()
plt.show()
