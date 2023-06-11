# pandas 모듈을 불러옵니다.
import pandas as pd
# matplotlib.pyplot 모듈을 불러옵니다.
import matplotlib.pyplot as plt
# matplotlib 모듈을 불러옵니다.
import matplotlib as mpl
# 한글 폰트 설정
mpl.rcParams['font.family'] = "NanumGothic"
mpl.rcParams['font.size'] = 10

# CSV 파일에서 데이터를 읽어옵니다.
df = pd.read_csv('dt2.csv', encoding='cp949')

# 브랜드 열을 기준으로 브랜드를 카테고리화합니다.
df['categorized_brand'] = df['brand'].apply(lambda x: 'CGV' if 'CGV' in x else (
    '메가박스' if '메가박스' in x else ('롯데시네마' if '롯데시네마' in x else '기타')))

# 데이터프레임을 카테고리화된 브랜드로 그룹화하고 스크린수와 좌석수를 따로 합산합니다.
screens_df = df.groupby('categorized_brand', sort=False).agg(
    {'screens': 'sum'}).sort_values(by='screens')
seats_df = df.groupby('categorized_brand', sort=False).agg(
    {'seats': 'sum'}).sort_values(by='seats')

# 스크린수와 좌석수에 대한 막대 그래프를 그립니다.

# 1행 2열의 서브플롯을 생성합니다.
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
# 스크린수에 대한 막대 그래프를 그립니다.
ax[0].bar(screens_df.index, screens_df['screens'])
ax[0].set_title('스크린수')
ax[0].set_ylabel('개')
# 좌석수에 대한 막대 그래프를 그립니다.
ax[1].bar(seats_df.index, seats_df['seats'])
ax[1].set_title('좌석수')
ax[1].set_ylabel('개')

plt.tight_layout()  # 그래프 간격을 조정합니다.
plt.show()  # 그래프를 출력합니다.
