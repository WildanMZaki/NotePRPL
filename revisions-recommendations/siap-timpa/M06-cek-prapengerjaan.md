# M06 — Cek Pra-Pengerjaan Kelompok

Sumber: `updates/PRPL 6 FIX.pdf` (2026-10-26 22:44, 13 halaman).
Pembanding: DFD `Silapus Latest.bpm` (2026-10-26), `BASELINE_PENAMAAN.md`, M05 final, Modul 6.
Draft lengkap untuk menambal bagian yang belum ada: [`../../m06/PROCESS_SPEC_M06.md`](../../m06/PROCESS_SPEC_M06.md) (docx: `progress/PRPL_M06_2B_RajinBelajar_ProcessSpecification_draft.docx`).

## Kesimpulan

**Belum aman.** Kerangka tabel spesifikasinya sudah benar, tapi ada tiga masalah besar:

1. **Logika prosesnya belum ditulis.** Tidak ada Structured English untuk ke-8 proses. Decision tree 3.1 hanya disebut, tidak digambar. Decision table 3.4 belum lengkap. Padahal logika proses adalah inti Modul 6 (kriteria Ketepatan logika 25% + Bentuk spesifikasi 20%).
2. **Masih memakai nama DFD lama.** `infoKatalog/Ketersediaan`, `dataBuku`, `simpanDataKoleksi`, "Membuat Laporan Transaksi Fisik", serta fitur reservasi yang sudah dihapus. Kriteria Kesesuaian dengan DFD bernilai 25%.
3. **Pengujian baru mencakup 2 dari 8 proses** (3.1 dan 3.4), dan traceability justru tidak memuat EV-03 dan EV-05.

Bagian yang sudah bagus dan bisa dipertahankan: format tabel per proses, aturan bisnis 3.1/3.2, dan temuan di TC-07 dan TC-08 (keduanya benar dan menunjukkan penelusuran yang sungguh-sungguh).

---

## Per Bagian

### Sampul (hal. 1)
| Masalah | Perbaikan | P |
|---|---|---|
| Judul masih "JUDUL JUDUL ..." | "PROCESS SPECIFICATION / SISTEM LAYANAN PERPUSTAKAAN KAMPUS (SILAPUS)" | P1 |

### Menginventarisasi Proses Primitif (hal. 2–3)
| Baris | Kolom | Sekarang | Seharusnya | P |
|---|---|---|---|---|
| 1.0 | Store | Ditulis: D1 | Baca & Tulis: D1 (cek NIM/NIP sudah terdaftar; EV-09) | P1 |
| 2.1 | Input / Output | `dataPencarian, dataBuku` / `infoKatalog/Ketersediaan` | `dataPencarian` (+ baca `dataKoleksiBuku`) / `informasiKoleksiBuku` | P1 |
| 2.2 | Output | `simpanDataKoleksi` | `statusPengelolaanKoleksi` (+ tulis `dataKoleksiBuku`); store Baca & Tulis D2 | P1 |
| 2.2 | Bentuk Logika | Decision Table (spesifikasinya: Structured English) | Structured English (CASE Tambah/Ubah/Hapus) | P2 |
| 3.1 | Store | Dibaca: D1, D2 | + D3 (`peminjamAktif`) untuk cek denda dan kuota | P1 |
| 3.1 | Bentuk Logika | Decision Table (spesifikasinya & bagian uji: Decision Tree) | pilih satu, lalu buat gambarnya/tabelnya (lihat 3.1 & 3.4 di bawah) | P1 |
| 3.3 | Store | Ditulis: D3 | Baca & Tulis D3 (validasi pembayaran) | P1 |
| 4.0 | Nama | Membuat Laporan Transaksi Fisik | Membuat Laporan Sirkulasi (nama di DFD & M03 siap-timpa) | P1 |
| semua | — | Tidak ada daftar parameter (LamaPinjam, TarifDenda, KuotaPinjam, BatasPerpanjangan) | tambah tabel parameter (salin dari draft) | P2 |

### Process Specification

| Proses | Elemen | Masalah | Perbaikan | P |
|---|---|---|---|---|
| semua | — | **Tidak ada Structured English** | Tambah blok Structured English tiap proses (salin dari draft, sesuaikan kata) | P1 |
| 1.0 | Data store dibaca | "-", padahal aturan 3 "NIM/NIP tidak boleh mendaftar ulang" | D1 Data Anggota | P1 |
| 1.0 | Event | EV-09 tercantum di inventaris, tapi spesifikasi hanya membahas pendaftaran | Tambah jalur EV-09 (update status) | P2 |
| 1.0 | Postcondition | "mendapat ID Anggota" (elemen tidak ada di M05) | "NoIdentitas tercatat sebagai anggota" | P3 |
| 2.1 | Input/Output/Referensi | `dataBuku`, `infoKatalog/Ketersediaan` | `dataKoleksiBuku`, `informasiKoleksiBuku` | P1 |
| 2.1 | Aturan 1 | "Hanya koleksi berstatus aktif" (tidak ada status aktif koleksi di M05) | hapus, atau "hanya eksemplar Tersedia yang dihitung" | P2 |
| 2.2 | Output | `simpanDataKoleksi (ke D2)` (nama sudah dihapus, PR-02) | `statusPengelolaanKoleksi`; tulis `dataKoleksiBuku` | P1 |
| 2.2 | Data store dibaca | "-", padahal "KodeBuku harus unik" | D2 Data Koleksi | P1 |
| 2.2 | Tujuan | "Menambah atau memperbarui" | + "menghapus" (EV-08) | P3 |
| 3.1 | Data store dibaca | D1, D2 | + D3 Transaksi Fisik (`peminjamAktif`) | P1 |
| 3.1 | Exception | "Anggota diblokir" | "Anggota tidak aktif" (StatusKeaktifan hanya Aktif/Nonaktif) | P2 |
| 3.1 | Referensi data | `dataPeminjaman` | `dataPeminjamanBaru`, `peminjamAktif` | P2 |
| 3.1 | Precondition | "Petugas sudah login" (detail implementasi) | "Petugas memasukkan NoIdentitas dan 1–3 KodeEksemplar" | P3 |
| 3.2 | Postcondition | "eksemplar menjadi Tersedia" (bertentangan dengan exception KondisiBuku Rusak/Hilang) | "Tersedia, atau Rusak/Hilang sesuai KondisiBuku" | P2 |
| 3.2 | Precondition | "tanggal kembali diinput" | tanggal kembali = tanggal sistem | P3 |
| 3.3 | Data store dibaca | "-" | D3 (`peminjamAktif`) untuk cek JumlahDibayar = TotalDenda | P1 |
| 3.3 | Precondition | hanya jalur dataKeterlambatan | + jalur pembayaran (`catatanDenda`) | P2 |
| 3.3 | Aturan 2 / Exception | "Belum Dibayar atau Lunas"; "Pembayaran denda gagal dikonfirmasi" | `[Tanpa Denda \| Belum Lunas \| Lunas]`; "Jumlah pembayaran tidak sesuai dengan total denda" | P2 |
| 3.3 | Referensi data | `dataPeminjaman` | `dataDenda`, `peminjamAktif` | P2 |
| 3.4 | Aturan 3 | "(misal 2 kali)" | "maksimal 2 kali" | P2 |
| 3.4 | Aturan 4 & Exception | Reservasi | **hapus**: tidak ada fitur reservasi di DFD dan sudah dihapus dari EV-05 | P1 |
| 3.4 | Precondition | "Belum melewati jatuh tempo" (ini kondisi yang diperiksa, bukan prasyarat) | "Anggota mengajukan perpanjangan untuk satu IDTransaksi" | P2 |
| 3.4 | Referensi data | `dataPeminjaman` | `pembaruanMasaPinjam` | P2 |
| 4.0 | Nama | Membuat Laporan Transaksi Fisik | Membuat Laporan Sirkulasi | P1 |
| 4.0 | Aturan 1 | "Hanya dapat diakses Kepala Perpustakaan" (hak akses, bukan logika) | ganti "Periode tidak boleh di masa depan" | P3 |

### Decision Table 3.4 (hal. 9–10)
| Masalah | Perbaikan | P |
|---|---|---|
| Header R1–R6, tetapi baris kondisi hanya K1–K3; K4 (batas) dan K5 (reservasi) yang dipakai di uji tidak ada di tabel | Lengkapi kondisi; hapus K5 reservasi | P1 |
| TC-07 menemukan K0 (transaksi tidak ditemukan) belum ada | Tambah K0 sebagai kondisi pertama (sesuai temuan sendiri) | P1 |
| TC-08: urutan alasan penolakan penting | Ini tanda 3.4 lebih cocok **decision tree** (urutan pemeriksaan menentukan alasan). Draft memakai decision tree 3.4 dan decision table 3.1 | P2 |

### Decision Tree 3.1
| Masalah | Perbaikan | P |
|---|---|---|
| Disebut di spesifikasi dan bagian uji, tetapi tidak ada gambarnya | Gambar pohon, atau pakai decision table (kondisi independen, 16 kombinasi) seperti draft DT-2 | P1 |
| TC-11 menemukan nilai kuota belum terdefinisi | KuotaPinjam = 3 (M05 v0.1 baseline, EV-03); masukkan ke tabel parameter | P2 |

### Memvalidasi dengan Contoh Uji (hal. 10–13)
| Masalah | Perbaikan | P |
|---|---|---|
| Baru 13 kasus, hanya untuk 3.4 dan 3.1 | Tambah uji untuk 1, 2.1, 2.2, 3.2, 3.3, 4 (draft punya 41 kasus) | P1 |
| TC-05 menguji reservasi | Hapus | P1 |
| Data uji berupa deskripsi ("denda Rp 3.000", "jatuh tempo kemarin") | Pakai nilai konkret dan nilai batas (tanggal, JumlahPerpanjangan = 1/2, kuota 3) | P2 |

### Traceability Review (hal. 13)
| Masalah | Perbaikan | P |
|---|---|---|
| Tidak ada baris EV-03 (3.1) dan EV-05 (3.4), padahal keduanya yang sudah diuji | Tambah | P1 |
| Nama lama: `infoKatalog/Ketersediaan`, `simpanDataKoleksi` | Nama baku DFD | P1 |
| Kasus Uji "Belum diuji" | Isi ID uji setelah paket uji lengkap | P1 |
| EV-08 berstatus "Lengkap" padahal output-nya tidak ada di DFD | "Perlu perbaikan" sampai output diganti | P2 |

### Bagian yang belum ada
Revision History · Log Kontribusi · Pertanyaan Refleksi (draft sudah punya jawaban) · Peer review (`_Review.pdf`). — **P1**

---

## Cara Tercepat

1. Pertahankan tabel spesifikasi kelompok, lalu perbaiki baris-baris di atas. Kebanyakan hanya ganti nama atau tambah store.
2. Salin dari draft: **Structured English** (8 proses), **DT-2** (3.1), **DTree-1** (3.4, gambar PNG), **tabel parameter**, **paket uji 41 kasus**, **traceability**, **refleksi**.
3. Kalau kelompok tetap ingin 3.4 memakai decision table, lengkapi tabelnya (K0, K4, tanpa reservasi) lalu pakai DT-2 untuk 3.1 alih-alih decision tree.
4. Item yang bergantung pada M05 (entri baru, `catatanDenda`, D3) mengikuti [`M05-data-dictionary.md`](M05-data-dictionary.md).
