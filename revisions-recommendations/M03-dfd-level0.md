# M03 — DFD Level 0

File: `baselines/PRPL_M03_2B_RajinBelajar_DFD-2.pdf`. Event list, event table, dan CD di dokumen ini ikut revisi M02.

- [ ] RV-M03-01 · Terapkan revisi M02 (event & CD) · **P1**
- [ ] RV-M03-02 · Tabel pengelompokan event · **P1** (AUD-A-05, B-05)
- [ ] RV-M03-03 · Tabel "Mendefinisikan Proses" · **P1** (AUD-B-04, B-05)
- [ ] RV-M03-04 · Matriks balancing CD → L0 · **P1** (AUD-B-03)
- [ ] RV-M03-05 · Ganti gambar L0 · P2
- [ ] RV-M03-06 · Tabel audit kesalahan DFD terlalu optimis · P2
- [ ] RV-M03-07 · Nama proses 4 · P2 (BL-DFD-05)

---

### RV-M03-01 · Ikut revisi M02 · P1
RV-M02-02 sampai RV-M02-07 diterapkan juga ke bagian Identifikasi Event, Event Table, dan Context Diagram di M03.

### RV-M03-02 · Pengelompokan event · P1
- **Sekarang:** 3.0 menangani "EV-03, EV-04, EV-05, EV-06, EV-07" dengan store "Transaksi Peminjaman". Kolom event 4.0 kosong. Store kandidat 2.0 adalah "Data Koleksi Buku, Data Eksemplar".
- **Seharusnya:**

| Proses | Nama | Event | Data Store |
|---|---|---|---|
| 1 | Mengelola Keanggotaan | EV-01, EV-09 | D1 Data Anggota |
| 2 | Mengelola Katalog Koleksi | EV-02, EV-08 | D2 Data Koleksi |
| 3 | Memproses Sirkulasi dan Denda | EV-03, EV-04, EV-05 | D1, D2, D3 Transaksi Fisik |
| 4 | Membuat Laporan Transaksi Fisik* | EV-06, EV-07 | D2, D3 |

\* tunggu RV-M03-07.

### RV-M03-03 · Tabel "Mendefinisikan Proses" · P1

| Proses | Input | Output | Store dibaca | Store diubah | Event |
|---|---|---|---|---|---|
| 1 Mengelola Keanggotaan | dataPendaftaran, statusKeaktifan | statusPendaftaran, dataVerifikasi | — (D1 bila AUD-B-08 disetujui) | D1 | EV-01, EV-09 |
| 2 Mengelola Katalog Koleksi | dataPencarian, dataKoleksiBaru | informasiKoleksiBuku (+ statusPengelolaanKoleksi bila AUD-B-12) | D2 | D2 | EV-02, EV-08 |
| 3 Memproses Sirkulasi dan Denda | dataTransaksiFisik, permintaanPerpanjangan, catatanDenda | statusTransaksiDanBukti, buktiPengembalianDanDenda, statusPerpanjangan | D1, D2, D3 | D2, D3 | EV-03, EV-04, EV-05 |
| 4 Membuat Laporan Transaksi Fisik | permintaanLaporan | laporanBulanan | D2, D3 | — | EV-06, EV-07 |

Kolom Tujuan tetap, kecuali proses 3: "mencatat dan memvalidasi peminjaman, pengembalian, perpanjangan, serta menghitung dan mencatat denda keterlambatan".

### RV-M03-04 · Matriks balancing CD → L0 · P1
- **Sekarang:** semua baris "Balanced / Persis sesuai Context" walaupun namanya berbeda. Tidak ada baris Konfirmasi Denda dan Laporan Operasional.
- **Seharusnya** (setelah CD digambar ulang):

| Entitas | Flow CD | Arah | Proses L0 | Flow L0 | Status |
|---|---|---|---|---|---|
| Anggota Perpustakaan | dataPendaftaran | Masuk | 1 | dataPendaftaran | Balanced |
| Anggota Perpustakaan | statusPendaftaran | Keluar | 1 | statusPendaftaran | Balanced |
| Anggota Perpustakaan | dataPencarian | Masuk | 2 | dataPencarian | Balanced |
| Anggota Perpustakaan | informasiKoleksiBuku | Keluar | 2 | informasiKoleksiBuku | Balanced |
| Anggota Perpustakaan | permintaanPerpanjangan | Masuk | 3 | permintaanPerpanjangan | Balanced |
| Anggota Perpustakaan | statusPerpanjangan | Keluar | 3 | statusPerpanjangan | Balanced |
| Petugas Perpustakaan | dataKoleksiBaru | Masuk | 2 | dataKoleksiBaru | Balanced |
| Petugas Perpustakaan | dataTransaksiFisik | Masuk | 3 | dataTransaksiFisik | Balanced |
| Petugas Perpustakaan | catatanDenda | Masuk | 3 | catatanDenda | Balanced |
| Petugas Perpustakaan | statusTransaksiDanBukti | Keluar | 3 | statusTransaksiDanBukti | Balanced |
| Petugas Perpustakaan | buktiPengembalianDanDenda | Keluar | 3 | buktiPengembalianDanDenda | Balanced |
| Kepala Perpustakaan | permintaanLaporan | Masuk | 4 | permintaanLaporan | Balanced |
| Kepala Perpustakaan | laporanBulanan | Keluar | 4 | laporanBulanan | Balanced |
| Sistem Akademik | dataVerifikasi | Keluar | 1 | dataVerifikasi | Balanced |
| Sistem Akademik | statusKeaktifan | Masuk | 1 | statusKeaktifan | Balanced |

Tambahkan catatan revisi: "Laporan Operasional dihapus karena tidak dihasilkan proses mana pun dan tidak berasal dari event".

### RV-M03-05 · Gambar L0 · P2
Ganti dengan ekspor `Silapus Latest.bpm` (diagram "DFD Level 0"), setelah flow tambahan AUD-B diterapkan.

### RV-M03-06 · Tabel audit kesalahan DFD · P2
- **Sekarang:** semua "Ya", termasuk "Flow lintas batas seimbang dengan context diagram" dan "Semua process memiliki input dan output yang logis".
- **Seharusnya:** jujur terhadap temuan. Contoh: baris CD↔L0 → "Tidak (v1): 8 nama berbeda, Laporan Operasional tanpa padanan → diperbaiki di v2". Dosen menilai audit dari bukti, bukan dari semuanya "Ya" (Modul 4 kriteria Audit 20%).

### RV-M03-07 · Nama proses 4 · P2
Pengelompokan di M03 sendiri memakai "Membuat Laporan Sirkulasi". Proses 3 sudah memakai "Sirkulasi". Rekomendasi: **Membuat Laporan Sirkulasi** (laporan juga berisi denda dan koleksi, bukan hanya transaksi fisik). Bila disetujui: ubah baseline lalu `.bpm`.
