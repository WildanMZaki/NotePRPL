# Urgent Changes

Perubahan mendesak yang harus segera diterapkan ke dokumen. Centang kalau sudah diterapkan.

---

## UC-01 · Inventaris Data M05: isi Status Entri + koreksi (2026-10-21)

Sumber: inventaris M05 versi terakhir (`updates/PRPL_M05_2B_RajinBelajar_DataDictionary.pdf`, sudah ditambah kolom "Jenis Struktur").
Terkait: RV-M05-10, RV-M05-11, RV-M05-12, RV-M05-17 di [`revisions-recommendations/M05-data-dictionary.md`](revisions-recommendations/M05-data-dictionary.md).

**Arti Status Entri:**
- **Baku**: nama resmi, sama dengan DFD
- **Alias**: nama lain dari entri yang sudah ada
- **Perlu diperbaiki**: harus diganti atau dihapus

Lihat juga [`validasi-silang/PANDUAN_CEK_VALIDASI.md`](validasi-silang/PANDUAN_CEK_VALIDASI.md) bagian 1–2.

### Checklist
- [ ] Isi kolom Status Entri (tabel A)
- [ ] No 1: hapus "DFD 1.1" dan "Proses 1.1" (proses 1 tidak didekomposisi)
- [ ] No 6: tambah lokasi DFD 2.1 dan sumber Proses 2.1
- [ ] No 7: **hapus** `infoKatalog/Ketersediaan` (baris inventaris + entri komposit)
- [ ] No 13: **balik arah** `catatanDenda`: Petugas Perpustakaan → Proses 3, Proses 3.3; tambah lokasi CD
- [ ] No 2, 4, 16: Jenis Struktur jadi Komposit (atau, kalau tetap Elementer, definisikan di tabel elemen)
- [ ] No 5, 17: tetap Elementer, tapi masukkan ke tabel elemen
- [ ] Tambah 16 baris flow store + store (tabel B)
- [ ] Buat entri komposit untuk baris tabel B (salin dari `progress/PRPL_M05_2B_RajinBelajar_DataDictionary.xlsx` sheet `2_Entri_Komposit` dan `3_Entri_Store`)

### A. Inventaris yang sudah ada (koreksi ditandai **tebal**)

| No | Nama Data | Jenis | Lokasi DFD | Sumber | Tujuan | Jenis Struktur | Status Entri |
|---|---|---|---|---|---|---|---|
| 1 | dataPendaftaran | Flow | CD, DFD 0 | Anggota Perpustakaan | **Proses 1** | Komposit | Baku |
| 2 | statusPendaftaran | Flow | CD, DFD 0 | Proses 1 | Anggota Perpustakaan | **Komposit** | Baku |
| 3 | dataVerifikasi | Flow | CD, DFD 0 | Proses 1 | Sistem Akademik | Komposit | Baku |
| 4 | statusKeaktifan | Flow | CD, DFD 0 | Sistem Akademik | Proses 1 | **Komposit** | Baku (alias: Status Keaktifan Mahasiswa) |
| 5 | dataPencarian | Flow | CD, DFD 0, DFD 2.1 | Anggota Perpustakaan | Proses 2, Proses 2.1 | Elementer | Baku |
| 6 | informasiKoleksiBuku | Flow | CD, DFD 0, **DFD 2.1** | Proses 2, **Proses 2.1** | Anggota Perpustakaan | Komposit | Baku (alias: Informasi Katalog) |
| 7 | ~~infoKatalog/Ketersediaan~~ | | | | | | **Perlu diperbaiki: hapus** |
| 8 | dataKoleksiBaru | Flow | CD, DFD 0, DFD 2.2 | Petugas Perpustakaan | Proses 2, Proses 2.2 | Komposit | Baku (alias: Data Koleksi Buku) |
| 9 | dataTransaksiFisik | Flow | CD, DFD 0 | Petugas Perpustakaan | Proses 3 | Komposit | Baku |
| 10 | dataTransaksiPeminjaman | Flow | DFD 3.1 | Petugas Perpustakaan | Proses 3.1 | Komposit | Baku (alias: formTransaksiPinjam) |
| 11 | dataTransaksiPengembalian | Flow | DFD 3.2 | Petugas Perpustakaan | Proses 3.2 | Komposit | Baku (alias: formTransaksiKembali) |
| 12 | statusTransaksiDanBukti | Flow | CD, DFD 0, DFD 3.1, 3.2 | Proses 3, Proses 3.1, Proses 3.2 | Petugas Perpustakaan | Komposit | Baku (alias: Status Transaksi) |
| 13 | catatanDenda | Flow | **CD**, DFD 0, DFD 3.3 | **Petugas Perpustakaan** | **Proses 3, Proses 3.3** | Komposit | Baku (alias: Konfirmasi Denda, buktiKonfirmasiDenda) |
| 14 | buktiPengembalianDanDenda | Flow | CD, DFD 0, DFD 3.3 | Proses 3, Proses 3.3 | Petugas Perpustakaan | Komposit | Baku |
| 15 | permintaanPerpanjangan | Flow | CD, DFD 0, DFD 3.4 | Anggota Perpustakaan | Proses 3, Proses 3.4 | Komposit | Baku |
| 16 | statusPerpanjangan | Flow | CD, DFD 0, DFD 3.4 | Proses 3, Proses 3.4 | Anggota Perpustakaan | **Komposit** | Baku |
| 17 | permintaanLaporan | Flow | CD, DFD 0 | Kepala Perpustakaan | Proses 4 | Elementer | Baku |
| 18 | laporanBulanan | Flow | CD, DFD 0 | Proses 4 | Kepala Perpustakaan | Komposit | Baku (alias: laporanSirkulasiBulanan) |
| 19 | dataKeterlambatan | Flow | DFD 3.2, 3.3 | Proses 3.2 | Proses 3.3 | Komposit | Baku |

**Alasan koreksi:**
- **No 1:** proses 1 tidak punya DFD Level 1.
- **No 2, 4, 16:** isinya lebih dari satu data (status + identitas/tanggal), jadi komposit. Contoh: `statusPerpanjangan` memuat TanggalJatuhTempo baru, `statusKeaktifan` perlu NIM pemiliknya.
- **No 7:** nama lama sebelum merge. Di DFD master sudah jadi `informasiKoleksiBuku` (PR-03). Kalau dibiarkan, Level 0 dan Level 1 tidak balance (RV-M05-11).
- **No 13:** arahnya terbalik. Di DFD, `catatanDenda` adalah input catatan pembayaran dari Petugas ke 3.3 (RV-M05-10).

### B. Baris yang belum ada (flow yang melibatkan data store + store)

Nomor menyambung setelah baris 7 dihapus (baris 8–19 di tabel A jadi 7–18). Totalnya 34 entri, sama dengan DFD.

| No | Nama Data | Jenis | Lokasi DFD | Sumber | Tujuan | Jenis Struktur | Status Entri |
|---|---|---|---|---|---|---|---|
| 19 | dataAnggota | Flow | DFD 0 | Proses 1 | D1 Data Anggota | Komposit | Baku |
| 20 | statusAnggota | Flow | DFD 0, DFD 3.1, 3.4 | D1 Data Anggota | Proses 3, Proses 3.1, Proses 3.4 | Komposit | Baku |
| 21 | dataKoleksiBuku | Flow | DFD 0, DFD 2.1, 2.2 | D2 (baca: ke 2.1) / Proses 2.2 (tulis) | Proses 2.1 / D2 Data Koleksi | Komposit | Baku |
| 22 | dataEksemplar | Flow | DFD 0, DFD 3.1 | D2 Data Koleksi | Proses 3, Proses 3.1 | Komposit | Baku |
| 23 | pembaruanEksemplar | Flow | DFD 0, DFD 3.1, 3.2 | Proses 3, Proses 3.1, Proses 3.2 | D2 Data Koleksi | Komposit | Baku |
| 24 | dataKoleksi | Flow | DFD 0 | D2 Data Koleksi | Proses 4 | Komposit | Baku |
| 25 | peminjamAktif | Flow | DFD 0, DFD 3.2, 3.4 | D3 Transaksi Fisik | Proses 3, Proses 3.2, Proses 3.4 | Komposit | Baku |
| 26 | dataPeminjaman | Flow | DFD 0 | Proses 3 | D3 Transaksi Fisik | Komposit | Baku |
| 27 | dataPeminjamanBaru | Flow | DFD 3.1 | Proses 3.1 | D3 Transaksi Fisik | Komposit | Baku |
| 28 | pembaruanPengembalian | Flow | DFD 3.2 | Proses 3.2 | D3 Transaksi Fisik | Komposit | Baku |
| 29 | dataDenda | Flow | DFD 3.3 | Proses 3.3 | D3 Transaksi Fisik | Komposit | Baku |
| 30 | pembaruanMasaPinjam | Flow | DFD 3.4 | Proses 3.4 | D3 Transaksi Fisik | Komposit | Baku |
| 31 | dataTransaksi | Flow | DFD 0 | D3 Transaksi Fisik | Proses 4 | Komposit | Baku |
| 32 | D1 Data Anggota | Store | DFD 0, DFD 3.1, 3.4 | Proses 1 | Proses 3 (3.1, 3.4) | Komposit | Baku |
| 33 | D2 Data Koleksi | Store | DFD 0, DFD 2.1, 2.2, 3.1, 3.2 | Proses 2.2, 3.1, 3.2 | Proses 2.1, 3.1, 4 | Komposit | Baku |
| 34 | D3 Transaksi Fisik | Store | DFD 0, DFD 3.1–3.4 | Proses 3.1–3.4 | Proses 3.2, 3.4, 4 | Komposit | Baku (alias: dataTransaksiSirkulasi) |
