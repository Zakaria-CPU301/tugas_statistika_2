# ---------------------------------------------------------
# 1. MEMBUAT DATASET MENGGUNAKAN R (Sengaja ada duplikat)
# ---------------------------------------------------------
ID_Produk <- c('P001', 'P002', 'P003', 'P004', 'P002', 'P005', 'P001')
Nama_Produk <- c('Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Mouse', 'Printer', 'Laptop')
Jumlah_Terjual <- c(15, 50, 30, 20, 50, 10, 15)
Harga_Satuan <- c(7000000, 150000, 300000, 1500000, 150000, 800000, 7000000)

df_sebelum <- data.frame(ID_Produk, Nama_Produk, Jumlah_Terjual, Harga_Satuan)

print("=== DATASET SEBELUM CLEANING (DENGAN DUPLIKAT) ===")
print(df_sebelum)
cat("\n--------------------------------------------------\n\n")

# Menyimpan dataset sebelum cleaning ke CSV
write.csv(df_sebelum, "dataset_sebelum_cleaning_r.csv", row.names = FALSE)

# ---------------------------------------------------------
# 2. PEMERIKSAAN & PEMBERSIHAN DATA DUPLIKAT
# ---------------------------------------------------------
# Memeriksa jumlah baris duplikat
jumlah_duplikat <- sum(duplicated(df_sebelum))
cat(paste("Jumlah baris duplikat ditemukan:", jumlah_duplikat, "baris\n\n"))

# Membersihkan data duplikat (mengambil baris unik)
df_sesudah <- df_sebelum[!duplicated(df_sebelum), ]

print("=== DATASET SESUDAH CLEANING (BERSIH) ===")
print(df_sesudah)
cat("\n--------------------------------------------------\n\n")

# Menyimpan dataset sesudah cleaning ke CSV
write.csv(df_sesudah, "dataset_sesudah_cleaning_r.csv", row.names = FALSE)

# ---------------------------------------------------------
# 3. HASIL TRANSFORMASI DATA (Total Penjualan = Jumlah Terjual * Harga Satuan)
# ---------------------------------------------------------
df_sesudah$Total_Penjualan <- df_sesudah$Jumlah_Terjual * df_sesudah$Harga_Satuan

print("=== HASIL TRANSFORMASI DATA (DENGAN TOTAL PENJUALAN) ===")
print(df_sesudah[, c('Nama_Produk', 'Jumlah_Terjual', 'Harga_Satuan', 'Total_Penjualan')])
cat("\n--------------------------------------------------\n\n")

# ---------------------------------------------------------
# 4. MEMBUAT DIAGRAM BATANG MENGGUNAKAN R (ggplot2)
# ---------------------------------------------------------
# Pastikan package ggplot2 sudah terinstall (jika belum, jalankan: install.packages("ggplot2"))
library(ggplot2)

ggplot(df_sesudah, aes(x = Nama_Produk, y = Total_Penjualan, fill = Nama_Produk)) +
  geom_bar(stat = "identity", color = "black", show.legend = FALSE) +
  labs(
    title = "Diagram Batang Total Penjualan Setiap Produk (R)",
    x = "Nama Produk",
    y = "Total Penjualan (Rupiah)"
  ) +
  theme_minimal()

# Menyimpan grafik ke file PNG
ggsave("grafik_r_lengkap.png", width = 8, height = 5)

# ---------------------------------------------------------
# 5. MENJELASKAN PRODUK DENGAN TOTAL PENJUALAN TERBESAR (KESIMPULAN)
# ---------------------------------------------------------
produk_terbesar <- df_sesudah[which.max(df_sesudah$Total_Penjualan), ]

print("=== KESIMPULAN ANALISIS ===")
cat(paste("Produk dengan total penjualan terbesar adalah:", produk_terbesar$Nama_Produk, "\n"))
cat(paste("Jumlah Terjual :", produk_terbesar$Jumlah_Terjual, "unit\n"))
cat(paste("Harga Satuan   : Rp", format(produk_terbesar$Harga_Satuan, big.mark = ","), "\n"))
cat(paste("Total Penjualan: Rp", format(produk_terbesar$Total_Penjualan, big.mark = ","), "\n"))
