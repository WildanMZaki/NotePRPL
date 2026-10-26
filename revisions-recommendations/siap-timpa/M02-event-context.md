# M02 — Event Context (Siap Timpa)

Sumber: `baselines/PRPL_M02_2B_RajinBelajar_EventContext-1.pdf`. Urutan dan judul bagian sama dengan dokumen; salin per bagian lalu timpa. Daftar perubahan ada di [Catatan Perubahan](#catatan-perubahan) paling bawah.

Nama aliran data memakai nama baku DFD (`manajemen/BASELINE_PENAMAAN.md`), supaya Event ↔ Context Diagram ↔ DFD Level 0 balance.

---

## ENTITAS EKSTERNAL

| ID | External Entity | Alasan Di Luar Sistem | Input ke Sistem | Output dari Sistem |
|---|---|---|---|---|
| EE-01 | Anggota | Pengguna luar yang mengajukan permohonan layanan dan menerima status transaksi. | dataPendaftaran, dataPencarian, permintaanPerpanjangan | statusPendaftaran, informasiKoleksiBuku, statusPerpanjangan |
| EE-02 | Petugas Perpustakaan | Operator internal organisasi perpustakaan yang memvalidasi & mencatat transaksi sirkulasi. | dataTransaksiFisik, dataKoleksiBaru, catatanDenda | statusTransaksiDanBukti, buktiPengembalianDanDenda, statusPengelolaanKoleksi |
| EE-03 | Sistem Akademik | Sistem luar milik kampus untuk verifikasi status keaktifan civitas akademika. | statusKeaktifan | dataVerifikasi (berdasarkan NIM/NIP) |
| EE-04 | Kepala Perpustakaan | Pimpinan organisasi yang memerlukan informasi eksekutif untuk pengambilan keputusan. | permintaanLaporan | laporanBulanan (sirkulasi, statistik koleksi & denda) |

## IDENTIFIKASI EVENT

| ID | Nama Event Bisnis | Jenis | Sumber / Pemicu | Respons Singkat Sistem SILAPUS |
|---|---|---|---|---|
| EV-01 | Anggota mengajukan pendaftaran anggota baru. | F | Anggota | Memverifikasi status keaktifan ke Sistem Akademik dan menyimpan data anggota baru. |
| EV-02 | Anggota melakukan pencarian koleksi buku. | F | Anggota | Mencari data katalog dan menampilkan daftar ketersediaan eksemplar buku. |
| EV-03 | Petugas mencatat peminjaman buku. | F | Petugas | Memvalidasi status anggota & ketersediaan eksemplar, lalu mencatat transaksi peminjaman. |
| EV-04 | Petugas mencatat pengembalian buku. | F | Petugas | Memperbarui status eksemplar menjadi tersedia dan mengkalkulasi denda jika terlambat. |
| EV-05 | Anggota mengajukan perpanjangan peminjaman. | F | Anggota | Memvalidasi batas perpanjangan & denda, lalu memperbarui tanggal jatuh tempo baru. |
| EV-06 | Kepala Perpustakaan meminta laporan bulanan. | F | Kepala Perpustakaan | Merekapitulasi data sirkulasi, koleksi, dan denda lalu menyajikan laporan bulanan. |
| EV-07 | Sistem menghasilkan laporan rekapitulasi bulanan otomatis. | T | Waktu (Akhir Bulan) | Memproses rekapitulasi data bulanan secara otomatis pada hari kerja terakhir setiap bulan. |
| EV-08 | Petugas mengelola data koleksi buku. | F | Petugas | Menyimpan, memperbarui, atau menghapus data master koleksi buku perpustakaan. |
| EV-09 | Sistem Akademik mengirim update status mahasiswa. | F | Sistem Akademik | Update status aktif/nonaktif anggota. |

*Jenis Event: F = Flow, T = Temporal

## EVENT TABLE

### Event Number: 1

| Elemen | Detail Isian |
|---|---|
| Event Name | Anggota mengajukan pendaftaran anggota baru |
| Description | Mahasiswa atau dosen mendaftar menjadi anggota perpustakaan untuk memperoleh hak akses peminjaman. |
| Inputs | dataPendaftaran (NIM/NIP, Nama, Email, Program Studi) |
| Outputs | statusPendaftaran (memuat ID Anggota), dataVerifikasi |
| Frequency | Setiap kali ada civitas akademika baru yang mendaftar. |
| Response logis | 1. Sistem menerima dataPendaftaran dari Anggota.<br>2. Sistem mengirimkan dataVerifikasi (NIM/NIP) ke Sistem Akademik.<br>3. Sistem Akademik mengembalikan statusKeaktifan.<br>4. Jika status 'Aktif', sistem menyimpan data anggota baru dan membuat ID Anggota.<br>5. Sistem menampilkan statusPendaftaran berhasil kepada Anggota. |
| Error Conditions | 1. NIM/NIP tidak terdaftar di Sistem Akademik.<br>2. Status mahasiswa tidak aktif / cuti.<br>3. Data formulir pendaftaran tidak lengkap. |

### Event Number: 2

| Elemen | Detail Isian |
|---|---|
| Event Name | Anggota melakukan pencarian koleksi buku |
| Description | Anggota mencari koleksi buku berdasarkan kata kunci judul, pengarang, atau subjek |
| Inputs | dataPencarian (judul/pengarang) |
| Outputs | informasiKoleksiBuku (Daftar Buku, Lokasi Rak) |
| Frequency | Setiap kali anggota membutuhkan referensi buku |
| Response logis | 1. Sistem menerima dataPencarian dari Anggota.<br>2. Sistem melakukan pencarian pada basis data koleksi buku.<br>3. Sistem menyajikan informasiKoleksiBuku dan status ketersediaan stok eksemplar.<br>4. Jika buku tidak ditemukan, sistem menampilkan pesan alternatif koleksi. |
| Error Conditions | 1. Kata kunci tidak cocok dengan koleksi mana pun.<br>2. Sistem pencarian mengalami timeout. |

### Event Number: 3

| Elemen | Detail Isian |
|---|---|
| Event Name | Petugas mencatat peminjaman buku |
| Description | Petugas akan memproses transaksi peminjaman buku oleh anggota di meja peminjaman |
| Inputs | dataTransaksiFisik (ID anggota, Kode buku) |
| Outputs | statusTransaksiDanBukti (status transaksi dan bukti peminjaman) |
| Frequency | Setiap kali ada transaksi peminjaman buku fisik |
| Response logis | 1. Petugas menginputkan ID Anggota dan Kode Buku.<br>2. Sistem mengecek status aktif anggota dan memeriksa kuota peminjaman.<br>3. Sistem memeriksa status ketersediaan eksemplar buku.<br>4. Jika valid, sistem mencatat data transaksi peminjaman baru dan mengubah status eksemplar menjadi 'Dipinjam'.<br>5. Sistem menghasilkan bukti peminjaman bagi Anggota melalui Petugas. |
| Error Conditions | 1. Status anggota tidak aktif atau memiliki denda.<br>2. Buku sedang dalam status dipinjam.<br>3. Anggota sudah melebihi jumlah kuota peminjaman. |

### Event Number: 4

| Elemen | Detail Isian |
|---|---|
| Event Name | Petugas mencatat pengembalian buku |
| Description | Petugas memproses pengembalian buku dan mengkalkulasi denda jika terjadi keterlambatan |
| Inputs | dataTransaksiFisik (Kode Eksemplar Buku, Tanggal Pengembalian), catatanDenda (pembayaran denda) |
| Outputs | buktiPengembalianDanDenda (jika ada denda), statusTransaksiDanBukti |
| Frequency | Setiap kali ada transaksi pengembalian buku |
| Response logis | 1. Petugas menginputkan Kode Eksemplar Buku yang dikembalikan.<br>2. Sistem mengambil data peminjaman aktif terkait.<br>3. Sistem membandingkan tanggal pengembalian dengan tanggal jatuh tempo.<br>4. Jika terlambat, sistem menghitung denda berdasarkan tarif harian.<br>5. Sistem memperbarui status peminjaman menjadi 'Selesai' dan status eksemplar menjadi 'Tersedia'.<br>6. Sistem menerbitkan buktiPengembalianDanDenda.<br>7. Jika anggota membayar denda, Petugas menginputkan catatanDenda dan sistem mencatat denda menjadi 'Lunas'. |
| Error Conditions | 1. Data peminjaman aktif untuk eksemplar buku tersebut tidak ditemukan.<br>2. Jumlah pembayaran denda tidak sesuai dengan total denda. |

### Event Number: 5

| Elemen | Detail Isian |
|---|---|
| Event Name | Anggota mengajukan perpanjangan peminjaman |
| Description | Anggota meminta perpanjangan durasi peminjaman untuk buku yang sedang dipinjam |
| Inputs | permintaanPerpanjangan (ID Anggota, ID Transaksi Peminjaman) |
| Outputs | statusPerpanjangan (status dan Tanggal Jatuh Tempo Baru) |
| Frequency | Setiap kali anggota melakukan perpanjangan peminjaman buku |
| Response logis | 1. Sistem menerima permintaanPerpanjangan dari Anggota.<br>2. Sistem memvalidasi status keaktifan anggota dan memeriksa tunggakan denda.<br>3. Sistem memeriksa batas maksimal frekuensi perpanjangan.<br>4. Jika valid, sistem memperbarui tanggal jatuh tempo baru pada transaksi.<br>5. Sistem mengirimkan statusPerpanjangan berhasil dan Tanggal Jatuh Tempo Baru. |
| Error Conditions | 1. Buku telah mencapai batas maksimal perpanjangan (maksimal 2 kali).<br>2. Peminjaman sudah melewati tanggal jatuh tempo.<br>3. Anggota memiliki denda aktif. |

### Event Number: 6

| Elemen | Detail Isian |
|---|---|
| Event Name | Kepala Perpustakaan meminta laporan bulanan |
| Description | Kepala Perpustakaan meminta rekapitulasi sirkulasi, koleksi, dan denda untuk satu bulan. |
| Inputs | permintaanLaporan (Periode laporan) |
| Outputs | laporanBulanan |
| Frequency | Sesuai kebutuhan, umumnya 1–2 kali per bulan |
| Response logis | 1. Sistem menerima permintaanLaporan dari Kepala Perpustakaan.<br>2. Sistem mengambil data transaksi pada periode tersebut.<br>3. Sistem mengambil data koleksi.<br>4. Sistem merekap jumlah peminjaman, pengembalian, keterlambatan, dan denda.<br>5. Sistem menyajikan laporanBulanan kepada Kepala Perpustakaan. |
| Error Conditions | 1. Periode laporan belum berjalan (di masa depan).<br>2. Format periode laporan tidak valid. |

### Event Number: 7

| Elemen | Detail Isian |
|---|---|
| Event Name | Sistem menghasilkan laporan rekapitulasi bulanan otomatis |
| Description | Sistem membuat laporan bulanan secara otomatis pada hari kerja terakhir setiap bulan. |
| Inputs | - (dipicu waktu; periode = bulan berjalan) |
| Outputs | laporanBulanan |
| Frequency | Satu kali setiap bulan |
| Response logis | 1. Sistem mendeteksi hari kerja terakhir bulan berjalan.<br>2. Sistem mengambil data transaksi dan data koleksi bulan berjalan.<br>3. Sistem merekap jumlah peminjaman, pengembalian, keterlambatan, dan denda.<br>4. Sistem menyajikan laporanBulanan kepada Kepala Perpustakaan. |
| Error Conditions | 1. Tidak ada transaksi pada periode tersebut (laporan tetap dibuat dengan nilai 0). |

### Event Number: 8

| Elemen | Detail Isian |
|---|---|
| Event Name | Petugas mengelola data koleksi buku |
| Description | Petugas menambah, memperbarui, atau menghapus data koleksi buku dan eksemplarnya. |
| Inputs | dataKoleksiBaru |
| Outputs | statusPengelolaanKoleksi |
| Frequency | Setiap kali ada koleksi baru atau perubahan data koleksi |
| Response logis | 1. Petugas menginputkan dataKoleksiBaru.<br>2. Sistem memeriksa kelengkapan dan keunikan kode buku.<br>3. Jika valid, sistem menyimpan, memperbarui, atau menghapus data koleksi.<br>4. Sistem menampilkan statusPengelolaanKoleksi (berhasil atau gagal beserta alasannya) kepada Petugas. |
| Error Conditions | 1. Kode buku sudah terdaftar (saat menambah).<br>2. Kode buku tidak ditemukan (saat memperbarui/menghapus).<br>3. Eksemplar sedang dipinjam (saat menghapus).<br>4. Data koleksi tidak lengkap. |

### Event Number: 9

| Elemen | Detail Isian |
|---|---|
| Event Name | Sistem Akademik mengirim update status mahasiswa |
| Description | Sistem Akademik mengirim perubahan status keaktifan civitas akademika yang sudah menjadi anggota. |
| Inputs | statusKeaktifan |
| Outputs | - (status anggota diperbarui di Data Anggota) |
| Frequency | Setiap ada perubahan status di Sistem Akademik |
| Response logis | 1. Sistem menerima statusKeaktifan dari Sistem Akademik.<br>2. Sistem mencari data anggota dengan NIM/NIP tersebut.<br>3. Sistem memperbarui status anggota menjadi aktif/nonaktif. |
| Error Conditions | 1. NIM/NIP tidak terdaftar sebagai anggota. |

## CONTEXT DIAGRAM

Gambar tetap, label panah diganti:

| Panah | Label lama | Label baru |
|---|---|---|
| Anggota Perpustakaan → SILAPUS | Data Pendaftaran, Data Pencarian, Permintaan Perpanjangan | dataPendaftaran, dataPencarian, permintaanPerpanjangan |
| SILAPUS → Anggota Perpustakaan | Status Pendaftaran, Informasi Katalog, Status Perpanjangan | statusPendaftaran, informasiKoleksiBuku, statusPerpanjangan |
| Petugas Perpustakaan → SILAPUS | Data Transaksi Fisik, Data Koleksi Buku, Konfirmasi Denda | dataTransaksiFisik, dataKoleksiBaru, catatanDenda |
| SILAPUS → Petugas Perpustakaan | Status Transaksi, Bukti Pengembalian dan Denda, Laporan Operasional | statusTransaksiDanBukti, buktiPengembalianDanDenda, statusPengelolaanKoleksi |
| Kepala Perpustakaan → SILAPUS | Permintaan Laporan | permintaanLaporan |
| SILAPUS → Kepala Perpustakaan | Laporan Bulanan Sirkulasi & Denda | laporanBulanan |
| Sistem Akademik → SILAPUS | Status Keaktifan Mahasiswa | statusKeaktifan |
| SILAPUS → Sistem Akademik | Data Verifikasi Mahasiswa | dataVerifikasi |

## EVENT DIAGRAM

Gambar tetap, isi kotak diganti:

| Kotak | Isi lama | Isi baru |
|---|---|---|
| 3. Input | Form Pendaftaran (NIM/NIP, Nama, Email, Prodi) | dataPendaftaran (NIM/NIP, Nama, Email, Prodi) |
| 5. Output | Status Pendaftaran, Data Verifikasi, ID Anggota | statusPendaftaran (memuat ID Anggota), dataVerifikasi |

Kotak lain tidak berubah.

## MATRIKS KETERLACAKAN DAN BALANCING

| ID Event | Entitas Eksternal | Input pada Event Table | Input pada Context Diagram | Output pada Event Table | Output pada Context Diagram | Status |
|---|---|---|---|---|---|---|
| EV-01 | Anggota & Sistem Akademik | dataPendaftaran, statusKeaktifan | dataPendaftaran, statusKeaktifan | statusPendaftaran, dataVerifikasi | statusPendaftaran, dataVerifikasi | Balanced |
| EV-02 | Anggota | dataPencarian | dataPencarian | informasiKoleksiBuku | informasiKoleksiBuku | Balanced |
| EV-03 | Petugas Perpustakaan | dataTransaksiFisik (ID Anggota, Kode Eksemplar) | dataTransaksiFisik | statusTransaksiDanBukti | statusTransaksiDanBukti | Balanced |
| EV-04 | Petugas Perpustakaan | dataTransaksiFisik (Kode Eksemplar, Tanggal kembali), catatanDenda | dataTransaksiFisik, catatanDenda | buktiPengembalianDanDenda, statusTransaksiDanBukti | buktiPengembalianDanDenda, statusTransaksiDanBukti | Balanced |
| EV-05 | Anggota | permintaanPerpanjangan (ID Transaksi) | permintaanPerpanjangan | statusPerpanjangan (Tanggal Jatuh Tempo Baru) | statusPerpanjangan | Balanced |
| EV-06 | Kepala Perpustakaan | permintaanLaporan | permintaanLaporan | laporanBulanan | laporanBulanan | Balanced |
| EV-07 | Kepala Perpustakaan | - (temporal) | - | laporanBulanan | laporanBulanan | Balanced |
| EV-08 | Petugas Perpustakaan | dataKoleksiBaru | dataKoleksiBaru | statusPengelolaanKoleksi | statusPengelolaanKoleksi | Balanced |
| EV-09 | Sistem Akademik | statusKeaktifan | statusKeaktifan | - | - | Balanced |

---

## Catatan Perubahan

Perubahan **isi** (karena balancing/konsistensi) ditandai ★. Sisanya hanya typo/tanda baca.

| Bagian | Perubahan | Alasan |
|---|---|---|
| Entitas Eksternal | ★ Semua input/output diganti ke nama baku DFD. ★ EE-02 + output `statusPengelolaanKoleksi`. ★ EE-01: hapus "Data Peminjaman" (input) dan "Bukti Peminjaman" (output). ★ EE-02: hapus "Laporan Operasional"; "Konfirmasi Denda" → `catatanDenda`; "Data Koleksi Buku" → `dataKoleksiBaru`. ★ EE-03: input/output disesuaikan arah CD (SILAPUS menerima `statusKeaktifan`, mengirim `dataVerifikasi`); "NIM" → "NIM/NIP" | Tabel entitas harus sama dengan CD dan DFD L0 (AUD-A-07, AUD-B-02). Peminjaman diinput Petugas, bukti diterima Petugas |
| Identifikasi Event | "mengalkulasi" → "mengkalkulasi" (sama dengan M03); titik di akhir nama event | Typo |
| Event 1 | ★ Description "Mahasiswa" → "Mahasiswa atau dosen" (sama dengan M03). ★ Inputs/Outputs/Response pakai nama baku; "ID Anggota Digital" dipindah ke dalam statusPendaftaran | Konsistensi M02 = M03 = DFD (RV-M02-04, RV-M02-10) |
| Event 2 | ★ Inputs/Outputs/Response pakai nama baku | RV-M02-04 |
| Event 3 | "peninjaman", "tansaksi", "peminjakan", "angggota" diperbaiki. ★ Inputs/Outputs pakai nama baku. ★ Response 5: bukti diberikan "melalui Petugas". ★ Error 1: "diblokir" → "tidak aktif" | Bukti mengalir ke Petugas di DFD; domain status anggota tidak punya "diblokir" (RV-M02-07) |
| Event 4 | ★ Inputs + `catatanDenda`; ★ Response + langkah 7 (pembayaran denda); ★ Error 2 "Pembayaran denda gagal dikonfirmasi" → "Jumlah pembayaran denda tidak sesuai dengan total denda" | `catatanDenda` ada di CD tapi belum punya event; pembayaran dicatat Petugas, bukan Bagian Keuangan |
| Event 5 | ★ "(misal: max 2 kali)" → "(maksimal 2 kali)"; ★ Error 2 reservasi → "Peminjaman sudah melewati tanggal jatuh tempo" | Tidak ada fitur reservasi; "misal" tidak boleh di event table (RV-M02-07, RV-M02-09). Angka 2 diambil dari event table ini sendiri (menutup TBD-01) |
| Event 6–9 | ★ **Baru**. EV-08 memakai output baru `statusPengelolaanKoleksi` | Event list punya 9 event tapi event table baru 5; proses 2.2, 4, dan 1 (EV-09) butuh sumber untuk M06 (RV-M02-03) |
| Context Diagram | ★ Label diganti ke nama baku; ★ hapus "Laporan Operasional"; ★ tambah `statusPengelolaanKoleksi` (SILAPUS → Petugas) | CD ↔ L0 balance (AUD-B-01, AUD-B-02). Aliran baru = jalur hasil/gagal EV-08 (AUD-B-12) |
| Event Diagram | ★ Label input/output kotak 3 dan 5 | Konsisten dengan Event 1 |
| Matriks | ★ Semua kolom pakai nama baku; ★ tambah baris EV-06 s.d. EV-09; ★ EV-04 + `catatanDenda` | Setiap aliran CD harus terlacak ke event (RV-M02-06) |

Koreksi audit: Bagian Keuangan (AUD-A-01) dan penomoran event (AUD-A-02) **sudah benar di baseline M02**. Temuan itu berasal dari versi `submitted/`.
