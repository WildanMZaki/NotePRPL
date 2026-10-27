# Process Specification M06 — Draft v0.2 (2026-10-27)

Isi sama dengan `progress/PRPL_M06_2B_RajinBelajar_ProcessSpecification_draft.docx` (dibangkitkan dari `generator/m06_data.py`). Semua nama elemen sudah sesuai M05 di `updates/` (disesuaikan 2026-10-27).

## Menginventarisasi Proses Primitif

| No. Proses | Nama Proses | Input | Output | Store Dibaca atau Ditulis | Event Terkait | Bentuk Logika |
|---|---|---|---|---|---|---|
| 1 | Mengelola Keanggotaan | dataPendaftaran, statusKeaktifan | statusPendaftaran, dataVerifikasi | Baca: D1 Data Anggota (dataAnggota)<br>Tulis: D1 Data Anggota (dataAnggota) | EV-01, EV-09 | Decision table + Structured English |
| 2.1 | Mencari Katalog Buku | dataPencarian | informasiKoleksiBuku | Baca: D2 Data Koleksi (dataKoleksiBuku) | EV-02 | Structured English |
| 2.2 | Mengelola Data Koleksi | dataKoleksiBaru | statusPengelolaanKoleksi | Baca & Tulis: D2 Data Koleksi (dataKoleksiBuku) | EV-08 | Structured English (CASE) |
| 3.1 | Memproses Peminjaman Buku | dataTransaksiPeminjaman | statusTransaksiDanBukti | Baca: D1 (statusAnggota), D2 (dataEksemplar), D3 (peminjamAktif)<br>Tulis: D2 (pembaruanEksemplar), D3 (dataPeminjamanBaru) | EV-03 | Decision table + Structured English |
| 3.2 | Memproses Pengembalian Buku | dataTransaksiPengembalian | statusTransaksiDanBukti, dataKeterlambatan (ke 3.3) | Baca: D3 (peminjamAktif)<br>Tulis: D2 (pembaruanEksemplar), D3 (pembaruanPengembalian) | EV-04 | Structured English (FOR EACH) |
| 3.3 | Menghitung dan Mencatat Denda | dataKeterlambatan (dari 3.2), catatanDenda | buktiPengembalianDanDenda | Baca: D3 (peminjamAktif)<br>Tulis: D3 (dataDenda) | EV-04 | Structured English (CASE) |
| 3.4 | Memperpanjang Peminjaman | permintaanPerpanjangan | statusPerpanjangan | Baca: D1 (statusAnggota), D3 (peminjamAktif)<br>Tulis: D3 (pembaruanMasaPinjam) | EV-05 | Decision tree + Structured English |
| 4 | Membuat Laporan Sirkulasi | permintaanLaporan | laporanBulanan | Baca: D2 (dataKoleksi), D3 (dataTransaksi) | EV-06, EV-07 | Structured English |

Proses 2 (Mengelola Katalog Koleksi) dan Proses 3 (Memproses Sirkulasi dan Denda) tidak dibuatkan spesifikasi karena sudah dijelaskan oleh diagram anaknya (Modul 6 §1.2).

## Parameter dan Aturan Bisnis

| Parameter | Nilai | Sumber |
|---|---|---|
| LamaPinjam | 7 hari kalender | M05: aturan dataPeminjaman & elemen TanggalJatuhTempo |
| TarifDenda | Rp1.000 per hari per eksemplar | M05: elemen TotalDenda (kelipatan Rp1.000/hari) |
| KuotaPinjam | 3 eksemplar per anggota | M05 v0.1 (baseline): aturan formTransaksiPinjam; EV-03 error 3 |
| BatasPerpanjangan | 2 kali per transaksi | EV-05 error 1 |
| TambahanPerpanjangan | 7 hari dari TanggalJatuhTempo lama | Asumsi kelompok, sama dengan LamaPinjam (perlu dikonfirmasi) |

| ID | Aturan Bisnis | Sumber |
|---|---|---|
| BR-01 | Data pendaftaran wajib lengkap: NoIdentitas, NamaLengkap, ProgramStudi, EmailKampus. | EV-01 error 3; M05 dataPendaftaran |
| BR-02 | EmailKampus wajib memakai domain polban.ac.id. | M05 dataPendaftaran aturan 2 |
| BR-03 | NoIdentitas yang sudah terdaftar tidak dapat mendaftar kembali. | M05 dataPendaftaran aturan 3 |
| BR-04 | Pendaftaran hanya diterima bila StatusAkademik pada statusKeaktifan dari Sistem Akademik = Aktif. | EV-01 error 1-2; M05 dataPendaftaran aturan 1 |
| BR-05 | KodeBuku harus unik. | M05 dataKoleksiBaru aturan 1 |
| BR-06 | JumlahEksemplar minimal 1. | M05 dataKoleksiBaru aturan 3 |
| BR-07 | Eksemplar yang sedang dipinjam tidak boleh dihapus. | EV-08 error 3 |
| BR-08 | Hanya anggota dengan status Aktif yang boleh meminjam dan memperpanjang. | EV-03 error 1; EV-05 response 2; M05 dataTransaksiFisik aturan 2 |
| BR-09 | Anggota yang masih memiliki denda belum lunas atau pinjaman terlambat tidak boleh meminjam. | EV-03 error 1; M05 dataTransaksiPeminjaman aturan 1, peminjamAktif |
| BR-10 | Jumlah eksemplar yang dipinjam bersamaan maksimal 3 (KuotaPinjam). | EV-03 error 3; M05 dataTransaksiPeminjaman aturan 2 |
| BR-11 | Hanya eksemplar dengan StatusEksemplar = Tersedia yang dapat dipinjam. | EV-03 error 2; M05 dataEksemplar |
| BR-12 | TanggalJatuhTempo = TanggalPinjam + 7 hari (LamaPinjam). | M05 dataPeminjaman; elemen TanggalJatuhTempo |
| BR-13 | Eksemplar yang dikembalikan harus memiliki transaksi peminjaman aktif. | EV-04 error 1; M05 dataTransaksiPengembalian aturan 1 |
| BR-14 | Pengembalian terlambat bila TanggalKembali > TanggalJatuhTempo; JumlahHariTerlambat dihitung dalam hari kalender. | M05 dataKeterlambatan aturan 1-2 |
| BR-15 | TotalDenda = JumlahHariTerlambat x TarifDenda (Rp1.000). | M05 catatanDenda aturan 1; elemen TotalDenda |
| BR-16 | Denda dibayar lunas sekaligus: JumlahDibayar harus sama dengan TotalDenda. | M01 Batasan (tidak menerima hutang); EV-04 error 2 |
| BR-17 | Perpanjangan hanya untuk transaksi milik anggota yang mengajukan. | M05 permintaanPerpanjangan aturan 1 |
| BR-18 | Perpanjangan ditolak bila sudah lewat TanggalJatuhTempo atau anggota memiliki denda belum lunas. | EV-05 error 2-3; M05 permintaanPerpanjangan aturan 2 |
| BR-19 | Satu transaksi maksimal diperpanjang 2 kali (BatasPerpanjangan). | EV-05 error 1 |
| BR-20 | Perpanjangan menambah 7 hari dari TanggalJatuhTempo lama. | Asumsi kelompok (TambahanPerpanjangan) |
| BR-21 | Laporan merekap transaksi pada Periode yang diminta; Periode tidak boleh di masa depan. | EV-06 error 1; M05 laporanBulanan aturan 2 |
| BR-22 | Laporan otomatis dibuat pada hari kerja terakhir setiap bulan untuk bulan berjalan. | EV-07 |
| BR-23 | KondisiBuku Rusak atau Hilang saat pengembalian mengubah StatusEksemplar menjadi Rusak atau Hilang. | M05 dataTransaksiPengembalian aturan 3; elemen KondisiBuku |
| BR-24 | StatusKetersediaan = Tersedia bila minimal satu eksemplar berstatus Tersedia, selain itu Tidak Tersedia. | EV-02; M05 informasiKoleksiBuku aturan 2 |
| BR-25 | Pembaruan status dari Sistem Akademik hanya diterapkan pada NoIdentitas yang sudah menjadi anggota. | EV-09 error 1 |

## Memilih Bentuk Logika

| No. Proses | Karakter Logika | Bentuk Logika | Alasan Pemilihan |
|---|---|---|---|
| 1 | Tiga kondisi independen (kelengkapan data, sudah terdaftar, status dari Sistem Akademik) menentukan diterima/ditolak, ditambah jalur EV-09. | Decision table + Structured English | Decision table memastikan semua kombinasi kondisi pendaftaran tertangani; Structured English untuk urutan kirim-verifikasi-simpan dan jalur EV-09. |
| 2.1 | Sekuensial: baca kata kunci, cari, hitung ketersediaan per buku. | Structured English | Hanya satu percabangan (ada hasil atau tidak) dan satu perulangan. |
| 2.2 | Tiga jenis perubahan (Tambah, Ubah, Hapus) dengan validasi berbeda. | Structured English (CASE) | Pilihan jalur ditentukan satu nilai (JenisPerubahan), cocok dengan CASE. |
| 3.1 | Empat kondisi independen (status anggota, denda/terlambat, kuota, status eksemplar) menentukan hasil. | Decision table + Structured English | 16 kombinasi kondisi; decision table menjamin tidak ada kombinasi yang terlewat. Structured English untuk perulangan per eksemplar. |
| 3.2 | Sekuensial per eksemplar dengan satu keputusan (terlambat atau tidak). | Structured English (FOR EACH) | Logika dominan sekuensial dengan sedikit percabangan. |
| 3.3 | Dua pemicu berbeda (data keterlambatan dan catatan pembayaran) dengan validasi pembayaran. | Structured English (CASE) | Pemicu menentukan jalur; percabangan di tiap jalur sedikit. |
| 3.4 | Pemeriksaan berurutan: transaksi, status anggota, jatuh tempo, denda, batas perpanjangan. Pemeriksaan pertama yang gagal menentukan alasan penolakan. | Decision tree + Structured English | Urutan keputusan penting untuk menentukan alasan penolakan yang dikirim ke anggota. |
| 4 | Sekuensial: tentukan periode, ambil data, rekap. | Structured English | Tidak ada kombinasi kondisi yang rumit. |

## Menulis Process Specification

### Proses 1 Mengelola Keanggotaan

| Elemen | Isi |
|---|---|
| Nomor dan nama proses | 1 Mengelola Keanggotaan |
| Tujuan | Memverifikasi calon anggota ke Sistem Akademik, mencatat anggota baru, dan memperbarui status anggota dari Sistem Akademik. |
| Input | dataPendaftaran (dari Anggota Perpustakaan); statusKeaktifan (dari Sistem Akademik) |
| Output | dataVerifikasi (ke Sistem Akademik); statusPendaftaran (ke Anggota Perpustakaan) |
| Data store dibaca | D1 Data Anggota melalui dataAnggota (baca: cek NoIdentitas sudah terdaftar, cari anggota untuk EV-09) |
| Data store ditulis | D1 Data Anggota melalui dataAnggota (buat record anggota baru, ubah StatusKeaktifan) |
| Precondition | EV-01: Anggota mengirim formulir pendaftaran. EV-09: Sistem Akademik mengirim statusKeaktifan. |
| Postcondition | Berhasil: satu record anggota baru tersimpan di D1 dengan StatusKeaktifan = Aktif dan TanggalDaftar = tanggal hari ini; Anggota menerima statusPendaftaran Berhasil. Gagal: D1 tidak berubah; Anggota menerima statusPendaftaran Gagal beserta KeteranganGagal. EV-09: StatusKeaktifan anggota di D1 sama dengan data Sistem Akademik. |
| Aturan bisnis | BR-01, BR-02, BR-03, BR-04, BR-25 |
| Exception | Data tidak lengkap atau email bukan polban.ac.id → statusPendaftaran Gagal "Data pendaftaran tidak lengkap".<br>NoIdentitas sudah terdaftar → Gagal "NIM/NIP sudah terdaftar".<br>StatusAkademik = Tidak Terdaftar → Gagal "NIM/NIP tidak terdaftar di Sistem Akademik".<br>StatusAkademik = Nonaktif → Gagal "Status akademik tidak aktif".<br>EV-09 untuk NoIdentitas yang bukan anggota → diabaikan, D1 tidak berubah. |
| Referensi data | dataPendaftaran, dataVerifikasi, statusKeaktifan, statusPendaftaran, dataAnggota; elemen NoIdentitas, NamaLengkap, ProgramStudi, EmailKampus, StatusKeaktifan, StatusAkademik, TanggalDaftar, StatusHasil, KeteranganGagal |
| Bentuk logika dan alasan | Decision table (DT-1) untuk EV-01 + Structured English. Tiga kondisi independen menentukan hasil pendaftaran. |

**Structured English**

```
CASE pemicu
  CASE dataPendaftaran diterima (EV-01):
    READ dataPendaftaran (NoIdentitas, NamaLengkap, ProgramStudi, EmailKampus)
    VALIDATE kelengkapan data dan domain EmailKampus = polban.ac.id
    IF data tidak lengkap OR EmailKampus tidak valid THEN
      DISPLAY statusPendaftaran (StatusHasil = Gagal, KeteranganGagal = "Data pendaftaran tidak lengkap")
    ELSE
      READ dataAnggota FROM D1 Data Anggota WHERE NoIdentitas
      IF NoIdentitas ditemukan THEN
        DISPLAY statusPendaftaran (StatusHasil = Gagal, KeteranganGagal = "NIM/NIP sudah terdaftar")
      ELSE
        SEND dataVerifikasi (NoIdentitas, NamaLengkap, ProgramStudi, EmailKampus) TO Sistem Akademik
        READ statusKeaktifan FROM Sistem Akademik
        CASE StatusAkademik
          Aktif:
            CREATE dataAnggota (NoIdentitas, NamaLengkap, ProgramStudi, EmailKampus,
                                StatusKeaktifan = Aktif, TanggalDaftar = tanggal hari ini) IN D1 Data Anggota
            DISPLAY statusPendaftaran (StatusHasil = Berhasil, NoIdentitas, TanggalDaftar)
          Nonaktif:
            DISPLAY statusPendaftaran (StatusHasil = Gagal, KeteranganGagal = "Status akademik tidak aktif")
          Tidak Terdaftar:
            DISPLAY statusPendaftaran (StatusHasil = Gagal, KeteranganGagal = "NIM/NIP tidak terdaftar di Sistem Akademik")
        END CASE
      END IF
    END IF
  CASE statusKeaktifan diterima tanpa pendaftaran (EV-09):
    READ statusKeaktifan (NoIdentitas, StatusAkademik)
    READ dataAnggota FROM D1 Data Anggota WHERE NoIdentitas
    IF NoIdentitas ditemukan THEN
      UPDATE dataAnggota (StatusKeaktifan = StatusAkademik) IN D1 Data Anggota
    ELSE
      abaikan (tidak ada perubahan)
    END IF
END CASE
```

**Decision Table Proses 1 Mengelola Keanggotaan (EV-01)**

| Kondisi atau Tindakan | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| C1 Data lengkap dan EmailKampus valid | T | Y | Y | Y | Y |
| C2 NoIdentitas sudah terdaftar di D1 | - | Y | T | T | T |
| C3 StatusAkademik dari Sistem Akademik | - | - | Aktif | Nonaktif | Tidak Terdaftar |
| A1 Kirim dataVerifikasi ke Sistem Akademik |  |  | X | X | X |
| A2 Simpan dataAnggota ke D1 |  |  | X |  |  |
| A3 statusPendaftaran Berhasil |  |  | X |  |  |
| A4 statusPendaftaran Gagal + KeteranganGagal | X | X |  | X | X |
| Keterangan gagal | Data pendaftaran tidak lengkap | NIM/NIP sudah terdaftar | - | Status akademik tidak aktif | NIM/NIP tidak terdaftar di Sistem Akademik |

Pemeriksaan kelengkapan: Kombinasi: C1 (2) x C2 (2) x C3 (3) = 12. R1 menutup 6 (C1 = T), R2 menutup 3 (C1 = Y, C2 = Y), R3–R5 menutup 3 sisanya. Total 12, tidak ada aturan ganda atau bertentangan. Tanda '-' dipakai karena kondisi tersebut tidak diperiksa lagi setelah kondisi sebelumnya gagal.

### Proses 2.1 Mencari Katalog Buku

| Elemen | Isi |
|---|---|
| Nomor dan nama proses | 2.1 Mencari Katalog Buku |
| Tujuan | Menampilkan daftar koleksi yang cocok dengan kata kunci beserta status ketersediaannya. |
| Input | dataPencarian (dari Anggota Perpustakaan) |
| Output | informasiKoleksiBuku (ke Anggota Perpustakaan) |
| Data store dibaca | D2 Data Koleksi melalui dataKoleksiBuku (baca) |
| Data store ditulis | - |
| Precondition | Anggota memasukkan kata kunci pencarian. |
| Postcondition | Anggota menerima daftar buku yang cocok beserta StatusKetersediaan, atau pesan bahwa koleksi tidak ditemukan. D2 tidak berubah. |
| Aturan bisnis | BR-24 |
| Exception | KataKunci kosong → informasiKoleksiBuku berisi pesan "Kata kunci wajib diisi".<br>Tidak ada koleksi yang cocok → informasiKoleksiBuku berisi pesan "Koleksi tidak ditemukan".<br>Pencarian gagal diproses (timeout) → informasiKoleksiBuku berisi pesan "Pencarian gagal, silakan ulangi". |
| Referensi data | dataPencarian, dataKoleksiBuku, informasiKoleksiBuku; elemen KataKunci, KodeBuku, JudulBuku, Pengarang, Penerbit, TahunTerbit, Kategori, KodeEksemplar, StatusEksemplar, StatusKetersediaan |
| Bentuk logika dan alasan | Structured English. Sekuensial dengan satu percabangan dan satu perulangan. |

**Structured English**

```
READ dataPencarian (KataKunci)
IF KataKunci kosong THEN
  DISPLAY informasiKoleksiBuku (pesan "Kata kunci wajib diisi")
ELSE
  READ dataKoleksiBuku FROM D2 Data Koleksi
       WHERE JudulBuku OR Pengarang OR Kategori mengandung KataKunci
  IF tidak ada buku yang cocok THEN
    DISPLAY informasiKoleksiBuku (pesan "Koleksi tidak ditemukan")
  ELSE
    FOR EACH buku yang cocok DO
      CALCULATE jumlah eksemplar dengan StatusEksemplar = Tersedia
      IF jumlah >= 1 THEN
        StatusKetersediaan = Tersedia
      ELSE
        StatusKetersediaan = Tidak Tersedia
      END IF
      ADD (KodeBuku, JudulBuku, Pengarang, Penerbit, TahunTerbit, Kategori, StatusKetersediaan) TO informasiKoleksiBuku
    END FOR
    DISPLAY informasiKoleksiBuku
  END IF
END IF
```

### Proses 2.2 Mengelola Data Koleksi

| Elemen | Isi |
|---|---|
| Nomor dan nama proses | 2.2 Mengelola Data Koleksi |
| Tujuan | Menambah, mengubah, atau menghapus data buku dan eksemplarnya di katalog. |
| Input | dataKoleksiBaru (dari Petugas Perpustakaan) |
| Output | statusPengelolaanKoleksi (ke Petugas Perpustakaan) |
| Data store dibaca | D2 Data Koleksi melalui dataKoleksiBuku (baca: cek KodeBuku, cek eksemplar dipinjam) |
| Data store ditulis | D2 Data Koleksi melalui dataKoleksiBuku (buat, ubah, hapus) |
| Precondition | Petugas mengisi data koleksi dan memilih JenisPerubahan. |
| Postcondition | Berhasil: D2 berisi data buku sesuai perubahan; eksemplar baru berstatus Tersedia; Petugas menerima statusPengelolaanKoleksi Berhasil. Gagal: D2 tidak berubah; Petugas menerima Gagal beserta KeteranganGagal. |
| Aturan bisnis | BR-05, BR-06, BR-07 |
| Exception | Data tidak lengkap → Gagal "Data koleksi tidak lengkap".<br>Tambah dengan KodeBuku yang sudah ada → Gagal "Kode buku sudah terdaftar".<br>Tambah dengan JumlahEksemplar < 1 → Gagal "Jumlah eksemplar minimal 1".<br>Ubah/Hapus dengan KodeBuku tidak ditemukan → Gagal "Kode buku tidak ditemukan".<br>Hapus saat ada eksemplar berstatus Dipinjam → Gagal "Eksemplar sedang dipinjam". |
| Referensi data | dataKoleksiBaru, dataKoleksiBuku, statusPengelolaanKoleksi; elemen JenisPerubahan, KodeBuku, JudulBuku, Pengarang, Penerbit, TahunTerbit, ISBN, Kategori, JumlahEksemplar, LokasiRak, KodeEksemplar, StatusEksemplar, StatusHasil, KeteranganGagal |
| Bentuk logika dan alasan | Structured English dengan CASE. Jalur ditentukan satu nilai (JenisPerubahan). |

**Structured English**

```
READ dataKoleksiBaru (JenisPerubahan, KodeBuku, JudulBuku, Pengarang, Penerbit, TahunTerbit, ISBN, Kategori,
                    JumlahEksemplar, LokasiRak)
IF data wajib tidak lengkap THEN
  SEND statusPengelolaanKoleksi (StatusHasil = Gagal, KeteranganGagal = "Data koleksi tidak lengkap")
ELSE
  READ dataKoleksiBuku FROM D2 Data Koleksi WHERE KodeBuku
  CASE JenisPerubahan
    Tambah:
      IF KodeBuku ditemukan THEN
        SEND statusPengelolaanKoleksi (Gagal, "Kode buku sudah terdaftar")
      ELSE IF JumlahEksemplar < 1 THEN
        SEND statusPengelolaanKoleksi (Gagal, "Jumlah eksemplar minimal 1")
      ELSE
        CREATE dataKoleksiBuku (KodeBuku, JudulBuku, Pengarang, Penerbit, TahunTerbit, ISBN, Kategori) IN D2
        FOR EACH eksemplar ke-1 sampai JumlahEksemplar DO
          CREATE KodeEksemplar dengan StatusEksemplar = Tersedia, LokasiRak IN D2
        END FOR
        SEND statusPengelolaanKoleksi (StatusHasil = Berhasil, KodeBuku)
      END IF
    Ubah:
      IF KodeBuku tidak ditemukan THEN
        SEND statusPengelolaanKoleksi (Gagal, "Kode buku tidak ditemukan")
      ELSE
        UPDATE dataKoleksiBuku IN D2
        SEND statusPengelolaanKoleksi (StatusHasil = Berhasil, KodeBuku)
      END IF
    Hapus:
      IF KodeBuku tidak ditemukan THEN
        SEND statusPengelolaanKoleksi (Gagal, "Kode buku tidak ditemukan")
      ELSE IF ada eksemplar dengan StatusEksemplar = Dipinjam THEN
        SEND statusPengelolaanKoleksi (Gagal, "Eksemplar sedang dipinjam")
      ELSE
        DELETE dataKoleksiBuku dan seluruh eksemplarnya FROM D2
        SEND statusPengelolaanKoleksi (StatusHasil = Berhasil, KodeBuku)
      END IF
  END CASE
END IF
```

### Proses 3.1 Memproses Peminjaman Buku

| Elemen | Isi |
|---|---|
| Nomor dan nama proses | 3.1 Memproses Peminjaman Buku |
| Tujuan | Memvalidasi anggota dan eksemplar, lalu mencatat transaksi peminjaman baru. |
| Input | dataTransaksiPeminjaman (dari Petugas Perpustakaan); statusAnggota (D1); dataEksemplar (D2); peminjamAktif (D3) |
| Output | statusTransaksiDanBukti (ke Petugas Perpustakaan) |
| Data store dibaca | D1 Data Anggota (statusAnggota); D2 Data Koleksi (dataEksemplar); D3 Transaksi Fisik (peminjamAktif) |
| Data store ditulis | D2 Data Koleksi (pembaruanEksemplar: StatusEksemplar = Dipinjam); D3 Transaksi Fisik (dataPeminjamanBaru) |
| Precondition | Petugas memasukkan NoIdentitas dan 1 sampai 3 KodeEksemplar. |
| Postcondition | Setiap eksemplar yang lolos: satu transaksi baru di D3 (StatusTransaksi = Aktif, StatusDenda = Tanpa Denda, JumlahPerpanjangan = 0, TanggalJatuhTempo = TanggalPinjam + 7 hari) dan StatusEksemplar = Dipinjam di D2. Petugas menerima statusTransaksiDanBukti per eksemplar. Bila anggota ditolak, D2 dan D3 tidak berubah. |
| Aturan bisnis | BR-08, BR-09, BR-10, BR-11, BR-12 |
| Exception | statusAnggota ≠ Aktif → Gagal "Anggota tidak aktif".<br>Masih ada denda belum lunas atau pinjaman terlambat → Gagal "Masih memiliki denda atau pinjaman terlambat".<br>Pinjaman aktif + eksemplar diminta > 3 → Gagal "Kuota pinjam penuh".<br>StatusEksemplar ≠ Tersedia → eksemplar tersebut Gagal "Eksemplar tidak tersedia" (eksemplar lain tetap diproses). |
| Referensi data | dataTransaksiPeminjaman, statusAnggota, dataEksemplar, peminjamAktif, pembaruanEksemplar, dataPeminjamanBaru, statusTransaksiDanBukti; elemen NoIdentitas, KodeEksemplar, StatusKeaktifan, StatusEksemplar, StatusTransaksi, StatusDenda, IDTransaksi, NoBukti, TanggalPinjam, TanggalJatuhTempo, JumlahPerpanjangan, StatusHasil, KeteranganGagal |
| Bentuk logika dan alasan | Decision table (DT-2) + Structured English. Empat kondisi independen; Structured English untuk perulangan per eksemplar. |

**Structured English**

```
READ dataTransaksiPeminjaman (NoIdentitas, {KodeEksemplar})
READ statusAnggota FROM D1 Data Anggota WHERE NoIdentitas
READ peminjamAktif FROM D3 Transaksi Fisik WHERE NoIdentitas
IF statusAnggota ≠ Aktif THEN
  SEND statusTransaksiDanBukti (StatusHasil = Gagal, KeteranganGagal = "Anggota tidak aktif")
ELSE IF peminjamAktif memuat StatusDenda = Belum Lunas OR StatusTransaksi = Terlambat THEN
  SEND statusTransaksiDanBukti (StatusHasil = Gagal, KeteranganGagal = "Masih memiliki denda atau pinjaman terlambat")
ELSE IF (jumlah peminjamAktif dengan StatusTransaksi = Aktif) + (jumlah KodeEksemplar) > 3 THEN
  SEND statusTransaksiDanBukti (StatusHasil = Gagal, KeteranganGagal = "Kuota pinjam penuh")
ELSE
  FOR EACH KodeEksemplar DO
    READ dataEksemplar FROM D2 Data Koleksi WHERE KodeEksemplar
    IF StatusEksemplar ≠ Tersedia THEN
      ADD (KodeEksemplar, StatusHasil = Gagal, KeteranganGagal = "Eksemplar tidak tersedia") TO statusTransaksiDanBukti
    ELSE
      CREATE IDTransaksi dan NoBukti
      TanggalPinjam = tanggal hari ini
      CALCULATE TanggalJatuhTempo = TanggalPinjam + 7 hari
      WRITE dataPeminjamanBaru (IDTransaksi, NoIdentitas, KodeEksemplar, TanggalPinjam, TanggalJatuhTempo,
                                StatusTransaksi = Aktif, StatusDenda = Tanpa Denda, JumlahPerpanjangan = 0)
            TO D3 Transaksi Fisik
      UPDATE pembaruanEksemplar (KodeEksemplar, StatusEksemplar = Dipinjam) IN D2 Data Koleksi
      ADD (NoBukti, IDTransaksi, KodeEksemplar, TanggalJatuhTempo, StatusHasil = Berhasil) TO statusTransaksiDanBukti
    END IF
  END FOR
  SEND statusTransaksiDanBukti TO Petugas Perpustakaan
END IF
```

**Decision Table Proses 3.1 Memproses Peminjaman Buku (per eksemplar)**

| Kondisi atau Tindakan | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| C1 statusAnggota = Aktif | T | Y | Y | Y | Y |
| C2 Ada denda belum lunas atau pinjaman terlambat | - | Y | T | T | T |
| C3 Pinjaman aktif + eksemplar diminta <= 3 | - | - | T | Y | Y |
| C4 StatusEksemplar = Tersedia | - | - | - | T | Y |
| A1 Tulis dataPeminjamanBaru ke D3 |  |  |  |  | X |
| A2 Tulis pembaruanEksemplar (Dipinjam) ke D2 |  |  |  |  | X |
| A3 statusTransaksiDanBukti Berhasil (NoBukti, IDTransaksi, TanggalJatuhTempo) |  |  |  |  | X |
| A4 statusTransaksiDanBukti Gagal + KeteranganGagal | X | X | X | X |  |
| Keterangan gagal | Anggota tidak aktif | Masih memiliki denda atau pinjaman terlambat | Kuota pinjam penuh | Eksemplar tidak tersedia | - |

Pemeriksaan kelengkapan: Kombinasi: 2^4 = 16. R1 menutup 8 (C1 = T), R2 menutup 4, R3 menutup 2, R4 dan R5 masing-masing 1. Total 16, tidak ada aturan ganda atau bertentangan, dan setiap tindakan dijalankan oleh minimal satu aturan.

### Proses 3.2 Memproses Pengembalian Buku

| Elemen | Isi |
|---|---|
| Nomor dan nama proses | 3.2 Memproses Pengembalian Buku |
| Tujuan | Mencatat pengembalian eksemplar, memulihkan status eksemplar, dan meneruskan data keterlambatan. |
| Input | dataTransaksiPengembalian (dari Petugas Perpustakaan); peminjamAktif (D3) |
| Output | statusTransaksiDanBukti (ke Petugas Perpustakaan); dataKeterlambatan (ke 3.3) |
| Data store dibaca | D3 Transaksi Fisik (peminjamAktif) |
| Data store ditulis | D2 Data Koleksi (pembaruanEksemplar); D3 Transaksi Fisik (pembaruanPengembalian) |
| Precondition | Petugas memasukkan KodeEksemplar yang dikembalikan beserta KondisiBuku. |
| Postcondition | Transaksi terkait berstatus Selesai dengan TanggalKembali = tanggal hari ini; StatusEksemplar = Tersedia (atau Rusak/Hilang sesuai KondisiBuku); bila terlambat, dataKeterlambatan dikirim ke 3.3. |
| Aturan bisnis | BR-13, BR-14, BR-23 |
| Exception | Tidak ada transaksi aktif untuk KodeEksemplar → eksemplar tersebut Gagal "Data peminjaman aktif tidak ditemukan". |
| Referensi data | dataTransaksiPengembalian, peminjamAktif, pembaruanEksemplar, pembaruanPengembalian, dataKeterlambatan, statusTransaksiDanBukti; elemen KodeEksemplar, KondisiBuku, IDTransaksi, NoIdentitas, TanggalJatuhTempo, TanggalKembali, JumlahHariTerlambat, StatusTransaksi, StatusEksemplar, NoBukti, StatusHasil, KeteranganGagal |
| Bentuk logika dan alasan | Structured English dengan FOR EACH. Dominan sekuensial, satu keputusan keterlambatan per eksemplar. |

**Structured English**

```
READ dataTransaksiPengembalian ({KodeEksemplar + KondisiBuku})
FOR EACH KodeEksemplar DO
  READ peminjamAktif FROM D3 Transaksi Fisik
       WHERE KodeEksemplar AND StatusTransaksi IN (Aktif, Terlambat)
  IF transaksi tidak ditemukan THEN
    ADD (KodeEksemplar, StatusHasil = Gagal, KeteranganGagal = "Data peminjaman aktif tidak ditemukan") TO statusTransaksiDanBukti
  ELSE
    TanggalKembali = tanggal hari ini
    UPDATE pembaruanPengembalian (IDTransaksi, TanggalKembali, StatusTransaksi = Selesai) IN D3 Transaksi Fisik
    IF KondisiBuku = Baik THEN
      StatusEksemplar = Tersedia
    ELSE
      StatusEksemplar = KondisiBuku   (Rusak atau Hilang)
    END IF
    UPDATE pembaruanEksemplar (KodeEksemplar, StatusEksemplar) IN D2 Data Koleksi
    IF TanggalKembali > TanggalJatuhTempo THEN
      CALCULATE JumlahHariTerlambat = TanggalKembali - TanggalJatuhTempo (hari kalender)
      SEND dataKeterlambatan (IDTransaksi, NoIdentitas, KodeEksemplar, TanggalJatuhTempo, TanggalKembali,
                              JumlahHariTerlambat) TO 3.3
    END IF
    ADD (NoBukti, IDTransaksi, KodeEksemplar, TanggalKembali, StatusHasil = Berhasil) TO statusTransaksiDanBukti
  END IF
END FOR
SEND statusTransaksiDanBukti TO Petugas Perpustakaan
```

### Proses 3.3 Menghitung dan Mencatat Denda

| Elemen | Isi |
|---|---|
| Nomor dan nama proses | 3.3 Menghitung dan Mencatat Denda |
| Tujuan | Menghitung denda keterlambatan dan mencatat pelunasan denda. |
| Input | dataKeterlambatan (dari 3.2); catatanDenda (dari Petugas Perpustakaan); peminjamAktif (D3) |
| Output | buktiPengembalianDanDenda (ke Petugas Perpustakaan) |
| Data store dibaca | D3 Transaksi Fisik (peminjamAktif: transaksi dengan StatusDenda = Belum Lunas) |
| Data store ditulis | D3 Transaksi Fisik (dataDenda) |
| Precondition | Hitung: ada pengembalian terlambat dari 3.2. Bayar: Petugas menerima uang denda dari anggota. |
| Postcondition | Hitung: transaksi memiliki TotalDenda = JumlahHariTerlambat x Rp1.000 dan StatusDenda = Belum Lunas. Bayar: StatusDenda = Lunas dan TanggalBayar terisi. Petugas menerima buktiPengembalianDanDenda. |
| Aturan bisnis | BR-15, BR-16 |
| Exception | catatanDenda untuk transaksi tanpa denda belum lunas → buktiPengembalianDanDenda Gagal "Tidak ada denda yang perlu dibayar".<br>JumlahDibayar ≠ TotalDenda → Gagal "Jumlah pembayaran tidak sesuai dengan total denda". |
| Referensi data | dataKeterlambatan, catatanDenda, peminjamAktif, dataDenda, buktiPengembalianDanDenda; elemen IDTransaksi, NoIdentitas, KodeEksemplar, TanggalKembali, JumlahHariTerlambat, TarifDenda, TotalDenda, JumlahDibayar, TanggalBayar, StatusDenda, NoBukti, StatusHasil, KeteranganGagal |
| Bentuk logika dan alasan | Structured English dengan CASE. Pemicu (hitung atau bayar) menentukan jalur. |

**Structured English**

```
CASE pemicu
  CASE dataKeterlambatan diterima dari 3.2:
    READ dataKeterlambatan (IDTransaksi, NoIdentitas, KodeEksemplar, TanggalJatuhTempo, TanggalKembali, JumlahHariTerlambat)
    CALCULATE TotalDenda = JumlahHariTerlambat x TarifDenda (Rp1.000)
    UPDATE dataDenda (IDTransaksi, JumlahHariTerlambat, TotalDenda, StatusDenda = Belum Lunas) IN D3 Transaksi Fisik
    CREATE NoBukti
    SEND buktiPengembalianDanDenda (NoBukti, NoIdentitas, KodeEksemplar, TanggalKembali, TotalDenda,
                                    StatusDenda = Belum Lunas) TO Petugas Perpustakaan
  CASE catatanDenda diterima dari Petugas:
    READ catatanDenda (IDTransaksi, JumlahDibayar, TanggalBayar)
    READ peminjamAktif FROM D3 Transaksi Fisik WHERE IDTransaksi AND StatusDenda = Belum Lunas
    IF transaksi tidak ditemukan THEN
      SEND buktiPengembalianDanDenda (StatusHasil = Gagal, KeteranganGagal = "Tidak ada denda yang perlu dibayar")
    ELSE IF JumlahDibayar ≠ TotalDenda THEN
      SEND buktiPengembalianDanDenda (StatusHasil = Gagal, KeteranganGagal = "Jumlah pembayaran tidak sesuai dengan total denda")
    ELSE
      UPDATE dataDenda (IDTransaksi, StatusDenda = Lunas, TanggalBayar) IN D3 Transaksi Fisik
      CREATE NoBukti
      SEND buktiPengembalianDanDenda (NoBukti, NoIdentitas, KodeEksemplar, TotalDenda, StatusDenda = Lunas,
                                      TanggalBayar) TO Petugas Perpustakaan
    END IF
END CASE
```

### Proses 3.4 Memperpanjang Peminjaman

| Elemen | Isi |
|---|---|
| Nomor dan nama proses | 3.4 Memperpanjang Peminjaman |
| Tujuan | Memvalidasi permintaan perpanjangan dan memperbarui tanggal jatuh tempo. |
| Input | permintaanPerpanjangan (dari Anggota Perpustakaan); statusAnggota (D1); peminjamAktif (D3) |
| Output | statusPerpanjangan (ke Anggota Perpustakaan) |
| Data store dibaca | D1 Data Anggota (statusAnggota); D3 Transaksi Fisik (peminjamAktif) |
| Data store ditulis | D3 Transaksi Fisik (pembaruanMasaPinjam) |
| Precondition | Anggota mengajukan perpanjangan untuk satu IDTransaksi. |
| Postcondition | Berhasil: TanggalJatuhTempo bertambah 7 hari dan JumlahPerpanjangan bertambah 1 di D3; anggota menerima TanggalJatuhTempo baru. Gagal: D3 tidak berubah; anggota menerima alasan penolakan. |
| Aturan bisnis | BR-08, BR-17, BR-18, BR-19, BR-20 |
| Exception | IDTransaksi tidak ditemukan atau bukan milik NoIdentitas → Gagal "Transaksi tidak ditemukan".<br>statusAnggota ≠ Aktif → Gagal "Anggota tidak aktif".<br>Tanggal hari ini > TanggalJatuhTempo → Gagal "Sudah melewati tanggal jatuh tempo".<br>Ada denda belum lunas → Gagal "Memiliki denda aktif".<br>JumlahPerpanjangan >= 2 → Gagal "Batas perpanjangan tercapai". |
| Referensi data | permintaanPerpanjangan, statusAnggota, peminjamAktif, pembaruanMasaPinjam, statusPerpanjangan; elemen NoIdentitas, IDTransaksi, StatusKeaktifan, TanggalJatuhTempo, StatusDenda, JumlahPerpanjangan, StatusHasil, KeteranganGagal |
| Bentuk logika dan alasan | Decision tree (DTree-1) + Structured English. Urutan pemeriksaan menentukan alasan penolakan yang dikirim. |

**Structured English**

```
READ permintaanPerpanjangan (NoIdentitas, IDTransaksi)
READ peminjamAktif FROM D3 Transaksi Fisik WHERE NoIdentitas
IF IDTransaksi tidak ada di peminjamAktif THEN
  SEND statusPerpanjangan (StatusHasil = Gagal, KeteranganGagal = "Transaksi tidak ditemukan")
ELSE
  READ statusAnggota FROM D1 Data Anggota WHERE NoIdentitas
  IF statusAnggota ≠ Aktif THEN
    SEND statusPerpanjangan (Gagal, "Anggota tidak aktif")
  ELSE IF tanggal hari ini > TanggalJatuhTempo THEN
    SEND statusPerpanjangan (Gagal, "Sudah melewati tanggal jatuh tempo")
  ELSE IF peminjamAktif memuat StatusDenda = Belum Lunas THEN
    SEND statusPerpanjangan (Gagal, "Memiliki denda aktif")
  ELSE IF JumlahPerpanjangan >= 2 THEN
    SEND statusPerpanjangan (Gagal, "Batas perpanjangan tercapai")
  ELSE
    CALCULATE TanggalJatuhTempo = TanggalJatuhTempo + 7 hari
    CALCULATE JumlahPerpanjangan = JumlahPerpanjangan + 1
    UPDATE pembaruanMasaPinjam (IDTransaksi, TanggalJatuhTempo, JumlahPerpanjangan) IN D3 Transaksi Fisik
    SEND statusPerpanjangan (StatusHasil = Berhasil, IDTransaksi, TanggalJatuhTempo) TO Anggota Perpustakaan
  END IF
END IF
```

**Decision Tree Proses 3.4 Memperpanjang Peminjaman** (gambar: `progress/PRPL_M06_2B_RajinBelajar_DecisionTree_3.4.png`)

| Urutan | Pertanyaan | Bila Tidak | Bila Ya |
|---|---|---|---|
| 1 | IDTransaksi milik NoIdentitas dan masih aktif? | Gagal: Transaksi tidak ditemukan | lanjut |
| 2 | statusAnggota = Aktif? | Gagal: Anggota tidak aktif | lanjut |
| 3 | Tanggal hari ini <= TanggalJatuhTempo? | Gagal: Sudah melewati tanggal jatuh tempo | lanjut |
| 4 | Tidak ada denda belum lunas? | Gagal: Memiliki denda aktif | lanjut |
| 5 | JumlahPerpanjangan < 2? | Gagal: Batas perpanjangan tercapai | Berhasil: TanggalJatuhTempo + 7 hari, JumlahPerpanjangan + 1, kirim statusPerpanjangan |

### Proses 4 Membuat Laporan Sirkulasi

| Elemen | Isi |
|---|---|
| Nomor dan nama proses | 4 Membuat Laporan Sirkulasi |
| Tujuan | Merekap sirkulasi, keterlambatan, denda, dan buku terpopuler dalam satu periode bulanan untuk Kepala Perpustakaan. |
| Input | permintaanLaporan (dari Kepala Perpustakaan) atau pemicu waktu EV-07; dataTransaksi (D3); dataKoleksi (D2) |
| Output | laporanBulanan (ke Kepala Perpustakaan) |
| Data store dibaca | D3 Transaksi Fisik (dataTransaksi); D2 Data Koleksi (dataKoleksi) |
| Data store ditulis | - |
| Precondition | EV-06: Kepala Perpustakaan memilih Periode. EV-07: hari kerja terakhir bulan berjalan. |
| Postcondition | Kepala Perpustakaan menerima laporanBulanan untuk Periode tersebut. D2 dan D3 tidak berubah. |
| Aturan bisnis | BR-21, BR-22 |
| Exception | Periode tidak valid atau di masa depan → laporanBulanan berisi pesan "Periode laporan tidak valid" tanpa rekap.<br>Tidak ada transaksi pada Periode → laporan tetap dibuat dengan nilai 0. |
| Referensi data | permintaanLaporan, dataTransaksi, dataKoleksi, laporanBulanan; elemen Periode, IDTransaksi, KodeEksemplar, KodeBuku, JudulBuku, TanggalPinjam, TanggalKembali, TotalDenda, TotalDendaBulanan, TotalPeminjaman, TotalPengembalian, JumlahKeterlambatan, BukuPalingBanyakDipinjam, JumlahDipinjam |
| Bentuk logika dan alasan | Structured English. Dominan sekuensial dengan satu perulangan. |

**Structured English**

```
IF dipicu permintaanLaporan (EV-06) THEN
  READ permintaanLaporan (Periode)
  IF Periode tidak valid OR Periode di masa depan THEN
    DISPLAY laporanBulanan (pesan "Periode laporan tidak valid")
    STOP
  END IF
ELSE   (EV-07, hari kerja terakhir bulan berjalan)
  Periode = bulan dan tahun berjalan
END IF
READ dataTransaksi FROM D3 Transaksi Fisik WHERE TanggalPinjam atau TanggalKembali di dalam Periode
CALCULATE TotalPeminjaman = jumlah transaksi dengan TanggalPinjam di dalam Periode
CALCULATE TotalPengembalian = jumlah transaksi dengan TanggalKembali di dalam Periode
CALCULATE JumlahKeterlambatan = jumlah transaksi dengan TotalDenda > 0 di dalam Periode
CALCULATE TotalDendaBulanan = jumlah TotalDenda di dalam Periode
READ dataKoleksi FROM D2 Data Koleksi
FOR EACH KodeBuku DO
  CALCULATE JumlahDipinjam = jumlah transaksi pada Periode untuk eksemplar dari KodeBuku tersebut
END FOR
SELECT 10 KodeBuku dengan JumlahDipinjam terbesar sebagai BukuPalingBanyakDipinjam
DISPLAY laporanBulanan (Periode, TotalPeminjaman, TotalPengembalian, JumlahKeterlambatan, TotalDendaBulanan,
                        {BukuPalingBanyakDipinjam}) TO Kepala Perpustakaan
```

## Memvalidasi dengan Contoh Uji

Tanggal hari ini pada semua kasus uji = 2026-10-26 (Senin).

| ID Uji | Proses | Aturan atau Jalur | Data Uji | Hasil yang Diharapkan | Hasil Penelusuran | Status | Temuan |
|---|---|---|---|---|---|---|---|
| TC-01 | 1 | DT-1 R1 (BR-01) | NoIdentitas 251511099, NamaLengkap 'Budi Santoso', ProgramStudi 'D3 Teknik Informatika', EmailKampus kosong | statusPendaftaran Gagal 'Data pendaftaran tidak lengkap'; tidak ada dataVerifikasi; D1 tetap | IF data tidak lengkap → DISPLAY Gagal | Lulus | - |
| TC-02 | 1 | DT-1 R1 (BR-02) | Data lengkap, EmailKampus budi@gmail.com | statusPendaftaran Gagal 'Data pendaftaran tidak lengkap' | EmailKampus tidak valid → DISPLAY Gagal | Lulus | - |
| TC-03 | 1 | DT-1 R2 (BR-03) | NoIdentitas 251511088 (sudah ada di D1), data lengkap | statusPendaftaran Gagal 'NIM/NIP sudah terdaftar'; tidak ada dataVerifikasi | READ dataAnggota ditemukan → DISPLAY Gagal | Lulus | - |
| TC-04 | 1 | DT-1 R3 (BR-04) | NoIdentitas 251511099 belum terdaftar, data lengkap; Sistem Akademik membalas Aktif | dataVerifikasi terkirim; record baru di D1 (StatusKeaktifan Aktif, TanggalDaftar 2026-10-26); statusPendaftaran Berhasil | CASE Aktif → CREATE dataAnggota, DISPLAY Berhasil | Lulus | - |
| TC-05 | 1 | DT-1 R4 (BR-04) | Sama dengan TC-04, Sistem Akademik membalas Nonaktif | statusPendaftaran Gagal 'Status akademik tidak aktif'; D1 tetap | CASE Nonaktif → DISPLAY Gagal | Lulus | - |
| TC-06 | 1 | DT-1 R5 (BR-04) | NoIdentitas 999999999; Sistem Akademik membalas Tidak Terdaftar | statusPendaftaran Gagal 'NIM/NIP tidak terdaftar di Sistem Akademik' | CASE Tidak Terdaftar → DISPLAY Gagal | Lulus | Domain StatusAkademik ditambah nilai Tidak Terdaftar di M05 |
| TC-07 | 1 | EV-09 (BR-25) | statusKeaktifan dari Sistem Akademik: 251511088, Nonaktif | StatusKeaktifan anggota 251511088 di D1 menjadi Nonaktif | CASE EV-09 → UPDATE dataAnggota | Lulus | - |
| TC-08 | 1 | EV-09 exception (BR-25) | statusKeaktifan: 251511777 (bukan anggota), Aktif | Diabaikan; D1 tetap | NoIdentitas tidak ditemukan → abaikan | Lulus | - |
| TC-09 | 2.1 | Jalur normal (BR-24) | KataKunci 'basis data'; D2: 2 buku cocok, buku A 1 eksemplar Tersedia, buku B semua Dipinjam | informasiKoleksiBuku: buku A Tersedia, buku B Tidak Tersedia | FOR EACH → hitung eksemplar Tersedia | Lulus | - |
| TC-10 | 2.1 | Tidak ditemukan | KataKunci 'astronomi kuantum' (tidak ada di D2) | informasiKoleksiBuku berisi pesan 'Koleksi tidak ditemukan' | IF tidak ada yang cocok → DISPLAY pesan | Lulus | - |
| TC-11 | 2.1 | Exception kata kunci kosong | KataKunci '' | Pesan 'Kata kunci wajib diisi'; D2 tidak dibaca | IF KataKunci kosong → DISPLAY pesan | Lulus | - |
| TC-12 | 2.2 | Tambah normal (BR-05, BR-06) | Tambah, KodeBuku 101202 (belum ada), data lengkap, JumlahEksemplar 2, LokasiRak R03-B | 1 buku + 2 eksemplar Tersedia di D2; statusPengelolaanKoleksi Berhasil | CASE Tambah → CREATE + FOR EACH eksemplar | Lulus | - |
| TC-13 | 2.2 | Tambah duplikat (BR-05) | Tambah, KodeBuku 101202 (sudah ada) | Gagal 'Kode buku sudah terdaftar'; D2 tetap | KodeBuku ditemukan → Gagal | Lulus | - |
| TC-14 | 2.2 | Nilai batas JumlahEksemplar (BR-06) | Tambah, KodeBuku 101203, JumlahEksemplar 0 | Gagal 'Jumlah eksemplar minimal 1' | JumlahEksemplar < 1 → Gagal | Lulus | - |
| TC-15 | 2.2 | Ubah tidak ditemukan | Ubah, KodeBuku 999999 | Gagal 'Kode buku tidak ditemukan' | CASE Ubah, tidak ditemukan → Gagal | Lulus | - |
| TC-16 | 2.2 | Hapus saat dipinjam (BR-07) | Hapus, KodeBuku 101202, salah satu eksemplar Dipinjam | Gagal 'Eksemplar sedang dipinjam'; D2 tetap | CASE Hapus, ada Dipinjam → Gagal | Lulus | - |
| TC-17 | 2.2 | Exception data tidak lengkap | Tambah, JudulBuku kosong | Gagal 'Data koleksi tidak lengkap' | IF data wajib tidak lengkap → Gagal | Lulus | JenisPerubahan ditambahkan ke struktur dataKoleksiBaru M05 |
| TC-18 | 3.1 | DT-2 R1 (BR-08) | NoIdentitas 251511077 (Nonaktif), KodeEksemplar 101202-1 | Gagal 'Anggota tidak aktif'; D2, D3 tetap | statusAnggota ≠ Aktif → Gagal | Lulus | - |
| TC-19 | 3.1 | DT-2 R2 (BR-09) | Anggota Aktif dengan 1 transaksi StatusDenda Belum Lunas; minta 101202-1 | Gagal 'Masih memiliki denda atau pinjaman terlambat' | peminjamAktif memuat Belum Lunas → Gagal | Lulus | - |
| TC-20 | 3.1 | DT-2 R3 (BR-10) | Anggota Aktif, 2 pinjaman Aktif, minta 2 eksemplar (total 4) | Gagal 'Kuota pinjam penuh' | 2 + 2 > 3 → Gagal | Lulus | - |
| TC-21 | 3.1 | DT-2 R4 (BR-11) | Anggota Aktif tanpa pinjaman; minta 101202-2 (Dipinjam) | Eksemplar 101202-2 Gagal 'Eksemplar tidak tersedia' | StatusEksemplar ≠ Tersedia → Gagal per eksemplar | Lulus | - |
| TC-22 | 3.1 | DT-2 R5, nilai batas kuota (BR-10, BR-12) | Anggota Aktif, 1 pinjaman Aktif; minta 101202-1 dan 101203-1 (Tersedia); tanggal 2026-10-26 | 2 transaksi baru (TanggalJatuhTempo 2026-11-02, JumlahPerpanjangan 0); kedua eksemplar Dipinjam; bukti Berhasil | 1 + 2 = 3 tidak > 3 → FOR EACH WRITE + UPDATE | Lulus | - |
| TC-23 | 3.2 | Tepat waktu, nilai batas (BR-14) | 101202-1 Baik; TanggalJatuhTempo 2026-10-26; dikembalikan 2026-10-26 | Transaksi Selesai; eksemplar Tersedia; tidak ada dataKeterlambatan | TanggalKembali = TanggalJatuhTempo → tidak terlambat | Lulus | - |
| TC-24 | 3.2 | Terlambat (BR-14) | 101202-1 Baik; TanggalJatuhTempo 2026-10-23; dikembalikan 2026-10-26 | Transaksi Selesai; dataKeterlambatan ke 3.3 dengan JumlahHariTerlambat 3 | TanggalKembali > TanggalJatuhTempo → SEND dataKeterlambatan | Lulus | - |
| TC-25 | 3.2 | Exception tanpa transaksi (BR-13) | 999999-1 tidak sedang dipinjam | Gagal 'Data peminjaman aktif tidak ditemukan'; D2, D3 tetap | transaksi tidak ditemukan → Gagal | Lulus | - |
| TC-26 | 3.2 | Kondisi rusak (BR-23) | 101202-1 KondisiBuku Rusak, tepat waktu | Transaksi Selesai; StatusEksemplar Rusak | KondisiBuku ≠ Baik → StatusEksemplar = KondisiBuku | Lulus | Domain StatusEksemplar di M05 disatukan menjadi Tersedia, Dipinjam, Rusak, Hilang |
| TC-27 | 3.3 | Hitung denda (BR-15) | dataKeterlambatan JumlahHariTerlambat 3 | TotalDenda 3000, StatusDenda Belum Lunas di D3; buktiPengembalianDanDenda dikirim | CALCULATE 3 x 1.000 | Lulus | - |
| TC-28 | 3.3 | Bayar lunas (BR-16) | catatanDenda IDTransaksi TRX-20261019-001, JumlahDibayar 3000, TanggalBayar 2026-10-26; TotalDenda 3000 | StatusDenda Lunas, TanggalBayar 2026-10-26; bukti Lunas | JumlahDibayar = TotalDenda → UPDATE Lunas | Lulus | - |
| TC-29 | 3.3 | Bayar kurang (BR-16) | JumlahDibayar 1000; TotalDenda 3000 | Gagal 'Jumlah pembayaran tidak sesuai dengan total denda'; D3 tetap | JumlahDibayar ≠ TotalDenda → Gagal | Lulus | - |
| TC-30 | 3.3 | Exception tanpa denda | catatanDenda untuk transaksi StatusDenda Tanpa Denda | Gagal 'Tidak ada denda yang perlu dibayar' | transaksi Belum Lunas tidak ditemukan → Gagal | Lulus | - |
| TC-31 | 3.4 | DTree-1 berhasil (BR-19, BR-20) | IDTransaksi milik anggota Aktif; TanggalJatuhTempo 2026-10-30; JumlahPerpanjangan 0; tanpa denda; tanggal 2026-10-26 | TanggalJatuhTempo 2026-11-06; JumlahPerpanjangan 1; statusPerpanjangan Berhasil | semua pemeriksaan lolos → UPDATE pembaruanMasaPinjam | Lulus | - |
| TC-32 | 3.4 | Nilai batas JumlahPerpanjangan = 1 (BR-19) | Sama dengan TC-31 tetapi JumlahPerpanjangan 1 | Berhasil; JumlahPerpanjangan menjadi 2 | 1 < 2 → Berhasil | Lulus | - |
| TC-33 | 3.4 | Batas tercapai (BR-19) | JumlahPerpanjangan 2 | Gagal 'Batas perpanjangan tercapai' | 2 >= 2 → Gagal | Lulus | - |
| TC-34 | 3.4 | Nilai batas jatuh tempo hari ini (BR-18) | TanggalJatuhTempo 2026-10-26; tanggal 2026-10-26 | Berhasil (belum lewat jatuh tempo) | hari ini > jatuh tempo bernilai salah → lanjut | Lulus | - |
| TC-35 | 3.4 | Lewat jatuh tempo (BR-18) | TanggalJatuhTempo 2026-10-25; tanggal 2026-10-26 | Gagal 'Sudah melewati tanggal jatuh tempo' | hari ini > jatuh tempo → Gagal | Lulus | - |
| TC-36 | 3.4 | Ada denda (BR-18) | Anggota punya transaksi lain dengan StatusDenda Belum Lunas | Gagal 'Memiliki denda aktif' | peminjamAktif memuat Belum Lunas → Gagal | Lulus | - |
| TC-37 | 3.4 | Anggota tidak aktif (BR-08) | statusAnggota Nonaktif | Gagal 'Anggota tidak aktif' | statusAnggota ≠ Aktif → Gagal | Lulus | - |
| TC-38 | 3.4 | Bukan pemilik (BR-17) | IDTransaksi milik anggota lain | Gagal 'Transaksi tidak ditemukan' | IDTransaksi tidak ada di peminjamAktif → Gagal | Lulus | - |
| TC-39 | 4 | EV-06 normal (BR-21) | permintaanLaporan Periode 2026-10; D3 berisi 120 peminjaman, 110 pengembalian, 8 terlambat, total denda 24000 | laporanBulanan: TotalPeminjaman 120, TotalPengembalian 110, JumlahKeterlambatan 8, TotalDenda 24000, 10 buku terpopuler | READ + CALCULATE + SELECT 10 | Lulus | - |
| TC-40 | 4 | Exception periode masa depan (BR-21) | Periode 2026-12; tanggal 2026-10-26 | laporanBulanan berisi pesan 'Periode laporan tidak valid' | Periode di masa depan → DISPLAY pesan, STOP | Lulus | - |
| TC-41 | 4 | EV-07 tanpa transaksi (BR-22) | Pemicu waktu 2026-10-30; D3 tidak punya transaksi Oktober | laporanBulanan Periode 2026-10 dengan semua nilai 0 | Periode = bulan berjalan; jumlah 0 | Lulus | - |

## Traceability Review

| Event ID | Process ID | Input atau Output | Entri Kamus Data | Aturan Bisnis | Kasus Uji | Status |
|---|---|---|---|---|---|---|
| EV-01 | 1 | In: dataPendaftaran | dataPendaftaran | BR-01, BR-02, BR-03 | TC-01..03 | Terlacak |
| EV-01 | 1 | Out: dataVerifikasi | dataVerifikasi | BR-04 | TC-04..06 | Terlacak |
| EV-01, EV-09 | 1 | In: statusKeaktifan | statusKeaktifan | BR-04, BR-25 | TC-04..08 | Terlacak |
| EV-01 | 1 | Out: statusPendaftaran | statusPendaftaran | BR-01..04 | TC-01..06 | Terlacak |
| EV-01, EV-09 | 1 | Baca/Tulis: dataAnggota (D1) | dataAnggota | BR-03, BR-25 | TC-03, TC-04, TC-07 | Terlacak |
| EV-02 | 2.1 | In: dataPencarian | dataPencarian | - | TC-09..11 | Terlacak |
| EV-02 | 2.1 | Baca: dataKoleksiBuku (D2) | dataKoleksiBuku | BR-24 | TC-09 | Terlacak |
| EV-02 | 2.1 | Out: informasiKoleksiBuku | informasiKoleksiBuku | BR-24 | TC-09..11 | Terlacak |
| EV-08 | 2.2 | In: dataKoleksiBaru | dataKoleksiBaru | BR-05, BR-06 | TC-12..17 | Terlacak |
| EV-08 | 2.2 | Baca/Tulis: dataKoleksiBuku (D2) | dataKoleksiBuku | BR-05, BR-07 | TC-12..16 | Terlacak |
| EV-08 | 2.2 | Out: statusPengelolaanKoleksi | statusPengelolaanKoleksi | BR-05..07 | TC-12..17 | Terlacak |
| EV-03 | 3.1 | In: dataTransaksiPeminjaman | dataTransaksiPeminjaman | BR-10 | TC-18..22 | Terlacak |
| EV-03 | 3.1 | Baca: statusAnggota (D1) | statusAnggota | BR-08 | TC-18 | Terlacak |
| EV-03 | 3.1 | Baca: peminjamAktif (D3) | peminjamAktif | BR-09, BR-10 | TC-19, TC-20, TC-22 | Terlacak |
| EV-03 | 3.1 | Baca: dataEksemplar (D2) | dataEksemplar | BR-11 | TC-21, TC-22 | Terlacak |
| EV-03 | 3.1 | Tulis: pembaruanEksemplar (D2) | pembaruanEksemplar | BR-11 | TC-22 | Terlacak |
| EV-03 | 3.1 | Tulis: dataPeminjamanBaru (D3) | dataPeminjamanBaru | BR-12 | TC-22 | Terlacak |
| EV-03, EV-04 | 3.1, 3.2 | Out: statusTransaksiDanBukti | statusTransaksiDanBukti | BR-08..13 | TC-18..25 | Terlacak |
| EV-04 | 3.2 | In: dataTransaksiPengembalian | dataTransaksiPengembalian | BR-13, BR-23 | TC-23..26 | Terlacak |
| EV-04 | 3.2 | Baca: peminjamAktif (D3) | peminjamAktif | BR-13 | TC-23..25 | Terlacak |
| EV-04 | 3.2 | Tulis: pembaruanPengembalian (D3) | pembaruanPengembalian | BR-13 | TC-23, TC-24 | Terlacak |
| EV-04 | 3.2 | Tulis: pembaruanEksemplar (D2) | pembaruanEksemplar | BR-23 | TC-26 | Terlacak |
| EV-04 | 3.2 → 3.3 | Internal: dataKeterlambatan | dataKeterlambatan | BR-14 | TC-24, TC-27 | Terlacak |
| EV-04 | 3.3 | In: catatanDenda | catatanDenda | BR-16 | TC-28..30 | Terlacak |
| EV-04 | 3.3 | Baca: peminjamAktif (D3) | peminjamAktif | BR-16 | TC-28..30 | Terlacak |
| EV-04 | 3.3 | Tulis: dataDenda (D3) | dataDenda | BR-15, BR-16 | TC-27, TC-28 | Terlacak |
| EV-04 | 3.3 | Out: buktiPengembalianDanDenda | buktiPengembalianDanDenda | BR-15, BR-16 | TC-27..30 | Terlacak |
| EV-05 | 3.4 | In: permintaanPerpanjangan | permintaanPerpanjangan | BR-17 | TC-31..38 | Terlacak |
| EV-05 | 3.4 | Baca: statusAnggota (D1), peminjamAktif (D3) | statusAnggota, peminjamAktif | BR-08, BR-18 | TC-35..37 | Terlacak |
| EV-05 | 3.4 | Tulis: pembaruanMasaPinjam (D3) | pembaruanMasaPinjam | BR-19, BR-20 | TC-31, TC-32 | Terlacak |
| EV-05 | 3.4 | Out: statusPerpanjangan | statusPerpanjangan | BR-17..20 | TC-31..38 | Terlacak |
| EV-06, EV-07 | 4 | In: permintaanLaporan | permintaanLaporan | BR-21, BR-22 | TC-39..41 | Terlacak |
| EV-06, EV-07 | 4 | Baca: dataTransaksi (D3), dataKoleksi (D2) | dataTransaksi, dataKoleksi | BR-21 | TC-39, TC-41 | Terlacak |
| EV-06, EV-07 | 4 | Out: laporanBulanan | laporanBulanan | BR-21, BR-22 | TC-39..41 | Terlacak |

## Revision History

| Versi | Tanggal | Artefak atau Bagian | Perubahan | Alasan | Penyusun | Reviewer |
|---|---|---|---|---|---|---|
| 0.1 | 2026-10-26 | Seluruh dokumen | Draf awal: inventaris proses primitif, 8 process specification, 2 decision table, 1 decision tree, 41 kasus uji, traceability | Modul 6 | Wildan (dibantu AI) |  |
| 0.2 | 2026-10-27 | Spesifikasi, uji, traceability | Nama elemen disamakan dengan M05 yang sudah disesuaikan (JudulBuku, StatusAkademik, StatusKeaktifan, TotalDendaBulanan, StatusHasil Gagal); status traceability menjadi Terlacak | Kamus data M05 diperbarui | Wildan (dibantu AI) |  |

## Pertanyaan Refleksi

1. **Proses apa yang paling cocok menggunakan decision table dan mengapa?**
   Proses 3.1 Memproses Peminjaman Buku. Hasilnya ditentukan empat kondisi independen (status anggota, denda/terlambat, kuota, status eksemplar) yang membentuk 16 kombinasi. Decision table memastikan setiap kombinasi punya tindakan dan tidak ada aturan yang bertentangan. Proses 1 juga memakai decision table karena tiga kondisinya menentukan diterima atau ditolaknya pendaftaran.

2. **Apakah ada input-output DFD yang tidak diperlukan saat menulis spesifikasi, atau data yang dibutuhkan tetapi belum tersedia?**
   Ada data yang dibutuhkan tetapi belum tersedia. Saat menulis spesifikasi ditemukan bahwa 3.1 dan 3.3 perlu membaca Transaksi Fisik (kuota, denda), 2.2 perlu membaca Data Koleksi (kode buku unik), Proses 1 perlu membaca Data Anggota (pendaftaran ganda), dan 2.2 tidak punya output ke Petugas. DFD kemudian direvisi (AUD-04 s.d. AUD-08 di Modul 4). Beberapa elemen juga perlu ditambahkan ke kamus data, misalnya JumlahPerpanjangan dan StatusDenda pada data transaksi.

3. **Bagaimana process specification membantu transisi dari analisis kebutuhan menuju desain dan pengujian?**
   Process specification mengubah aturan bisnis dari event table dan kamus data menjadi langkah logika yang pasti, sehingga perancang tahu urutan validasi dan data yang dibaca atau ditulis. Setiap aturan pada decision table dan setiap cabang decision tree langsung menjadi kasus uji, dan domain elemen dari kamus data memberi nilai batas serta contoh tidak valid untuk pengujian.
