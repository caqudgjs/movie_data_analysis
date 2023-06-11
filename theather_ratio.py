import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = "NanumGothic"
mpl.rcParams['font.size'] = 10

# CSV 파일을 읽어서 DataFrame을 생성합니다.
df = pd.read_csv('dt.csv', encoding='cp949')

# 'brand' 열 값을 기준으로 'categorized_brand' 열을 생성합니다.
# 브랜드 이름에 따라 'CGV', '메가박스', '롯데시네마', '기타'로 분류됩니다.
df['categorized_brand'] = df['brand'].apply(lambda x: 'CGV' if 'CGV' in x else (
    '메가박스' if '메가박스' in x else ('롯데시네마' if '롯데시네마' in x else '기타')))

# 브랜드 카테고리별 빈도수를 계산합니다.
brand_counts = df['categorized_brand'].value_counts()

# 새로운 figure와 axes를 생성합니다.
fig, ax = plt.subplots(figsize=(8, 6))

# 브랜드 카테고리별 비율을 파이 차트로 그립니다.
# kind='pie'는 파이 차트를 그리는 옵션입니다.
# autopct='%1.1f%%'는 각 파이 조각에 퍼센트 값을 표시합니다.
# startangle=0은 첫 번째 파이 조각이 x축에서 시작하도록 설정합니다.
# labels=None은 기본 레이블을 제거합니다.
# ax=ax는 현재 axes에 그림을 그리도록 설정합니다.
brand_counts.plot(kind='pie', autopct='%1.1f%%',
                  startangle=0, labels=None, ax=ax)

# y축 레이블을 제거합니다.
plt.ylabel('')

# 범례를 추가합니다.
# labels에는 브랜드 카테고리의 이름을 사용합니다.
# loc='upper right'는 범례를 오른쪽 상단에 배치합니다.
plt.legend(labels=brand_counts.index, loc='upper right')

# 차트의 가로세로 비율을 동일하게 설정합니다.
plt.axis('equal')

# 제목을 추가합니다.
# loc='left'는 제목을 왼쪽에 배치합니다.
# fontsize=20, fontweight='bold'는 제목의 크기와 굵기를 설정합니다.
plt.title('상영관 비율', loc='left', fontsize=20, fontweight='bold')

# 차트를 표시합니다.
plt.show()
