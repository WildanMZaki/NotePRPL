# M04 — Dekomposisi, Balancing, Audit DFD

File: `baselines/PRPL_M04_2B_RajinBelajar_DFDDecomposition.pdf` (sumber: `progress/PRPL_M04_...docx`), diagram `Silapus Latest.bpm`.

- [ ] RV-M04-01 · Daftar Koreksi: No 1 & No 3 + baris baru · **P1** (AUD-D-01, A-01)
- [ ] RV-M04-02 · Nama proses di "Tujuan proses induk" & tabel keputusan · **P1**
- [ ] RV-M04-03 · Gambar diagram anak dari `.bpm` terbaru · **P1**
- [ ] RV-M04-04 · Matriks balancing Proses 2 · **P1** (AUD-B-06)
- [ ] RV-M04-05 · Matriks balancing Proses 3 · **P1** (AUD-B-06)
- [ ] RV-M04-06 · Bagian "Hasil Peer Review dari Kelompok Lain" · **P1** (AUD-D-03)
- [ ] RV-M04-07 · Lembar Audit DFD · **P1** (AUD-D-02)
- [ ] RV-M04-08 · Identitas versi, revision history, log kontribusi · **P1** (AUD-D-05)
- [ ] RV-M04-09 · Bagian "Melakukan Peer Review" (untuk Kelompok 4) · P2
- [ ] RV-M04-10 · Kolom risiko pemodelan · P2
- [ ] RV-M04-11 · Flow tambahan di DFD (3.1, 3.3, 2.2, 1) · P2 (keputusan dulu)
- [ ] RV-M04-12 · Refleksi + berkas pengumpulan · P3

---

### RV-M04-01 · Daftar Koreksi · P1

| No | Nama Alur | Dari ke | Sekarang tertulis | Seharusnya |
|---|---|---|---|---|
| 1 | Konfirmasi Denda | Petugas → Proses 3 | Menjadi "Catatan Denda". Alasan: "konfirmasi denda dilakukan oleh bagian keuangan bukan petugas" | Menjadi `catatanDenda`. Alasan: "yang dikirim Petugas adalah catatan pembayaran denda, bukan konfirmasi; Bagian Keuangan di luar lingkup (M01 stakeholder)" |
| 3 | Kriteria pencarian | Proses 2 → Data koleksi | "–", dipertahankan | **Dihapus**. Alasan: pencarian hanya membaca D2; kriteria tidak disimpan (peer review PR-01, AUD-02) |

Tambah baris untuk semua perubahan merge (dari `TEMUAN_DAN_REVISI.md` REV-2026-10-19):

| No | Nama Alur | Menjadi | Alasan |
|---|---|---|---|
| 4 | Simpan Data (1 → D1) | dataAnggota | Kata kerja → kata benda (AUD-01) |
| 5 | Info Katalog/ketersediaan | informasiKoleksiBuku | PR-03 |
| 6 | Status Perpanjang | statusPerpanjangan | PR-05 / AI-06 |
| 7 | Data Buku (D2 ↔ 2) | dataKoleksiBuku | PR-04 |
| 8 | Bukti pengembalian denda | buktiPengembalianDanDenda | AI-03 |
| 9 | Semua flow | camelCase | Konsistensi dengan kamus data |

### RV-M04-02 · Nama proses · P1
- **Sekarang:** "3. Memproses Transaksi Fisik dan Denda"; anak 3.1–3.4 huruf kecil ("Memproses peminjaman buku", "Menghitung & mencatat denda").
- **Seharusnya:** "3. Memproses Sirkulasi dan Denda"; anak: Memproses Peminjaman Buku, Memproses Pengembalian Buku, Menghitung dan Mencatat Denda, Memperpanjang Peminjaman.

### RV-M04-03 · Gambar · P1
Ekspor ulang L0, L1-P2, L1-P3 dari `Silapus Latest.bpm`. Hapus gambar "Proses 2 sebelum perbaikan" atau beri label "versi lama (v0.1)".

### RV-M04-04 · Matriks balancing Proses 2 · P1

| No | Aliran pada Induk | Arah | Aliran Ekuivalen pada Anak | Status | Catatan |
|---|---|---|---|---|---|
| 1 | dataPencarian (Anggota → 2) | Masuk | dataPencarian (Anggota → 2.1) | Balance | Nama, arah, makna sama |
| 2 | dataKoleksiBaru (Petugas → 2) | Masuk | dataKoleksiBaru (Petugas → 2.2) | Balance | Sama |
| 3 | dataKoleksiBuku (D2 → 2, sisi baca) | Masuk | dataKoleksiBuku (D2 → 2.1) | Balance | Flow dua arah di induk, sisi baca muncul di 2.1 |
| 4 | informasiKoleksiBuku (2 → Anggota) | Keluar | informasiKoleksiBuku (2.1 → Anggota) | Balance | Sudah diseragamkan (PR-03) |
| 5 | dataKoleksiBuku (2 → D2, sisi tulis) | Keluar | dataKoleksiBuku (2.2 → D2) | Balance | Sisi tulis muncul di 2.2 (PR-02, PR-04) |

Tambahkan juga versi v0.1 (sebelum revisi) sebagai bukti di revision history. Jangan dihapus, karena dosen menilai "revisi terlacak".

### RV-M04-05 · Matriks balancing Proses 3 · P1

| No | Aliran pada Induk | Arah | Aliran Ekuivalen pada Anak | Status | Catatan |
|---|---|---|---|---|---|
| 1 | dataTransaksiFisik (Petugas → 3) | Masuk | dataTransaksiPeminjaman (→ 3.1), dataTransaksiPengembalian (→ 3.2) | Balance | Dipecah; struktur `dataTransaksiFisik = [dataTransaksiPeminjaman \| dataTransaksiPengembalian]` di kamus data |
| 2 | catatanDenda (Petugas → 3) | Masuk | catatanDenda (→ 3.3) | Balance | |
| 3 | permintaanPerpanjangan (Anggota → 3) | Masuk | permintaanPerpanjangan (→ 3.4) | Balance | |
| 4 | statusAnggota (D1 → 3) | Masuk | statusAnggota (D1 → 3.1, D1 → 3.4) | Balance | Dibaca dua proses anak |
| 5 | dataEksemplar (D2 → 3) | Masuk | dataEksemplar (D2 → 3.1) | Balance | |
| 6 | peminjamAktif (D3 → 3) | Masuk | peminjamAktif (D3 → 3.2, 3.4; + 3.1, 3.3 bila RV-M04-11) | Balance | |
| 7 | statusTransaksiDanBukti (3 → Petugas) | Keluar | statusTransaksiDanBukti (3.1 →, 3.2 →) | Balance | AI-02 |
| 8 | buktiPengembalianDanDenda (3 → Petugas) | Keluar | buktiPengembalianDanDenda (3.3 →) | Balance | AI-03 |
| 9 | statusPerpanjangan (3 → Anggota) | Keluar | statusPerpanjangan (3.4 →) | Balance | AI-06 |
| 10 | pembaruanEksemplar (3 → D2) | Keluar | pembaruanEksemplar (3.1 → D2, 3.2 → D2) | Balance | AI-07 |
| 11 | dataPeminjaman (3 → D3) | Keluar | dataPeminjamanBaru (3.1), pembaruanPengembalian (3.2), dataDenda (3.3), pembaruanMasaPinjam (3.4) | Balance | Dipecah per aksi (PR-08, AI-10); struktur `dataPeminjaman = [ ... ]` di kamus data |
| 12 | — | — | dataKeterlambatan (3.2 → 3.3) | Balance | Flow internal |

### RV-M04-06 · Hasil Peer Review dari Kelompok Lain · P1
- **Sekarang:** placeholder "... hasil evaluasi dari kelompok".
- **Seharusnya:** tabel temuan dari `catatan peer review.txt` dengan kolom ID, Temuan, Respons (Diterima/Ditolak/Klarifikasi), Tindakan, Status. Isinya sudah ada di `TEMUAN_DAN_REVISI.md` bagian A (PR-01..PR-08). PR-07 statusnya "Ditolak sebagian, dengan alasan" (Modul 4 §3.5 butir 5: penolakan wajib beralasan).

### RV-M04-07 · Lembar Audit DFD · P1
- **Sekarang:** kolom Status "Open / Closed"; isi baris bergeser (AUD-01 kosong, isinya pindah ke AUD-02).
- **Seharusnya:** perbaiki susunan tabel; AUD-01, AUD-02, AUD-03 = **Closed** beserta tindakan yang diambil. Tambah baris temuan audit internal AI-02..AI-11, dan bila disetujui AUD-B-07/B-11 (gray hole 3.1, 3.3).

### RV-M04-08 · Identitas & revision history · P1
Aturan kerja Batch 2: setiap artefak memuat **versi, tanggal, penyusun, reviewer, status validasi**. Tambahkan:
- tabel identitas di halaman awal
- revision history (Lampiran A modul)
- log kontribusi individu (Lampiran B)
- catatan penggunaan AI (lihat `TEMUAN_DAN_REVISI.md`)

### RV-M04-09 · "Melakukan Peer Review" (untuk Kelompok 4) · P2
Bagian ini adalah review kita untuk Kelompok 4. Kolom checklist masih kosong. Isi dari `validasi-silang/PRPL_2B_RajinBelajar_ValidasiSilang_Kelompok4_M04-M05.docx` bagian 1, atau pindahkan bagian ini ke `_Review.pdf` dan rujuk dari dokumen utama.

### RV-M04-10 · Kolom risiko pemodelan · P2
Proses 2 masih menyebut "Kriteria Pencarian" dan "Simpan Data Koleksi" sebagai risiko. Tambahkan "→ ditutup pada v2 (lihat Daftar Koreksi)". Proses 3: "gray hole" diperjelas: "aturan kuota/denda 3.1 butuh baca D3 (AUD-B-07)".

### RV-M04-11 · Flow tambahan DFD · P2 (butuh keputusan)

| Usulan | Flow | Alasan | Balance |
|---|---|---|---|
| AUD-B-07 | `peminjamAktif` D3 → 3.1 | Cek kuota 3 eksemplar & denda belum lunas | Aman (L0 sudah punya) |
| AUD-B-11 | `peminjamAktif` D3 → 3.3 | Validasi JumlahDibayar = JumlahDenda saat bayar terpisah | Aman |
| AUD-B-12 | `statusPengelolaanKoleksi` 2.2 → Petugas (+ L0, CD) | Jalur gagal EV-08 | Perlu tambah di L0 dan CD |
| AUD-B-08 | `dataAnggota` D1 ↔ 1 (dua arah) | Cek pendaftaran ganda, EV-09 | Aman |

Setelah diterapkan: update baseline → `.bpm` → matriks RV-M04-05 → kamus data (`m05_data.py`).

### RV-M04-12 · Refleksi & berkas · P3
Jawab 3 pertanyaan refleksi Modul 4. Siapkan `_DFDDecomposition.pdf`, `_Source.zip` (`.bpm` + ekspor PNG), `_Review.pdf`.
