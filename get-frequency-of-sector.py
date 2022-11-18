
# 섹터의 빈도수를 구합니다.
# 상위 30개 섹터의 빈도수를 sector_count_top 변수에 할당합니다.
# sector_count_top
sector_count_top = df["Sector"].value_counts().head(30)
sector_count_top.index


# df_sector_30
df_sector_30  = df[df["Sector"].isin(sector_count_top.index)]

# Seaborn countplot 활용하여 빈도수를 표현합니다.
plt.figure(figsize=(10,8))
sns.countplot(data=df_sector_30, y="Sector")

print(plt.colormaps())


# 빈도수가 가장 많은 데이터 색인하기
plt.figure(figsize=(10,8))
sns.countplot(data=df_sector_30, y="Sector", palette="magma",
              order=sector_count_top.index).set_title("섹터별 빈도수")

