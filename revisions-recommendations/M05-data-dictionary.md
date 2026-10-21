# M05 — Kamus Data

File dikumpulkan (v0.1): `baselines/PRPL_M05_2B_RajinBelajar_DataDictionary.pdf`
Draft perbaikan (v0.2): `progress/PRPL_M05_2B_RajinBelajar_DataDictionary.xlsx` + `..._draft.docx`, dibangkitkan dari `manajemen/generator/m05_data.py`
Detail evaluasi: [`../EVALUASI_DATA_DICTIONARY.md`](../EVALUASI_DATA_DICTIONARY.md) (K-01..K-17)

- [x] RV-M05-01 · Susun ulang inventaris, entri komposit, store, penguraian, elemen, alias, TBD · **P1** (draft v0.2)
- [ ] RV-M05-02 · Review keputusan desain v0.2 · **P1**
- [ ] RV-M05-03 · Pindahkan draft ke dokumen utama + ekspor PDF · **P1**
- [ ] RV-M05-04 · Tambah bagian Validasi Silang di dokumen · **P1**
- [ ] RV-M05-05 · Identitas versi + revision history + `_Review.pdf` · **P1**
- [ ] RV-M05-06 · Tutup TBD-01..07 · P2
- [ ] RV-M05-07 · Sinkronkan setelah flow DFD tambahan disetujui · P2
- [ ] RV-M05-08 · Hapus alias "(CD)" setelah CD direvisi · P2
- [ ] RV-M05-09 · Refleksi Modul 5 + hapus xlsx lama `Kelompok6` · P3

**Tambahan dari cek `updates/` 2026-10-21 (v0.1b):**
- [ ] RV-M05-20 · Putuskan basis dokumen: lanjut v0.1b atau pindah ke v0.2 · **P1** (keputusan)
- [ ] RV-M05-10 · `catatanDenda` arah & maknanya terbalik · **P1**
- [ ] RV-M05-11 · Hapus entri basi `infoKatalog/Ketersediaan` · **P1**
- [ ] RV-M05-12 · Store D1–D3 hilang dari inventaris, tanpa entri store · **P1**
- [ ] RV-M05-13 · Penguraian masih pakai nama lama & beda isi dengan entri · **P1**
- [ ] RV-M05-14 · Satu konsep banyak nama · **P1**
- [ ] RV-M05-16 · `dataTransaksiFisik` belum jadi [peminjaman \| pengembalian]; kardinalitas buku tidak konsisten · **P1**
- [ ] RV-M05-17 · Flow bertanda "Elementer" tidak didefinisikan di mana pun · **P1**
- [ ] RV-M05-15 · `@` di hampir semua flow · P2
- [ ] RV-M05-18 · Elemen baru belum ada di tabel elemen · P2
- [ ] RV-M05-19 · Nilai hitungan sistem dijadikan input; `IDPetugas` tidak tersimpan · P2

---

### RV-M05-02 · Keputusan desain yang perlu disetujui · P1

| Keputusan | Pilihan di v0.2 | Alternatif | Dasar |
|---|---|---|---|
| Identitas anggota | `NomorIdentitas = [NIM \| NIP]` | NIM saja | EV-01 & asumsi M01 "mahasiswa atau dosen" (TBD-03) |
| Satuan transaksi | 1 IDTransaksi = 1 eksemplar; kuota dihitung dari transaksi aktif | 1 transaksi banyak eksemplar | Perpanjangan & denda per buku jadi sederhana |
| StatusAnggota | [Aktif \| Nonaktif]; denda dicek dari D3 | tambah "Diblokir" | Tidak ada proses yang menulis status blokir ke D1 |
| Format kode | `SIL-BK-0012`, `TRX-20261019-001` | — | Contoh dari v0.1, panjang diperbaiki |
| Kedalaman penguraian | sampai elemen dasar (angka/huruf), seperti Kelompok 4 | berhenti di elemen elementer | Lihat catatan di bawah |

**Catatan kedalaman penguraian (jawaban pertanyaan 2026-10-21):**
- Modul 5 **mewajibkan** penguraian sampai **elemen elementer yang bermakna**. Acuannya: §1.4 "setiap struktur harus dapat diuraikan sampai elemen elementer", Langkah 3.5 "berhenti ketika seluruh komponen telah menjadi elemen elementer yang bermakna".
- Modul 5 **juga mewajibkan** setiap elemen punya tipe konseptual, format, panjang, domain, null, sumber, dan contoh (§1.7, Langkah 4). Ini *tipe konseptual*, bukan tipe kolom SQL. Jadi masih ranah analisis, bukan perancangan basis data.
- Yang **tidak wajib**: memecah elemen sampai karakter (`angka = [0..9]`, `huruf = [A..Z]`). §1.5 menyatakan elementer itu kontekstual: "Alamat dapat dianggap elementer jika hanya ditampilkan".
- Yang **di luar ranah**: nama tabel, tipe kolom DBMS (VARCHAR, INT), indeks, foreign key fisik. Ini sudah dihapus di v0.2.
- Generator punya saklar `SAMPAI_DASAR` di `build_m05.py`. Isi `False` kalau kelompok mau penguraian berhenti di elemen elementer, karena format dan panjangnya sudah ada di tabel elemen.

### RV-M05-03 · Pindahkan ke dokumen utama · P1
Urutan bab mengikuti Modul 5 Bagian IV: Inventaris → Entri Komposit (flow lalu store) → Menguraikan Struktur Data → Mendefinisikan Elemen → Daftar Alias → Daftar TBD → Validasi Silang. Semua tabel ada di draft docx; salin, jangan ketik ulang.

### RV-M05-04 · Validasi Silang · P1
Pakai tabel "Validasi Silang Internal — Proses 3.1" di `EVALUASI_DATA_DICTIONARY.md`. Catat temuan DFD yang muncul (gray hole 3.1 → AUD-B-07) sebagai "perubahan DFD yang muncul setelah kamus data diperiksa". Ini sekaligus jawaban refleksi M05 no. 2.

### RV-M05-05 · Identitas & review · P1
Tabel identitas (versi 0.2, tanggal, penyusun, reviewer, status validasi), revision history (v0.1 → v0.2 beserta alasan K-01..K-17), log kontribusi, dan `_Review.pdf` berisi hasil validasi silang dari kelompok lain terhadap kamus data kita.

### RV-M05-06 · TBD · P2
Lihat sheet `7_TBD`. Yang paling mendesak: TBD-01 (batas perpanjangan) dan TBD-07 (sumber aturan 7 hari & Rp1.000; sebagian bisa dirujuk ke M01 Batasan "tidak menerima hutang" dan Asumsi "tarif denda harian bersifat tetap").

### RV-M05-07 · Sinkron dengan DFD · P2
Bila RV-M04-11 disetujui, ubah di `m05_data.py`:
- tujuan `peminjamAktif` (+3.1, +3.3)
- tambah entri `statusPengelolaanKoleksi`
- `dataAnggota` dua arah

Lalu jalankan `python manajemen/generator/build_m05.py`.

### RV-M05-08 · Alias CD · P2
Alias seperti "Informasi Katalog (CD)" hanya ada karena CD belum direvisi. Setelah RV-M02-05, hapus alias itu dari `ALIAS`.

### RV-M05-09 · Kerapian · P3
Jawab 3 refleksi Modul 5. Hapus `progress/PRPL_M05_2B_Kelompok6_DataDictionary.xlsx` setelah v0.2 disetujui.


---

## Temuan dari `updates/PRPL_M05_2B_RajinBelajar_DataDictionary.pdf` (v0.1b)

Status ketentuan K-01..K-17 ada di [`../EVALUASI_DATA_DICTIONARY.md`](../EVALUASI_DATA_DICTIONARY.md) bagian "Cek Ulang".

### RV-M05-20 · Basis dokumen · P1 (keputusan)
v0.1b dan v0.2 (generator) sekarang berjalan **terpisah**, jadi ada dua versi kebenaran, persis masalah file `.bpm` dulu. Rekomendasi: **v0.2 sebagai basis**, karena lengkap 34/34, sudah divalidasi otomatis, dan tidak sirkular. Tambahan bagus dari v0.1b dipindahkan ke `m05_data.py`:
- `NomorPanggil` di hasil pencarian
- `Kategori` (atau samakan dengan `Subjek`)
- `JumlahEksemplar` di `dataKoleksiBaru`
- `KondisiBuku` [Baik | Rusak] saat pengembalian. Ini menjawab "bagaimana eksemplar bisa jadi Rusak" lewat 3.2.
- Teks alias, periode, dan volume yang lebih natural

Kalau kelompok memilih lanjut v0.1b, semua RV-M05-10..19 wajib dikerjakan manual.

### RV-M05-10 · `catatanDenda` terbalik · P1
- **Sekarang (v0.1b):** inventaris No 13 dan entri No 10 menulis arus "Proses 3, Proses 3.3 -> Petugas Perpustakaan", isinya rincian denda (`TotalDenda`, `StatusDenda`).
- **DFD:** `catatanDenda` = **Petugas → 3.3** (input), yaitu catatan pembayaran denda dari Petugas. Rincian denda untuk Petugas adalah `buktiPengembalianDanDenda`.
- **Seharusnya:** `catatanDenda = IDTransaksi + JumlahDibayar + TanggalBayar`, arus Petugas Perpustakaan → 3.3. Isi entri lama pindah ke `buktiPengembalianDanDenda`.

### RV-M05-11 · `infoKatalog/Ketersediaan` · P1
Nama ini berasal dari file Rere sebelum merge. Di DFD master hanya ada `informasiKoleksiBuku` (PR-03). Hapus inventaris No 7 dan entri No 4, lalu gabungkan isinya (JumlahEksemplar, LokasiRak) ke `informasiKoleksiBuku`. Kalau dipertahankan, Level 0 dan Level 1 jadi tidak balance lagi.

### RV-M05-12 · Store hilang · P1
v0.1 masih punya 3 baris store; v0.1b tidak punya sama sekali, dan tidak ada entri store (record, kunci, retensi, akses; Modul 5 §1.3). Tambahkan D1 Data Anggota, D2 Data Koleksi, D3 Transaksi Fisik, plus 16 flow Tipe 2 (daftarnya di EVALUASI).

### RV-M05-13 · Penguraian ≠ entri · P1

| Flow | Entri komposit v0.1b | Penguraian v0.1b |
|---|---|---|
| informasiKoleksiBuku | `@KodeBuku + Judul + Pengarang + Penerbit + TahunTerbit + Kategori + StatusKetersediaan` | `{HasilPencarian}`, `HasilPencarian = @ISBN + JudulBuku + ... + 1{DetailEksemplar}` |
| dataTransaksiPeminjaman | `@NIM + @KodeBuku + TanggalPinjam + TanggalJatuhTempo + IDPetugas` | judul `formTransaksiPinjam = @NIM + 1{@KodeEksemplar}3 + TanggalPinjam` |
| dataTransaksiPengembalian | `@NIM + @KodeBuku + TanggalKembali + KondisiBuku + IDPetugas` | judul `formTransaksiKembali = @KodeEksemplar + TanggalKembali + (KondisiFisikBuku)` |
| permintaanPerpanjangan | `@NIM + @KodeBuku + TanggalPengajuan` | `@IDTransaksi + @NIM + @KodeEksemplar` |
| catatanDenda | rincian denda | judul `buktiKonfirmasiDenda` (pembayaran) |
| laporanBulanan | `Periode + ... + {BukuPalingBanyakDipinjam}` | judul `laporanSirkulasiBulanan = PeriodeLaporan + ...` |

Penguraian harus menguraikan struktur **yang sama** dengan entri komposit, dengan nama yang sama.

### RV-M05-14 · Satu konsep banyak nama · P1

| Konsep | Nama di v0.1b | Pilih satu (v0.2) |
|---|---|---|
| Kode eksemplar | KodeBuku, KodeEksemplar | KodeEksemplar (KodeBuku = alias) |
| Judul | Judul, JudulBuku | JudulBuku |
| Topik | Kategori | Subjek atau Kategori, pilih salah satu |
| Status eksemplar | StatusKetersediaan, StatusEksemplar | StatusEksemplar |
| Nomor bukti | NoBukti, IDTransaksi | IDTransaksi (atau definisikan NoBukti terpisah, terkait TBD-06) |
| Status denda | StatusDenda [Belum Dibayar \| Lunas], StatusPembayaran, StatusDenda [Tanpa Denda \| Belum Lunas \| Lunas] | StatusDenda dengan satu domain |
| Kondisi buku | KondisiBuku, KondisiFisikBuku | satu nama |
| Periode | Periode, PeriodeLaporan | PeriodeLaporan |
| Tarif | TarifDenda (di struktur), "Rp 1.000" (di elemen) | parameter TarifDendaHarian |

### RV-M05-15 · `@` di flow · P2
`@NIM + @KodeBuku` muncul di 10+ struktur flow, bahkan `1{@KodeEksemplar}3` di dalam iterasi. `@` hanya untuk kunci record data store (Modul 5 Langkah 4.4).

### RV-M05-16 · `dataTransaksiFisik` & kardinalitas · P1
- `dataTransaksiFisik = @NIM + @KodeBuku + JenisTransaksi + TanggalTransaksi + IDPetugas` bukan gabungan dari dua anaknya. Akibatnya baris balancing No 1 Proses 3 di M04 tidak sah. Seharusnya `dataTransaksiFisik = [dataTransaksiPeminjaman | dataTransaksiPengembalian]`.
- Entri `dataTransaksiPeminjaman` berisi 1 KodeBuku, tapi penguraiannya `1{KodeEksemplar}3`. Ini temuan yang sama persis dengan yang kita berikan ke Kelompok 4 (VS-13). Kalau tidak diperbaiki, mereka bisa membalikkannya ke kita.

### RV-M05-17 · Flow "Elementer" tanpa definisi · P1
`statusPendaftaran`, `statusKeaktifan`, `dataPencarian`, `statusPerpanjangan`, `permintaanLaporan` diberi status "Elementer" di inventaris. Tapi kelimanya tidak punya entri komposit dan tidak ada di tabel elemen. Flow boleh elementer, asalkan didefinisikan sebagai elemen (domain, contoh). Strukturnya sudah ada di v0.2. Contohnya, `statusPerpanjangan` sebenarnya komposit (jatuh tempo baru + status).

### RV-M05-18 · Elemen baru tidak terdefinisi · P2
Belum ada di tabel elemen: IDPetugas, JenisTransaksi, TanggalTransaksi, TanggalPengajuan, NoBukti, TarifDenda, KondisiBuku, StatusPembayaran, Kategori, JumlahEksemplar, StatusKetersediaan, BukuPalingBanyakDipinjam, NomorPanggil, NoWhatsapp, serta karakter dasar (karakterNama, karakterTeks, karakterEmail, huruf, angka). Modul 5 §1.10: setiap elemen yang dipakai harus didefinisikan.

### RV-M05-19 · Nilai hitungan sebagai input · P2
- `dataTransaksiPeminjaman` (input dari Petugas) memuat `TanggalJatuhTempo`, padahal nilai itu dihitung sistem (TanggalPinjam + 7 hari). Begitu juga `TanggalTransaksi`/`TanggalKembali` yang seharusnya tanggal sistem. Ini membingungkan process spec: siapa yang menghitung?
- `IDPetugas` dikirim di tiga flow, tapi tidak disimpan di store mana pun dan tidak dipakai proses mana pun. Aturan "petugas yang login" adalah detail implementasi (Modul 4 §1.8). Hapus, atau tambahkan ke RecordTransaksi kalau memang perlu dilacak.
