# M06 — Process Specification (persiapan)

Belum dikerjakan. File ini berisi bekal supaya M06 langsung konsisten dengan DFD dan kamus data.

- [ ] RV-M06-01 · Inventaris proses primitif (tabel di bawah) · **P1**
- [ ] RV-M06-02 · Prasyarat: keputusan RV-M04-11 dan TBD-01 · **P1**
- [ ] RV-M06-03 · Pemilihan teknik per proses · **P1**
- [ ] RV-M06-04 · Paket uji dari contoh tidak valid kamus data · P2
- [ ] RV-M06-05 · Traceability matrix Event ↔ Proses ↔ Kamus ↔ Uji · P2

---

### RV-M06-01 · Inventaris proses primitif (Modul 6 Langkah 1)

| No | Nama | Input | Output | Store dibaca / ditulis | Event | Bentuk logika (usulan) |
|---|---|---|---|---|---|---|
| 1 | Mengelola Keanggotaan | dataPendaftaran, statusKeaktifan | statusPendaftaran, dataVerifikasi, dataAnggota | tulis D1 (baca D1 bila AUD-B-08) | EV-01, EV-09 | Decision table: kelengkapan × StatusAkademik × sudah terdaftar |
| 2.1 | Mencari Katalog Buku | dataPencarian, dataKoleksiBuku | informasiKoleksiBuku | baca D2 | EV-02 | Structured English |
| 2.2 | Mengelola Data Koleksi | dataKoleksiBaru | dataKoleksiBuku (+ statusPengelolaanKoleksi) | tulis D2 | EV-08 | Structured English dengan CASE JenisPerubahan |
| 3.1 | Memproses Peminjaman Buku | dataTransaksiPeminjaman, statusAnggota, dataEksemplar (+ peminjamAktif) | statusTransaksiDanBukti, pembaruanEksemplar, dataPeminjamanBaru | baca D1, D2 (+D3); tulis D2, D3 | EV-03 | **Decision table**: StatusAnggota × denda belum lunas × kuota × StatusEksemplar |
| 3.2 | Memproses Pengembalian Buku | dataTransaksiPengembalian, peminjamAktif | statusTransaksiDanBukti, pembaruanEksemplar, pembaruanPengembalian, dataKeterlambatan | baca D3; tulis D2, D3 | EV-04 | Structured English (FOR EACH KodeEksemplar) |
| 3.3 | Menghitung dan Mencatat Denda | dataKeterlambatan, catatanDenda (+ peminjamAktif) | buktiPengembalianDanDenda, dataDenda | tulis D3 (+ baca D3) | EV-04 | Structured English + decision tree (hitung vs bayar) |
| 3.4 | Memperpanjang Peminjaman | permintaanPerpanjangan, statusAnggota, peminjamAktif | statusPerpanjangan, pembaruanMasaPinjam | baca D1, D3; tulis D3 | EV-05 | **Decision tree**: pemilik? → aktif? → lewat jatuh tempo? → denda? → batas? |
| 4 | Membuat Laporan Transaksi Fisik | permintaanLaporan, dataTransaksi, dataKoleksi | laporanBulanan | baca D2, D3 | EV-06, EV-07 | Structured English |

Proses 2 dan 3 adalah induk, jadi **tidak** dibuatkan spec (Modul 6 §1.2).

### RV-M06-02 · Prasyarat · P1
- **3.1 dan 3.3:** tanpa flow `peminjamAktif`, logika kuota/denda tidak punya data. Modul 6 §1.1: spesifikasi tidak boleh memakai data yang tidak tersedia di DFD.
- **3.4:** butuh angka BatasPerpanjangan (TBD-01).
- **2.2:** tanpa output ke Petugas, exception tidak punya jalur keluar (Modul 6 kriteria Penanganan exception 10%).

### RV-M06-03 · Teknik · P1
Alasan pemilihan ditulis berdasarkan karakter logika (Modul 6 Langkah 2.4):
- 3.1 punya 4 kondisi independen, jadi decision table.
- 3.4 urutan pengecekannya penting, jadi decision tree.
- Sisanya dominan sekuensial, jadi Structured English.

### RV-M06-04 · Paket uji · P2
Ambil "Contoh Tidak Valid" dari sheet `5_Elemen` sebagai data uji jalur gagal. Contoh: `KodeEksemplar = SIL-0012`, `JumlahDibayar = 1000` saat denda 3000. Nilai batas: jatuh tempo = hari ini; JumlahPerpanjangan = BatasPerpanjangan.

### RV-M06-05 · Traceability · P2
Kolom: Event ID (RV-M02-02) | Process ID | Input/Output | Entri Kamus Data | Aturan Bisnis (sheet `8_Parameter`/TBD) | Kasus Uji | Status.
