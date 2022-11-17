# Market column에 어떤 데이터들이 있는지 unique로 확인합니다.
df["Market"].unique()

# value_counts()로 빈도수를 구합니다.
df["Market"].value_counts()

# 빈도수를 시각화 합니다.
df["Market"].value_counts().plot.barh()

# Seaborn countplot 활용하여 빈도수를 표현합니다.
sns.countplot(data=df,x="Market")
