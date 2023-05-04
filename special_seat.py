import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 설정
mpl.rcParams['font.family'] = "NanumGothic"
mpl.rcParams['font.size'] = 10

# CSV 파일에서 데이터 읽어오기
df = pd.read_csv('dt1.csv', encoding='cp949')

# 브랜드 분류하기
df['categorized_brand'] = df['brand'].apply(lambda x: 'CGV' if 'CGV' in x else ('메가박스' if '메가박스' in x else ('롯데시네마' if '롯데시네마' in x else '기타')))

# 필요한 열만 추출하여 새로운 데이터프레임 만들기
sub_df = df[['categorized_brand', '3D', '4D', 'IMAX']]

# 브랜드별로 3D, 4D, IMAX 상영관 수 합산하여 그룹화하기
grouped_df = sub_df.groupby('categorized_brand').sum()

# 막대그래프 그리기
grouped_df.plot(kind='bar')
plt.title('3D, 4D, IMAX 상영관 개수', loc='left')
plt.xlabel('영화관 브랜드')
plt.ylabel('상영관 개수')
plt.xticks(rotation=0)
plt.show()