# M04 — Dekomposisi, Balancing, dan Audit DFD (Siap Timpa)

Sumber: `baselines/PRPL_M04_2B_RajinBelajar_DFDDecomposition.pdf` (file kerja `progress/PRPL_M04_2B_RajinBelajar_DFDDecomposition.docx`). Urutan dan judul bagian sama dengan dokumen; salin per bagian lalu timpa. Bagian bertanda **(baru)** belum ada di dokumen. Daftar perubahan ada di [Catatan Perubahan](#catatan-perubahan) paling bawah.

Semua gambar diekspor ulang dari `Silapus Latest.bpm`.

---

## Mengaudit Baseline DFD

Gambar tetap (DFD Level 0 sebelum koreksi).

## Daftar Koreksi

| NO | Nama Alur | Dari ke | Menjadi | Alasan |
|---|---|---|---|---|
| 1 | Konfirmasi Denda | Petugas Perpustakaan ke Proses 3 | catatanDenda | Karena yang dikirim petugas adalah catatan pembayaran denda, bukan konfirmasi dari bagian keuangan |
| 2 | Info katalog / ketersediaan | Proses 2 ke Anggota Perpustakaan | informasiKoleksiBuku | Karena Anggota Perpustakaan melakukan Data pencarian sehingga penamaan yang cocok adalah informasi koleksi buku |
| 3 | kriteriaPencarian | Proses 2 ke Data koleksi | Dihapus | Karena kriteria pencarian tidak perlu disimpan; Proses 2 hanya membaca Data koleksi saat pencarian |
| 4 | simpanData | Proses 1 ke Data anggota | dataAnggota (dua arah) | Karena nama aliran harus kata benda, dan Proses 1 juga perlu membaca Data anggota untuk mencegah pendaftaran ganda |
| 5 | statusPerpanjang | Proses 3 ke Anggota Perpustakaan | statusPerpanjangan | Karena nama aliran harus kata benda yang lengkap dan sama dengan diagram anak |
| 6 | Data anggota, Data koleksi, Transaksi FIsik | Nama data store | Data Anggota, Data Koleksi, Transaksi Fisik | Karena penulisan nama data store harus seragam |
| 7 | Membuat Laporan Transaksi Fisik | Nama Proses 4 | Membuat Laporan Sirkulasi | Karena laporan merekap sirkulasi, koleksi, dan denda, dan sama dengan nama di Modul 3 |
| 8 | (belum ada) | Proses 2 ke Petugas Perpustakaan | statusPengelolaanKoleksi | Karena petugas perlu menerima hasil pengelolaan koleksi, termasuk alasan bila gagal |

## DFD Level 0 Setelah Koreksi **(baru)**

Gambar: ekspor diagram **DFD Level 0** dari `Silapus Latest.bpm`.

## Menentukan Proses yang Didekomposisi

Tujuan proses induk
- 1. Mengelola Keanggotaan: mengelola pendaftaran dan status keaktifan anggota perpustakaan.
- 2. Mengelola Katalog Koleksi: menyediakan informasi katalog dan memperbarui data koleksi perpustakaan.
- 3. Memproses Sirkulasi dan Denda: mencatat dan memvalidasi peminjaman, pengembalian, dan perpanjangan koleksi fisik serta menghitung denda keterlambatan.
- 4. Membuat Laporan Sirkulasi: menyusun laporan bulanan sirkulasi dan denda untuk Kepala Perpustakaan.

| Proses Induk | Alasan Diuraikan atau Tidak | Calon Proses Anak | Risiko Pemodelan |
|---|---|---|---|
| 1 Mengelola Keanggotaan | Tidak diuraikan, karena aturan bisnisnya sedikit (data pendaftaran harus lengkap dan anggota harus terverifikasi aktif), hanya memiliki satu tujuan yaitu mengelola data anggota, hanya mengakses satu data store, dan input-outputnya sudah jelas. | Primitif | Logika terlalu sederhana untuk dipecah lagi, jika dilakukan dekomposisi lagi akan membingungkan untuk membaca diagram |
| 2 Mengelola Katalog Koleksi | Diuraikan, karena menggabungkan dua tujuan berbeda, yaitu pencarian katalog oleh anggota (hanya membaca) dan pengelolaan koleksi baru oleh petugas (menulis data), dan masing-masing punya aturan sendiri. | 2.1 Mencari Katalog Buku<br>2.2 Mengelola Data Koleksi | Aliran “Kriteria Pencarian” dan “Simpan Data Koleksi” pada Level 1 tidak ada di Level 0 (di sana hanya “Data Buku” dua arah), sehingga diagram tidak balance. Nama aliran tidak konsisten (“Data Buku” dan “Data koleksi” untuk store yang sama). Proses 2.2 dapat menjadi sekadar memindahkan data jika tidak ada aturan validasi. |
| 3 Memproses Sirkulasi dan Denda | Diuraikan, karena melakukan beberapa perubahan data berbeda (peminjaman, pengembalian, perpanjangan, perhitungan denda), memuat banyak aturan bisnis dan pengecualian, serta mengakses 3 data store dengan tujuan berbeda. | 3.1 Memproses Peminjaman Buku<br>3.2 Memproses Pengembalian Buku<br>3.3 Menghitung dan Mencatat Denda<br>3.4 Memperpanjang Peminjaman | Dirasa akan terjadi Gray Hole karena belum ada spesifikasi pada aturan bisnis peminjaman, pengembalian, dan denda tercampur dalam satu proses tunggal. |
| 4 Membuat Laporan Sirkulasi | Tidak diuraikan, karena transformasinya hanya satu jalur (mengambil data, merekap, menyusun laporan bulanan), aturan bisnisnya sedikit, hanya membaca data store untuk satu tujuan, dan input-outputnya sudah jelas. | Primitif | Prosesnya sudah linear dan juga sudah mudah dibaca, jika dipecah lagi malah akan memindahkan data saja |

## Membuat Diagram Anak

**Proses 2**

Gambar: diagram sebelum perbaikan (tetap).

Proses 2 setelah perbaikan metode balancing

Gambar: ekspor diagram **DFD Level 1 Proses 2** dari `Silapus Latest.bpm`.

**Proses 3**

Gambar: ekspor diagram **DFD Level 1 Proses 3** dari `Silapus Latest.bpm`.

## Mengisi Matriks Balancing Proses 2

| No. | Aliran Pada Induk | Arah | Aliran Ekuivalen pada Anak | Status | Catatan |
|---|---|---|---|---|---|
| 1 | dataPencarian (Anggota → 2.0) | Masuk | dataPencarian (Anggota → 2.1) | Balance | Nama, arah, dan makna sama. |
| 2 | dataKoleksiBaru (Petugas → 2.0) | Masuk | dataKoleksiBaru (Petugas → 2.2) | Balance | Nama, arah, dan makna sama. |
| 3 | dataKoleksiBuku (D2 → 2.0, sisi baca) | Masuk | dataKoleksiBuku (D2 → 2.1) | Balance | Di induk berupa panah dua arah. Sisi baca muncul di 2.1. |
| 4 | informasiKoleksiBuku (2.0 → Anggota) | Keluar | informasiKoleksiBuku (2.1 → Anggota) | Balance | Nama, arah, dan makna sama. |
| 5 | dataKoleksiBuku (2.0 → D2, sisi tulis) | Keluar | dataKoleksiBuku (2.2 → D2) | Balance | Di induk berupa panah dua arah. Sisi tulis muncul di 2.2; 2.2 juga membaca D2 untuk memeriksa kode buku. |
| 6 | statusPengelolaanKoleksi (2.0 → Petugas) | Keluar | statusPengelolaanKoleksi (2.2 → Petugas) | Balance | Nama, arah, dan makna sama. |

## Mengisi Matriks Balancing Proses 3

| No. | Aliran Pada Induk | Arah | Aliran Ekuivalen pada Anak | Status | Catatan |
|---|---|---|---|---|---|
| 1 | catatanDenda (Petugas Perpustakaan → 3) | Masuk | catatanDenda (Petugas Perpustakaan → 3.3) | Balance | Nama dan arah sama. |
| 2 | statusTransaksiDanBukti (3 → Petugas Perpustakaan) | Keluar | statusTransaksiDanBukti (3.1 → Petugas Perpustakaan)<br>statusTransaksiDanBukti (3.2 → Petugas Perpustakaan) | Balance | Nama dan arah sama, muncul di dua proses anak. |
| 3 | buktiPengembalianDanDenda (3 → Petugas Perpustakaan) | Keluar | buktiPengembalianDanDenda (3.3 → Petugas Perpustakaan) | Balance | Nama dan arah sama. |
| 4 | dataTransaksiFisik (Petugas Perpustakaan → 3) | Masuk | dataTransaksiPeminjaman (Petugas Perpustakaan → 3.1)<br>dataTransaksiPengembalian (Petugas Perpustakaan → 3.2) | Balance | Aliran dipecah di DFD anak; strukturnya didefinisikan di kamus data: dataTransaksiFisik = [dataTransaksiPeminjaman \| dataTransaksiPengembalian]. |
| 5 | permintaanPerpanjangan (Anggota Perpustakaan → 3) | Masuk | permintaanPerpanjangan (Anggota Perpustakaan → 3.4) | Balance | Nama dan arah sama. |
| 6 | statusPerpanjangan (3 → Anggota Perpustakaan) | Keluar | statusPerpanjangan (3.4 → Anggota Perpustakaan) | Balance | Nama dan arah sama. |
| 7 | pembaruanEksemplar (3 → Data Koleksi) | Keluar | pembaruanEksemplar (3.1 → Data Koleksi)<br>pembaruanEksemplar (3.2 → Data Koleksi) | Balance | Nama dan arah sama. |
| 8 | dataEksemplar (Data Koleksi → 3) | Masuk | dataEksemplar (Data Koleksi → 3.1) | Balance | Nama dan arah sama. |
| 9 | statusAnggota (Data Anggota → 3) | Masuk | statusAnggota (Data Anggota → 3.1)<br>statusAnggota (Data Anggota → 3.4) | Balance | Aliran dipecah ke dua proses di DFD anak, ekuivalen. |
| 10 | dataPeminjaman (3 → Transaksi Fisik) | Keluar | dataPeminjamanBaru (3.1 → Transaksi Fisik)<br>pembaruanPengembalian (3.2 → Transaksi Fisik)<br>dataDenda (3.3 → Transaksi Fisik)<br>pembaruanMasaPinjam (3.4 → Transaksi Fisik) | Balance | Aliran dipecah per aksi; strukturnya didefinisikan di kamus data: dataPeminjaman = [dataPeminjamanBaru \| pembaruanPengembalian \| dataDenda \| pembaruanMasaPinjam]. |
| 11 | peminjamAktif (Transaksi Fisik → 3) | Masuk | peminjamAktif (Transaksi Fisik → 3.1)<br>peminjamAktif (Transaksi Fisik → 3.2)<br>peminjamAktif (Transaksi Fisik → 3.3)<br>peminjamAktif (Transaksi Fisik → 3.4) | Balance | Nama dan arah sama, dibaca empat proses anak. |
| 12 | (tidak ada di induk) | - | dataKeterlambatan (3.2 → 3.3) | Balance | Merupakan aliran data internal antar proses di level anak, tidak perlu muncul di induk. |

## Hasil Peer Review dari Kelompok Lain

| ID | Lokasi | Temuan | Respons | Tindakan | Status |
|---|---|---|---|---|---|
| PR-01 | DFD Level 1 Proses 2: 2.1 → Data Koleksi | Kriteria Pencarian disimpan dalam data koleksi (apakah memang menyimpan kriteria pencarian?). | Diterima | Aliran Kriteria Pencarian dihapus; 2.1 hanya membaca dataKoleksiBuku. | Closed |
| PR-02 | DFD Level 1 Proses 2: 2.2 → Data Koleksi | Aliran "Simpan Data Koleksi" menggunakan kata kerja. | Diterima | Diganti menjadi dataKoleksiBuku (kata benda, sama dengan Level 0). | Closed |
| PR-03 | DFD Level 0 vs Level 1 Proses 2 | Nama berbeda: "Info buku" di Level 0, "Info Katalog/Ketersediaan" di 2.1. | Diterima | Keduanya menjadi informasiKoleksiBuku. | Closed |
| PR-04 | DFD Level 0 vs Level 1 Proses 2 | "Data Buku" di Level 0 dipecah menjadi "Simpan Data Koleksi" (2.2) dan "Data Buku" (2.1). | Diterima | Level 0 dataKoleksiBuku dua arah; 2.1 membaca dan 2.2 menulis dengan nama yang sama. | Closed |
| PR-05 | DFD Level 0 vs 3.4 | Nama berbeda: "Status Perpanjangan" vs "Status permintaan". | Diterima | Keduanya menjadi statusPerpanjangan. | Closed |
| PR-06 | DFD Level 0 vs 3.1 | Nama berbeda: "Data Peminjaman" vs "Data Peminjam". | Diterima | Lihat PR-08. | Closed |
| PR-07 | DFD Level 0 vs 3.1 dan 3.2 | "Data transaksi fisik" dipecah menjadi data transaksi peminjaman dan pengembalian. | Ditolak sebagian | Pemecahan dipertahankan karena sah selama strukturnya didefinisikan di kamus data: dataTransaksiFisik = [dataTransaksiPeminjaman \| dataTransaksiPengembalian]. | Closed |
| PR-08 | DFD Level 1 Proses 3 → Transaksi Fisik | Aliran ke data store 3.1–3.4 seluruhnya bernama "Data peminjam". | Diterima | Dibedakan per aksi: dataPeminjamanBaru (3.1), pembaruanPengembalian (3.2), dataDenda (3.3), pembaruanMasaPinjam (3.4); dataPeminjaman di Level 0 didefinisikan sebagai gabungannya di kamus data. | Closed |

## Melakukan Peer Review

DFD lvl 0 — gambar tetap
DFD Level 1 Proses 2 — gambar tetap
DFD Level 1 Proses 3 — gambar tetap

| Proses | Interpretasi Tujuan | Sintaks | Semantik | Balancing | Keterbacaan |
|---|---|---|---|---|---|
| DFD Lvl 0 Proses 2 | Bertujuan untuk menerima pengajuan pinjaman buku dari anggota, memeriksa data anggota, stok, dan mencatat peminjaman baru | ✗ | ✓ | - | ✓ |
| Lvl 1 proses 2 | Mendekomposisi Proses 2 menjadi 3 sub proses:<br>2.1. Untuk memvalidasi kelayakan anggota<br>2.2. Untuk melakukan cek ketersediaan buku fisik<br>2.3. Serta pencatatan transaksi dan pencetakan bukti peminjaman ke anggota | ✗ | ✗ | ✓ | ✓ |
| Lvl 1 proses 3 | Mendekomposisi Proses 3 menjadi 4 sub proses:<br>3.1. Memverifikasi batas tanggal pengembalian buku<br>3.2. Menghitung tarif denda jika terlambat<br>3.3. Menyimpan data pengembalian<br>3.4. Mengembalikan status buku menjadi tersedia jika sudah dikembalikan | ✗ | ✗ | ✗ | ✓ |

Catatan:
- DFD Level 0 - Proses 2: Sintaks tidak dicentang karena aliran data penghubung ke seluruh data store tidak diberi nama.
- DFD Level 1 - Proses 2: Sintaks tidak dicentang karena aliran masuk dan keluar ke seluruh data store tidak memiliki nama. Semantik tidak dicentang karena pada proses 2.1 tidak ada output ke entitas Anggota, jika seperti itu sistem tidak dapat menyampaikan hasil validasi kelayakan anggota.
- DFD Level 1 - Proses 3: Sintaks tidak dicentang karena aliran ke data store tidak memiliki nama. Semantik tidak dicentang karena terjadi gray hole pada proses 3.2 dan 3.3. Balancing tidak dicentang karena akses ke Data Koleksi pada DFD Level 0 dua arah, padahal di DFD anak hanya ada aliran tulis dari 3.4.

## Lembar Audit DFD

| ID | Komponen | Lokasi | Temuan Berbasis Bukti | Dampak | Tindakan Koreksi | Status |
|---|---|---|---|---|---|---|
| AUD - 01 | Aliran Data (simpanData) | Baseline DFD (Level 0): Proses 1 Mengelola Keanggotaan → Data Store 1 Data anggota | Nama aliran data menuju data store ditulis simpanData yang menggunakan kata kerja "simpan" dan istilah yang terlalu umum "Data". | Melanggar aturan sintaks penamaan DFD dan kamus data karena aliran data wajib berupa kata benda spesifik yang merepresentasikan informasi, bukan aktivitas/proses. | Ubah nama aliran simpanData pada Level 0 menjadi kata benda spesifik, yaitu dataAnggota. | Closed |
| AUD - 02 | Aliran Data (kriteriaPencarian) | DFD Anak Proses 2: Proses 2.1 Mencari Katalog Buku → Data Store 2 Data koleksi | Terdapat panah aliran kriteriaPencarian yang mengarah masuk ke Data Store 2 Data koleksi, serta tidak memiliki padanan di Level 0. | Panah menuju data store bermakna menulis/mengubah data, padahal Proses 2.1 hanya membaca katalog (read-only), serta menyebabkan diagram tidak balance dengan Level 0. | Hapus aliran kriteriaPencarian menuju Data Store 2 Data koleksi sehingga Proses 2.1 hanya menerima aliran baca dataKoleksiBuku dari D2. | Closed |
| AUD - 03 | Proses 3.4 & Aliran Data ke 3 Transaksi Fisik | DFD Anak Proses 3: Proses 3.4 Memperpanjang Peminjaman ↔ Data Store 3 Transaksi Fisik | Kedua panah antara Proses 3.4 dan Data Store 3 Transaksi Fisik (Data peminjam dan Info peminjam aktif) mengarah masuk ke Proses 3.4. | Proses 3.4 hanya membaca data tanpa memiliki aliran keluar (write) untuk menyimpan pembaruan perpanjangan peminjaman ke Data Store 3 Transaksi Fisik. | Perbaiki arah panah agar satu panah masuk dari D3 ke 3.4 untuk membaca (peminjamAktif) dan satu panah keluar dari 3.4 ke D3 untuk menulis (pembaruanMasaPinjam). | Closed |
| AUD - 04 | Proses 3.1 & Aliran Data dari 3 Transaksi Fisik | DFD Anak Proses 3: Proses 3.1 Memproses Peminjaman Buku ← Data Store 3 Transaksi Fisik | Proses 3.1 harus menolak peminjaman bila kuota penuh atau anggota masih memiliki denda, tetapi 3.1 tidak membaca Data Store 3 Transaksi Fisik. | Output penolakan tidak dapat dijelaskan dari input (gray hole). | Tambahkan aliran baca peminjamAktif dari D3 ke 3.1. | Closed |
| AUD - 05 | Proses 3.3 & Aliran Data dari 3 Transaksi Fisik | DFD Anak Proses 3: Proses 3.3 Menghitung dan Mencatat Denda ← Data Store 3 Transaksi Fisik | Proses 3.3 harus memeriksa jumlah pembayaran sama dengan total denda, tetapi 3.3 tidak membaca Data Store 3 Transaksi Fisik saat pembayaran dilakukan terpisah dari pengembalian. | Validasi pembayaran denda tidak memiliki sumber data (gray hole). | Tambahkan aliran baca peminjamAktif dari D3 ke 3.3. | Closed |
| AUD - 06 | Aliran Data (dataAnggota) | Baseline DFD (Level 0): Proses 1 Mengelola Keanggotaan ↔ Data Store 1 Data Anggota | Proses 1 harus menolak NIM/NIP yang sudah terdaftar dan memperbarui status dari Sistem Akademik, tetapi aliran dataAnggota hanya menulis ke Data Store 1. | Aturan pendaftaran ganda dan EV-09 tidak memiliki sumber data. | Jadikan aliran dataAnggota dua arah (baca dan tulis). | Closed |
| AUD - 07 | Proses 2.2 & Aliran Data dataKoleksiBuku | DFD Anak Proses 2: Proses 2.2 Mengelola Data Koleksi ↔ Data Store 2 Data Koleksi | Proses 2.2 harus memastikan kode buku unik dan eksemplar yang dihapus tidak sedang dipinjam, tetapi 2.2 hanya menulis ke Data Store 2. | Aturan keunikan kode buku tidak memiliki sumber data. | Jadikan aliran dataKoleksiBuku pada 2.2 dua arah (baca dan tulis). | Closed |
| AUD - 08 | Proses 2.2 & Petugas Perpustakaan | DFD Level 0 Proses 2 dan DFD Anak Proses 2.2 → Petugas Perpustakaan | Proses 2.2 menerima dataKoleksiBaru dari Petugas, tetapi tidak ada aliran balik ke Petugas sehingga data yang ditolak tidak bisa diberitahukan. | Jalur gagal EV-08 berakhir tanpa output. | Tambahkan aliran statusPengelolaanKoleksi dari Proses 2 / 2.2 ke Petugas Perpustakaan (juga di Context Diagram). | Closed |

## Revision History **(baru)**

| Versi | Tanggal | Artefak atau Bagian | Perubahan | Alasan | Penyusun | Reviewer |
|---|---|---|---|---|---|---|
| 0.1 | 2026-10-19 | DFD Level 0, Level 1 Proses 2 & 3 | Dekomposisi awal Proses 2 dan Proses 3, matriks balancing, lembar audit | Modul 4 | Kelompok 6 | |
| 0.2 | 2026-10-19 | DFD Level 0, Level 1 Proses 2 & 3 | Penyeragaman nama aliran (camelCase), perbaikan nama sesuai peer review dan audit internal, penghapusan kriteriaPencarian | Hasil peer review (PR-01–PR-08) dan audit internal | Wildan (dibantu AI) | |
| 0.3 | 2026-10-26 | DFD Level 0, Level 1 Proses 2 & 3; Daftar Koreksi, Matriks, Lembar Audit | dataAnggota dua arah; peminjamAktif ke 3.1 dan 3.3; dataKoleksiBuku pada 2.2 dua arah; aliran baru statusPengelolaanKoleksi; Proses 4 menjadi Membuat Laporan Sirkulasi; matriks dan audit diperbarui | AUD-04 – AUD-08 | Wildan (dibantu AI) | |

## Log Kontribusi Individu **(baru)**

| Nama atau NIM | Peran | Aktivitas | Durasi | Artefak atau Bukti | Refleksi Singkat |
|---|---|---|---|---|---|
| Wildan M Zaki (251511062) | | | | | |
| Sahizidan Lukman Hakim (251511060) | | | | | |
| M. Rayhan Maulana Farid (251511054) | | | | | |
| Irfan Ardiansah Sulaeman (251511043) | | | | | |
| Aisy Fathryan Siswandar (251511033) | | | | | |

## Pertanyaan Refleksi **(baru)**

1. **Perubahan apa pada DFD Level 0 yang paling berdampak terhadap diagram anak?**
   Penyeragaman nama aliran data. Setelah nama di Level 0 ditetapkan (misalnya statusPerpanjangan, peminjamAktif, dataPeminjaman), seluruh aliran di diagram anak harus mengikuti nama yang sama agar balance. Penghapusan kriteriaPencarian juga mengubah Proses 2.1 menjadi proses yang hanya membaca Data Koleksi.

2. **Apa bukti bahwa proses terbawah sudah cukup rinci untuk dibuatkan process specification?**
   Setiap proses anak hanya punya satu tujuan, input dan outputnya dapat disebutkan satu per satu, dan data store yang dibaca atau ditulis jelas. Contohnya, 3.1 hanya memproses peminjaman: input dataTransaksiPeminjaman, statusAnggota, dataEksemplar, peminjamAktif; output statusTransaksiDanBukti, pembaruanEksemplar, dataPeminjamanBaru. Logikanya dapat ditulis sebagai decision table tanpa perlu dipecah lagi.

3. **Aliran apa yang dipecah menjadi komponen, dan bagaimana definisinya menjaga balancing?**
   dataTransaksiFisik dipecah menjadi dataTransaksiPeminjaman dan dataTransaksiPengembalian, sedangkan dataPeminjaman dipecah menjadi dataPeminjamanBaru, pembaruanPengembalian, dataDenda, dan pembaruanMasaPinjam. Keduanya didefinisikan di kamus data sebagai struktur pilihan [ ... | ... ], sehingga aliran induk terbukti terdiri dari aliran anak dan diagram tetap balance.

---

## Catatan Perubahan

Perubahan **isi** (karena balancing/konsistensi) ditandai ★. Sisanya hanya typo/tanda baca.

| Bagian | Perubahan | Alasan |
|---|---|---|
| Mengaudit Baseline DFD | Tidak berubah | — |
| Daftar Koreksi | ★ No 1: Menjadi "Catatan Denda" → "catatanDenda"; Alasan diganti (sebelumnya "konfirmasi denda dilakukan oleh bagian keuangan bukan petugas") | Bagian Keuangan tidak ada di CD/DFD/stakeholder (AUD-A-01, AUD-D-01) |
| | ★ No 2: Menjadi "Info buku" → "informasiKoleksiBuku" | Sama dengan nama di DFD |
| | ★ No 3: "–" (dipertahankan) → "Dihapus" + alasan baru | Bertentangan dengan AUD-02 dan peer review PR-01 |
| | ★ No 4–8 baru (simpanData, statusPerpanjang, nama store, nama Proses 4, aliran baru statusPengelolaanKoleksi) | Semua perubahan sejak baseline harus tercatat |
| DFD Level 0 Setelah Koreksi | ★ Bagian baru (gambar) | Dokumen hanya punya gambar Level 0 sebelum koreksi |
| Tujuan proses induk | ★ "Memproses Transaksi Fisik dan Denda" → "Memproses Sirkulasi dan Denda"; ★ "Membuat Laporan Transaksi Fisik: menyusun laporan bulanan transaksi fisik" → "Membuat Laporan Sirkulasi: menyusun laporan bulanan sirkulasi dan denda" | Sama dengan DFD dan M03 |
| Tabel keputusan dekomposisi | "jika dilakukan ; dekomposisi lagi  akan" dirapikan. ★ Nama proses 3 & 4 dan nama calon anak 3.1–3.4 disamakan dengan DFD | Typo; konsistensi nama |
| Membuat Diagram Anak | "seletah" → "setelah"; ★ gambar Proses 2 & 3 diekspor ulang | DFD terbaru |
| Matriks Proses 2 | ★ Semua baris pakai nama baku; baris 4 & 5 jadi Balance; ★ baris 6 baru (statusPengelolaanKoleksi); catatan baris 5 + 2.2 membaca D2 | Nama sudah diseragamkan (PR-02..04); AUD-07, AUD-08 |
| Matriks Proses 3 | ★ Semua baris pakai nama baku; baris 2, 3, 6, 10, 11 jadi Balance; ★ baris 4 & 10 merujuk definisi kamus data; ★ baris 11 + 3.1 dan 3.3 | AI-02..11, PR-07/08, AUD-04/05 |
| Hasil Peer Review dari Kelompok Lain | ★ Placeholder "… hasil evaluasi dari kelompok" diganti tabel PR-01..PR-08 + respons | Modul 4 §3.5: setiap temuan diberi respons (AUD-D-03) |
| Melakukan Peer Review | "memeriksan", "Medekompossisi", "Memverivikasi", "tarid", "pemngembalian" diperbaiki. ★ Kolom checklist diisi + catatan | Kolom kosong (AUD-D-04). Balancing L1 Proses 2 dicentang karena DFD Level 0 Kelompok 4 versi terbaru sudah dua arah ke Data Koleksi |
| Lembar Audit DFD | ★ Status "Open / Closed" → "Closed"; ★ nama aliran disamakan (simpanData, kriteriaPencarian, dataKoleksiBuku, peminjamAktif, pembaruanMasaPinjam); ★ AUD-04..08 baru | Status nyata (AUD-D-02); perubahan DFD 2026-10-26 |
| Revision History, Log Kontribusi, Refleksi | ★ Bagian baru | Wajib menurut Modul 4 Bagian IV dan aturan kerja Batch 2 (AUD-D-05, AUD-D-06). Kolom Reviewer dan Log Kontribusi diisi kelompok |

**Perubahan di `Silapus Latest.bpm` (2026-10-26, sudah diterapkan, backup di `_backup/`):** `dataAnggota` dua arah; `peminjamAktif` D3 → 3.1 dan D3 → 3.3; `dataKoleksiBuku` di 2.2 dua arah; aliran baru `statusPengelolaanKoleksi` (Proses 2 → Petugas di Level 0, 2.2 → Petugas di Level 1); nama Proses 4 → Membuat Laporan Sirkulasi. Empat panah baru posisinya perlu dirapikan di PowerDesigner sebelum diekspor.

**Butuh dari M05 supaya matriks baris 4 & 10 sah:** definisi `dataTransaksiFisik` dan `dataPeminjaman` sebagai struktur pilihan. Lihat [`KEBUTUHAN-DARI-M05.md`](KEBUTUHAN-DARI-M05.md).
