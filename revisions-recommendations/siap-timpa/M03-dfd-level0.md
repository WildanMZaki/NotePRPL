# M03 — DFD Level 0 (Siap Timpa)

Sumber: `baselines/PRPL_M03_2B_RajinBelajar_DFD-2.pdf`. Urutan dan judul bagian sama dengan dokumen; salin per bagian lalu timpa. Daftar perubahan ada di [Catatan Perubahan](#catatan-perubahan) paling bawah.

---

## Identifikasi Event

Identik dengan M02. Salin bagian **IDENTIFIKASI EVENT** dari [`M02-event-context.md`](M02-event-context.md#identifikasi-event).

## EVENT TABLE

Identik dengan M02. Salin **Event Number 1 s.d. 9** dari [`M02-event-context.md`](M02-event-context.md#event-table).

## Context Diagram

Identik dengan M02. Ganti label sesuai tabel **CONTEXT DIAGRAM** di [`M02-event-context.md`](M02-event-context.md#context-diagram).

## Pengelompokan Event

Berdasarkan objek bisnis, data yang dikelola, dan tujuan proses.

| Process ID | Nama Kandidat Process | Event yang Ditangani | Alasan Pengelompokan | Data Store Kandidat |
|---|---|---|---|---|
| 1.0 | Mengelola Keanggotaan | EV-01, EV-09 | Membuat dan memperbarui data anggota, dan keduanya berinteraksi dengan Sistem Akademik | D1 Data Anggota |
| 2.0 | Mengelola Katalog Koleksi | EV-02, EV-08 | Mengakses data master koleksi buku: EV-08 mengisi dan mengubah katalog, EV-02 mencari dan menampilkannya. | D2 Data Koleksi |
| 3.0 | Memproses Sirkulasi dan Denda | EV-03, EV-04, EV-05 | Siklus transaksi pada objek yang sama: peminjaman, perpanjangan, dan pengembalian mengubah transaksi peminjaman dan status eksemplar. | D3 Transaksi Fisik |
| 4.0 | Membuat Laporan Sirkulasi | EV-06, EV-07 | Menghasilkan laporan bulanan dari data sirkulasi, koleksi, dan denda | - (membaca D2 Data Koleksi dan D3 Transaksi Fisik) |

## Kerangka DFD Level 0

Ganti gambar dengan ekspor diagram **DFD Level 0** dari `Silapus Latest.bpm`.

## Mendefinisikan Proses

| Process ID | Nama | Tujuan | Input | Output | Data Store dibaca | Data Store diubah | Event |
|---|---|---|---|---|---|---|---|
| 1.0 | Mengelola Keanggotaan | Memvalidasi keaktifan mahasiswa ke Sistem Akademik dan mencatat data anggota baru ke basis data | dataPendaftaran, statusKeaktifan | statusPendaftaran, dataVerifikasi | Data Anggota | Data Anggota | EV-01, EV-09 |
| 2.0 | Mengelola Katalog Koleksi | Mengelola katalog buku dan menyajikan informasi ketersediaan buku | dataPencarian, dataKoleksiBaru | informasiKoleksiBuku, statusPengelolaanKoleksi | Data Koleksi | Data Koleksi | EV-02, EV-08 |
| 3.0 | Memproses Sirkulasi dan Denda | Memproses transaksi sirkulasi fisik, memperbarui status eksemplar, mengkalkulasi denda keterlambatan, dan perpanjangan | dataTransaksiFisik, permintaanPerpanjangan, catatanDenda | statusTransaksiDanBukti, buktiPengembalianDanDenda, statusPerpanjangan | Data Anggota, Data Koleksi, Transaksi Fisik | Data Koleksi, Transaksi Fisik | EV-03, EV-04, EV-05 |
| 4.0 | Membuat Laporan Sirkulasi | Merekap data sirkulasi, koleksi, dan denda bulanan untuk menyajikan laporan periodik bagi Kepala Perpustakaan. | permintaanLaporan | laporanBulanan | Data Koleksi, Transaksi Fisik | - | EV-06, EV-07 |

## Matriks Balancing Context Diagram ke DFD Level 0

| Entitas Eksternal | Aliran Data pada Context Diagram | Arah Aliran | Diproses oleh (DFD Level 0) | Aliran Data pada DFD Level 0 | Status Balancing | Catatan Penyesuaian |
|---|---|---|---|---|---|---|
| Anggota | dataPendaftaran | Masuk ( → ) | 1.0 | dataPendaftaran | Balanced | Persis sesuai Context. |
| Anggota | statusPendaftaran | Keluar ( ← ) | 1.0 | statusPendaftaran | Balanced | Persis sesuai Context. |
| Anggota | dataPencarian | Masuk ( → ) | 2.0 | dataPencarian | Balanced | Persis sesuai Context. |
| Anggota | informasiKoleksiBuku | Keluar ( ← ) | 2.0 | informasiKoleksiBuku | Balanced | Persis sesuai Context. |
| Anggota | permintaanPerpanjangan | Masuk ( → ) | 3.0 | permintaanPerpanjangan | Balanced | Persis sesuai Context. |
| Anggota | statusPerpanjangan | Keluar ( ← ) | 3.0 | statusPerpanjangan | Balanced | Memuat tanggal jatuh tempo baru. |
| Petugas Perpustakaan | dataTransaksiFisik | Masuk ( → ) | 3.0 | dataTransaksiFisik | Balanced | Mencakup pinjam & kembali. |
| Petugas Perpustakaan | catatanDenda | Masuk ( → ) | 3.0 | catatanDenda | Balanced | Catatan pembayaran denda. |
| Petugas Perpustakaan | statusTransaksiDanBukti | Keluar ( ← ) | 3.0 | statusTransaksiDanBukti | Balanced | Memuat bukti. |
| Petugas Perpustakaan | buktiPengembalianDanDenda | Keluar ( ← ) | 3.0 | buktiPengembalianDanDenda | Balanced | Persis sesuai Context. |
| Petugas Perpustakaan | dataKoleksiBaru | Masuk ( → ) | 2.0 | dataKoleksiBaru | Balanced | Pengelolaan master katalog. |
| Petugas Perpustakaan | statusPengelolaanKoleksi | Keluar ( ← ) | 2.0 | statusPengelolaanKoleksi | Balanced | Hasil pengelolaan katalog. |
| Kepala Perpustakaan | permintaanLaporan | Masuk ( → ) | 4.0 | permintaanLaporan | Balanced | Persis sesuai Context. |
| Kepala Perpustakaan | laporanBulanan | Keluar ( ← ) | 4.0 | laporanBulanan | Balanced | Persis sesuai Context. |
| Sistem Akademik | dataVerifikasi | Keluar ( ← ) | 1.0 | dataVerifikasi | Balanced | Pengecekan NIM/NIP. |
| Sistem Akademik | statusKeaktifan | Masuk ( → ) | 1.0 | statusKeaktifan | Balanced | Jawaban dari Sistem Akademik. |

## Audit Kesalahan DFD

| Pemeriksaan | Ya/Tidak | Temuan | Tindakan |
|---|---|---|---|
| Semua process memiliki input dan output yang logis. | Ya | Setiap proses dalam sistem telah dilengkapi dengan data input yang relevan dari entitas luar serta menghasilkan output balasan yang sesuai dengan kebutuhan fungsional sistem perpustakaan | Tidak ada tindakan, alur sudah sesuai logika bisnis perpustakaan. |
| Tidak ada entity-entity, entity-store, atau store-store flow. | Ya | Semua alur data (flow) sudah terhubung dengan benar melalui perantara proses; tidak ada garis yang menghubungkan langsung antar entitas maupun langsung antar data store | Memastikan kembali posisi garis panah di PowerDesigner tidak ada yang langsung menembus antar entitas. |
| Nama process menggunakan kata kerja + objek. | Ya | Sebelumnya belum kata kerja | Mengganti kalimat nama proses menjadi bentuk baku kata kerja + objek yang jelas. |
| Nama flow dan store menggunakan kata benda. | Ya | Sebelumnya penamaan proses masih menggunakan kata kerja yang belum baku atau dinominalisasi. | Menyeragamkan penamaan di seluruh diagram agar sesuai dengan kamus data sistem. |
| Flow lintas batas seimbang dengan context diagram. | Ya | Sebelumnya terdapat nama aliran yang berbeda antara Context Diagram dan DFD Level 0, serta aliran Laporan Operasional yang tidak dihasilkan proses mana pun. | Menyamakan nama aliran dengan DFD Level 0, menghapus Laporan Operasional, lalu melakukan cross-check silang menggunakan matriks balancing. |
| Nomor process unik dan tidak dimaknai sebagai urutan eksekusi. | Ya | Nomor proses lebih diperlakukan sebagai identifier atau penanda pembedaan proses | Mempertahankan format penomoran berbasis nomor induk proses utama. |
| Bentuk, ukuran, dan arah garis konsisten. | Ya | Simbol proses, entitas, dan data store menggunakan standar notasi pemodelan yang seragam di seluruh diagram. | Mengatur perataan posisi objek agar terlihat rapi dan proporsional. |
| Diagram masih terbaca tanpa garis silang berlebihan. | Ya | Garis sudah dibuat terbaca tidak bersilangan | Mengatur ulang tata letak (layout) jarak antar komponen jika ada alur yang terlalu padat. |

---

## Catatan Perubahan

Perubahan **isi** (karena balancing/konsistensi) ditandai ★. Sisanya hanya typo/tanda baca.

| Bagian | Perubahan | Alasan |
|---|---|---|
| Identifikasi Event, Event Table, Context Diagram | ★ Ikut M02 (identik) | M02 dan M03 memuat bagian yang sama; satu sumber supaya tidak berbeda lagi |
| Pengelompokan Event | "EV-9" → "EV-09". ★ Data Store Kandidat diganti ke store DFD: "Data Koleksi Buku, Data Eksemplar" → "D2 Data Koleksi"; "Transaksi Peminjaman." → "D3 Transaksi Fisik"; "Arsip Laporan Bulanan" → "- (membaca D2 Data Koleksi dan D3 Transaksi Fisik)" | Store kandidat harus sama dengan DFD L0 (AUD-B-05). Tidak ada store arsip laporan di DFD |
| Kerangka DFD Level 0 | ★ Gambar diganti ekspor `.bpm` terbaru | DFD sudah direvisi di M04 (nama camelCase, `dataAnggota` dua arah, Proses 4 "Membuat Laporan Sirkulasi") |
| Mendefinisikan Proses | "Mendefiniskan" → "Mendefinisikan"; "Proccess" → "Process"; "SIstem" → "Sistem"; "mengalkulasi" → "mengkalkulasi". ★ Input/Output pakai nama baku. ★ Proses 1: Data Store dibaca "-" → "Data Anggota". ★ Proses 2: Output "Info Katalog/Ketersediaan" → `informasiKoleksiBuku`, + `statusPengelolaanKoleksi`. ★ Proses 3: nama → "Memproses Sirkulasi dan Denda" (sama dengan tabel Pengelompokan); + input `catatanDenda`, + output `buktiPengembalianDanDenda`; store dibaca "-" → "Data Anggota, Data Koleksi, Transaksi Fisik"; store diubah + "Data Koleksi". ★ Proses 4: Input/Output tadinya tertukar ("Laporan Bulanan" di kolom Input) → Input `permintaanLaporan`, Output `laporanBulanan`; store dibaca + "Data Koleksi" | Tabel harus sama dengan DFD L0 (AUD-B-04, AUD-B-05). `dataAnggota` dua arah untuk cek pendaftaran ganda & EV-09 (AUD-B-08) |
| Matriks CD → L0 | ★ Semua nama pakai nama baku. ★ Tambah baris `catatanDenda` (sebelumnya tidak ada) dan `statusPengelolaanKoleksi` (aliran baru, AUD-B-12). Catatan "Diperjelas memuat ..." disederhanakan karena nama sekarang sama persis | Klaim "Persis sesuai Context" sebelumnya tidak sesuai bukti (AUD-B-03) |
| Audit Kesalahan DFD | ★ Baris "Flow lintas batas": Temuan & Tindakan diganti (pola kalimat "Sebelumnya ..." sama dengan baris lain) | Temuan lama tidak membahas CD; sekarang mencatat perbaikan CD (RV-M03-06) |

Nama Proses 4: dipilih **Membuat Laporan Sirkulasi** (sudah dipakai M03 di dua tabel). `Silapus Latest.bpm` sudah diubah mengikuti nama ini (2026-10-26).
