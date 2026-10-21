# Audit Balancing Seluruh Modul + Rencana Perbaikan — 2026-10-21

PIC: Wildan · Dibantu AI (Claude): penelusuran dibuat dengan membandingkan isi PDF baseline, DFD master `Silapus Latest.bpm`, dan instruksi modul. Semua temuan **harus diverifikasi kelompok** sebelum diterapkan.

Sumber yang diaudit:
- M01 `baselines/PRPL_M01_...Charter-1.pdf`
- M02 `baselines/PRPL_M02_...EventContext-1.pdf` (entitas eksternal, event list, event table, CD)
- M03 `baselines/PRPL_M03_...DFD-2.pdf` (event, CD, pengelompokan, L0, matriks CD→L0, audit)
- M04 `baselines/PRPL_M04_...DFDDecomposition.pdf` + `Silapus Latest.bpm` (L0, L1-P2, L1-P3)
- M05 `baselines/PRPL_M05_...DataDictionary.pdf` (detail di `EVALUASI_DATA_DICTIONARY.md`)

Rantai yang diperiksa: **Event → Context Diagram → DFD Level 0 → DFD Level 1 → Kamus Data** (Modul 4 §1.4, Modul 5 §1.10, Modul 6 §1.13).

Prioritas:
- **P1:** wajib beres sebelum revisi M05 dan sebelum M06, karena memblokir keterlacakan.
- **P2:** perlu sebelum M06.
- **P3:** kerapian.

---

## A. Event (M02/M03) ↔ Context Diagram

| ID | Temuan berbasis bukti | Dampak | Rekomendasi | P |
|---|---|---|---|---|
| AUD-A-01 | **Bagian Keuangan** ada di M02 (EE-04, EV-09 "konfirmasi pembayaran denda"), tapi tidak ada di CD M02 maupun M03. M03 menghapusnya dari event list tanpa catatan revisi. Di M04 Daftar Koreksi No 1 alasannya masih "konfirmasi denda dilakukan oleh bagian keuangan". | Event tanpa flow, dan alasan revisi M04 bertentangan dengan diagram. | Pilih satu: **(a, disarankan)** hapus Bagian Keuangan dari M02 dan nyatakan pembayaran denda diterima petugas (`catatanDenda`), atau (b) masukkan kembali ke CD, L0, L1 dan kamus data. Lalu perbaiki alasan Daftar Koreksi No 1 M04. | P1 |
| AUD-A-02 | Nomor event tidak stabil. M02 punya EV-09 Bagian Keuangan dan EV-10 Sistem Akademik, sedangkan M03 punya EV-09 = Sistem Akademik. | Rujukan event di M06 (traceability) akan rancu. | Tetapkan daftar event final (EV-01..EV-09) dan pakai nomor yang sama di semua dokumen. | P2 |
| AUD-A-03 | Event table detail hanya ada untuk EV-01..EV-05. EV-06 (laporan diminta), EV-07 (laporan otomatis), EV-08 (kelola koleksi), dan EV-09 (update status akademik) tidak punya input/output/response/error condition. | Proses 2.2 dan 4 tidak punya sumber kebutuhan untuk process spec M06 (Modul 6 §3.6 butuh Event ID). | Lengkapi event table EV-06..EV-09. | P1 |
| AUD-A-04 | EV-09 "Sistem Akademik mengirim update status" tidak punya flow tersendiri. Di CD hanya ada `Status Keaktifan Mahasiswa`, yang di EV-01 merupakan jawaban atas verifikasi. | Event tidak terlacak ke DFD. | Nyatakan `statusKeaktifan` juga dipakai untuk pembaruan (Proses 1 lalu menulis `dataAnggota`), atau hapus event ini. Tulis keputusannya di event table. | P2 |
| AUD-A-05 | EV-07 (temporal, akhir bulan) tidak punya pemicu di DFD; Proses 4 hanya menerima `permintaanLaporan`. Di M03, tabel pengelompokan menaruh EV-06/EV-07 di proses 3.0, sementara kolom event proses 4.0 kosong. | Proses 4 tidak terlacak ke EV-06/07. | Perbaiki tabel pengelompokan (EV-06, EV-07 masuk Proses 4). Di process spec 4 jelaskan PeriodeLaporan diisi otomatis untuk EV-07 (sudah dicatat di kamus data v0.2). | P2 |
| AUD-A-06 | Ada error condition di luar cakupan sistem: EV-05 "buku sedang direservasi" (tidak ada fitur reservasi), EV-04 "pembayaran denda gagal dikonfirmasi" (terkait A-01), EV-03 "status anggota diblokir" (domain status tidak punya Diblokir). | Process spec akan memuat cabang yang tidak punya data. | Hapus atau ubah. Di kamus data v0.2 error condition dipetakan ke `AlasanPenolakan`. | P2 |
| AUD-A-07 | Tabel entitas eksternal M02 tidak sama dengan CD: Anggota tercatat menerima "Bukti Peminjaman" dan mengirim "Data Peminjaman"; Petugas menerima "Laporan Operasional"; nama flow Sistem Akademik berbeda/terbalik ("Informasi Keaktifan", "Status Permintaan Verifikasi"). | Tidak balance antara entitas eksternal dan CD. | Samakan tabel entitas eksternal dengan CD hasil revisi (B-01). | P2 |
| AUD-A-08 | Output EV-01 "ID Anggota Digital" tidak ada di CD/DFD. | Kecil. | Sudah ditangani sebagai alias `NomorIdentitas` di kamus data v0.2; cukup sebut di event table. | P3 |

## B. Context Diagram ↔ DFD Level 0 ↔ DFD Level 1

| ID | Temuan berbasis bukti | Dampak | Rekomendasi | P |
|---|---|---|---|---|
| AUD-B-01 | Delapan flow CD beda nama dengan L0: Informasi Katalog / `informasiKoleksiBuku`, Data Koleksi Buku / `dataKoleksiBaru`, Konfirmasi Denda / `catatanDenda`, Status Transaksi / `statusTransaksiDanBukti`, Laporan Bulanan Sirkulasi & Denda / `laporanBulanan`, Status Keaktifan Mahasiswa / `statusKeaktifan`, Data Verifikasi Mahasiswa / `dataVerifikasi`, plus format penulisan (spasi vs camelCase). | CD ↔ L0 tidak balance secara nama (Modul 4 kriteria Balancing). | Gambar ulang CD dengan nama baseline. Sebaiknya di PowerDesigner (file yang sama dengan DFD) supaya nama otomatis sama. | P1 |
| AUD-B-02 | CD punya flow **Laporan Operasional** (Sistem → Petugas) yang tidak ada di L0 dan tidak berasal dari event mana pun. | Output CD tanpa proses penghasil (L0 tidak balance). | Hapus dari CD dan dari tabel entitas eksternal. | P1 |
| AUD-B-03 | Matriks balancing CD→L0 di M03 menulis "Balanced / Persis sesuai Context" untuk flow yang namanya berbeda, dan tidak punya baris untuk Konfirmasi Denda serta Laporan Operasional. | Klaim balancing tidak sesuai bukti. | Isi ulang matriks setelah B-01/B-02. | P1 |
| AUD-B-04 | Nama proses tidak konsisten di dalam M03 sendiri: pengelompokan menulis "Memproses Sirkulasi dan Denda" dan "Membuat Laporan Sirkulasi", sedangkan tabel proses menulis "Memproses Transaksi Fisik dan Denda". | Identitas proses berbeda antar dokumen. | Baseline sekarang **Memproses Sirkulasi dan Denda**. Putuskan nama proses 4 (BL-DFD-05) lalu seragamkan M03, M04, M05. | P2 |
| AUD-B-05 | Tabel "Mendefinisikan Proses" M03: proses 4 hanya membaca Transaksi Fisik, padahal L0 juga membaca Data Koleksi (`dataKoleksi`). Kandidat store di pengelompokan (Data Koleksi Buku, Data Eksemplar, Transaksi Peminjaman, Arsip Laporan Bulanan) tidak sama dengan D1-D3. | Dokumen tidak sama dengan diagram. | Perbarui tabel proses dan kandidat store. | P2 |
| AUD-B-06 | L0 ↔ L1-P2 dan L0 ↔ L1-P3 di `.bpm` **sudah balance** sejak merge 2026-10-19. Tapi matriks di M04 baseline masih memakai nama lama dan berstatus "Tidak Balance". Baris "dataTransaksiFisik dipecah" dan "dataPeminjaman dipecah" hanya sah bila ada definisi komposit. | Matriks M04 tidak sama dengan diagram. | Isi ulang matriks M04 dengan nama baseline. Definisi komposit sudah ada di kamus data v0.2 (`dataTransaksiFisik`, `dataPeminjaman`), jadi tinggal dirujuk. | P1 |
| AUD-B-07 | **Gray hole di 3.1.** EV-03 menolak peminjaman bila kuota penuh atau anggota punya denda, tapi 3.1 hanya membaca `statusAnggota` (D1) dan `dataEksemplar` (D2). 3.1 tidak membaca D3, jadi jumlah pinjaman aktif dan denda tidak bisa diketahui. | Output penolakan tidak bisa dijelaskan dari input (Modul 4 §1.6). Process spec 3.1 tidak bisa ditulis. | Tambah flow baca `peminjamAktif` D3 → 3.1. Balance aman karena L0 sudah punya `peminjamAktif` D3 → 3. | P1 |
| AUD-B-08 | Proses 1 perlu menolak pendaftaran ganda (aturan M05 v0.1 "NIM yang sudah terdaftar tidak dapat mendaftar kembali"), tapi hanya **menulis** D1. | Aturan tidak punya sumber data. | Jadikan `dataAnggota` dua arah (baca + tulis), atau hapus aturan itu. | P2 |
| AUD-B-09 | 2.2 menerima JenisPerubahan Ubah/Hapus (EV-08) tapi tidak membaca D2. | Kecil; validasi "KodeEksemplar harus sudah ada" butuh baca. | Opsional: sisi 2.2 juga baca. Karena L0 `dataKoleksiBuku` sudah dua arah, balance tetap aman. | P3 |
| AUD-B-11 | **Gray hole di 3.3** (ditemukan 2026-10-21). Bila anggota membayar denda di lain waktu (bukan saat pengembalian), 3.3 hanya menerima `catatanDenda`. 3.3 tidak membaca D3, sehingga tidak tahu `JumlahDenda` untuk memvalidasi `JumlahDibayar = JumlahDenda`. | Aturan "tidak dicicil" tidak punya sumber data. | Tambah flow baca `peminjamAktif` D3 → 3.3 (balance aman). | P1 |
| AUD-B-12 | **Jalur gagal 2.2 tanpa output** (ditemukan 2026-10-21). Petugas mengirim `dataKoleksiBaru`, tetapi tidak ada flow balik ke Petugas. Bila KodeEksemplar duplikat atau eksemplar yang mau dihapus sedang dipinjam, sistem tidak bisa memberi tahu. Temuan ini sama jenisnya dengan yang kita berikan ke Kelompok 4 (VS-03), jadi harus kita perbaiki juga. | Event EV-08 tidak punya response yang terlihat. | Tambah flow `statusPengelolaanKoleksi` 2.2 → Petugas (dan 2 → Petugas di L0, serta di CD). | P2 |
| AUD-B-10 | Nama `dataKoleksiBaru` terlalu sempit karena EV-08 mencakup ubah/hapus. | Makna nama tidak sesuai isi. | Pertahankan nama (biaya rename tinggi), tapi jelaskan lewat `JenisPerubahan` di kamus data (sudah di v0.2). | P3 |

## C. DFD ↔ Kamus Data (M05)

Ringkasan dari `EVALUASI_DATA_DICTIONARY.md`:

| ID | Temuan | Rekomendasi | P | Status |
|---|---|---|---|---|
| AUD-C-01 | Inventaris M05 v0.1 hanya 12 dari 34 flow/store | Pakai inventaris v0.2 | P1 | ✅ draft v0.2 |
| AUD-C-02 | Nama di kamus ≠ DFD (`formTransaksiPinjam`, `buktiKonfirmasiDenda`, ...) | Nama = DFD, nama lama jadi alias | P1 | ✅ draft v0.2 |
| AUD-C-03 | Nomor proses salah (1.1, 3.3 ↔ 3.4) | Diperbaiki | P1 | ✅ draft v0.2 |
| AUD-C-04 | "Menguraikan Struktur Data" dan "Validasi Silang" kosong | Penguraian otomatis + validasi silang 3.1 | P1 | ✅ draft v0.2 |
| AUD-C-05 | Format bertentangan dengan contoh, `@` dipakai di flow, nama tabel fisik di alias, aturan di luar cakupan | Diperbaiki | P1 | ✅ draft v0.2 |
| AUD-C-06 | Aturan bisnis tanpa sumber (7 hari, Rp1.000, maks perpanjangan) | TBD-01, TBD-07 | P2 | ⏳ keputusan kelompok |

## D. Konsistensi Dokumen (M04 baseline)

| ID | Temuan | Rekomendasi | P |
|---|---|---|---|
| AUD-D-01 | Daftar Koreksi No 3 "Kriteria pencarian dipertahankan" bertentangan dengan AUD-02 dan peer review yang menghapusnya | Ubah jadi "dihapus" (BL-M04-02) | P1 |
| AUD-D-02 | Lembar Audit masih "Open / Closed" dan isinya bergeser antar baris di PDF | Isi status nyata, rapikan tabel (BL-M04-07) | P1 |
| AUD-D-03 | Bagian "Hasil Peer Review dari Kelompok Lain" masih placeholder ("... hasil evaluasi dari kelompok") | Isi dengan `catatan peer review.txt` + respons (`TEMUAN_DAN_REVISI.md` bagian A) | P1 |
| AUD-D-04 | Kolom Sintaks/Semantik/Balancing/Keterbacaan pada review untuk Kelompok 4 kosong | Diisi di dokumen validasi silang (lihat `validasi-silang/`) | P1 |
| AUD-D-05 | Tidak ada identitas versi / tanggal / penyusun / reviewer / status validasi, padahal ini wajib di setiap artefak (aturan kerja Batch 2) | Tambah tabel identitas & revision history di M04, M05, M06 | P1 |
| AUD-D-06 | Pertanyaan refleksi M04 belum dijawab, `_Source.zip` & `_Review.pdf` belum ada | BL-M04-10, BL-M04-11 | P2 |

---

## Rencana Perbaikan

### Fase 1 — malam ini / revisi M05
| Langkah | Item | PIC (usulan) |
|---|---|---|
| 1 | Review kamus data v0.2 (`progress/PRPL_M05_2B_RajinBelajar_DataDictionary.xlsx`), terutama keputusan desain di EVALUASI bagian akhir | Semua |
| 2 | Cek penguraian atom & domain elemen | Zidan |
| 3 | Cocokkan list flow dengan hasil Gemini, lengkapi periode/volume | Irfan + Rere |
| 4 | Putuskan AUD-A-01 (Bagian Keuangan) dan AUD-B-07 (3.1 baca D3) | Semua |
| 5 | Pindahkan isi draft docx ke dokumen M05 utama + ekspor PDF | Wildan |

### Fase 2 — sebelum M06
| Langkah | Item |
|---|---|
| 6 | Terapkan B-07, B-11 (dan B-08, B-12 bila disetujui) di `Silapus Latest.bpm`, ekspor ulang diagram |
| 7 | Gambar ulang CD (B-01, B-02), lalu perbarui matriks CD→L0 (B-03) dan tabel entitas eksternal (A-07) |
| 8 | Lengkapi event table EV-06..EV-09 (A-03), rapikan nomor event (A-02), error condition (A-06), pengelompokan (A-05) |
| 9 | Perbarui dokumen M04: matriks (B-06), daftar koreksi (D-01), audit (D-02), peer review (D-03), identitas versi (D-05) |
| 10 | Tutup TBD-01..TBD-07 |

### Fase 3 — kerapian
B-09, B-10, A-08, nama proses 4 (B-04).

Catatan: setiap perubahan nama mengikuti alur di `CLAUDE.md`: baseline, lalu TEMUAN_DAN_REVISI, lalu `.bpm`, M04, M05, M06.
