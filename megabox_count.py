import pandas as pd

# CSV 파일을 'cp949' 인코딩으로 읽어옵니다.
df = pd.read_csv('dt.csv', encoding='cp949')

# DataFrame에서 'province'와 'brand' 열을 추출합니다.
province_brand = df[['province', 'brand']]

# 'brand' 열에서 '메가박스'를 포함하는 행을 필터링합니다.
megabox_brands = province_brand[province_brand['brand'].str.contains('메가박스')]

# 'categorized_brand' 열에 '메가박스' 값을 할당합니다.
megabox_brands['categorized_brand'] = '메가박스'

# 'province'와 'categorized_brand'로 데이터를 그룹화하고 각 그룹의 크기/개수를 계산합니다.
brand_counts = megabox_brands.groupby(
    ['province', 'categorized_brand']).size().reset_index(name='counts')

# 'categorized_brand' 값이 '기타'인 행을 필터링합니다.
brand_counts = brand_counts[brand_counts['categorized_brand'] != '기타']

# 메가박스 영화관의 총 개수를 계산합니다.
total_count = brand_counts['counts'].sum()

# 각 지역별 브랜드 개수를 출력합니다.
print(brand_counts)

# 전국 메가박스 영화관의 총 개수를 출력합니다.
print("전국 메가박스 영화관의 총 개수:", total_count)
