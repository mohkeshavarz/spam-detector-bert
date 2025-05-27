import os
import csv
from pathlib import Path

def extract_body(file_path):
    """فقط body ایمیل رو جدا می‌کنه"""
    with open(file_path, "r", encoding="latin-1") as f:
        content = f.read()
        # جدا کردن header از body با یک خط خالی
        parts = content.split("\n\n", 1)
        if len(parts) > 1:
            return parts[1].strip()
        else:
            return ""

def convert_to_csv(spam_dir, ham_dir, output_file):
    rows = []

    # اسپم‌ها
    for filename in os.listdir(spam_dir):
        path = os.path.join(spam_dir, filename)
        text = extract_body(path)
        rows.append(["spam", text])

    # ایمیل‌های سالم
    for filename in os.listdir(ham_dir):
        path = os.path.join(ham_dir, filename)
        text = extract_body(path)
        rows.append(["ham", text])

    # نوشتن CSV
    with open(output_file, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["label", "text"])
        writer.writerows(rows)

    print(f"✅ فایل CSV ساخته شد: {output_file}")

if __name__ == "__main__":
    spam_dir = "data/english/spam"
    ham_dir = "data/english/ham/easy_ham"  # چون مسیر شما این شکلیه
    output_file = "data/english/emails.csv"

    convert_to_csv(spam_dir, ham_dir, output_file)
