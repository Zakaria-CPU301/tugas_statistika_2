import pandas as pd
import matplotlib.pyplot as plt

data = {
    'ID_Produk': ['P001', 'P002', 'P003', 'P004', 'P002', 'P005', 'P001'],
    'Nama_Produk': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Mouse', 'Printer', 'Laptop'],
    'Jumlah_Terjual': [15, 50, 30, 20, 50, 10, 15],
    'Harga_Satuan': [7000000, 150000, 300000, 1500000, 150000, 800000, 7000000]
}

df_sebelum = pd.DataFrame(data)
print("=== DATASET SEBELUM CLEANING (DENGAN DUPLIKAT) ===")
print(df_sebelum)
print("\n" + "="*50 + "\n")

df_sebelum.to_csv('dataset_sebelum_cleaning.csv', index=False)

jumlah_duplikat = df_sebelum.duplicated().sum()
print(f"Jumlah baris duplikat ditemukan: {jumlah_duplikat} baris")

df_sesudah = df_sebelum.drop_duplicates().reset_index(drop=True)

print("\n=== DATASET SESUDAH CLEANING (BERSIH) ===")
print(df_sesudah)
print("\n" + "="*50 + "\n")

df_sesudah.to_csv('dataset_sesudah_cleaning.csv', index=False)

df_sesudah['Total_Penjualan'] = df_sesudah['Jumlah_Terjual'] * df_sesudah['Harga_Satuan']

print("=== HASIL TRANSFORMASI DATA (DENGAN TOTAL PENJUALAN) ===")
print(df_sesudah[['Nama_Produk', 'Jumlah_Terjual', 'Harga_Satuan', 'Total_Penjualan']])
print("\n" + "="*50 + "\n")

plt.figure(figsize=(9, 5))
plt.bar(df_sesudah['Nama_Produk'], df_sesudah['Total_Penjualan'], color='skyblue', edgecolor='black')
plt.title('Diagram Batang Total Penjualan Setiap Produk (Python)', fontsize=14)
plt.xlabel('Nama Produk', fontsize=12)
plt.ylabel('Total Penjualan (Rupiah)', fontsize=12)
plt.xticks(rotation=15)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('grafik_python.png')
plt.show()

produk_terbesar = df_sesudah.loc[df_sesudah['Total_Penjualan'].idxmax()]

print("=== KESIMPULAN ANALISIS ===")
print(f"Produk dengan total penjualan terbesar adalah: {produk_terbesar['Nama_Produk']}")
print(f"Jumlah Terjual : {produk_terbesar['Jumlah_Terjual']} unit")
print(f"Harga Satuan   : Rp {produk_terbesar['Harga_Satuan']:,}")
print(f"Total Penjualan: Rp {produk_terbesar['Total_Penjualan']:,}")
