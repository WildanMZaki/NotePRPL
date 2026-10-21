# M02 — Entitas Eksternal, Event List, Event Table, Context Diagram

File: `baselines/PRPL_M02_2B_RajinBelajar_EventContext-1.pdf` (event list dan CD juga diulang di M03, jadi revisinya diterapkan ke dua dokumen)

- [ ] RV-M02-01 · Putuskan nasib Bagian Keuangan · **P1** (AUD-A-01)
- [ ] RV-M02-02 · Tetapkan daftar event final EV-01..EV-09 · **P1** (AUD-A-02)
- [ ] RV-M02-03 · Tambah event table EV-06..EV-09 · **P1** (AUD-A-03)
- [ ] RV-M02-04 · Samakan nama input/output event table dengan DFD · **P1**
- [ ] RV-M02-05 · Gambar ulang Context Diagram · **P1** (AUD-B-01, B-02)
- [ ] RV-M02-06 · Perbarui matriks keterlacakan event ↔ CD · **P1**
- [ ] RV-M02-07 · Error condition di luar cakupan · P2 (AUD-A-06)
- [ ] RV-M02-08 · Tabel entitas eksternal ≠ CD · P2 (AUD-A-07)
- [ ] RV-M02-09 · Angka batas perpanjangan · P2 (TBD-01)
- [ ] RV-M02-10 · "ID Anggota Digital" · P3 (AUD-A-08)
- [ ] RV-M02-11 · Typo · P3

---

### RV-M02-01 · Bagian Keuangan · P1
- **Lokasi:** tabel Entitas Eksternal (EE-04), Identifikasi Event (EV-09)
- **Sekarang:** Bagian Keuangan ada sebagai entitas dan event, tapi tidak ada di CD M02, CD M03, DFD, maupun daftar stakeholder M01.
- **Rekomendasi (opsi a):** hapus EE-04 dan EV-09 Bagian Keuangan. Pembayaran denda diterima Petugas di meja layanan dan dicatat lewat `catatanDenda`. Opsi ini konsisten dengan M01 (stakeholder dan batasan "cash/non-cash"), CD, dan DFD.
- **Dampak:** alasan Daftar Koreksi No 1 di M04 (RV-M04-01), error condition EV-04 (RV-M02-07).

### RV-M02-02 · Daftar event final · P1
Pakai penomoran M03 (karena Bagian Keuangan dihapus):

| ID | Event | Jenis | Sumber | Proses |
|---|---|---|---|---|
| EV-01 | Anggota mengajukan pendaftaran anggota baru | F | Anggota Perpustakaan | 1 |
| EV-02 | Anggota melakukan pencarian koleksi buku | F | Anggota Perpustakaan | 2 (2.1) |
| EV-03 | Petugas mencatat peminjaman buku | F | Petugas Perpustakaan | 3 (3.1) |
| EV-04 | Petugas mencatat pengembalian buku | F | Petugas Perpustakaan | 3 (3.2, 3.3) |
| EV-05 | Anggota mengajukan perpanjangan peminjaman | F | Anggota Perpustakaan | 3 (3.4) |
| EV-06 | Kepala Perpustakaan meminta laporan bulanan | F | Kepala Perpustakaan | 4 |
| EV-07 | Sistem menghasilkan laporan bulanan otomatis | T | Waktu (hari kerja terakhir) | 4 |
| EV-08 | Petugas mengelola data koleksi buku | F | Petugas Perpustakaan | 2 (2.2) |
| EV-09 | Sistem Akademik mengirim pembaruan status akademik | F | Sistem Akademik | 1 |

Catatan: pembayaran denda yang terjadi terpisah dari pengembalian saat ini bagian dari EV-04 (flow `catatanDenda`). Kalau kelompok mau, boleh dijadikan event sendiri (EV-10 "Petugas mencatat pembayaran denda").

### RV-M02-03 · Event table EV-06..EV-09 · P1
Draf isi (nama sudah baseline):

**EV-06 Kepala Perpustakaan meminta laporan bulanan**
- Description: Kepala Perpustakaan meminta rekap sirkulasi, denda, dan koleksi untuk satu bulan.
- Inputs: `permintaanLaporan` (PeriodeLaporan)
- Outputs: `laporanBulanan`
- Frequency: sesuai kebutuhan, umumnya 1–2 kali per bulan
- Response: 1) terima PeriodeLaporan; 2) baca transaksi pada periode dari D3; 3) baca data eksemplar dari D2; 4) hitung ringkasan sirkulasi, denda, koleksi; 5) kirim `laporanBulanan`.
- Error: PeriodeLaporan di masa depan; format periode tidak valid.

**EV-07 Sistem menghasilkan laporan bulanan otomatis (temporal)**
- Trigger: hari kerja terakhir setiap bulan
- Inputs: — (PeriodeLaporan = bulan berjalan, diisi sistem)
- Outputs: `laporanBulanan`
- Response: sama dengan EV-06 langkah 2–5.
- Error: — (bila tidak ada transaksi, laporan tetap terbit dengan nilai 0).

**EV-08 Petugas mengelola data koleksi buku**
- Inputs: `dataKoleksiBaru` (JenisPerubahan + DataBuku + eksemplar)
- Outputs: *(saat ini tidak ada di DFD; lihat AUD-B-12, usulan `statusPengelolaanKoleksi`)*
- Response: 1) terima data; 2) CASE JenisPerubahan: Tambah → simpan eksemplar baru; Ubah → perbarui; Hapus → hapus bila tidak Dipinjam; 3) tulis ke D2.
- Error: KodeEksemplar sudah ada (Tambah); KodeEksemplar tidak ditemukan (Ubah/Hapus); eksemplar sedang Dipinjam (Hapus); data buku tidak lengkap.

**EV-09 Sistem Akademik mengirim pembaruan status akademik**
- Inputs: `statusKeaktifan` (NomorIdentitas + StatusAkademik)
- Outputs: — (perubahan D1 lewat `dataAnggota`)
- Response: 1) terima status; 2) cari anggota di D1; 3) StatusAkademik ≠ Aktif → StatusAnggota = Nonaktif, sebaliknya Aktif.
- Error: NomorIdentitas tidak terdaftar sebagai anggota (diabaikan).
- **Catatan:** EV-09 butuh Proses 1 membaca D1 (lihat AUD-B-08).

### RV-M02-04 · Nama input/output event table = DFD · P1

| Event | Sekarang | Seharusnya |
|---|---|---|
| EV-01 Inputs | Form Pendaftaran (NIM/NIP, Nama, Email, Program Studi) | `dataPendaftaran`; `statusKeaktifan` |
| EV-01 Outputs | Status Pendaftaran, Data Verifikasi Mahasiswa, ID Anggota Digital | `statusPendaftaran`, `dataVerifikasi` |
| EV-02 Inputs | Data Pencarian (judul/pengarang) | `dataPencarian` |
| EV-02 Outputs | Informasi Katalog (Daftar Buku, Lokasi Rak) | `informasiKoleksiBuku` |
| EV-03 Inputs | Data Transaksi Fisik (ID anggota, Kode buku) | `dataTransaksiPeminjaman` (bagian dari `dataTransaksiFisik`) |
| EV-03 Outputs | Status transaksi dan bukti peminjaman | `statusTransaksiDanBukti` |
| EV-04 Inputs | Data Transaksi Buku (Kode Eksemplar, Tanggal Pengembalian) | `dataTransaksiPengembalian`; `catatanDenda` (bila bayar). Catatan: tanggal diisi sistem. |
| EV-04 Outputs | Bukti pengembalian dan denda (jika ada), Status Transaksi | `statusTransaksiDanBukti`, `buktiPengembalianDanDenda` |
| EV-05 Inputs | Permintaan Perpanjangan (ID Anggota, ID Transaksi) | `permintaanPerpanjangan` |
| EV-05 Outputs | Status Perpanjangan, Tanggal Jatuh Tempo Baru | `statusPerpanjangan` (TanggalJatuhTempo baru ada di dalamnya) |

Response logis juga diselaraskan: EV-03 langkah 1 "ID Anggota dan Kode Buku" → "NomorIdentitas dan KodeEksemplar".

### RV-M02-05 · Gambar ulang Context Diagram · P1
Flow final (15). **Hapus "Laporan Operasional"**, tambah `statusPengelolaanKoleksi` bila AUD-B-12 disetujui.

| Entitas | Masuk ke sistem | Keluar dari sistem |
|---|---|---|
| Anggota Perpustakaan | dataPendaftaran, dataPencarian, permintaanPerpanjangan | statusPendaftaran, informasiKoleksiBuku, statusPerpanjangan |
| Petugas Perpustakaan | dataKoleksiBaru, dataTransaksiFisik, catatanDenda | statusTransaksiDanBukti, buktiPengembalianDanDenda |
| Kepala Perpustakaan | permintaanLaporan | laporanBulanan |
| Sistem Akademik | statusKeaktifan | dataVerifikasi |

Saran: gambar CD di PowerDesigner (diagram baru di `Silapus Latest.bpm`) supaya nama flow sama dengan DFD dan bisa dicek otomatis.

### RV-M02-06 · Matriks keterlacakan event ↔ CD · P1
Isi ulang dengan EV-01..EV-09 dan nama flow RV-M02-05. EV-07 tidak punya input CD (temporal), tulis "— (temporal)". EV-09 input `statusKeaktifan`.

### RV-M02-07 · Error condition di luar cakupan · P2

| Event | Sekarang | Seharusnya |
|---|---|---|
| EV-03 | Status anggota diblokir atau memiliki denda | Status anggota Nonaktif, atau memiliki denda belum lunas |
| EV-04 | Pembayaran denda gagal dikonfirmasi | Jumlah dibayar tidak sama dengan jumlah denda |
| EV-05 | Buku sedang direservasi oleh peminjam lain | **Hapus** (tidak ada fitur reservasi). Ganti: "Sudah lewat tanggal jatuh tempo" |

Daftar alasan penolakan di kamus data (`AlasanPenolakan`) mengikuti tabel ini.

### RV-M02-08 · Tabel entitas eksternal · P2

| Entitas | Sekarang | Seharusnya |
|---|---|---|
| Anggota: input | Data Pendaftaran, Data Pencarian, Permintaan Perpanjangan, **Data Peminjaman** | hapus "Data Peminjaman" (peminjaman diinput Petugas) |
| Anggota: output | ..., **Bukti Peminjaman** | hapus (bukti diterima Petugas dalam `statusTransaksiDanBukti`) |
| Petugas: output | ..., **Laporan Operasional** | hapus |
| Sistem Akademik | input "Informasi Keaktifan Mahasiswa", output "Status Permintaan Verifikasi" | dari sudut sistem: SILAPUS mengirim `dataVerifikasi`, menerima `statusKeaktifan` |
| Bagian Keuangan | EE-04 | hapus (RV-M02-01) |

### RV-M02-09 · Batas perpanjangan · P2
EV-05 error "misal: max 2 kali" → angka pasti setelah TBD-01 diputuskan. Kata "misal" tidak boleh ada di event table.

### RV-M02-10 · ID Anggota Digital · P3
Hapus dari output EV-01 atau sebutkan "NomorIdentitas sebagai identitas anggota, dikembalikan dalam statusPendaftaran".

### RV-M02-11 · Typo · P3
"peninjaman", "peminjakan", "tansaksi", "angggota", "mengalkulasi" (baku: mengkalkulasi/menghitung).
