# Baseline Penamaan SILAPUS (Single Source of Truth)

> Semua artefak (DFD .bpm, dokumen M04, kamus data M05, process spec M06, dan revisi M02/M03)
> **wajib** memakai nama di file ini persis (ejaan + kapitalisasi). Kalau mau ganti nama,
> ubah di sini dulu → catat di `TEMUAN_DAN_REVISI.md` → baru terapkan ke semua artefak.

- Sumber baseline: `Silapus Latest.bpm` (dulu `SILAPUS wildan.bpm`) hasil merge 2026-10-19 (lihat REV-2026-10-19 di `TEMUAN_DAN_REVISI.md`)
- Status: **v0.2 (draft, belum disepakati kelompok)**

## Konvensi

| Objek | Konvensi | Contoh |
|---|---|---|
| Aliran data (flow) | camelCase, kata benda, tanpa spasi | `dataPeminjaman`, `statusPerpanjangan` |
| Proses | Kata kerja + objek, Title Case, **tanpa** nomor di nama (nomor tampil dari NumberID PowerDesigner) | `Memproses Sirkulasi dan Denda` |
| Data store | `D<n> <Nama>` saat ditulis di dokumen; di .bpm cukup nama (nomor dari NumberID) | `D3 Transaksi Fisik` |
| External entity | Title Case | `Petugas Perpustakaan` |
| Elemen data (kamus) | PascalCase (sesuai contoh modul: `TanggalJatuhTempo`) | `KodeEksemplar` |

Catatan: nama flow camelCase diambil dari perubahan Irfan (Level 0) dan Rere (Level 1 Proses 2). Kamus data M05 juga sudah camelCase di sheet Inventaris, tapi sheet Data_Komposit masih PascalCase → harus diseragamkan (lihat BACKLOG M05).

## External Entity

| Nama | Muncul di |
|---|---|
| Anggota Perpustakaan | CD, L0, L1-P2, L1-P3 |
| Petugas Perpustakaan | CD, L0, L1-P2, L1-P3 |
| Sistem Akademik | CD, L0 |
| Kepala Perpustakaan | CD, L0 |

## Data Store

| No | Nama | Ditulis oleh | Dibaca oleh |
|---|---|---|---|
| D1 | Data Anggota | 1 | 3 (3.1, 3.4) |
| D2 | Data Koleksi | 2 (2.2), 3 (3.1, 3.2) | 2 (2.1), 3 (3.1), 4 |
| D3 | Transaksi Fisik | 3 (3.1–3.4) | 3 (3.2, 3.4), 4 |


## Proses

| No | Nama | Primitif? |
|---|---|---|
| 1 | Mengelola Keanggotaan | Ya |
| 2 | Mengelola Katalog Koleksi | Tidak → 2.1, 2.2 |
| 2.1 | Mencari Katalog Buku | Ya |
| 2.2 | Mengelola Data Koleksi | Ya |
| 3 | Memproses Sirkulasi dan Denda | Tidak → 3.1–3.4 |
| 3.1 | Memproses Peminjaman Buku | Ya |
| 3.2 | Memproses Pengembalian Buku | Ya |
| 3.3 | Menghitung dan Mencatat Denda | Ya |
| 3.4 | Memperpanjang Peminjaman | Ya |
| 4 | Membuat Laporan Transaksi Fisik | Ya (lihat BL-DFD-05 soal nama) |

Proses primitif untuk M06: **1, 2.1, 2.2, 3.1, 3.2, 3.3, 3.4, 4** (8 process spec).

## Aliran Data — DFD Level 0

| Flow | Dari → Ke |
|---|---|
| dataPendaftaran | Anggota Perpustakaan → 1 |
| statusPendaftaran | 1 → Anggota Perpustakaan |
| dataVerifikasi | 1 → Sistem Akademik |
| statusKeaktifan | Sistem Akademik → 1 |
| dataAnggota | 1 → D1 (tulis) |
| dataPencarian | Anggota Perpustakaan → 2 |
| informasiKoleksiBuku | 2 → Anggota Perpustakaan |
| dataKoleksiBaru | Petugas Perpustakaan → 2 |
| dataKoleksiBuku | D2 ↔ 2 (baca + tulis) |
| permintaanPerpanjangan | Anggota Perpustakaan → 3 |
| statusPerpanjangan | 3 → Anggota Perpustakaan |
| dataTransaksiFisik | Petugas Perpustakaan → 3 |
| statusTransaksiDanBukti | 3 → Petugas Perpustakaan |
| catatanDenda | Petugas Perpustakaan → 3 |
| buktiPengembalianDanDenda | 3 → Petugas Perpustakaan |
| statusAnggota | D1 → 3 (baca) |
| dataEksemplar | D2 → 3 (baca) |
| pembaruanEksemplar | 3 → D2 (tulis) |
| peminjamAktif | D3 → 3 (baca) |
| dataPeminjaman | 3 → D3 (tulis) |
| permintaanLaporan | Kepala Perpustakaan → 4 |
| laporanBulanan | 4 → Kepala Perpustakaan |
| dataTransaksi | D3 → 4 (baca) |
| dataKoleksi | D2 → 4 (baca) |

## Aliran Data — DFD Level 1 Proses 2

| Flow | Dari → Ke | Padanan Level 0 |
|---|---|---|
| dataPencarian | Anggota Perpustakaan → 2.1 | sama |
| informasiKoleksiBuku | 2.1 → Anggota Perpustakaan | sama |
| dataKoleksiBuku | D2 → 2.1 (baca) | sisi baca `dataKoleksiBuku` |
| dataKoleksiBaru | Petugas Perpustakaan → 2.2 | sama |
| dataKoleksiBuku | 2.2 → D2 (tulis) | sisi tulis `dataKoleksiBuku` |

## Aliran Data — DFD Level 1 Proses 3

| Flow | Dari → Ke | Padanan Level 0 |
|---|---|---|
| dataTransaksiPeminjaman | Petugas Perpustakaan → 3.1 | komponen `dataTransaksiFisik`* |
| dataTransaksiPengembalian | Petugas Perpustakaan → 3.2 | komponen `dataTransaksiFisik`* |
| statusTransaksiDanBukti | 3.1 → Petugas Perpustakaan | sama |
| statusTransaksiDanBukti | 3.2 → Petugas Perpustakaan | sama |
| catatanDenda | Petugas Perpustakaan → 3.3 | sama |
| buktiPengembalianDanDenda | 3.3 → Petugas Perpustakaan | sama |
| permintaanPerpanjangan | Anggota Perpustakaan → 3.4 | sama |
| statusPerpanjangan | 3.4 → Anggota Perpustakaan | sama |
| statusAnggota | D1 → 3.1, D1 → 3.4 (baca) | sama |
| dataEksemplar | D2 → 3.1 (baca) | sama |
| pembaruanEksemplar | 3.1 → D2, 3.2 → D2 (tulis) | sama |
| peminjamAktif | D3 → 3.2, D3 → 3.4 (baca) | sama |
| dataPeminjamanBaru | 3.1 → D3 (tulis) | komponen `dataPeminjaman`** |
| pembaruanPengembalian | 3.2 → D3 (tulis) | komponen `dataPeminjaman`** |
| dataDenda | 3.3 → D3 (tulis) | komponen `dataPeminjaman`** |
| pembaruanMasaPinjam | 3.4 → D3 (tulis) | komponen `dataPeminjaman`** |
| dataKeterlambatan | 3.2 → 3.3 | internal (tidak perlu di Level 0) |

\* Wajib didefinisikan di kamus data: `dataTransaksiFisik = [dataTransaksiPeminjaman | dataTransaksiPengembalian]`
\*\* Wajib didefinisikan di kamus data: `dataPeminjaman = [dataPeminjamanBaru | pembaruanPengembalian | dataDenda | pembaruanMasaPinjam]`

Tanpa dua definisi itu, matriks balancing baris terkait **tidak sah** (Modul 4 §1.4). Status: sudah didefinisikan di kamus data v0.2 (2026-10-21).

**Usulan perubahan (belum diterapkan, AUD-B-07):** tambah `peminjamAktif` D3 → 3.1 (baca) agar aturan kuota & denda pada peminjaman punya sumber data. Balance tetap aman karena Level 0 sudah punya `peminjamAktif` D3 → 3.
