import pandas as pd
import seaborn as sns

# # 종목명이 영문으로 표기 될 때 아래의 주석을 풀고 데이터를 받아서 분석
# url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
# df_listing = pd.read_html(url, header=0)[0]
# cols_ren = {'회사명':'Name', '종목코드':'Symbol', '업종':'Sector', '주요제품':'Industry', 
#                     '상장일':'ListingDate', '결산월':'SettleMonth',  '대표자명':'Representative', 
#                     '홈페이지':'HomePage', '지역':'Region', }
# df = df_listing.rename(columns = cols_ren)
# df['Symbol'] = df['Symbol'].apply(lambda x: '{:06d}'.format(x))
# df['ListingDate'] = pd.to_datetime(df['ListingDate'])


# to_csv로 저장해둔 krx.csv 파일을 pd.read_csv 로 불러옵니다.

df = pd.read_csv("krx.csv",dtype={"Symbol":object})

# Name 컬럼 하나만 가져옵니다.
df["Name"]

# df["Name"] 의 type을 봅니다.
type(df["Name"])

# 0번째 행만 가져옵니다. 행인덱스를 가져올때는 .loc를 사용합니다.
# loc는 위치(locate)를 의미합니다.
df.loc[0]


# df.loc[0] 의 type을 봅니다.
type(df.loc[0])


# df 변수의 타입을 봅니다.
type(df)

# 여러 컬럼을 지정할 때는 리스트 형태로 묶어주어야 합니다. 
# 2차원 행렬은 대괄호가 [] 2개가 있다는 것을 기억해 주세요. 
df[["Symbol","Name"]]

# 여러 개의 행을 가져올 때도 [] 대괄호를 통해 리스트 형태로 묶어줍니다.
df.loc[[0,1,2,5]]


# 1개의 컬럼을 가져올 때도 대괄호[] 2개를 써서 리스트 형태로 묶어주게 되면 데이터프레임 형태로 반환됩니다.
# "Name" 을 데이터프레임으로 가져옵니다.
df[["Name"]]

type(df[["Name"]])


# 행과 열 함께 가져오기
# .loc[행, 열]
df.loc[5,"Name"]

# .loc[행, 열]
df.loc[1]

# 두개의 loc함수의 시간차이 확인, 같이 쓰는 게 더 빠른
# %timeit
%timeit df.loc[2, "Name"]

# %timeit
%timeit df.loc[2]["Name"]

# 여러 개의 행과 하나의 컬럼 가져오기
# .loc[행, 열]
df.loc[[0,1],"Name"]

# 여러개의 행과 여러 개의 컬럼 가져오기
# .loc[행, 열]
df.loc[[0,1],["Name", "Symbol"]]
