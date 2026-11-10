import pandas as pd
import matplotlib.pyplot as plt

data = {
    'ID_Produk': [
        'P001', 'P002', 'P003', 'P004', 'P002', 'P005', 'P001 ',
        'P006', 'P007', 'P008', 'P009', 'P010', 'P011', 'P012',
        'P013', 'P014', 'P015'
    ],
    
    'Nama_Produk': [
        'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Mouse', 'Printer', 'Laptop',
        'Webcam', 'Headset', 'Flashdisk', 'SSD', 'RAM', 'Speaker',
        'Kamera', 'Tablet', None, 'Router'
    ],
    
    'Jumlah_Terjual': [
        15, 50, 30, 20, 50, 10, 15,
        25, 40, 100, 35, 20, -5, 15,
        0, 200, 30
    ],
    
    'Harga_Satuan': [
        7000000, 150000, 300000, 1500000, 150000, 800000, 7000000,
        500000, 750000, 120000, 900000, 600000, 450000, 5000000,
        3500000, 0, None
    ]
}

df_sebelum = pd.DataFrame(data)

print("=== DATASET SEBELUM CLEANING ===")
print(df_sebelum)
print("\n" + "="*60 + "\n")

df_sebelum.to_csv('dataset_sebelum_cleaning.csv', index=False)

print("=== PEMERIKSAAN DATA KOSONG ===")

data_kosong = df_sebelum.isnull().sum()
print(data_kosong)

total_kosong = df_sebelum.isnull().sum().sum()
print(f"\nTotal data kosong: {total_kosong} data")

if total_kosong == 0:
    print("Tidak ditemukan data kosong.")
else:
    print("Ditemukan data kosong.")

print("\n" + "="*60 + "\n")

print("=== PEMERIKSAAN DATA DUPLIKAT ===")

jumlah_duplikat = df_sebelum.duplicated().sum()
print(f"Jumlah baris duplikat ditemukan: {jumlah_duplikat} baris")

if jumlah_duplikat > 0:
    print("\nData yang terdeteksi sebagai duplikat:")
    print(df_sebelum[df_sebelum.duplicated(keep=False)])
else:
    print("Tidak ditemukan data duplikat.")

print("\n" + "="*60 + "\n")

print("=== PEMERIKSAAN TIPE DATA ===")
print(df_sebelum.dtypes)

print("\n" + "="*60 + "\n")

df_clean = df_sebelum.dropna().copy()

print("=== SETELAH MEMBERSIHKAN DATA KOSONG ===")
print(df_clean)

print("\n" + "="*60 + "\n")

df_clean = df_clean.drop_duplicates().reset_index(drop=True)

print("=== SETELAH MEMBERSIHKAN DATA DUPLIKAT ===")
print(df_clean)

print("\n" + "="*60 + "\n")

print("=== PEMERIKSAAN NILAI TIDAK VALID ===")

jumlah_negatif = df_clean[
    df_clean['Jumlah_Terjual'] < 0
]

print("\nData dengan Jumlah_Terjual negatif:")
print(jumlah_negatif)

harga_tidak_valid = df_clean[
    df_clean['Harga_Satuan'] <= 0
]

print("\nData dengan Harga_Satuan <= 0:")
print(harga_tidak_valid)

print("\n" + "="*60 + "\n")

df_clean = df_clean[
    (df_clean['Jumlah_Terjual'] >= 0) &
    (df_clean['Harga_Satuan'] > 0)
].copy()

print("=== SETELAH MEMBERSIHKAN NILAI TIDAK VALID ===")
print(df_clean)

print("\n" + "="*60 + "\n")

print("=== PEMERIKSAAN OUTLIER ===")

def cek_outlier_iqr(df, kolom):
    Q1 = df[kolom].quantile(0.25)
    Q3 = df[kolom].quantile(0.75)
    IQR = Q3 - Q1

    batas_bawah = Q1 - (1.5 * IQR)
    batas_atas = Q3 + (1.5 * IQR)

    outlier = df[
        (df[kolom] < batas_bawah) |
        (df[kolom] > batas_atas)
    ]

    print(f"\nKolom: {kolom}")
    print(f"Q1           : {Q1}")
    print(f"Q3           : {Q3}")
    print(f"IQR          : {IQR}")
    print(f"Batas bawah  : {batas_bawah}")
    print(f"Batas atas   : {batas_atas}")

    if len(outlier) > 0:
        print("\nData yang terdeteksi sebagai outlier:")
        print(outlier)
    else:
        print("\nTidak ditemukan outlier.")

    return outlier

outlier_jumlah = cek_outlier_iqr(
    df_clean,
    'Jumlah_Terjual'
)

outlier_harga = cek_outlier_iqr(
    df_clean,
    'Harga_Satuan'
)

print("\n" + "="*60 + "\n")

print("=== PEMERIKSAAN KONSISTENSI ID PRODUK ===")

konsistensi_id = (
    df_clean
    .groupby('ID_Produk')['Nama_Produk']
    .nunique()
)

id_tidak_konsisten = konsistensi_id[
    konsistensi_id > 1
]

if len(id_tidak_konsisten) > 0:
    print("Ditemukan ID Produk dengan Nama Produk berbeda:")
    print(id_tidak_konsisten)
else:
    print("Semua ID Produk memiliki Nama Produk yang konsisten.")

print("\n" + "="*60 + "\n")

df_sesudah = df_clean.reset_index(drop=True)

print("=== DATASET SESUDAH CLEANING ===")
print(df_sesudah)

print(f"\nJumlah baris sebelum cleaning : {len(df_sebelum)}")
print(f"Jumlah baris sesudah cleaning : {len(df_sesudah)}")

print("\n" + "="*60 + "\n")

df_sesudah.to_csv(
    'dataset_sesudah_cleaning.csv',
    index=False
)

df_sesudah['Total_Penjualan'] = (
    df_sesudah['Jumlah_Terjual'] *
    df_sesudah['Harga_Satuan']
)

print("=== HASIL TRANSFORMASI DATA ===")

print(
    df_sesudah[
        [
            'ID_Produk',
            'Nama_Produk',
            'Jumlah_Terjual',
            'Harga_Satuan',
            'Total_Penjualan'
        ]
    ]
)

print("\n" + "="*60 + "\n")

plt.figure(figsize=(9, 5))

plt.bar(
    df_sesudah['Nama_Produk'],
    df_sesudah['Total_Penjualan'],
    color='skyblue',
    edgecolor='black'
)

plt.title(
    'Diagram Batang Total Penjualan Setiap Produk (Python)',
    fontsize=14
)

plt.xlabel('Nama Produk', fontsize=12)
plt.ylabel('Total Penjualan (Rupiah)', fontsize=12)

plt.xticks(rotation=15)

plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.7
)

plt.tight_layout()

plt.savefig('grafik_python.png')
plt.show()

produk_terbesar = df_sesudah.loc[
    df_sesudah['Total_Penjualan'].idxmax()
]

print("=== KESIMPULAN ANALISIS ===")

print(
    f"Produk dengan total penjualan terbesar adalah: "
    f"{produk_terbesar['Nama_Produk']}"
)

print(
    f"Jumlah Terjual : "
    f"{produk_terbesar['Jumlah_Terjual']} unit"
)

print(
    f"Harga Satuan   : "
    f"Rp {produk_terbesar['Harga_Satuan']:,}"
)

print(
    f"Total Penjualan: "
    f"Rp {produk_terbesar['Total_Penjualan']:,}"
)

print("\n" + "="*60)
print("PROSES CLEANING DAN ANALISIS DATA SELESAI.")
