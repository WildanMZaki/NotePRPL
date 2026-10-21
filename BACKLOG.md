# Backlog & Progress — PRPL SILAPUS Kelompok 6 (RajinBelajar), Kelas 2B

Terakhir diperbarui: 2026-10-21

File terkait:
- `BASELINE_PENAMAAN.md` — nama resmi proses/flow/store. **Cek di sini dulu sebelum menulis nama apa pun.**
- `TEMUAN_DAN_REVISI.md` — peer review, audit internal, revision history.
- `revisions-recommendations/` — **rekomendasi revisi per modul** (RV-M0x-nn) dengan checklist; mulai dari README-nya.
- `AUDIT_BALANCING.md` — audit lintas modul (AUD-A/B/C/D) + rencana perbaikan 3 fase.
- `EVALUASI_DATA_DICTIONARY.md` — list flow per diagram vs kamus data, koreksi hasil Gemini, kepatuhan M05 ke instruksi.

## Target malam 2026-10-21

| Target | PIC | Status | Hasil |
|---|---|---|---|
| Audit seluruh modul + rencana perbaikan | Wildan | ✅ draft | `manajemen/AUDIT_BALANCING.md` |
| List evaluasi data dictionary | Irfan + Rere | ✅ draft (perlu dicocokkan dgn Gemini) | `manajemen/EVALUASI_DATA_DICTIONARY.md` |
| Perbaikan kamus data hasil evaluasi + penguraian atom | Irfan, Rere, Zidan | ✅ draft v0.2 | `progress/PRPL_M05_2B_RajinBelajar_DataDictionary.xlsx`, `..._draft.docx` |
| Dokumen validasi silang M04 + M05 Kelompok 4 | — | ✅ draft | `validasi-silang/PRPL_2B_RajinBelajar_ValidasiSilang_Kelompok4_M04-M05.docx` |

Legenda status: ✅ selesai · 🔄 sedang · ⏳ belum · ⚠️ butuh keputusan kelompok · 🧊 ditunda

## Ringkasan Modul

| Modul | Artefak | Status | Lokasi |
|---|---|---|---|
| M01 | Project Charter | ✅ Disubmit (bisa direvisi) | `submitted/PRPL_M01_...Charter-1.pdf` |
| M02 | Event List, Event Table, Context Diagram | ✅ Disubmit (perlu revisi, lihat BL-X) | `submitted/PRPL_M02_...EventContext-1.pdf` |
| M03 | DFD Level 0 + balancing CD→L0 | ✅ Disubmit (perlu revisi nama flow) | `submitted/PRPL_M03_...DFD-2.pdf` |
| M04 | Dekomposisi, balancing, audit DFD | 🔄 Minggu ini | `baselines/PRPL_M04_...pdf`, `Silapus Latest.bpm` |
| M05 | Kamus Data | 🔄 revisi (draft v0.2) | `baselines/PRPL_M05_...pdf` (v0.1), `progress/PRPL_M05_2B_RajinBelajar_DataDictionary.xlsx` (v0.2) |
| M06 | Process Specification | ⏳ | — |

Rantai dampak (Modul Batch 2): **DFD (.bpm) → dokumen M04 → kamus data M05 → process spec M06**. Setiap rename di .bpm wajib diteruskan ke semua yang di kanannya.

---

## M04 — DFD Decomposition

### DFD (.bpm)

| ID | Item | Status | PIC |
|---|---|---|---|
| BL-DFD-00 | Merge .bpm Wildan + Irfan + Rere + peer review + audit internal | ✅ 2026-10-19 (lihat REV di TEMUAN_DAN_REVISI) | Wildan |
| BL-DFD-01 | Buka `Silapus Latest.bpm` di PowerDesigner: cek file bisa dibuka, nomor proses tampil (1, 2, 2.1, 3.4, …) setelah prefiks nomor dihapus dari nama, label tidak tumpang tindih, panah `dataKoleksiBuku` L0 dua arah | ✅ (file sudah dibuka & disimpan ulang jadi `Silapus Latest.bpm`) | Wildan |
| BL-DFD-02 | Sepakati di grup: file `Silapus Latest.bpm` jadi **satu-satunya** file master; file Irfan/Rere dipensiunkan supaya tidak ada fork lagi | ✅ (file Irfan/Rere sudah tidak ada di folder) | Semua |
| BL-DFD-03 | Sepakati AI-10: flow tulis ke D3 dibedakan per aksi (`dataPeminjamanBaru`, `pembaruanPengembalian`, `dataDenda`, `pembaruanMasaPinjam`) + `dataPeminjaman` sebagai komposit, alih-alih semua disamakan `dataPeminjaman` | ⚠️ | Semua |
| BL-DFD-04 | Sepakati konvensi camelCase untuk flow (datang dari Irfan/Rere) — berdampak ke dokumen M03 & M04 yang masih pakai nama berspasi | ⚠️ | Semua |
| BL-DFD-05 | Nama proses 4 `Membuat Laporan Transaksi Fisik` vs pengelompokan event di M03 `Membuat Laporan Sirkulasi`; proses 3 sudah jadi `...Sirkulasi...`, jadi proses 4 sebaiknya disamakan | ⚠️ | — |
| BL-DFD-06 | Ekspor ulang PNG/PDF semua diagram (L0, L1-P2, L1-P3) dari .bpm terbaru untuk dokumen & `Source.zip` | ⏳ | — |
| BL-DFD-08 | Tambah `peminjamAktif` D3 → 3.1 (gray hole 3.1, AUD-B-07); opsional `dataAnggota` dua arah (AUD-B-08) | ⚠️ | — |
| BL-DFD-07 | Context Diagram tidak ada di .bpm mana pun → cari file sumbernya, samakan nama flow lintas batas dengan L0 (camelCase, `catatanDenda`, `informasiKoleksiBuku`, `statusPerpanjangan`, dst.) + hapus `Laporan Operasional` (AUD-B-01/02) | ⏳ | — |

### Dokumen M04 (`progress/...DFDDecomposition.docx`)

| ID | Item | Status |
|---|---|---|
| BL-M04-01 | Ganti nama proses 3 di "Tujuan proses induk" & tabel keputusan → `Memproses Sirkulasi dan Denda` | ⏳ |
| BL-M04-02 | **Daftar Koreksi No 3** (Kriteria pencarian dipertahankan) bertentangan dengan AUD-02 & peer review → ubah jadi "dihapus" + alasan: pencarian hanya membaca D2 | ⏳ |
| BL-M04-03 | Daftar Koreksi No 1: alasan "konfirmasi denda dilakukan bagian keuangan" — Bagian Keuangan tidak ada di DFD/CD M03. Perbaiki alasannya (lihat BL-X-01) | ⏳ |
| BL-M04-04 | Kolom "Risiko Pemodelan" proses 2 masih menyebut `Kriteria Pencarian`/`Simpan Data Koleksi` → perbarui atau tandai "sudah ditutup" | ⏳ |
| BL-M04-05 | Matriks balancing P2: semua baris jadi Balance dengan nama baru (lihat BASELINE L1-P2) | ⏳ |
| BL-M04-06 | Matriks balancing P3: perbarui 12 baris dengan nama baru; baris 4 & 10 status "Balance — dipecah, struktur di kamus data" + rujuk entri M05 | ⏳ |
| BL-M04-07 | Lembar Audit: ganti "Open / Closed" jadi status nyata (AUD-01..03 = Closed) + tambahkan temuan AI-xx & PR-xx | ⏳ |
| BL-M04-08 | Tabel "Melakukan Peer Review": isinya membahas proses peminjaman/pengembalian yang tidak sama dengan DFD kita — pastikan ini memang review terhadap DFD kelompok lain, dan kolom Sintaks/Semantik/Balancing/Keterbacaan masih kosong | ✅ terjawab: itu review untuk Kelompok 4; kolom sudah diisi di dokumen validasi silang |
| BL-M04-09 | Ganti semua gambar diagram dengan ekspor terbaru (BL-DFD-06) | ⏳ |
| BL-M04-10 | Jawab 3 pertanyaan refleksi Modul 4 | ⏳ |
| BL-M04-11 | Lengkapi berkas: `PRPL_M04_2B_RajinBelajar_DFDDecomposition.pdf`, `_Source.zip` (bpm + PNG/PDF), `_Review.pdf` (temuan, respons, revision history, log kontribusi) | ⏳ |

---

## M05 — Kamus Data (`progress/PRPL_M05_2B_Kelompok6_DataDictionary.xlsx`)

Masalah utama: kamus data dibuat dari nama yang **tidak sama** dengan DFD dan nomor proses yang salah. Harus disusun ulang dari `BASELINE_PENAMAAN.md`.

**Update 2026-10-21:** item BL-M05-01 s.d. BL-M05-17 sudah ditangani di draft v0.2 (generator `manajemen/generator/`), kecuali yang bertanda ⚠️. Sisa: review kelompok, pindahkan ke dokumen utama, ekspor PDF, `_Review.pdf`, jawab refleksi.

| ID | Item | Status |
|---|---|---|
| BL-M05-01 | Nama file: `Kelompok6` vs `RajinBelajar` di file lain → seragamkan identitas kelompok (`PRPL_M05_2B_RajinBelajar_DataDictionary.xlsx`) | ⏳ |
| BL-M05-02 | Inventaris baru 12 entri; DFD punya ±30 flow unik + 3 store. Tambahkan semua (Modul 5 §1.11: seluruh flow & store wajib tercatat) | ⏳ |
| BL-M05-03 | Tambah entri komposit wajib untuk balancing: `dataTransaksiFisik = [dataTransaksiPeminjaman \| dataTransaksiPengembalian]` dan `dataPeminjaman = [dataPeminjamanBaru \| pembaruanPengembalian \| dataDenda \| pembaruanMasaPinjam]` | ⏳ |
| BL-M05-04 | Nomor proses di inventaris salah: proses 1 **tidak** didekomposisi (bukan "Proses 1.1"); 3.3 = denda, 3.4 = perpanjangan (di xlsx terbalik) | ⏳ |
| BL-M05-05 | Nama flow tidak ada di DFD: `formTransaksiPinjam`, `formTransaksiKembali`, `buktiKonfirmasiDenda`, `infoKatalogKoleksi`, `statusKeaktifanMahasiswa`, `laporanSirkulasiBulanan` → ganti ke nama baseline | ⏳ |
| BL-M05-06 | Store tercatat sebagai `dataAnggota`/`dataKoleksiBuku`/`dataTransaksiSirkulasi` padahal di DFD itu nama flow → pakai `D1 Data Anggota`, `D2 Data Koleksi`, `D3 Transaksi Fisik` | ⏳ |
| BL-M05-07 | Sheet Data_Komposit pakai PascalCase (`DataPendaftaran`) sedangkan Inventaris camelCase → satu nama untuk satu konsep | ⏳ |
| BL-M05-08 | Kolom Alias berisi nama tabel fisik (`tb_anggota`, `tb_koleksi`) — Modul 4 §1.8 melarang detail implementasi; ganti dengan istilah bisnis yang memang dipakai | ⏳ |
| BL-M05-09 | `RecordTransaksi` punya 3 tanda `@` (IDTransaksi, NIM, KodeEksemplar) — kunci cuma `@IDTransaksi`; NIM & KodeEksemplar adalah rujukan | ⏳ |
| BL-M05-10 | Format vs contoh bertentangan: `KodeEksemplar` An(10) tapi contoh `SIL-BK-0012` = 11 karakter; `IDTransaksi` An(12) tapi `TRX-20261019-001` = 16 karakter | ⏳ |
| BL-M05-11 | `NIM` 9 digit, padahal EV-01 menyebut anggota = mahasiswa **atau dosen** (NIP). Putuskan: dosen di luar scope, atau tambah elemen `NomorIdentitas = [NIM \| NIP]` | ⚠️ |
| BL-M05-12 | Domain `StatusAnggota` [Aktif \| Bebas Denda \| Diblokir] mencampur status keaktifan & status denda; Sistem Akademik mengirim aktif/nonaktif/cuti (M02 EV-01 error) | ⏳ |
| BL-M05-13 | Aturan bisnis tanpa sumber: jatuh tempo +7 hari, denda Rp1.000/hari → jadikan TBD dengan pemilik, atau rujuk ke sumber kebutuhan | ⏳ |
| BL-M05-14 | Elemen yang dipakai di struktur tapi belum didefinisikan: `TanggalKembali`, `NamaLengkap`, `ProgramStudi`, `EmailKampus`, `ISBN`, `JudulBuku`, `Pengarang`, `TahunTerbit`, `TanggalDaftar`, dll. + elemen untuk aturan perpanjangan (`JumlahPerpanjangan`) | ⏳ |
| BL-M05-15 | `DataPendaftaran` memuat `(NoWhatsApp)` yang tidak ada di event table EV-01 | ⏳ |
| BL-M05-16 | Matriks validasi silang sudah menulis "Digunakan di Process Spec: Ya / Validated" padahal M06 belum dibuat | ⏳ |
| BL-M05-17 | Entri komposit belum punya Periode, Volume, Aturan bisnis (atribut wajib Modul 5 §1.6) | ⏳ |
| BL-M05-18 | Ekspor PDF + `_Review.pdf` (temuan, respons, revision history, log kontribusi) | ⏳ |
| BL-M05-19 | Review keputusan desain v0.2: NomorIdentitas = [NIM \| NIP], 1 transaksi = 1 eksemplar, StatusAnggota [Aktif \| Nonaktif], format KodeEksemplar/IDTransaksi | ⚠️ |
| BL-M05-20 | Jawab 3 pertanyaan refleksi Modul 5 | ⏳ |

## Validasi Silang (kelompok lain)

| ID | Item | Status |
|---|---|---|
| BL-VS-01 | Review isi `validasi-silang/PRPL_2B_RajinBelajar_ValidasiSilang_Kelompok4_M04-M05.docx` (23 temuan), sesuaikan nama file bila dosen menentukan format | ⏳ |
| BL-VS-02 | Kirim ke Kelompok 4, catat respons mereka (Diterima/Ditolak/Klarifikasi) di kolom Status | ⏳ |
| BL-VS-03 | Minta & catat hasil validasi silang kelompok lain terhadap M04/M05 kita → `TEMUAN_DAN_REVISI.md` | ⏳ |

---

## M06 — Process Specification (persiapan)

| ID | Item | Status |
|---|---|---|
| BL-M06-01 | Inventaris proses primitif: 1, 2.1, 2.2, 3.1, 3.2, 3.3, 3.4, 4 (input/output/store dari BASELINE) | ⏳ |
| BL-M06-02 | Kandidat decision table: 3.1 (status anggota × ketersediaan × kuota × denda) dan 3.4 (status anggota × batas perpanjangan × denda aktif) | ⏳ |
| BL-M06-03 | Semua elemen yang dipakai spec harus sudah ada di M05 (tunggu BL-M05-14) | ⏳ |

---

## Lintas Modul (revisi M02/M03 yang sudah disubmit)

| ID | Item | Status |
|---|---|---|
| BL-X-01 | **Bagian Keuangan**: ada di M02 (EE-04, EV-09 konfirmasi pembayaran denda) tapi hilang di M03/DFD. Pilih: (a) dihapus konsisten dari M02, atau (b) dimasukkan kembali ke CD & DFD. Pengaruh ke `catatanDenda` & alasan BL-M04-03 | ⚠️ |
| BL-X-02 | Nomor event tidak stabil: M02 punya EV-09 Bagian Keuangan & EV-10 Sistem Akademik; M03 EV-09 = Sistem Akademik | ⏳ |
| BL-X-03 | EV-09/EV-10 "Sistem Akademik mengirim update status" tidak punya flow di CD/DFD (hanya `dataVerifikasi`/`statusKeaktifan` saat pendaftaran) | ⏳ |
| BL-X-04 | EV-07 (temporal, laporan otomatis akhir bulan) tidak ada pemicunya di DFD — proses 4 hanya dari `permintaanLaporan` | ⏳ |
| BL-X-05 | Error condition yang tidak didukung DFD: EV-05 "buku sedang direservasi" (tidak ada fitur reservasi), EV-04 "pembayaran denda gagal dikonfirmasi" (tidak ada flow pembayaran) | ⏳ |
| BL-X-06 | Batas perpanjangan: EV-05 "misal max 2 kali" — perlu angka pasti (lihat juga catatan optimasi 🧊) → TBD di M05 | ⚠️ |
| BL-X-07 | Kandidat store di M03 (`Data Koleksi Buku, Data Eksemplar`, `Transaksi Peminjaman`, `Arsip Laporan Bulanan`) tidak sama dengan store di DFD (D1–D3) | ⏳ |
| BL-X-08 | Nama flow di CD/L0 M03 berbeda dengan baseline baru (mis. `Status Transaksi & Bukti Pinjam`, `Informasi Katalog & Ketersediaan`, `Konfirmasi Denda`) → revisi matriks balancing CD→L0 | ⏳ |
| BL-X-09 | Typo di event table M02/M03 ("peminjakan", "tansaksi", "angggota", "peninjaman") | ⏳ |

---

## 🧊 Ditunda (catatan optimasi personal — tidak dikerjakan sekarang)

- Batasan perpanjangan mandiri oleh anggota (mis. maks 3 kali) — bentrok dengan EV-05 "max 2 kali" (BL-X-06).
- Anggota bisa melihat status peminjaman & pengembalian, bukan hanya status perpanjangan (berhubungan dengan P_05 di Charter yang tidak dipilih sebagai prioritas).

Kalau nanti diambil, dampaknya: event baru → CD → L0 → L1-P3 → M05 → M06.
