# 데이터 분석을 위해 pandas, 시각화를 위해 seaborn 불러오기
import pandas as pd
import seaborn as sns

# # 종목명이 영문으로 표기 될 때 아래의 주석을 풀기
# url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
# df_listing = pd.read_html(url, header=0)[0]
# cols_ren = {'회사명':'Name', '종목코드':'Symbol', '업종':'Sector', '주요제품':'Industry', 
#                     '상장일':'ListingDate', '결산월':'SettleMonth',  '대표자명':'Representative', 
#                     '홈페이지':'HomePage', '지역':'Region', }
# df = df_listing.rename(columns = cols_ren)
# df['Symbol'] = df['Symbol'].apply(lambda x: '{:06d}'.format(x))
# df['ListingDate'] = pd.to_datetime(df['ListingDate'])
# df

# to_csv로 저장해둔 krx.csv 파일을 pd.read_csv 로 불러옵니다.
df = pd.read_csv("krx.csv",dtype={"Symbol":object})
df.shape

#{'회사명':'Name', '종목코드':'Symbol', '업종':'Sector', '주요제품':'Industry', '상장일':'ListingDate', 
# '결산월':'SettleMonth', '대표자명':'Representative', '홈페이지':'HomePage', '지역':'Region', }


# head 로 위에 있는 데이터 일부만 가져옵니다.
df.head(2)

# tail 로 아래 있는 데이터 일부만 가져옵니다.
df.tail()

# sample을 사용하면 랜덤하게 ()안의 갯수만큼 가져옵니다. 
# ()안에 값을 써주지 않으면 한 개만 가져옵니다.
df.sample()

# info 로 요약 데이터를 봅니다.
df.info()

# describe 로 기술통계값을 봅니다.
df.describe()

# 중복을 제외한 unique 값의 갯수를 봅니다.
df.nunique()

# index 값 보기
df.index

# 컬럼값 보기
df.columns

# 값만 보기
df.values


