# Panduan Cek Validasi Silang Kamus Data

Dipakai untuk memeriksa kamus data kelompok lain (saat ini Kelompok 4) **dan** kamus data kita sendiri dengan cara yang sama.
Dokumen hasil review untuk Kelompok 4: `validasi-silang/PRPL_2B_RajinBelajar_ValidasiSilang_Kelompok4_M04-M05.docx` (lokal). ID temuan VS-xx di bawah merujuk ke dokumen itu.

## 1. Istilah: Baku, Sinonim, Homonim (Modul 5 §1.8)

| Istilah | Arti | Contoh | Aturan |
|---|---|---|---|
| **Baku** | Nama resmi yang dipilih untuk satu konsep. Dipakai di DFD, kamus data, process spec | `KodeEksemplar` | Satu konsep, satu nama baku |
| **Sinonim** | Dua nama berbeda untuk konsep yang sama | `IDAnggota` dan `NIM` | Pilih satu jadi baku, sisanya dicatat sebagai **alias** (bukan elemen terpisah) |
| **Homonim** | Satu nama dipakai untuk dua makna | `Status` untuk anggota dan untuk buku | Pecah: `StatusAnggota`, `StatusBuku` |

Kolom **Status Entri** di inventaris menjawab pertanyaan: *apakah nama ini nama resmi, atau nama lain dari sesuatu yang sudah ada?* Dasarnya Modul 5 Langkah 1 butir 4–5: "kelompokkan entri yang identik dan tandai calon alias", "tandai nama terlalu umum".

Contoh salah kaprah (Kelompok 4, VS-09): `infoDenda` ditandai "Sinonim", padahal namanya sama persis. Itu bukan sinonim.

## 2. Kolom Status Entri: Elementer / Komposit / Store?

Kurang tepat kalau dipakai di kolom **Status Entri**:
1. "Store" dobel dengan kolom **Jenis** (Flow/Store).
2. Elementer/Komposit itu **jenis struktur**, bukan **status nama**. Itu urusan Langkah 2–3 (entri komposit, penguraian).

**Yang aman:**

| Kolom | Isi |
|---|---|
| Jenis | Flow / Store |
| Status Entri | Baku / Alias dari `<nama baku>` / Perlu diperbaiki (nama terlalu umum) |
| Tipe Entri *(kolom tambahan, opsional)* | Komposit / Elementer |

Konsekuensinya: setiap flow bertanda **Elementer** wajib muncul di tabel elemen (domain, contoh). Kalau tidak, artinya flow itu tidak terdefinisi. Ini juga terjadi di kamus data kita (RV-M05-17).

## 3. Cara Baca Notasi (Modul 5 §1.4)

| Tulisan | Arti |
|---|---|
| `KodeBuku` | tepat 1 |
| `(KodeBuku)` | opsional, 0 atau 1 |
| `{KodeBuku}` | berulang, jumlah bebas |
| `1{KodeBuku}5` | minimal 1, maksimal 5 |
| `[A \| B]` | pilih salah satu |
| `@KodeBuku` | elemen kunci **record data store** |

Kesalahan umum: `hari = {1 | 2 | ... | 31}`. Kurung kurawal artinya pengulangan, padahal maksudnya pilihan, jadi seharusnya `[ ]` (VS-14).

## 4. Cara Cek per Temuan

### VS-10 · Aliran data store tidak diinventarisasi · Tinggi
- **Aturan:** Modul 5 §1.11, "Seluruh data flow dan data store pada DFD tercatat dalam inventaris". Panah ke/dari store juga data flow.
- **Langkah cek:**
  1. Buka semua gambar DFD (L0, L1). Hitung setiap panah yang menyentuh data store.
  2. Buka tabel Inventaris. Cari satu baris untuk setiap panah tadi.
  3. Panah yang tidak punya baris = temuan.
- **Bukti di Kelompok 4:** L0 ada 9 garis store (P1↔D1, D1→P2, P2↔D2, P2→D3, P3↔D2, P3↔D3, D1→4, D2→4, D3→4), L1-P2 ada 3, L1-P3 ada 3. Inventaris (18 baris) tidak memuat satu pun.
- **Akar masalah:** panah store tidak diberi nama di DFD (VS-01), sehingga tidak bisa ditulis di inventaris.

### VS-13 · Kardinalitas buku tidak konsisten · Tinggi
- **Aturan:** Modul 5 Langkah 3.3, "tentukan batas minimum dan maksimum pengulangan"; §1.11, struktur tidak saling bertentangan.
- **Langkah cek:**
  1. Cari setiap struktur yang memuat elemen yang sama (di sini: buku).
  2. Baca jumlahnya dengan tabel notasi di bagian 3.
  3. Kalau jumlahnya beda antar struktur untuk transaksi yang sama, itu temuan.
- **Bukti di Kelompok 4:**

| Lokasi | Isi | Artinya |
|---|---|---|
| Penguraian `pengajuanPeminjaman` | "1 anggota hanya bisa meminjam 1 buku", `= @IDAnggota + KodeBuku` | 1 buku |
| `buktiPeminjaman` | `{KodeBuku} + JudulBuku` | banyak kode, tapi judul cuma 1 |
| Store `Data Transaksi` | `1{KodeBuku}5` | 1–5 buku |

- **Dampak:** di M06 tidak jelas satu transaksi itu berapa buku, sehingga logika process spec tidak bisa ditulis.

### VS-15 · Sinonim/homonim tidak terkendali · Tinggi
- **Aturan:** Modul 5 §1.8, satu konsep satu nama baku; nama lain jadi alias.
- **Langkah cek:**
  1. Kumpulkan semua nama elemen dari struktur dan tabel elemen.
  2. Kelompokkan berdasarkan **makna**, bukan ejaan.
  3. Kelompok yang punya lebih dari satu nama atau lebih dari satu domain = temuan.
- **Bukti di Kelompok 4:**
  - `StatusAnggota = [Aktif | NonAktif]` vs `StatusKeanggotaan = [Aktif | Non-Aktif]`: konsep sama, nama dan ejaan nilainya beda.
  - `IDTransaksi` (bukti & store) vs `IDPeminjaman` (detail laporan): konsep sama.
  - `formPendaftaran` hanya memuat `NoIdentitas` (9–18 digit), tetapi di tempat lain anggota diidentifikasi dengan `IDAnggota` (10 digit). Asal-usul IDAnggota tidak dijelaskan.

### VS-12 · Notasi kunci `@` salah pakai · Sedang
- **Aturan:** Modul 5 §1.4 (`@` = elemen kunci), Langkah 4.4; §1.11 "setiap kunci dapat diidentifikasi".
- **Langkah cek:**
  1. Cari semua `@` di dokumen.
  2. Untuk tiap kemunculan, tanya: apakah ini struktur **record data store**?
  3. Kalau bukan store, `@` tidak perlu. Kalau store tidak punya `@`, kuncinya hilang.
- **Bukti di Kelompok 4:**
  - `infoDenda = @IDTransaksi + @IDAnggota + ...`: ini aliran, bukan store, dan `@`-nya dobel.
  - `dataPermintaanValidasi = IDAnggota + @TanggalPengajuan`: tanggal dijadikan kunci, padahal banyak pengajuan bisa terjadi di tanggal yang sama.
  - Store `Data Transaksi = IDTransaksi + ...`: justru tanpa `@`.

### VS-17 · Contoh bertentangan dengan aturan · Sedang
- **Aturan:** Modul 5 §1.11, "Format, domain, dan contoh data tidak saling bertentangan"; §1.7 contoh valid & tidak valid.
- **Langkah cek:**
  1. Untuk setiap baris tabel elemen, uji **contoh valid** terhadap kolom Domain/Aturan. Harus lolos.
  2. Uji **contoh tidak valid**. Harus melanggar minimal satu aturan, dan sebaiknya disebutkan aturan mana.
- **Bukti di Kelompok 4:**
  - `NoTelepon`: aturan "diawali 08", tapi contoh valid `81234567890`. Gagal.
  - `TanggalJatuhTempo`: aturan "7 hari kerja", contoh 19-10-2026 → 26-10-2026. Padahal 19 Okt 2026 hari Senin, jadi +7 hari kerja = **28-10-2026**. Contoh 26-10 adalah hasil 7 hari kalender. Gagal.
  - `EkstensiDomain`: aturan "hanya huruf", tapi contoh `ac.id` memuat titik. Gagal.

## 5. Cek Diri Sendiri Dulu

Sebelum dokumen validasi silang dikirim ke Kelompok 4, pastikan dua temuan ini **tidak** ada di kamus data kita, supaya tidak dibalikkan:

| Temuan untuk K4 | Masalah yang sama di kamus data kita (`updates/`) | Item revisi |
|---|---|---|
| VS-13 kardinalitas | `dataTransaksiPeminjaman` 1 buku vs penguraian `1{KodeEksemplar}3` | RV-M05-16 |
| VS-12 `@` | `@NIM + @KodeBuku` di hampir semua flow | RV-M05-15 |
| VS-15 sinonim | KodeBuku/KodeEksemplar, Judul/JudulBuku, NoBukti/IDTransaksi | RV-M05-14 |
| VS-10 inventaris | Store D1–D3 dan 16 flow store tidak ada di inventaris | RV-M05-12 |

Ternyata keempatnya juga terjadi di kamus data kita.
