# M01 — Project Charter (Siap Timpa)

Sumber: `baselines/PRPL_M01_2B_RajinBelajar_Charter-1.pdf`. Urutan dan judul bagian sama dengan dokumen; salin per bagian lalu timpa. Daftar perubahan ada di [Catatan Perubahan](#catatan-perubahan) paling bawah.

---

## A. Identitas Proyek

Proyek yang sedang dikerjakan ini adalah SILAPUS (Sistem Layanan Perpustakaan Kampus), yang disusun sebagai bagian dari mata kuliah Pengantar Rekayasa Perangkat Lunak (Praktik) dengan kode mata kuliah 25IF2112. Proyek ini dikerjakan oleh mahasiswa D3 Teknik Informatika, Politeknik Negeri Bandung, di bawah pengampuan Bapak Irwan Setiawan, S.Si., M.T. dan Bapak Yadhi Aditya Permana, S.T., M.Kom.

Proyek dikerjakan oleh Kelompok 6 (RajinBelajar) dari kelas 2B - D3, dengan anggota kelompok terdiri atas Wildan M Zaki (251511062), Sahizidan Lukman Hakim (251511060), M. Rayhan Maulana Farid (251511054), Irfan Ardiansah Sulaeman (251511043) dan Aisy Fathryan Siswandar (251511033).

## B. Latar Belakang

Perpustakaan kampus merupakan salah satu unit layanan penting yang mendukung kegiatan akademik, karena melayani berbagai kebutuhan seperti pendaftaran anggota, pencarian koleksi, peminjaman, pengembalian, perpanjangan, pembayaran denda, pengadaan koleksi, hingga penyusunan laporan kinerja layanan.

Namun, sebagian besar proses tersebut masih dilakukan secara manual melalui formulir dan spreadsheet yang terpisah, sehingga menimbulkan beberapa masalah seperti status ketersediaan koleksi tidak selalu terupdate secara real-time, pencatatan denda keterlambatan sering terlambat, status mahasiswa aktif/tidak dikarenakan layanan kampus yang belum terintegrasi dengan sistem akademik yang dapat menimbulkan rawan kesalahan pada peminjaman bagi anggota yang berhak, serta belum tersedia laporan berkala yang dapat merangkum kondisi koleksi, peminjaman, keterlambatan, dan denda secara otomatis.

Berdasarkan kondisi tersebut, diperlukan sebuah sistem informasi bernama SILAPUS (Sistem Layanan Perpustakaan Kampus) yang dapat mengintegrasikan seluruh proses layanan perpustakaan ke dalam satu sistem yang terpusat, sehingga data koleksi dan transaksi lebih akurat, pencatatan denda lebih konsisten, validasi keanggotaan dapat dilakukan secara otomatis melalui integrasi dengan Sistem Akademik, serta laporan kinerja layanan dapat dihasilkan lebih cepat dan andal untuk mendukung pengambilan keputusan oleh pihak manajemen perpustakaan.

## C. Problem Statement

| ID | Problem Statement | Stakeholder | Bukti/Fakta | Dampak | Prioritas |
|---|---|---|---|---|---|
| P_01 | Anggota sering tidak mengetahui apakah buku yang dicari masih tersedia, karena data koleksi masih dicatat di formulir dan spreadsheet yang terpisah sehingga datanya tidak valid, yang mengakibatkan ketika anggota datang ke rak ternyata bukunya tidak ada di rak tersebut | Anggota | proses pencatatan data masih melalui formulir dan spreadsheet yang terpisah sehingga status ketersediaan buku tidak selalu valid | pengalaman anggota terhadap layanan perpustakaan menjadi kurang nyaman | sedang |
| P_02 | Petugas belum dapat langsung melakukan cek status keanggotaan mahasiswa aktif atau tidak dikarenakan belum terkoneksi dengan sistem akademik, sehingga akan ada kesempatan bagi anggota yang sudah tidak aktif bisa meminjam | Sistem akademik | sistem harus dapat terhubung dengan sistem akademik untuk memvalidasi status mahasiswa apakah aktif atau tidak | berpeluang layanan akan disalahgunakan oleh anggota yang bukan berhaknya | tinggi |
| P_03 | petugas kesulitan mencatat denda tepat waktu dikarenakan proses pengembalian masih manual, sehingga berpotensi terjadi kesalahan pada pencatatan denda sesuai waktu pengembalian buku | Petugas | pencatatan denda yang terlambat atau tidak sesuai | berpotensi ada pendapatan denda yang terlewat sehingga data keuangan menjadi kurang akurat | tinggi |
| P_04 | Tidak ada laporan terkait dalam rentang tertentu (seperti per bulan), mengenai koleksi, peminjaman, keterlambatan dan denda untuk memantau kinerja layanan dan kondisi koleksi | Kepala Perpustakaan | Kepala Perpustakaan memerlukan laporan periodik mengenai koleksi, peminjaman, keterlambatan, dan denda. | Laporan telat | Tinggi |
| P_05 | Anggota tidak punya cara untuk melakukan cek status peminjamannya seperti kapan jatuh tempo dan dendanya, karena informasinya hanya dimiliki oleh petugas saja | Anggota | sebagian proses peminjaman masih dilakukan melalui formulir dan spreadsheet yang terpisah dan sepenuhnya dikelola oleh petugas sehingga anggota tidak dapat memeriksa status peminjamannya sendiri | Memungkinkan anggota jadi lebih sering terlambat mengembalikan buku dan juga tidak tahu bahwa dendanya akan terus bertambah | Sedang |

Setelah kelompok kami berdiskusi untuk memilih 3 dari problem statement yang sudah ditentukan, berdasarkan kriteria dampak, frekuensi, dan urgensi, kelompok kami memilih P_02, P_03, P_04 sebagai 3 masalah prioritas yang akan menjadi fokus analisis pada proyek SILAPUS ini.

Dari sisi frekuensi, P_02 dan P_03 terjadi hampir setiap hari seiring berlangsungnya transaksi peminjaman dan pengembalian, sehingga dampaknya langsung dirasakan oleh anggota maupun petugas secara rutin. Sementara P_04, meskipun frekuensinya bulanan, memiliki urgensi tinggi karena berkaitan langsung dengan kebutuhan Kepala Perpustakaan selaku pihak yang memiliki pengaruh besar terhadap keberlangsungan proyek ini.

Dengan demikian, ketiga masalah ini dinilai paling mendesak untuk diselesaikan lebih dahulu dibandingkan masalah lain.

## D. Tujuan

Secara umum, proyek ini bertujuan untuk membangun sistem layanan perpustakaan digital (SILAPUS) sehingga bisa mengatasi kendala utama transparansi data koleksi, keakuratan denda, dan pelaporan.

Secara lebih spesifiknya lagi, dijelaskan pada poin-poin berikut:
1. Menyediakan layanan pencarian katalog koleksi buku yang transparan dan real-time bagi anggota untuk mengeliminasi ketidakpastian fisik buku.
2. Mengotomatisasi pencatatan dan perhitungan denda keterlambatan saat pengembalian buku guna menghindari kebocoran pendapatan denda.
3. Menyediakan modul rekapitulasi laporan periodik (peminjaman, keterlambatan, dan denda) secara otomatis bagi Kepala Perpustakaan.

## E. Stakeholder

| Stakeholder | Peran/Kepentingan | Informasi Diberikan | Informasi Dibutuhkan | Pengaruh (T/S/R) |
|---|---|---|---|---|
| Anggota | Memperoleh pelayanan dan transaksi yang cepat dan jelas | Data diri, permintaan peminjaman, pengembalian | Koleksi buku, status transaksi | T |
| Petugas Perpustakaan | Mencatat dan memvalidasi transaksi secara akurat | Data validasi anggota, transaksi dan data koleksi | Status anggota | T |
| Kepala Perpustakaan | Memantau kinerja layanan dan kondisi koleksi | Permintaan laporan | Laporan periodik koleksi, peminjaman, keterlambatan, dan denda | S |
| Sistem Akademik | Menyediakan data status mahasiswa untuk validasi | Status mahasiswa | Permintaan validasi status | S |

Gambar Stakeholder map SILAPUS: *(gambar tetap)*

## F. Ruang Lingkup

| In Scope | Out of Scope | Asumsi | Dependensi | Batasan |
|---|---|---|---|---|
| Pendaftaran anggota, pencarian katalog buku, & pengelolaan data koleksi. | - | Anggota perpustakaan adalah mahasiswa atau dosen. | - | Masyarakat umum tidak bisa mendaftar. |
| Transaksi peminjaman, pengembalian, & perpanjangan. | Modul pengadaan (pembelian) koleksi buku baru. | Ada SOP yang sudah tetap terkait aturan-aturan durasi peminjaman. | - | Pengembangan akan difokuskan pada alur transaksi dalam ruang lingkup In Scope. |
| Validasi status mahasiswa terintegrasi Sistem Akademik. | Integrasi payment gateway denda online. | Integrasi terhadap sistem akademik cukup dengan NIM/NIP yang diinputkan ketika pendaftaran anggota. | Sistem Akademik Kampus: Ketersediaan akses data/API untuk validasi status mahasiswa. | Proses integrasi harus mempertimbangkan keamanan kedua sistem. |
| Perhitungan dan pencatatan denda otomatis saat pengembalian buku. | Fitur analitik prediktif berbasis machine learning untuk tren peminjaman. | Aturan tarif denda harian bersifat tetap sesuai kebijakan perpustakaan selama masa pengembangan. | - | Pembayaran dapat dilakukan cash maupun non-cash. Tidak menerima hutang. |
| Pembuatan laporan bulanan dari data peminjaman, koleksi, dan denda. | | Laporan yang dihasilkan cukup dalam berupa file pdf atau excel. Tidak harus langsung terkirim ke email kepala perpustakaan. | - | Harus ada batasan maksimal rentang penarikan data agar proses tidak terlalu berat. |

## G. Deliverable

| Kategori Deliverable | Nama Dokumen | Keterangan |
|---|---|---|
| Dokumen Inisiasi | Project Charter & Stakeholder Map. | Dokumen yang mendefinisikan masalah, ruang lingkup, tujuan, batas sistem awal, dan daftar pemangku kepentingan. |
| Model Analisis Terstruktur | Paket Diagram Terstruktur (Context Diagram & DFD). | Berisi Event List, Event Table, Context Diagram, Data Flow Diagram (DFD Level 0 dan bertingkat), Kamus Data, dan Process Specification. |
| Model Berorientasi Objek | Paket Diagram UML | Berisi Use Case Diagram & Specification, Domain Model, System Sequence Diagram (SSD), Operation Contract, Class Diagram, dan Deployment Diagram. |
| Spesifikasi Spesial | Dokumen SRS (Software Requirements Specification). | Dokumen final yang mengintegrasikan seluruh kebutuhan perangkat lunak SILAPUS secara lengkap dan tertelusur. |
| Dokumentasi Manajemen Proyek | Log Proyek & Pengendalian Versi. | Kumpulan lembar Revision History, Log Kontribusi Individu, dan Checklist Peer Review yang diperbarui setiap pertemuan. |

## H. Risiko Awal

| Risiko | Peluang | Dampak | Mitigasi | Pemilik Risiko |
|---|---|---|---|---|
| Data eksternal tidak tersedia (API/Akses ke Sistem Akademik kampus down atau belum siap). | Sedang | Tinggi (Validasi status mahasiswa akan terhambat sehingga pendaftaran dan transaksi peminjaman tidak bisa dilakukan). | Menganalisis batasan teknis dari awal dan menggunakan data dummy (tiruan) mahasiswa sementara waktu agar pengembangan dan pengujian tetap berjalan. | Analis |
| Kebutuhan berubah (Misal: Aturan tarif denda harian atau kebijakan perpustakaan tiba-tiba direvisi). | Sedang | Sedang (Menyebabkan rework atau pengulangan pembuatan diagram dan artefak pendukung). | Menetapkan baseline ruang lingkup yang tegas dan menerapkan prosedur persetujuan jika ada change request sesuai Mekanisme Perubahan. | Reviewer |
| Ruang lingkup tidak terkendali (Scope creep, misal: ada anggota yang memaksa ingin memasukkan modul payment gateway sungguhan). | Sedang | Tinggi (Biaya waktu membengkak dan proyek tidak selesai sesuai jadwal singkat yang ada). | Berpegang teguh secara disiplin pada tabel In Scope dan Out of Scope di bagian F saat membuat DFD dan model lainnya. | Koordinator |
| Kontribusi anggota kelompok tidak seimbang / komunikasi lemah. | Rendah | Tinggi (Bisa terjadi kesalahan interpretasi, delay, atau desain artefak yang tidak konsisten antar anggota). | Mencatat keputusan di notulen, melakukan peer review berkala, menggunakan revision history, dan mewajibkan pengisian log kontribusi individu. | Koordinator |

## I. Penjadwalan

| Tanggal | Agenda Kegiatan | Tenggat |
|---|---|---|
| 14 Sept 2026 | Penyusunan dokumen project charter, tahapan analisis masalah, stakeholder, dan dependensi proyek. | 18 Sept 2026 |
| 23 Sept 2026 | Penyusunan event list dari aplikasi, analisis berbagai kemungkinan yang perlu diperhatikan terhadap pengembangan aplikasi. | 30 Sept 2026 |
| 01 Okt 2026 | Penyusunan Data Flow Diagram (DFD), analisis alur keseluruhan dari aplikasi untuk diimplementasikan. | 07 Okt 2026 |

## J. Mekanisme Perubahan

1. Penomoran Versi
   Versi dokumen dihitung berdasarkan minggu pengumpulan tugas.
2. Pembaruan Versi
   Jika terdapat revisi saat berganti minggu, versi dokumen akan naik satu tingkat.
3. Pencatatan & Review
   Setiap perubahan wajib mencatat bagian yang diubah, alasan perubahan, nama pengedit, serta telah direvisi/disetujui oleh minimal satu anggota kelompok lain.

## K. Kriteria Keberhasilan

1. Sistem SILAPUS terbukti berhasil terhubung dengan Sistem Akademik untuk melakukan validasi status keaktifan mahasiswa.
2. Sistem mampu mengotomatisasi pencatatan serta perhitungan denda keterlambatan secara otomatis saat proses pengembalian buku.
3. Sistem dapat menghasilkan rekapitulasi laporan periodik (bulanan) mengenai peminjaman, keterlambatan, dan denda untuk Kepala Perpustakaan secara akurat.
4. Seluruh artefak proyek (seperti Event List, Context Diagram, dan DFD) memiliki konsistensi, kelengkapan dokumentasi, dan keterlacakan (traceability) yang jelas mulai dari identifikasi masalah hingga dokumentasi final.

---

## Catatan Perubahan

Perubahan **isi** (karena balancing/konsistensi) ditandai ★. Sisanya hanya typo/spasi.

| Bagian | Perubahan | Alasan |
|---|---|---|
| A | "Layaanan" → "Layanan"; "dibawah" → "di bawah"; ★ "[Nama Kelompok, misalnya Kelompok 1]" → "Kelompok 6 (RajinBelajar)" | Placeholder tertinggal (RV-M01-01) |
| B | "ter update" → "terupdate"; tambah titik di akhir paragraf 3 | Typo |
| C | Tabel: "kolekasi", "di catat", "datannya", "msaih", "spreasheet", "statu", "perpustakkan", "disalahgunaka n", "mengembailik an", "Perpustak aan" diperbaiki. Paragraf: "berrdiskusi", "dampak,frekuensi", "kelompomi", "P_02,P_03,P_04", "sebegai" diperbaiki; tambah titik di akhir kalimat | Typo |
| D | Tidak berubah | — |
| E | "Menperoleh" → "Memperoleh" | Typo |
| F | ★ In Scope baris 1 + "& pengelolaan data koleksi"; ★ Out of Scope baris 2 + "(pembelian)"; ★ Asumsi baris 3 "NIM" → "NIM/NIP"; ★ In Scope baris 5 + "koleksi"; "perpustakaa", "mempertimban gan" diperbaiki | Proses 2.2/EV-08 masuk lingkup (RV-M01-03); anggota mahasiswa/dosen → NoIdentitas = [NIM \| NIP] di M05 (RV-M01-04); laporan membaca D2 Data Koleksi |
| G | "Beroirentasi" → "Berorientasi"; "Model analisis Terstruktur" → "Model Analisis Terstruktur" | Typo |
| H | Judul & kolom "Resiko" → "Risiko"; "maksa" → "memaksa"; "Review er", "Koordin ator" disambung | Typo (KBBI: risiko) |
| I | "07 Okt2026" → "07 Okt 2026" | Typo |
| J | "&amp;" → "&"; "telat direvisi" → "telah direvisi" | Typo |
| K | Tidak berubah | — |

Tidak diterapkan (bukan balancing): RV-M01-02 urutan tujuan, RV-M01-06 tambah jadwal M04–M06.
