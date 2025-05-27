import os
import tarfile
import urllib.request

# مسیر ذخیره
os.makedirs("data/english", exist_ok=True)

# لینک‌ها
datasets = {
    "spam": "https://spamassassin.apache.org/old/publiccorpus/20021010_spam.tar.bz2",
    "ham": "https://spamassassin.apache.org/old/publiccorpus/20021010_easy_ham.tar.bz2"
}

for label, url in datasets.items():
    filename = url.split("/")[-1]
    filepath = f"data/english/{filename}"

    # دانلود
    if not os.path.exists(filepath):
        print(f"⬇️ Downloading {label}...")
        urllib.request.urlretrieve(url, filepath)
        print(f"✅ Downloaded: {filename}")

    # استخراج
    print(f"📦 Extracting {filename}...")
    with tarfile.open(filepath, "r:bz2") as tar:
        tar.extractall(path=f"data/english/{label}")
    print(f"✅ Extracted to: data/english/{label}")
