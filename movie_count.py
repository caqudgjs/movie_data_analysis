import pandas as pd

# CSV 파일에서 데이터를 읽어옵니다.
df = pd.read_csv('dt.csv', encoding='cp949')

# 'province'와 'brand' 열을 추출합니다.
province_brand = df[['province', 'brand']]

# 'brand' 열에서 "롯데시네마"를 포함하는 행만 필터링합니다.
lotte_cinema_brands = province_brand[province_brand['brand'].str.contains(
    '롯데시네마')].copy()

# 'categorized_brand'라는 새로운 열을 생성하고, "롯데시네마"로 값을 할당합니다.
lotte_cinema_brands['categorized_brand'] = '롯데시네마'

# 'province'와 'categorized_brand'로 그룹화한 후, 각 그룹별로 개수를 계산합니다.
brand_counts = lotte_cinema_brands.groupby(
    ['province', 'categorized_brand']).size().reset_index(name='counts')

# 'categorized_brand'가 '기타'인 행을 필터링합니다.
brand_counts = brand_counts[brand_counts['categorized_brand'] != '기타']

# 결과 DataFrame을 출력합니다.
print(brand_counts)


# CSV 파일에서 데이터를 읽어옵니다.
df = pd.read_csv('dt.csv', encoding='cp949')

# 'province'와 'brand' 열을 추출합니다.
province_brand = df[['province', 'brand']]

# 'brand' 열에서 "CGV"를 포함하는 행만 필터링합니다.
cgv_brands = province_brand[province_brand['brand'].str.contains('CGV')]

# 'categorized_brand'라는 새로운 열을 생성하고, "CGV"로 값을 할당합니다.
cgv_brands['categorized_brand'] = 'CGV'

# 'province'와 'categorized_brand'로 그룹화한 후, 각 그룹별로 개수를 계산합니다.
brand_counts = cgv_brands.groupby(
    ['province', 'categorized_brand']).size().reset_index(name='counts')

# 'categorized_brand'가 '기타'인 행을 필터링합니다.
brand_counts = brand_counts[brand_counts['categorized_brand'] != '기타']

# 결과 DataFrame을 출력합니다.
print(brand_counts)


# CSV 파일에서 데이터를 읽어옵니다.
df = pd.read_csv('dt.csv', encoding='cp949')

# 'province'와 'brand' 열을 추출합니다.
province_brand = df[['province', 'brand']]

# 'brand' 열에서 "메가박스"를 포함하는 행만 필터링합니다.
megabox_brands = province_brand[province_brand['brand'].str.contains('메가박스')]

# 'categorized_brand'라는 새로운 열을 생성하고, "메가박스"로 값을 할당합니다.
megabox_brands['categorized_brand'] = '메가박스'

# 'province'와 'categorized_brand'로 그룹화한 후, 각 그룹별로 개수를 계산합니다.
brand_counts = megabox_brands.groupby(
    ['province', 'categorized_brand']).size().reset_index(name='counts')

# 'categorized_brand'가 '기타'인 행을 필터링합니다.
brand_counts = brand_counts[brand_counts['categorized_brand'] != '기타']

# 결과 DataFrame을 출력합니다.
print(brand_counts)
