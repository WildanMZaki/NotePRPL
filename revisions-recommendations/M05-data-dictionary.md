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
