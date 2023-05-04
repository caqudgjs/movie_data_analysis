import pandas as pd

# Read in the data from a CSV file
df = pd.read_csv('dt.csv', encoding='cp949')

# Extract the province and brand columns
province_brand = df[['province', 'brand']]

# Filter the brand column to only include rows containing "롯데시네마"
lotte_cinema_brands = province_brand[province_brand['brand'].str.contains('롯데시네마')].copy()

# Create a new column for the categorized brand
lotte_cinema_brands['categorized_brand'] = '롯데시네마'

# Group by province and categorized brand, then count the number of occurrences
brand_counts = lotte_cinema_brands.groupby(['province', 'categorized_brand']).size().reset_index(name='counts')

# Filter out the '기타' category
brand_counts = brand_counts[brand_counts['categorized_brand'] != '기타']

# Print the resulting dataframe
print(brand_counts)

# Read in the data from a CSV file
df = pd.read_csv('dt.csv', encoding='cp949')

# Extract the province and brand columns
province_brand = df[['province', 'brand']]

# Filter the brand column to only include rows containing "CGV"
cgv_brands = province_brand[province_brand['brand'].str.contains('CGV')]

# Create a new column for the categorized brand
cgv_brands['categorized_brand'] = 'CGV'

# Group by province and categorized brand, then count the number of occurrences
brand_counts = cgv_brands.groupby(['province', 'categorized_brand']).size().reset_index(name='counts')

# Filter out the '기타' category
brand_counts = brand_counts[brand_counts['categorized_brand'] != '기타']

# Print the resulting dataframe
print(brand_counts)


# Read in the data from a CSV file
df = pd.read_csv('dt.csv', encoding='cp949')

# Extract the province and brand columns
province_brand = df[['province', 'brand']]

# Filter the brand column to only include rows containing "메가박스"
megabox_brands = province_brand[province_brand['brand'].str.contains('메가박스')]

# Create a new column for the categorized brand
megabox_brands['categorized_brand'] = '메가박스'

# Group by province and categorized brand, then count the number of occurrences
brand_counts = megabox_brands.groupby(['province', 'categorized_brand']).size().reset_index(name='counts')

# Filter out the '기타' category
brand_counts = brand_counts[brand_counts['categorized_brand'] != '기타']

# Print the resulting dataframe
print(brand_counts)
