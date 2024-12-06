import pandas as pd

# Đọc file CSV
df = pd.read_csv("datasets/datasets.csv")

# Shuffle các dòng
shuffled_df = df.sample(frac=1).reset_index(drop=True)

# Ghi file mới (nếu cần)
shuffled_df.to_csv("datasets/datasets.csv", index=False)

print("Các dòng đã được shuffle!")