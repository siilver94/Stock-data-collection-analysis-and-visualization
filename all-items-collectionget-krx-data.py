# 데이터 분석을 위해 pandas 불러오기
import pandas as pd

# FinanceDataReader 를 fdr 별칭으로 불러옵니다.
# 라이브러리의 version을 확인하고 싶을 때는 .__version__ 으로 확인합니다. 
import FinanceDataReader as fdr
fdr.__version__

# 도움말을 보고자 할때는 ? 를 사용하고 소스코드를 볼 때는 ??를 사용합니다.
# 주피터 노트북에서는 함수나 메소드의 괄호 안에서 shift + tab 키를 누르면 도움말을 볼 수 있습니다.

# fdr.StockListing??
df_krx = fdr.StockListing("KRX")
# KRX : KRX 종목 전체
# KOSPI : KOSPI 종목
# KOSDAQ : KOSDAQ 종목
# KONEX : KONEX 종목
# NASDAQ : 나스닥 종목
# NYSE : 뉴욕증권거래소 종목
# SP500 : S&P500 종목


# 한국거래소 상장종목 전체 가져오기
df_krx.head()

# 행과 열의 크기를 봅니다.(행, 열) 순
df_krx.shape

# 전체 데이터프레임의 요약정보를 봅니다.
df_krx.info()

# 기술통계 값을 요약합니다
df_krx.describe()

# to_csv로 Dataframe을 데이터 저장용 파일인 CSV 파일로 바꿀 수 있습니다.
df_krx.to_csv("krx.csv",index=False)

# CSV로 저장된 파일을 다시 DataFrame으로 읽어서 확인해 봅니다.
pd.read_csv("krx.csv")
