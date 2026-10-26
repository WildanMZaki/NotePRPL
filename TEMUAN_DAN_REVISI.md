# Temuan Review & Revision History

Dipakai sebagai bahan `PRPL_M0x_2B_RajinBelajar_Review.pdf` (temuan, respons, revision history).
Respons mengikuti Modul 4 §3.5: **Diterima / Ditolak (dengan alasan) / Perlu klarifikasi**.

## A. Temuan Peer Review (dari kelompok lain) — DFD M04

| ID | Lokasi | Temuan | Respons | Tindakan | Status |
|---|---|---|---|---|---|
| PR-01 | L1-P2, 2.1 → D2 | `Kriteria Pencarian` disimpan ke Data Koleksi — apakah memang disimpan? | Diterima | Flow dihapus (pencarian hanya membaca D2). Juga tidak dibawa ke Level 0 (versi Irfan sempat menambah `kriteriaPencarian` di L0). | Closed (.bpm) |
| PR-02 | L1-P2, 2.2 → D2 | `Simpan Data Koleksi` pakai kata kerja | Diterima | Diganti `dataKoleksiBuku` (kata benda, sama dengan L0 agar balance) | Closed (.bpm) |
| PR-03 | L0 vs L1-P2 | `Info buku` (L0) vs `Info Katalog/Ketersediaan` (2.1) | Diterima | Keduanya jadi `informasiKoleksiBuku` | Closed (.bpm) |
| PR-04 | L0 vs L1-P2 | `Data Buku` (L0) pecah jadi `Simpan Data Koleksi` + `Data Buku` | Diterima | L0 `dataKoleksiBuku` dua arah (baca+tulis); 2.1 baca `dataKoleksiBuku`, 2.2 tulis `dataKoleksiBuku` | Closed (.bpm) |
| PR-05 | L0 vs 3.4 | `Status Perpanjangan` vs `Status permintaan` | Diterima | Keduanya `statusPerpanjangan` | Closed (.bpm) |
| PR-06 | L0 vs 3.1 | `Data Peminjaman` vs `Data Peminjam` | Diterima | Lihat PR-08 | Closed (.bpm) |
| PR-07 | L0 vs 3.1/3.2 | `Data transaksi fisik` dipecah jadi peminjaman & pengembalian | Ditolak sebagian — pemecahan dipertahankan | Pemecahan sah asalkan didefinisikan di kamus data: `dataTransaksiFisik = [dataTransaksiPeminjaman \| dataTransaksiPengembalian]` | **Open** → BL-M05-03 |
| PR-08 | L1-P3 → D3 | Semua flow tulis ke D3 bernama `Data peminjam` | Diterima | 3.1 `dataPeminjamanBaru`, 3.2 `pembaruanPengembalian`, 3.3 `dataDenda`, 3.4 `pembaruanMasaPinjam`; L0 tetap `dataPeminjaman` sebagai komposit | Closed (.bpm), definisi kamus **Open** → BL-M05-03 |

## B. Temuan Audit Internal Kelompok — Matriks Balancing Proses 3

| ID | Baris Matriks | Temuan | Tindakan | Status |
|---|---|---|---|---|
| AI-02 | No 2 | Anak hanya `Status transaksi`, induk `Status transaksi dan bukti` | 3.1 & 3.2 → `statusTransaksiDanBukti` | Closed (.bpm) |
| AI-03 | No 3 | `Status pencatatan denda` ≠ `Bukti pengembalian dan denda` | 3.3 → `buktiPengembalianDanDenda` | Closed (.bpm) |
| AI-06 | No 6 | `Status permintaan` ≠ `Status Perpanjang` | Keduanya `statusPerpanjangan` | Closed (.bpm) |
| AI-07 | No 7 | `Pengembalian eksemplar` ≠ `Pembaruan eksemplar` | `pembaruanEksemplar` (di file Wildan sudah benar, di file Rere belum) | Closed (.bpm) |
| AI-10 | No 10 | `Data peminjam` (anak) ≠ `Data peminjaman` (induk) | **Diselesaikan berbeda dari usulan audit**: tidak disamakan semua jadi `dataPeminjaman`, tapi dibedakan per aksi sesuai PR-08 + `dataPeminjaman` didefinisikan sebagai komposit di kamus data. Alasan: kalau 3.1 juga bernama `dataPeminjaman` maka definisi komposit jadi sirkular. **Perlu disepakati kelompok.** | Closed (.bpm), perlu konfirmasi |
| AI-11 | No 11 | `Info peminjam aktif` (anak) ≠ `Peminjam aktif` (induk) | Keduanya `peminjamAktif` | Closed (.bpm) |

## C. Lembar Audit DFD (dokumen M04)

| ID | Temuan | Status setelah merge |
|---|---|---|
| AUD-01 | `Simpan Data` (1 → D1) pakai kata kerja | Closed — jadi `dataAnggota` |
| AUD-02 | `Kriteria Pencarian` masuk D2 + tidak balance | Closed — flow dihapus |
| AUD-03 | Kedua panah 3.4 ↔ D3 masuk ke 3.4 | Closed — di .bpm sudah 1 baca (`peminjamAktif`) + 1 tulis (`pembaruanMasaPinjam`) |

⚠️ Kontradiksi di dokumen M04: **Daftar Koreksi No 3** bilang `Kriteria pencarian` dipertahankan, sedangkan AUD-02 + PR-01 menghapusnya. Daftar Koreksi No 3 harus direvisi (→ BL-M04-02).

## D. Revision History

| Versi | Tanggal | Artefak | Perubahan | Alasan | Penyusun | Reviewer |
|---|---|---|---|---|---|---|
| 0.2 | 2026-10-19 | `SILAPUS wildan.bpm` (kini `Silapus Latest.bpm`) | Merge perubahan Irfan (Level 0) + Rere (L1-P2) + tindak lanjut peer review & audit internal. Detail di bawah. | PR-01..08, AI-02..11, AUD-01..03 | Wildan (dibantu AI, lihat catatan) | _belum_ |
| 0.2-draft | 2026-10-21 | Kamus Data M05 (`progress/PRPL_M05_2B_RajinBelajar_DataDictionary.xlsx` + `_draft.docx`) | Disusun ulang dari DFD master: inventaris 34 entri, 31 entri komposit, 3 entri store, penguraian sampai elemen dasar, 55 elemen, alias, 7 TBD, validasi silang 3.1. Nama lama jadi alias. | Evaluasi M05 (`EVALUASI_DATA_DICTIONARY.md`, K-01..K-17) | Wildan (dibantu AI) | _belum_ |
| - | 2026-10-21 | `AUDIT_BALANCING.md` | Audit lintas modul M01–M05: 8 temuan event↔CD, 10 temuan CD↔L0↔L1, 6 temuan kamus data, 6 temuan dokumen M04 + rencana 3 fase | Penugasan Wildan | Wildan (dibantu AI) | _belum_ |
| - | 2026-10-21 | `validasi-silang/PRPL_2B_RajinBelajar_ValidasiSilang_Kelompok4_M04-M05.docx` | Validasi silang M04 + M05 Kelompok 4: 23 temuan (7 Tinggi, 11 Sedang, 5 Rendah) | Tugas validasi silang | Wildan (dibantu AI) | _belum_ |

| 0.3 | 2026-10-26 | `Silapus Latest.bpm` | `dataAnggota` dua arah; `peminjamAktif` D3 → 3.1 & 3.3; `dataKoleksiBuku` di 2.2 dua arah; aliran baru `statusPengelolaanKoleksi` (L0 + L1-P2 + CD); Proses 4 → Membuat Laporan Sirkulasi. Backup: `_backup/Silapus Latest - sebelum M06 prep 2026-10-26.bpm` | AUD-B-07, B-08, B-09, B-11, B-12; data yang dibutuhkan process spec M06 | Wildan (dibantu AI) | _belum_ |
| - | 2026-10-26 | `revisions-recommendations/siap-timpa/` M01–M04 | Teks pengganti lengkap per bagian + catatan perubahan | Permintaan: revisi langsung timpa, fokus balancing | Wildan (dibantu AI) | _belum_ |
| 0.1 | 2026-10-26 | M06 draft (`progress/`) | 8 process spec, DT-1, DT-2, DTree-1, 41 kasus uji, traceability | Modul 6 | Wildan (dibantu AI) | _belum_ |

### Detail REV-2026-10-19 (`SILAPUS wildan.bpm`)

Backup sebelum merge: `_backup/SILAPUS wildan - sebelum merge 2026-10-19.bpm`

**Diambil dari file Irfan (Level 0):**
- Nama proses tanpa prefiks nomor (`1.0 Mengelola Keanggotaan` → `Mengelola Keanggotaan`, dst.) — nomor sudah dari NumberID.
- Proses 3: `Memproses Transaksi Fisik dan Denda` → `Memproses Sirkulasi dan Denda`.
- Semua flow Level 0 → camelCase; `Konfirmasi denda` → `catatanDenda`; `Bukti pengembalian denda` → `buktiPengembalianDanDenda`; `Info Katalog/ketersediaan` → `informasiKoleksiBuku`; `Data Buku` → `dataKoleksiBuku`.
- **Tidak diambil:** `kriteriaPencarian` (2 → D2) di Level 0 — bertentangan dengan PR-01/AUD-02.

**Diambil dari file Rere (Level 1 Proses 2):** flow camelCase (`dataKoleksiBaru`, `dataPencarian`, ...).
- **Tidak diambil:** `ResourceFlow_10` (flow tanpa nama 2 → D2 di Level 0) dan `Pengembalian eksemplar` (sudah dikoreksi jadi `pembaruanEksemplar`).
- Perubahan kecil posisi/ukuran simbol di file Rere tidak dibawa (hanya efek ukuran label).

**Perubahan tambahan (konsistensi):**
- Flow Level 1 Proses 3 ikut camelCase (sebelumnya belum diubah siapa pun).
- `simpanData` → `dataAnggota` (AUD-01).
- `dataKoleksiBuku` Level 0 diberi akses baca + tulis (simbol sudah panah dua arah, tapi objeknya cuma akses tulis).
- Nama anak proses dirapikan: `Memproses Pengembalian Buku`, `Menghitung dan Mencatat Denda`, `Memperpanjang Peminjaman`.
- Typo store `Transaksi FIsik` → `Transaksi Fisik`; kapitalisasi `Data anggota` → `Data Anggota`, `Data koleksi` → `Data Koleksi`, entitas `Kepala perpustakaan` → `Kepala Perpustakaan`.
- Nama diagram: `SILAPUS` → `DFD Level 0`, `Pengelolaan Katalog` → `DFD Level 1 Proses 2`, `Dekomposisi Transaksi Fisik` → `DFD Level 1 Proses 3`.

Catatan penggunaan AI (wajib dicatat sesuai aturan kerja kelompok): merge & rename di atas dilakukan dengan bantuan Claude (AI) lewat edit XML .bpm; hasil **harus** dibuka & diverifikasi di PowerDesigner oleh kelompok (lihat BL-DFD-01).

Catatan penggunaan AI 2026-10-21: inventaris, struktur, penguraian, tabel elemen kamus data v0.2, audit balancing, dan validasi silang Kelompok 4 disusun dengan bantuan Claude (AI) dari dokumen baseline dan instruksi modul. Keputusan desain yang diambil AI (NomorIdentitas = [NIM | NIP], 1 transaksi = 1 eksemplar, domain status, format kode) **wajib direview kelompok** sebelum dikumpulkan.
