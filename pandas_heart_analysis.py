import pandas as pd


df = pd.read_csv("heart.csv")

print("📋 İlk 5 Satır:")
print(df.head())

print("\n🔍 Eksik Veriler:")
print(df.isnull().sum())


print("\n⚠️ Eksik veri içeren satırlar:")
print(df[df.isnull().any(axis=1)])

print("\n📊 Temel İstatistikler:")
print(df.describe())