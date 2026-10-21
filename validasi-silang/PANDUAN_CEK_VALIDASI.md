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

---

## 6. Opsi Pengganti VS-12 (ditambahkan 2026-10-22)

VS-12 (`@`) ditunda karena kamus data kita juga punya masalah yang sama (UC-02, RV-M05-15). Bagian 4 tetap dipertahankan sebagai acuan. Berikut 3 opsi pengganti yang **mudah dicek** dan **tidak terjadi di kamus data kita** (sudah dicek terhadap `updates/` M05). Pilih satu.

| Opsi | Temuan | Severitas | Kenapa gampang | Aman untuk kita? |
|---|---|---|---|---|
| A | VS-14 · Notasi `{}` dipakai untuk pilihan | Sedang | Cukup cari pola `{ ... \| ... }` | ✅ kita pakai `[ ]` untuk pilihan (`StatusEksemplar`, `PeringkatPeminjaman`) |
| B | VS-16 · Satu elemen, panjang/domain berbeda | Sedang | Bandingkan definisi elemen yang sama di beberapa tempat | ✅ `NIM`, `KodeEksemplar`, `IDTransaksi`, tanggal kita konsisten. Cek ulang kalau ada tambahan baru |
| C | VS-06 · Nama aliran `triggerStatusBuku` | Sedang | Satu nama, satu aturan | ✅ semua nama aliran kita kata benda |

### Opsi A · VS-14 · Notasi pengulangan dipakai untuk pilihan · Sedang
- **Aturan:** Modul 5 §1.4 Gambar 31: `{}` = berulang, `[]` = memilih satu alternatif, `|` = pemisah alternatif.
- **Langkah cek:**
  1. Cari semua `{` di bagian penguraian.
  2. Kalau isi kurung kurawal memuat `|` (daftar pilihan), itu salah notasi: maksudnya memilih satu, tapi ditulis sebagai pengulangan.
  3. Cari juga `n{x}m` yang angkanya tidak masuk akal untuk elemennya.
- **Bukti di Kelompok 4:**
  - `hari = { 1 | 2 | ... | 31 }`, `bulan = { 1 | 2 | … | 12 }`, `tahun = { 2025 | … | 2500 }` (penguraian buktiPeminjaman, dataPengembalianBuku, dll.). Ditulis begini, artinya "hari adalah deretan angka 1, 2, ..., 31 yang berulang", bukan "salah satu dari 1–31".
  - `Pengarang = 1{huruf}3` (penguraian Data Koleksi) berarti nama pengarang hanya 1–3 huruf. Kemungkinan maksudnya 1–3 orang pengarang, yang di entri ditulis `(1{Pengarang}3)`.
- **Rekomendasi:** `Hari = [01 | 02 | ... | 31]` atau `Hari = 2{angka}2` dengan domain 01–31 di tabel elemen. `Pengarang = 1{karakter}50`; jumlah pengarang tetap `1{Pengarang}3` di struktur Data Koleksi.

### Opsi B · VS-16 · Satu elemen didefinisikan berbeda · Sedang
- **Aturan:** Modul 5 §1.8 (satu konsep satu definisi), §1.11 ("format, domain, dan contoh data tidak saling bertentangan").
- **Langkah cek:**
  1. Kelompok 4 menulis ulang definisi elemen di setiap penguraian. Ambil satu elemen (misal `NamaDepan`) dan cari semua kemunculan definisinya.
  2. Bandingkan panjang `n{x}m`, wajib/opsional, dan rentang nilainya.
  3. Bandingkan juga dengan tabel "Mendefinisikan Elemen".
  4. Kalau ada yang beda, itu temuan. Tulis keduanya beserta lokasinya.
- **Bukti di Kelompok 4:**

| Elemen | Definisi 1 | Definisi 2 |
|---|---|---|
| NamaDepan | `1{huruf}20` (buktiPeminjaman, formPendaftaran) | `1{huruf}30` (Data Anggota) |
| NamaBelakang | wajib: `NamaDepan + NamaBelakang` | opsional: `NamaDepan + (NamaBelakang)` (Data Anggota) |
| TotalDenda | `1{angka}6` (infoDenda, buktiPengembalian) | `1{angka}8` (Data Transaksi) |
| tahun | `{ 2025 \| … \| 2500 }` | `{ 2023 \| … \| 2500 }` dan `4{angka}4` |
| Hari | `{ 1 \| ... \| 31 }` | `2{angka}2` (Data Anggota) |

- **Dampak:** nama dengan 25 huruf valid di Data Anggota tapi tidak valid di formulir pendaftaran. Denda Rp1.500.000 (7 digit) bisa disimpan di Data Transaksi, tapi tidak bisa ditampilkan di bukti.
- **Rekomendasi:** definisikan satu kali di tabel elemen, lalu penguraian lain cukup merujuk nama elemennya.

### Opsi C · VS-06 · Nama aliran `triggerStatusBuku` · Sedang
- **Aturan:** Modul 1–3 tabel komponen DFD (Data Flow: "kata benda atau struktur data, bukan aktivitas"); Modul 4 §1.8 ("nama aliran menjelaskan informasi", DFD logis tanpa istilah teknis).
- **Langkah cek:**
  1. Baca semua nama aliran di DFD dan inventaris.
  2. Untuk tiap nama, tanya: apakah nama ini menyebut **informasi apa** yang mengalir, atau menyebut **sinyal/aksi**?
  3. Kata seperti trigger, sinyal, perintah, request, simpan, kirim menandakan aksi/kontrol, sehingga jadi temuan.
- **Bukti di Kelompok 4:** aliran 3.3 → 3.4 bernama `triggerStatusBuku` (inventaris No 15). Penjelasan di entrinya sendiri: "data status mutakhir dari buku yang baru saja dikembalikan". Artinya isinya memang informasi status, tapi namanya menggambarkan pemicu.
- **Rekomendasi:** ganti jadi `statusBukuKembali` atau `pembaruanStatusKoleksi`. Tulis juga ruas kiri strukturnya: `statusBukuKembali = KodeBuku + [Tersedia | Hilang | Rusak]` (sekaligus menutup VS-21).

### Ringkasan pilihan 5 item

| Status | Item |
|---|---|
| Dipakai | VS-10, VS-13, VS-15, VS-17 |
| Ditunda | VS-12 (bagian 4, kita juga kena) |
| Pengganti | pilih satu dari Opsi A (VS-14), B (VS-16), atau C (VS-06) |

Catatan: VS-10, VS-13, dan VS-15 juga terjadi di kamus data kita (bagian 5). Bedanya, perbaikannya sudah tercatat di UC-01 dan RV-M05-12/14/16. Kalau ingin aman total, ganti juga salah satunya dengan opsi yang tersisa.

---

## 7. Isian Tabel Temuan (versi singkat, siap salin)

Format Lampiran C. Bahasa dibuat singkat dan mudah dipahami.

### 4 item yang dipakai

| ID | Artefak | Lokasi | Jenis | Deskripsi Berbasis Bukti | Severitas | Rekomendasi | Status |
|---|---|---|---|---|---|---|---|
| VS-10 | M05 | Inventaris Data | Kelengkapan | Panah dari/ke data store di DFD tidak ada di inventaris. Ada 15 panah store, tidak satu pun tercatat. | Tinggi | Beri nama panah store di DFD, lalu masukkan ke inventaris. | Open |
| VS-13 | M05 | pengajuanPeminjaman, buktiPeminjaman, Data Transaksi | Konsistensi struktur | Jumlah buku per pinjam berbeda-beda: aturan bilang 1 buku, bukti `{KodeBuku}` (banyak), store `1{KodeBuku}5` (1–5). | Tinggi | Tentukan satu batas jumlah buku, pakai sama di semua struktur. | Open |
| VS-15 | M05 | StatusAnggota, StatusKeanggotaan, IDTransaksi, IDPeminjaman, NoIdentitas | Sinonim | Satu hal punya beberapa nama: StatusAnggota vs StatusKeanggotaan, IDTransaksi vs IDPeminjaman. Asal IDAnggota dari NoIdentitas tidak dijelaskan. | Tinggi | Pilih satu nama per hal, nama lain jadi alias. Jelaskan asal IDAnggota. | Open |
| VS-17 | M05 | Tabel elemen: NoTelepon, TanggalJatuhTempo | Contoh vs aturan | Contoh tidak sesuai aturannya: NoTelepon wajib awalan 08 tapi contoh `81234567890`; jatuh tempo 7 hari kerja tapi contoh 19→26 Okt (7 hari biasa, seharusnya 28 Okt). | Sedang | Samakan contoh dengan aturan, atau ubah aturannya. | Open |

### Pilih satu pengganti VS-12

| ID | Artefak | Lokasi | Jenis | Deskripsi Berbasis Bukti | Severitas | Rekomendasi | Status |
|---|---|---|---|---|---|---|---|
| VS-14 | M05 | Penguraian hari, bulan, tahun, Pengarang | Notasi | Pilihan ditulis pakai `{}` (artinya berulang), contoh `hari = {1 \| 2 \| ... \| 31}`. Seharusnya `[]`. `Pengarang = 1{huruf}3` berarti nama cuma 1–3 huruf. | Sedang | Pakai `[]` untuk pilihan. Pengarang ditulis `1{karakter}50`. | Open |
| VS-16 | M05 | NamaDepan, NamaBelakang, TotalDenda, tahun | Domain beda | Elemen yang sama ditulis beda: NamaDepan 20 vs 30 huruf, NamaBelakang wajib vs opsional, TotalDenda 6 vs 8 digit, tahun mulai 2025 vs 2023. | Sedang | Tulis definisi sekali di tabel elemen, yang lain cukup merujuk. | Open |
| VS-06 | M04 | DFD L1 Proses 3: aliran 3.3 → 3.4 | Penamaan | Nama `triggerStatusBuku` menggambarkan aksi/pemicu, padahal isinya data status buku. Nama aliran harus kata benda. | Sedang | Ganti jadi `statusBukuKembali`. | Open |

---

## 8. Opsi Tambahan Severitas Tinggi (M05) · ditambahkan 2026-10-22

Temuan Tinggi yang murni M05 hanya tiga, dan semuanya sudah dipakai (VS-10, VS-13, VS-15). Temuan Tinggi lain yang **memakai bukti kamus data M05** adalah VS-04: struktur data yang masuk ke 3.2 tidak cukup untuk menghasilkan output 3.2.

### Opsi D · VS-04 · Data masuk tidak cukup untuk menghitung denda (gray hole) · Tinggi
- **Aturan:**
  - Modul 4 §1.6, gray hole: output tidak dapat dijelaskan dari input.
  - Modul 5 §1.10: setiap elemen yang dipakai harus terlacak ke definisi dan sumbernya.
  - Modul 5 Langkah 5.1: telusuri input–output satu proses ke kamus data.
- **Langkah cek:**
  1. Pilih proses 3.2 Hitung Denda. Dari DFD L1-P3, inputnya hanya `statusKeterlambatan` (dari 3.1). 3.2 tidak membaca data store.
  2. Buka struktur input di kamus data: `statusKeterlambatan = [Terlambat | Tepat waktu]`. Isinya hanya satu nilai status.
  3. Buka struktur output: `infoDenda = IDTransaksi + IDAnggota + NamaAnggota + TerlambatHari + TotalDenda`.
  4. Tanya untuk tiap elemen output: dari mana 3.2 mendapatkannya? `TerlambatHari` butuh TanggalJatuhTempo dan TanggalKembali, sedangkan `IDTransaksi`, `IDAnggota`, `NamaAnggota` juga tidak ada di input. Tidak ada satu pun yang tersedia, jadi itu temuan.
- **Dampak:** proses 3.2 tidak bisa ditulis process spec-nya di M06, karena datanya tidak ada.
- **Aman untuk kita?** Untuk kasus ini aman. Aliran kita yang setara, `dataKeterlambatan` (3.2 → 3.3), sudah membawa `TanggalJatuhTempo + TanggalKembali + JumlahHariTerlambat`. Tapi kita sendiri punya gray hole lain di 3.1 dan 3.3 (AUD-B-07, AUD-B-11). Itu jenis temuan yang sama, jadi siapkan jawabannya kalau Kelompok 4 membalikkan: "sudah tercatat di audit internal, perbaikan berupa flow baca `peminjamAktif`".

| ID | Artefak | Lokasi | Jenis | Deskripsi Berbasis Bukti | Severitas | Rekomendasi | Status |
|---|---|---|---|---|---|---|---|
| VS-04 | M05 + M04 | Proses 3.2 Hitung Denda; struktur statusKeterlambatan & infoDenda | Gray hole | Input 3.2 hanya `statusKeterlambatan = [Terlambat \| Tepat waktu]`, tapi outputnya `infoDenda` berisi IDTransaksi, IDAnggota, NamaAnggota, TerlambatHari, TotalDenda. Data itu tidak ada di input, dan 3.2 tidak membaca data store. | Tinggi | Tambahkan IDTransaksi, IDAnggota, TanggalJatuhTempo, TanggalKembali ke `statusKeterlambatan`, atau beri 3.2 akses baca Data Transaksi. | Open |
