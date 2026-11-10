# ==========================================
# 1. MEMBUAT DATASET 17 DATA
# ==========================================

ID_Produk <- c(
  "P001", "P002", "P003", "P004", "P002",
  "P005", "P006", "P007", "P008", "P009",
  "P010", "P011", "P012", "P013", "P014",
  "P015", "P001 "
)

Nama_Produk <- c(
  "Laptop", "Mouse", "Keyboard", "Monitor", "Mouse",
  "Printer", "Speaker", "Webcam", "Headset", "Flashdisk",
  "Harddisk", "Router", "Smartphone", "Tablet", NA,
  "Tablet", "Laptop"
)

Jumlah_Terjual <- c(
  15, 50, 30, 20, 50,
  10, -5, 25, 40, 60,
  12, 18, 22, 0, 5,
  8, 15
)

Harga_Satuan <- c(
  7000000, 150000, 300000, 1500000, 150000,
  800000, 250000, 450000, 350000, 100000,
  1200000, 500000, 4500000, 0, 3500000,
  NA, 7000000
)

df_sebelum <- data.frame(
  ID_Produk,
  Nama_Produk,
  Jumlah_Terjual,
  Harga_Satuan
)

# ==========================================
# 2. DATASET SEBELUM CLEANING
# ==========================================

print("=== DATASET SEBELUM CLEANING ===")
print(df_sebelum)

cat("\n------------------------------------------\n\n")

write.csv(
  df_sebelum,
  "dataset_sebelum_cleaning_r.csv",
  row.names = FALSE
)

# ==========================================
# 3. CEK MISSING VALUE
# ==========================================

jumlah_missing <- sum(is.na(df_sebelum))

cat(
  paste(
    "Jumlah missing value ditemukan:",
    jumlah_missing,
    "\n\n"
  )
)

# ==========================================
# 4. CEK DUPLIKAT
# ==========================================

jumlah_duplikat <- sum(duplicated(df_sebelum))

cat(
  paste(
    "Jumlah baris duplikat ditemukan:",
    jumlah_duplikat,
    "baris\n\n"
  )
)

# ==========================================
# 5. HAPUS DUPLIKAT
# ==========================================

df_sesudah <- df_sebelum[!duplicated(df_sebelum), ]

# ==========================================
# 6. HAPUS MISSING VALUE
# ==========================================

df_sesudah <- na.omit(df_sesudah)

# ==========================================
# 7. HAPUS NILAI TIDAK VALID
# ==========================================

df_sesudah <- df_sesudah[
  df_sesudah$Jumlah_Terjual >= 0 &
  df_sesudah$Harga_Satuan > 0,
]

# ==========================================
# 8. DATASET SESUDAH CLEANING
# ==========================================

print("=== DATASET SESUDAH CLEANING ===")
print(df_sesudah)

cat("\n------------------------------------------\n\n")

write.csv(
  df_sesudah,
  "dataset_sesudah_cleaning_r.csv",
  row.names = FALSE
)

# ==========================================
# 9. TRANSFORMASI TOTAL PENJUALAN
# ==========================================

df_sesudah$Total_Penjualan <-
  df_sesudah$Jumlah_Terjual *
  df_sesudah$Harga_Satuan

print("=== HASIL TRANSFORMASI DATA ===")

print(
  df_sesudah[
    ,
    c(
      "Nama_Produk",
      "Jumlah_Terjual",
      "Harga_Satuan",
      "Total_Penjualan"
    )
  ]
)

cat("\n------------------------------------------\n\n")

# ==========================================
# 10. MEMBUAT DIAGRAM BATANG
# ==========================================

# Jalankan sekali jika ggplot2 belum terinstall:
# install.packages("ggplot2")

library(ggplot2)

grafik <- ggplot(
  df_sesudah,
  aes(
    x = Nama_Produk,
    y = Total_Penjualan,
    fill = Nama_Produk
  )
) +
  geom_bar(
    stat = "identity",
    color = "black",
    show.legend = FALSE
  ) +
  labs(
    title = "Diagram Batang Total Penjualan Setiap Produk (R)",
    x = "Nama Produk",
    y = "Total Penjualan (Rupiah)"
  ) +
  theme_minimal()

print(grafik)

# Simpan diagram sebagai PNG
ggsave(
  "diagram_total_penjualan_r.png",
  plot = grafik,
  width = 10,
  height = 6,
  dpi = 300
)

# ==========================================
# 11. MENENTUKAN PRODUK TERBESAR
# ==========================================

produk_terbesar <- df_sesudah[
  which.max(df_sesudah$Total_Penjualan),
]

# ==========================================
# 12. KESIMPULAN
# ==========================================

print("=== KESIMPULAN ANALISIS ===")

cat(
  paste(
    "Produk dengan total penjualan terbesar adalah:",
    produk_terbesar$Nama_Produk,
    "\n"
  )
)

cat(
  paste(
    "Jumlah Terjual:",
    produk_terbesar$Jumlah_Terjual,
    "unit\n"
  )
)

cat(
  paste(
    "Harga Satuan: Rp",
    format(
      produk_terbesar$Harga_Satuan,
      big.mark = "."
    ),
    "\n"
  )
)

cat(
  paste(
    "Total Penjualan: Rp",
    format(
      produk_terbesar$Total_Penjualan,
      big.mark = "."
    ),
    "\n"
  )
)