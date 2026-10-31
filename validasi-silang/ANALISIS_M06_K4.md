# Analisis Validasi Silang M06 Kelompok 4

Sumber: `PRPL_M06_2B_Kelompok 4_.pdf` (25 hlm), dicek silang ke `PRPL_M05_2B_Kelompok 4_DataDictionary (1).docx`.
Catatan: M05 yang kita pegang mungkin bukan versi terakhir mereka (traceability M06 merujuk entri #19-#26, inventaris M05 kita cuma 18 baris), jadi temuan soal nama flow ditulis "tidak ditemukan di M05 yang kami terima".

## A. Checklist

| Item | Hasil | Catatan singkat |
|---|---|---|
| **Clear and Descriptive Process Names** | | |
| Process Name Consistency | ✓ | Nama proses sama di bagian I, II, III. (Kecil: nomor "1"/"1.0" dan "4"/"4.0" dipakai bergantian.) |
| Meaningful Name | ✓ | Kata kerja + objek (Validasi Anggota, Hitung Denda, dst.). |
| **Accurate and Complete Inputs** | | |
| Inputs Identified | ✗ | 3.3: logika membaca `dataPengembalianBuku` dan `RincianDenda`, padahal input yang dicantumkan hanya `rincianPengembalian`. |
| Input Formats Described | ✗ | Referensi data kosong pada 3.3 dan 4, jadi format input tidak bisa ditelusuri ke kamus data. |
| **Accurate and Complete Outputs** | | |
| Outputs Identified | ✗ | 3.1: tabel menulis output `rincianKeterlambatan`, logika membuat `statusKeterlambatan` (nama di M05 juga `statusKeterlambatan`). Penolakan di 2.1/2.2 tidak punya output ke entitas. |
| Output Formats Described | ✗ | Sama dengan input: 3.3 dan 4 tanpa referensi data. |
| **Detailed Process Description** | | |
| Clear Step-by-Step Description | ✓ | Semua proses punya logika. |
| Business Logic Described | ✗ | Ada logika yang bertentangan dengan aturan/tes (lihat B1–B3). |
| Complex Processes Broken Down | ✓ | Proses 2 dan 3 sudah dipecah jadi 2.1–2.3 dan 3.1–3.4. |
| **Preconditions** | | |
| Preconditions Identified | ✓ | Ada di semua proses. |
| Environmental Preconditions | ✗ | Hanya Proses 4 yang menyebut kondisi sistem (akses data store). Ringan. |
| **Postconditions** | | |
| Expected Outcomes | ✓ | Ada di semua proses. |
| State Changes | ✓ | Perubahan D2/D3 disebut di 2.3, 3.3, 3.4. |
| **Business Rules and Constraints** | | |
| All Relevant Business Rules Included | ✗ | Nilai kuota dan jatuh tempo tidak konsisten (B4, B5). |
| Rule Application Points Defined | ✓ | Aturan ditempel per proses. |
| **Exception Handling** | | |
| Error Handling Described | ✗ | Exception 2.3 kosong; exception 3.2 (input negatif) tidak ada di decision tree. |
| Alternative Flows | ✗ | Jalur EV-09 (pembaruan status dari Sistem Akademik) tidak ada di logika Proses 1; jalur "piutang" di aturan 3.3 tidak ada di logika. |
| **Process Triggers** | | |
| Trigger Defined | ✗ | Pemicu hanya tersirat di precondition; Proses 4 tidak menyebut kapan laporan dibuat. Ringan. |
| Manual vs. Automated | ✗ | Tidak dinyatakan (mis. Proses 4 otomatis atau atas permintaan). Ringan. |
| **Dependencies** | | |
| Dependencies on Other Processes | ✓ | Precondition menyebut proses sebelumnya (2.2 dari 2.1, dst.). |
| External Systems or Data | ✓ | Sistem Akademik disebut di Proses 1. |
| **Timing and Performance Constraints** | | |
| Performance Requirements | ✗ | Tidak ada. Tidak diwajibkan di Modul 6, jadi cukup catatan ringan. |

## B. Temuan kritis (jelas, perbaikannya kecil)

| No | Lokasi | Temuan | Perbaikan kecil |
|---|---|---|---|
| B1 | IV. Decision Table (hlm 15) | Tindakan R3 dan R4 tertukar: R3 (buku tidak tersedia) ditandai "Tolak: kuota terlampau", R4 (kuota habis) ditandai "Tolak: buku tidak tersedia". | Tukar tanda X pada baris R3 dan R4. |
| B2 | 2.1 Decision Table vs TC-PS-2.1-R3 | Aturan bisnis 2 (tunggakan denda) tidak ada sebagai kondisi di decision table, tapi TC-PS-2.1-R3 menguji "tunggakan denda" sebagai R3. Di tabel, R3 justru "anggota tidak aktif". | Tambah satu kondisi "Bebas tunggakan denda?" + satu tindakan tolak, lalu sesuaikan nomor rule di TC. |
| B3 | 3.2 Decision Tree vs TC-PS-3.2-R2/R3 | Tree hanya punya cabang Terlambat/Tidak, tapi TC menguji cabang "KonfirmasiBayar Lunas/Belum Lunas" yang tidak ada di tree. | Tambah cabang status bayar di tree, atau pindahkan dua TC itu ke 3.3 (yang memang memeriksa pelunasan). |
| B4 | 2.1 aturan bisnis vs TC-PS-2.1-R4 vs traceability | Kuota pinjam ditulis ≤ 5 eksemplar di aturan dan exception, tapi TC-2.1-R4 dan traceability bilang maksimal 1 buku. | Pilih satu angka dan samakan di 3 tempat. |
| B5 | 2.3 aturan & logika vs TC-PS-2.3-01, traceability, M05 | Jatuh tempo ditulis "7 hari" dan logika `CURRENT_DATE + 7 DAYS` (hari kalender), tapi TC, traceability, dan M05 menyebut "7 hari kerja". Contoh 19-10 → 26-10 hanya benar untuk hari kalender. | Pilih kalender atau hari kerja, samakan teksnya. |
| B6 | 1 Kelola Data Anggota, logika | `IF ... StatusAkademik = Valid THEN SEND permintaanValidasi` memeriksa status akademik sebelum permintaan validasi dikirim (urutannya terbalik). | Kondisi pertama cukup validasi format NIM/Email. |
| B7 | 3.1 output | Output `rincianKeterlambatan` (tabel) vs `statusKeterlambatan` (logika dan M05). | Samakan satu nama. |
| B8 | 3.3 logika vs aturan bisnis | Aturan bilang denda boleh "lunas atau dicatat sebagai piutang", tapi logika menolak kalau belum lunas. | Hapus kata "piutang" di aturan, atau tambah cabangnya di logika. |

## C. Temuan ringan

| No | Lokasi | Temuan |
|---|---|---|
| C1 | 2.3 | Exception kosong (mis. gagal simpan ke D3). |
| C2 | 3.3, 4 | Referensi data kosong. |
| C3 | 3.4 | Referensi data menyebut `StatusBukuBaru`, inputnya `triggerStatusBuku`. Aturan hanya Dipinjam → Tersedia, padahal M05 `triggerStatusBuku` juga membawa Rusak/Hilang, dan traceability menyebut Rusak/Hilang. |
| C4 | 4 | Data store dibaca ditulis "1 Data Anggota, 2 Data Koleksi, 3 Data Transaksi" (tanpa "D"); data store ditulis kosong (isi "-"). Nama total denda: logika `TotalDendaTerkumpul`, TC `TotalDendaBulanan`. |
| C5 | 2.2, 2.3 | Status buku memakai tiga nama: `statusKetersediaan`, `statusEksemplar`, `StatusKoleksi` (M05: `StatusKoleksi`), dan `idEksemplar` tidak ada di M05 (kunci D2 = `KodeBuku`). |
| C6 | 2.2 logika | Kalau ada buku yang tidak tersedia, tidak ada output/penolakan untuk seluruh pengajuan (IF ALL ... tanpa ELSE). |
| C7 | II. Alasan bentuk logika | 3.2 memilih Decision Tree dengan alasan "alur sekuensial matematis" (lebih cocok Structured English); 2.2 memilih Structured English dengan alasan "kombinasi kondisi" (lebih cocok decision table). Alasan dan pilihan kurang nyambung. |
| C8 | Tabel 3.2 (hlm 10–11) | Baris lanjutan postcondition terpotong jadi baris tanpa label berisi "Process 3.3". |
| C9 | Traceability (hlm 20–23) | Sisa teks salinan seperti `more_horiz`, `78.`, `910.`, `26 27.` di kolom aturan bisnis. |
| C10 | Hlm 23–25 | Tabel contoh uji 3.1–4.0 muncul dua kali (sekali di bagian V, sekali lagi setelah traceability). |
| C11 | Proses 1 | NIP disebut di aturan bisnis tapi logika hanya memproses NIM; jalur EV-09 tidak ada di logika. |
| C12 | Proses 4 | Tidak disebut pemicu (otomatis akhir bulan / atas permintaan Kepala Perpustakaan); TotalPengembalian dihitung dari transaksi yang tanggal pinjam-nya di bulan itu, bukan tanggal kembali. |
