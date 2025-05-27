import pandas as pd

# بارگذاری فایل sms.tsv از پوشه data
df = pd.read_csv("data/sms.tsv", sep="\t", header=None, names=["label", "message"])

# نمایش ۵ پیام اول
print("🔹 نمونه‌ای از پیام‌ها:")
print(df.head())

# بررسی تعداد پیام‌های اسپم و غیر اسپم
print("\n🔸 تعداد پیام‌ها:")
print(df['label'].value_counts())

# بررسی null بودن مقادیر (نباید چیزی خالی باشه)
print("\n🔸 بررسی مقادیر خالی:")
print(df.isnull().sum())
