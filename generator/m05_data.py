# -*- coding: utf-8 -*-
"""Sumber tunggal isi Kamus Data M05 SILAPUS (Kelompok 6 / RajinBelajar).

Semua nama flow & store HARUS sama dengan manajemen/BASELINE_PENAMAAN.md dan
"Silapus Latest.bpm". Ubah isi di sini, lalu jalankan build_m05.py untuk
menghasilkan xlsx + docx.
"""

VERSI = "0.2"
TANGGAL = "2026-10-21"

# ---------------------------------------------------------------------------
# 1. INVENTARIS: setiap flow/store yang muncul di CD, DFD Level 0, Level 1.
#    tipe 1 = entitas/proses <-> proses (tanpa store); tipe 2 = melibatkan store
#    lama  = nama di M05 v0.1 (baseline) bila ada padanannya
# ---------------------------------------------------------------------------
INVENTARIS = [
    # nama, jenis, tipe, lokasi, sumber, tujuan, nama_di_CD, lama
    ("dataPendaftaran", "Flow", 1, "CD, L0", "Anggota Perpustakaan", "Proses 1", "Data Pendaftaran", "dataPendaftaran"),
    ("statusPendaftaran", "Flow", 1, "CD, L0", "Proses 1", "Anggota Perpustakaan", "Status Pendaftaran", None),
    ("dataVerifikasi", "Flow", 1, "CD, L0", "Proses 1", "Sistem Akademik", "Data Verifikasi Mahasiswa", None),
    ("statusKeaktifan", "Flow", 1, "CD, L0", "Sistem Akademik", "Proses 1", "Status Keaktifan Mahasiswa", "statusKeaktifanMahasiswa"),
    ("dataPencarian", "Flow", 1, "CD, L0, L1-P2", "Anggota Perpustakaan", "Proses 2 / 2.1", "Data Pencarian", "dataPencarian"),
    ("informasiKoleksiBuku", "Flow", 1, "CD, L0, L1-P2", "Proses 2 / 2.1", "Anggota Perpustakaan", "Informasi Katalog", "informasiKoleksiBuku"),
    ("dataKoleksiBaru", "Flow", 1, "CD, L0, L1-P2", "Petugas Perpustakaan", "Proses 2 / 2.2", "Data Koleksi Buku", None),
    ("dataTransaksiFisik", "Flow", 1, "CD, L0", "Petugas Perpustakaan", "Proses 3", "Data Transaksi Fisik", None),
    ("dataTransaksiPeminjaman", "Flow", 1, "L1-P3", "Petugas Perpustakaan", "Proses 3.1", None, "formTransaksiPinjam"),
    ("dataTransaksiPengembalian", "Flow", 1, "L1-P3", "Petugas Perpustakaan", "Proses 3.2", None, "formTransaksiKembali"),
    ("statusTransaksiDanBukti", "Flow", 1, "CD, L0, L1-P3", "Proses 3 / 3.1 / 3.2", "Petugas Perpustakaan", "Status Transaksi", None),
    ("catatanDenda", "Flow", 1, "CD, L0, L1-P3", "Petugas Perpustakaan", "Proses 3 / 3.3", "Konfirmasi Denda", "buktiKonfirmasiDenda"),
    ("buktiPengembalianDanDenda", "Flow", 1, "CD, L0, L1-P3", "Proses 3 / 3.3", "Petugas Perpustakaan", "Bukti Pengembalian dan Denda", None),
    ("dataKeterlambatan", "Flow", 1, "L1-P3 (internal)", "Proses 3.2", "Proses 3.3", None, None),
    ("permintaanPerpanjangan", "Flow", 1, "CD, L0, L1-P3", "Anggota Perpustakaan", "Proses 3 / 3.4", "Permintaan Perpanjangan", "permintaanPerpanjangan"),
    ("statusPerpanjangan", "Flow", 1, "CD, L0, L1-P3", "Proses 3 / 3.4", "Anggota Perpustakaan", "Status Perpanjangan", None),
    ("permintaanLaporan", "Flow", 1, "CD, L0", "Kepala Perpustakaan", "Proses 4", "Permintaan Laporan", None),
    ("laporanBulanan", "Flow", 1, "CD, L0", "Proses 4", "Kepala Perpustakaan", "Laporan Bulanan Sirkulasi & Denda", "laporanSirkulasiBulanan"),
    ("dataAnggota", "Flow", 2, "L0", "Proses 1", "D1 Data Anggota", None, None),
    ("statusAnggota", "Flow", 2, "L0, L1-P3", "D1 Data Anggota", "Proses 3 / 3.1 / 3.4", None, None),
    ("dataKoleksiBuku", "Flow", 2, "L0, L1-P2", "D2 Data Koleksi <-> Proses 2", "2.1 (baca), 2.2 (tulis)", None, None),
    ("dataEksemplar", "Flow", 2, "L0, L1-P3", "D2 Data Koleksi", "Proses 3 / 3.1", None, None),
    ("pembaruanEksemplar", "Flow", 2, "L0, L1-P3", "Proses 3 / 3.1 / 3.2", "D2 Data Koleksi", None, None),
    ("dataKoleksi", "Flow", 2, "L0", "D2 Data Koleksi", "Proses 4", None, None),
    ("peminjamAktif", "Flow", 2, "L0, L1-P3", "D3 Transaksi Fisik", "Proses 3 / 3.2 / 3.4", None, None),
    ("dataPeminjaman", "Flow", 2, "L0", "Proses 3", "D3 Transaksi Fisik", None, None),
    ("dataPeminjamanBaru", "Flow", 2, "L1-P3", "Proses 3.1", "D3 Transaksi Fisik", None, None),
    ("pembaruanPengembalian", "Flow", 2, "L1-P3", "Proses 3.2", "D3 Transaksi Fisik", None, None),
    ("dataDenda", "Flow", 2, "L1-P3", "Proses 3.3", "D3 Transaksi Fisik", None, None),
    ("pembaruanMasaPinjam", "Flow", 2, "L1-P3", "Proses 3.4", "D3 Transaksi Fisik", None, None),
    ("dataTransaksi", "Flow", 2, "L0", "D3 Transaksi Fisik", "Proses 4", None, None),
    ("D1 Data Anggota", "Store", 2, "L0, L1-P3", "Proses 1", "Proses 3 (3.1, 3.4)", None, "dataAnggota (store)"),
    ("D2 Data Koleksi", "Store", 2, "L0, L1-P2, L1-P3", "Proses 2 (2.2), 3 (3.1, 3.2)", "Proses 2 (2.1), 3 (3.1), 4", None, "dataKoleksiBuku (store)"),
    ("D3 Transaksi Fisik", "Store", 2, "L0, L1-P3", "Proses 3 (3.1-3.4)", "Proses 3 (3.2, 3.4), 4", None, "dataTransaksiSirkulasi"),
]

# ---------------------------------------------------------------------------
# 2. DEFINISI STRUKTUR (dipakai untuk entri komposit & penguraian otomatis)
#    kind: komposit | record | elemen | enum | dasar
# ---------------------------------------------------------------------------
DEF = {}
def d(nama, struktur, kind):
    DEF[nama] = (struktur, kind)

# --- dasar
d("angka", "[0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9]", "dasar")
d("hurufKapital", "[A | B | ... | Z]", "dasar")
d("hurufKecil", "[a | b | ... | z]", "dasar")
d("huruf", "[hurufKapital | hurufKecil]", "dasar")
d("spasi", '" "', "dasar")
d("tandaBaca", '["." | "," | "-" | "\'" | ":" | "/" | "(" | ")" | "&"]', "dasar")
d("karakter", "[huruf | angka | spasi | tandaBaca]", "dasar")
d("Tahun", "4{angka}4", "elemen")
d("Bulan", "2{angka}2", "elemen")
d("Hari", "2{angka}2", "elemen")

# --- elemen
d("NomorIdentitas", "[NIM | NIP]", "elemen")
d("NIM", "9{angka}9", "elemen")
d("NIP", "18{angka}18", "elemen")
d("KategoriAnggota", "[Mahasiswa | Dosen]", "enum")
d("NamaLengkap", '1{huruf | spasi | "." | "\'"}100', "elemen")
d("ProgramStudi", '3{huruf | spasi | "-"}60', "elemen")
d("EmailKampus", 'NamaPengguna + "@" + DomainKampus', "elemen")
d("NamaPengguna", '1{hurufKecil | angka | "." | "_"}40', "elemen")
d("DomainKampus", '[("polban.ac.id") | (Subdomain + ".polban.ac.id")]', "elemen")
d("Subdomain", "2{hurufKecil}10", "elemen")
for t in ("TanggalDaftar", "TanggalPinjam", "TanggalJatuhTempo", "TanggalKembali", "TanggalBayar", "TanggalLaporan"):
    d(t, 'Tahun + "-" + Bulan + "-" + Hari', "elemen")
d("StatusAnggota", "[Aktif | Nonaktif]", "enum")
d("StatusAkademik", "[Aktif | TidakAktif | Cuti | TidakTerdaftar]", "enum")
d("StatusProses", "[Berhasil | Ditolak]", "enum")
d("AlasanPenolakan", "[DataTidakLengkap | TidakTerdaftarAkademik | StatusAkademikTidakAktif | SudahTerdaftar | "
  "AnggotaNonaktif | MemilikiDendaBelumLunas | KuotaPinjamPenuh | EksemplarTidakTersedia | "
  "TransaksiTidakDitemukan | BatasPerpanjanganTercapai | SudahLewatJatuhTempo]", "enum")
d("KataKunci", "1{karakter}100", "elemen")
d("JenisPencarian", "[Judul | Pengarang | ISBN | Subjek]", "enum")
d("KodeEksemplar", '"SIL-BK-" + 4{angka}4', "elemen")
d("ISBN", "13{angka}13", "elemen")
d("JudulBuku", "1{karakter}200", "elemen")
d("Pengarang", "1{karakter}100", "elemen")
d("Penerbit", "1{karakter}100", "elemen")
d("TahunTerbit", "4{angka}4", "elemen")
d("Subjek", "1{karakter}50", "elemen")
d("LokasiRak", '"R" + 2{angka}2 + "-" + 1{hurufKapital}1', "elemen")
d("StatusEksemplar", "[Tersedia | Dipinjam | Rusak | Hilang]", "enum")
d("JumlahTersedia", "1{angka}3", "elemen")
d("JenisPerubahan", "[Tambah | Ubah | Hapus]", "enum")
d("IDTransaksi", '"TRX-" + Tahun + Bulan + Hari + "-" + 3{angka}3', "elemen")
d("JumlahPerpanjangan", "1{angka}1", "elemen")
d("JumlahHariTerlambat", "1{angka}3", "elemen")
d("JumlahDenda", "1{angka}7", "elemen")
d("JumlahDibayar", "1{angka}7", "elemen")
d("StatusTransaksi", "[Aktif | Terlambat | Selesai]", "enum")
d("StatusDenda", "[TanpaDenda | BelumLunas | Lunas]", "enum")
d("PeriodeLaporan", 'Tahun + "-" + Bulan', "elemen")
for t in ("TotalPeminjaman", "TotalPengembalian", "TotalPerpanjangan", "TotalKeterlambatan",
          "TotalEksemplar", "TotalTersedia", "TotalDipinjam", "TotalRusakHilang"):
    d(t, "1{angka}6", "elemen")
for t in ("TotalDendaTercatat", "TotalDendaLunas", "TotalDendaBelumLunas"):
    d(t, "1{angka}9", "elemen")

# --- struktur pembantu (komposit internal, bukan flow)
d("DataBuku", "ISBN + JudulBuku + 1{Pengarang}3 + Penerbit + TahunTerbit + Subjek", "komposit")
d("HasilPencarian", "DataBuku + LokasiRak + JumlahTersedia", "komposit")
d("EksemplarInput", "KodeEksemplar + LokasiRak + StatusEksemplar", "komposit")
d("BuktiTransaksi", "IDTransaksi + NomorIdentitas + KodeEksemplar + TanggalPinjam + TanggalJatuhTempo + (TanggalKembali) + StatusTransaksi", "komposit")
d("RingkasanSirkulasi", "TotalPeminjaman + TotalPengembalian + TotalPerpanjangan + TotalKeterlambatan", "komposit")
d("RingkasanDenda", "TotalDendaTercatat + TotalDendaLunas + TotalDendaBelumLunas", "komposit")
d("RingkasanKoleksi", "TotalEksemplar + TotalTersedia + TotalDipinjam + TotalRusakHilang", "komposit")
d("RecordAnggota", "@NomorIdentitas + KategoriAnggota + NamaLengkap + ProgramStudi + EmailKampus + TanggalDaftar + StatusAnggota", "record")
d("RecordEksemplar", "@KodeEksemplar + DataBuku + LokasiRak + StatusEksemplar", "record")
d("RecordTransaksi", "@IDTransaksi + NomorIdentitas + KodeEksemplar + TanggalPinjam + TanggalJatuhTempo + JumlahPerpanjangan + "
  "(TanggalKembali) + (JumlahHariTerlambat) + (JumlahDenda) + (JumlahDibayar) + (TanggalBayar) + StatusTransaksi + StatusDenda", "record")

# --- flow & store (nama = baseline DFD)
d("dataPendaftaran", "NomorIdentitas + KategoriAnggota + NamaLengkap + ProgramStudi + EmailKampus", "komposit")
d("statusPendaftaran", "NomorIdentitas + StatusProses + [TanggalDaftar | AlasanPenolakan]", "komposit")
d("dataVerifikasi", "NomorIdentitas + KategoriAnggota", "komposit")
d("statusKeaktifan", "NomorIdentitas + StatusAkademik", "komposit")
d("dataAnggota", "RecordAnggota", "komposit")
d("dataPencarian", "KataKunci + JenisPencarian", "komposit")
d("informasiKoleksiBuku", "0{HasilPencarian}50", "komposit")
d("dataKoleksiBaru", "JenisPerubahan + DataBuku + 1{EksemplarInput}50", "komposit")
d("dataKoleksiBuku", "1{RecordEksemplar}", "komposit")
d("dataTransaksiFisik", "[dataTransaksiPeminjaman | dataTransaksiPengembalian]", "komposit")
d("dataTransaksiPeminjaman", "NomorIdentitas + 1{KodeEksemplar}3", "komposit")
d("dataTransaksiPengembalian", "1{KodeEksemplar}3", "komposit")
d("statusTransaksiDanBukti", "StatusProses + [1{BuktiTransaksi}3 | AlasanPenolakan]", "komposit")
d("catatanDenda", "IDTransaksi + JumlahDibayar + TanggalBayar", "komposit")
d("dataKeterlambatan", "IDTransaksi + NomorIdentitas + KodeEksemplar + TanggalJatuhTempo + TanggalKembali + JumlahHariTerlambat", "komposit")
d("buktiPengembalianDanDenda", "IDTransaksi + NomorIdentitas + KodeEksemplar + TanggalJatuhTempo + TanggalKembali + "
  "JumlahHariTerlambat + JumlahDenda + (JumlahDibayar + TanggalBayar) + StatusDenda", "komposit")
d("permintaanPerpanjangan", "NomorIdentitas + IDTransaksi", "komposit")
d("statusPerpanjangan", "IDTransaksi + StatusProses + [TanggalJatuhTempo + JumlahPerpanjangan | AlasanPenolakan]", "komposit")
d("statusAnggota", "NomorIdentitas + StatusAnggota", "komposit")
d("dataEksemplar", "KodeEksemplar + JudulBuku + StatusEksemplar", "komposit")
d("pembaruanEksemplar", "KodeEksemplar + StatusEksemplar", "komposit")
d("dataKoleksi", "1{RecordEksemplar}", "komposit")
d("peminjamAktif", "0{RecordTransaksi}", "komposit")
d("dataPeminjaman", "[dataPeminjamanBaru | pembaruanPengembalian | dataDenda | pembaruanMasaPinjam]", "komposit")
d("dataPeminjamanBaru", "IDTransaksi + NomorIdentitas + KodeEksemplar + TanggalPinjam + TanggalJatuhTempo + JumlahPerpanjangan + StatusTransaksi + StatusDenda", "komposit")
d("pembaruanPengembalian", "IDTransaksi + TanggalKembali + StatusTransaksi", "komposit")
d("dataDenda", "IDTransaksi + JumlahHariTerlambat + JumlahDenda + StatusDenda + (JumlahDibayar + TanggalBayar)", "komposit")
d("pembaruanMasaPinjam", "IDTransaksi + TanggalJatuhTempo + JumlahPerpanjangan", "komposit")
d("dataTransaksi", "0{RecordTransaksi}", "komposit")
d("permintaanLaporan", "PeriodeLaporan", "komposit")
d("laporanBulanan", "PeriodeLaporan + TanggalLaporan + RingkasanSirkulasi + RingkasanDenda + RingkasanKoleksi", "komposit")
d("D1 Data Anggota", "{RecordAnggota}", "komposit")
d("D2 Data Koleksi", "{RecordEksemplar}", "komposit")
d("D3 Transaksi Fisik", "{RecordTransaksi}", "komposit")

# ---------------------------------------------------------------------------
# 3. ENTRI KOMPOSIT (atribut Modul 5 §1.6)
#    alias, bentuk, arus, penjelasan, periode, volume, aturan
# ---------------------------------------------------------------------------
KOMPOSIT = {
 "dataPendaftaran": ("Formulir Pendaftaran; Data Pendaftaran (CD)", "Aliran data (dokumen bisnis)",
   "Anggota Perpustakaan -> Proses 1 Mengelola Keanggotaan",
   "Identitas calon anggota yang diajukan untuk memperoleh hak layanan perpustakaan (EV-01).",
   "Setiap ada civitas akademika yang mendaftar; puncak pada awal tahun ajaran.",
   "Estimasi 50-100 per hari pada awal semester, <10 per hari di luar itu (asumsi kelompok).",
   "Semua elemen wajib. EmailKampus wajib berdomain polban.ac.id. NomorIdentitas yang sudah ada di D1 ditolak (SudahTerdaftar)."),
 "statusPendaftaran": ("Status Pendaftaran (CD)", "Aliran data", "Proses 1 -> Anggota Perpustakaan",
   "Hasil pemrosesan pendaftaran: berhasil beserta tanggal terdaftar, atau ditolak beserta alasannya.",
   "Setiap dataPendaftaran diproses.", "Sama dengan volume dataPendaftaran.",
   "Berhasil hanya jika StatusAkademik = Aktif. AlasanPenolakan yang mungkin: DataTidakLengkap, TidakTerdaftarAkademik, StatusAkademikTidakAktif, SudahTerdaftar."),
 "dataVerifikasi": ("Data Verifikasi Mahasiswa (CD); permintaan verifikasi", "Aliran data", "Proses 1 -> Sistem Akademik",
   "Permintaan pengecekan keaktifan civitas akademika ke Sistem Akademik kampus.",
   "Setiap dataPendaftaran lengkap diterima.", "Sama dengan volume dataPendaftaran.",
   "Dikirim hanya setelah dataPendaftaran lengkap."),
 "statusKeaktifan": ("Status Keaktifan Mahasiswa (CD); statusKeaktifanMahasiswa (M05 v0.1)", "Aliran data", "Sistem Akademik -> Proses 1",
   "Jawaban Sistem Akademik tentang status akademik pemilik NomorIdentitas.",
   "Sebagai respons dataVerifikasi.", "Sama dengan volume dataVerifikasi.",
   "TidakAktif, Cuti, dan TidakTerdaftar menyebabkan pendaftaran ditolak."),
 "dataAnggota": ("-", "Aliran data (tulis ke store)", "Proses 1 -> D1 Data Anggota",
   "Rekaman anggota baru yang disimpan setelah verifikasi berhasil.",
   "Setiap pendaftaran berhasil.", "Sama dengan jumlah pendaftaran berhasil.",
   "StatusAnggota awal = Aktif; TanggalDaftar = tanggal sistem."),
 "dataPencarian": ("Data Pencarian (CD); kata kunci pencarian", "Aliran data", "Anggota Perpustakaan -> Proses 2 / 2.1 Mencari Katalog Buku",
   "Kata kunci dan jenis pencarian yang dimasukkan anggota untuk mencari koleksi (EV-02).",
   "Setiap saat selama layanan berjalan.", "Estimasi 300-500 per hari kerja (M05 v0.1).",
   "KataKunci tidak boleh kosong. Pencarian hanya membaca D2; kriteria tidak disimpan (PR-01)."),
 "informasiKoleksiBuku": ("Informasi Katalog (CD); infoKatalogKoleksi (M05 v0.1)", "Aliran data", "Proses 2 / 2.1 -> Anggota Perpustakaan",
   "Daftar buku yang cocok dengan pencarian beserta lokasi rak dan jumlah eksemplar tersedia.",
   "Setiap dataPencarian diproses.", "Sama dengan volume dataPencarian; maksimal 50 hasil per pencarian (asumsi).",
   "JumlahTersedia dihitung dari eksemplar berstatus Tersedia. Jika 0 hasil, sistem menampilkan pemberitahuan koleksi tidak ditemukan (EV-02 error 1)."),
 "dataKoleksiBaru": ("Data Koleksi Buku (CD)", "Aliran data", "Petugas Perpustakaan -> Proses 2 / 2.2 Mengelola Data Koleksi",
   "Data buku dan eksemplar yang ditambah, diubah, atau dihapus petugas (EV-08).",
   "Saat ada pengadaan atau perubahan koleksi.", "Estimasi <50 per bulan (asumsi kelompok).",
   "KodeEksemplar harus unik saat Tambah dan harus sudah ada saat Ubah/Hapus. Eksemplar berstatus Dipinjam tidak boleh dihapus."),
 "dataKoleksiBuku": ("-", "Aliran data (baca & tulis store)", "D2 Data Koleksi -> 2.1 (baca); 2.2 -> D2 Data Koleksi (tulis)",
   "Rekaman eksemplar koleksi: dibaca untuk pencarian, ditulis saat pengelolaan koleksi.",
   "Setiap pencarian (baca) dan setiap perubahan koleksi (tulis).", "Mengikuti volume dataPencarian dan dataKoleksiBaru.",
   "Sisi baca (2.1) dan sisi tulis (2.2) bersama-sama menyeimbangkan flow dua arah pada Level 0."),
 "dataTransaksiFisik": ("Data Transaksi Fisik (CD)", "Aliran data (gabungan)", "Petugas Perpustakaan -> Proses 3",
   "Input transaksi sirkulasi fisik di meja layanan; berupa transaksi peminjaman ATAU pengembalian.",
   "Harian pada jam layanan.", "Estimasi 200-400 per hari kerja (gabungan pinjam + kembali).",
   "Pada Level 1 dipecah menjadi dataTransaksiPeminjaman (3.1) dan dataTransaksiPengembalian (3.2); pemecahan sah karena strukturnya didefinisikan di sini (Modul 4 §1.4)."),
 "dataTransaksiPeminjaman": ("formTransaksiPinjam (M05 v0.1)", "Aliran data", "Petugas Perpustakaan -> 3.1 Memproses Peminjaman Buku",
   "Identitas peminjam dan eksemplar yang akan dipinjam (EV-03).",
   "Harian pada jam layanan.", "Estimasi 100-200 per hari kerja (M05 v0.1).",
   "Maksimal 3 eksemplar per anggota secara bersamaan (termasuk yang sedang dipinjam). TanggalPinjam diisi sistem, bukan diinput."),
 "dataTransaksiPengembalian": ("formTransaksiKembali (M05 v0.1)", "Aliran data", "Petugas Perpustakaan -> 3.2 Memproses Pengembalian Buku",
   "Eksemplar yang dikembalikan anggota (EV-04).",
   "Harian pada jam layanan.", "Estimasi 100-200 per hari kerja (M05 v0.1).",
   "TanggalKembali diisi sistem. Eksemplar harus memiliki transaksi aktif (EV-04 error 1)."),
 "statusTransaksiDanBukti": ("Status Transaksi (CD)", "Aliran data", "3.1 / 3.2 -> Petugas Perpustakaan",
   "Hasil transaksi peminjaman/pengembalian: bukti per eksemplar bila berhasil, atau alasan penolakan.",
   "Setiap dataTransaksiPeminjaman / dataTransaksiPengembalian diproses.", "Sama dengan volume dataTransaksiFisik.",
   "Untuk pengembalian, TanggalKembali terisi pada BuktiTransaksi. Penolakan peminjaman: AnggotaNonaktif, MemilikiDendaBelumLunas, KuotaPinjamPenuh, EksemplarTidakTersedia."),
 "catatanDenda": ("Konfirmasi Denda (CD); buktiKonfirmasiDenda (M05 v0.1)", "Aliran data", "Petugas Perpustakaan -> 3.3 Menghitung dan Mencatat Denda",
   "Catatan pembayaran denda yang diterima petugas dari anggota.",
   "Setiap anggota membayar denda di meja layanan.", "Estimasi 15-30 per hari (M05 v0.1).",
   "JumlahDibayar harus sama dengan JumlahDenda (tidak dicicil, M05 v0.1). Setelah dicatat StatusDenda = Lunas."),
 "dataKeterlambatan": ("-", "Aliran data internal", "3.2 Memproses Pengembalian Buku -> 3.3 Menghitung dan Mencatat Denda",
   "Data pengembalian yang melewati jatuh tempo untuk dihitung dendanya.",
   "Hanya saat TanggalKembali > TanggalJatuhTempo.", "Estimasi 15-30 per hari.",
   "JumlahHariTerlambat = TanggalKembali - TanggalJatuhTempo (hari kalender), selalu >= 1."),
 "buktiPengembalianDanDenda": ("Bukti Pengembalian dan Denda (CD)", "Aliran data", "3.3 -> Petugas Perpustakaan",
   "Rincian keterlambatan dan denda atas pengembalian, termasuk status pembayarannya.",
   "Setiap ada keterlambatan atau pembayaran denda.", "Estimasi 15-30 per hari.",
   "JumlahDenda = JumlahHariTerlambat x TarifDendaHarian (Rp1.000 per hari per eksemplar, M05 v0.1)."),
 "permintaanPerpanjangan": ("Permintaan Perpanjangan (CD)", "Aliran data", "Anggota Perpustakaan -> 3.4 Memperpanjang Peminjaman",
   "Permohonan anggota untuk memperpanjang masa pinjam satu transaksi (EV-05).",
   "Sebelum atau pada TanggalJatuhTempo.", "Estimasi 30-50 per hari (M05 v0.1).",
   "NomorIdentitas harus pemilik IDTransaksi. Ditolak jika lewat jatuh tempo, ada denda belum lunas, atau batas perpanjangan tercapai (lihat TBD-01)."),
 "statusPerpanjangan": ("Status Perpanjangan (CD)", "Aliran data", "3.4 -> Anggota Perpustakaan",
   "Hasil permohonan perpanjangan: jatuh tempo baru bila berhasil, atau alasan penolakan.",
   "Setiap permintaanPerpanjangan diproses.", "Sama dengan permintaanPerpanjangan.",
   "TanggalJatuhTempo baru = TanggalJatuhTempo lama + LamaPinjam (7 hari, lihat TBD-02)."),
 "statusAnggota": ("-", "Aliran data (baca store)", "D1 Data Anggota -> 3.1, 3.4",
   "Status keanggotaan untuk memvalidasi hak meminjam/memperpanjang.",
   "Setiap transaksi peminjaman/perpanjangan.", "Mengikuti volume 3.1 dan 3.4.", "Hanya StatusAnggota = Aktif yang boleh bertransaksi."),
 "dataEksemplar": ("-", "Aliran data (baca store)", "D2 Data Koleksi -> 3.1",
   "Status eksemplar yang akan dipinjam.", "Setiap peminjaman.", "Mengikuti volume 3.1.",
   "Eksemplar hanya dapat dipinjam jika StatusEksemplar = Tersedia."),
 "pembaruanEksemplar": ("-", "Aliran data (tulis store)", "3.1, 3.2 -> D2 Data Koleksi",
   "Perubahan status eksemplar karena dipinjam atau dikembalikan.", "Setiap peminjaman/pengembalian berhasil.", "Mengikuti volume 3.1 + 3.2.",
   "3.1 menulis Dipinjam; 3.2 menulis Tersedia."),
 "dataKoleksi": ("-", "Aliran data (baca store)", "D2 Data Koleksi -> Proses 4",
   "Seluruh rekaman eksemplar untuk ringkasan koleksi pada laporan.", "Bulanan.", "1 kali per laporan.", "-"),
 "peminjamAktif": ("-", "Aliran data (baca store)", "D3 Transaksi Fisik -> 3.2, 3.4",
   "Transaksi yang masih berjalan (Aktif/Terlambat) atau dendanya belum lunas.",
   "Setiap pengembalian dan perpanjangan.", "Mengikuti volume 3.2 + 3.4.",
   "Disaring berdasarkan KodeEksemplar (3.2) atau IDTransaksi/NomorIdentitas (3.4). Lihat AUD-B-07: 3.1 juga membutuhkan flow ini."),
 "dataPeminjaman": ("-", "Aliran data (tulis store, gabungan)", "Proses 3 -> D3 Transaksi Fisik",
   "Semua penulisan Proses 3 ke D3 pada Level 0.", "Setiap transaksi sirkulasi.", "Gabungan volume 3.1-3.4.",
   "Pada Level 1 dipecah per aksi; pemecahan sah karena strukturnya [pilihan] didefinisikan di sini (PR-08, AI-10)."),
 "dataPeminjamanBaru": ("-", "Aliran data (tulis store)", "3.1 -> D3 Transaksi Fisik",
   "Rekaman transaksi peminjaman baru per eksemplar.", "Setiap peminjaman berhasil.", "Estimasi 100-200 per hari.",
   "TanggalJatuhTempo = TanggalPinjam + 7 hari; JumlahPerpanjangan = 0; StatusTransaksi = Aktif; StatusDenda = TanpaDenda."),
 "pembaruanPengembalian": ("-", "Aliran data (tulis store)", "3.2 -> D3 Transaksi Fisik",
   "Penutupan transaksi saat buku dikembalikan.", "Setiap pengembalian berhasil.", "Estimasi 100-200 per hari.",
   "StatusTransaksi menjadi Selesai."),
 "dataDenda": ("-", "Aliran data (tulis store)", "3.3 -> D3 Transaksi Fisik",
   "Pencatatan nilai denda dan pelunasannya.", "Setiap keterlambatan atau pembayaran denda.", "Estimasi 15-30 per hari.",
   "StatusDenda = BelumLunas saat dihitung; Lunas setelah catatanDenda diterima."),
 "pembaruanMasaPinjam": ("-", "Aliran data (tulis store)", "3.4 -> D3 Transaksi Fisik",
   "Jatuh tempo baru dan penambahan hitungan perpanjangan.", "Setiap perpanjangan berhasil.", "Estimasi 30-50 per hari.",
   "JumlahPerpanjangan bertambah 1 dan tidak boleh melebihi BatasPerpanjangan (TBD-01)."),
 "dataTransaksi": ("-", "Aliran data (baca store)", "D3 Transaksi Fisik -> Proses 4",
   "Transaksi dalam PeriodeLaporan untuk direkap.", "Bulanan.", "Estimasi ~3.000-6.000 rekaman per bulan.", "Hanya rekaman dengan TanggalPinjam/TanggalKembali/TanggalBayar di dalam PeriodeLaporan."),
 "permintaanLaporan": ("Permintaan Laporan (CD)", "Aliran data", "Kepala Perpustakaan -> Proses 4",
   "Periode laporan yang diminta Kepala Perpustakaan (EV-06).", "Sesuai kebutuhan, umumnya bulanan.", "1-2 per bulan.",
   "PeriodeLaporan tidak boleh di masa depan. Untuk EV-07 (temporal) periode diisi otomatis bulan berjalan (lihat AUD-A-05)."),
 "laporanBulanan": ("Laporan Bulanan Sirkulasi & Denda (CD); laporanSirkulasiBulanan (M05 v0.1)", "Aliran data (dokumen)", "Proses 4 -> Kepala Perpustakaan",
   "Rekap sirkulasi, denda, dan kondisi koleksi selama satu bulan.", "Bulanan (hari kerja terakhir, EV-07) atau saat diminta (EV-06).", "1 laporan per permintaan.",
   "Mencakup seluruh transaksi tanggal 1 sampai akhir bulan PeriodeLaporan."),
}

STORE = {
 # deskripsi, record, kunci, retensi, sumber (penulis), akses (pembaca)
 "D1 Data Anggota": ("Data anggota perpustakaan yang lolos verifikasi Sistem Akademik.", "RecordAnggota", "@NomorIdentitas",
   "TBD-05", "Proses 1 (dataAnggota)", "Proses 3: 3.1, 3.4 (statusAnggota)"),
 "D2 Data Koleksi": ("Data eksemplar buku fisik beserta data bukunya dan status ketersediaan.", "RecordEksemplar", "@KodeEksemplar",
   "Selama eksemplar tercatat sebagai koleksi; penghapusan lewat 2.2", "2.2 (dataKoleksiBuku), 3.1 & 3.2 (pembaruanEksemplar)",
   "2.1 (dataKoleksiBuku), 3.1 (dataEksemplar), 4 (dataKoleksi)"),
 "D3 Transaksi Fisik": ("Riwayat transaksi peminjaman per eksemplar, termasuk pengembalian, perpanjangan, dan denda.", "RecordTransaksi", "@IDTransaksi",
   "TBD-05", "3.1 (dataPeminjamanBaru), 3.2 (pembaruanPengembalian), 3.3 (dataDenda), 3.4 (pembaruanMasaPinjam)",
   "3.2, 3.4 (peminjamAktif), 4 (dataTransaksi)"),
}
STORE_VOL = {
 "D1 Data Anggota": ("Bertambah saat pendaftaran berhasil.", "Estimasi ribuan anggota (sesuai jumlah civitas aktif)."),
 "D2 Data Koleksi": ("Bertambah/berubah saat pengadaan & sirkulasi.", "Estimasi ribuan eksemplar."),
 "D3 Transaksi Fisik": ("Bertambah setiap peminjaman.", "Estimasi ~3.000 rekaman baru per bulan."),
}

# ---------------------------------------------------------------------------
# 4. ELEMEN (atribut Modul 5 §1.7 + §3.4)
#    definisi, tipe, format/panjang, domain/aturan, null, sumber, valid, tidak valid
# ---------------------------------------------------------------------------
ELEMEN = {
 "NomorIdentitas": ("Nomor induk civitas akademika yang menjadi identitas anggota; NIM untuk mahasiswa, NIP untuk dosen.", "Teks numerik", "[NIM | NIP]; 9 atau 18 digit",
   "Unik di D1. Panjang 9 bila KategoriAnggota = Mahasiswa, 18 bila Dosen.", "Wajib", "Diinput aktor, diverifikasi Sistem Akademik", "251511062", "25151106A (ada huruf)"),
 "NIM": ("Nomor Induk Mahasiswa Polban.", "Teks numerik", "9{angka}9", "Tepat 9 digit angka.", "Wajib bila Mahasiswa", "Diinput aktor", "251511062", "2515110 (7 digit)"),
 "NIP": ("Nomor Induk Pegawai untuk dosen.", "Teks numerik", "18{angka}18", "Tepat 18 digit angka.", "Wajib bila Dosen", "Diinput aktor", "198001012005011001", "19800101 (8 digit)"),
 "KategoriAnggota": ("Golongan civitas akademika pendaftar.", "Enumerasi", "Teks, maks 9", "[Mahasiswa | Dosen]", "Wajib", "Diinput aktor", "Mahasiswa", "Alumni"),
 "NamaLengkap": ("Nama lengkap anggota sesuai data akademik.", "Teks", "1{huruf|spasi|.|'}100", "Hanya huruf, spasi, titik, apostrof. Disimpan utuh (tidak dipecah depan/belakang karena hanya ditampilkan).", "Wajib", "Diinput aktor", "Wildan M. Zaki", "W1ldan_Z (angka & simbol)"),
 "ProgramStudi": ("Program studi (mahasiswa) atau homebase prodi (dosen).", "Teks", "3{huruf|spasi|-}60", "Nama prodi resmi.", "Wajib", "Diinput aktor", "D3 Teknik Informatika", "TI (terlalu pendek)"),
 "EmailKampus": ("Alamat email resmi kampus anggota.", "Teks format email", "NamaPengguna + @ + DomainKampus; maks 80", "Domain wajib polban.ac.id atau subdomainnya.", "Wajib", "Diinput aktor", "wildan.zaki.tif25@polban.ac.id", "wildan@gmail.com (bukan domain kampus)"),
 "NamaPengguna": ("Bagian email sebelum @.", "Teks", "1{hurufKecil|angka|.|_}40", "Huruf kecil, angka, titik, garis bawah.", "Wajib", "Diinput aktor", "wildan.zaki.tif25", "Wildan Zaki (spasi & kapital)"),
 "DomainKampus": ("Bagian email setelah @.", "Teks", "polban.ac.id atau Subdomain.polban.ac.id", "Harus berakhiran polban.ac.id.", "Wajib", "Diinput aktor", "polban.ac.id", "polban.com"),
 "Subdomain": ("Subdomain unit kampus pada email.", "Teks", "2{hurufKecil}10", "Huruf kecil saja.", "Opsional", "Diinput aktor", "jtk", "j (1 huruf)"),
 "TanggalDaftar": ("Tanggal anggota resmi terdaftar.", "Tanggal", "YYYY-MM-DD (10)", "Tanggal kalender valid, tidak di masa depan.", "Wajib", "Dihitung sistem (tanggal proses)", "2026-10-21", "21/10/2026"),
 "TanggalPinjam": ("Tanggal eksemplar diserahkan kepada peminjam.", "Tanggal", "YYYY-MM-DD (10)", "Tanggal kalender valid = tanggal transaksi.", "Wajib", "Dihitung sistem", "2026-10-19", "2026-13-01 (bulan 13)"),
 "TanggalJatuhTempo": ("Tanggal terakhir pengembalian tanpa denda.", "Tanggal", "YYYY-MM-DD (10)", "= TanggalPinjam + 7 hari; setelah perpanjangan = jatuh tempo lama + 7 hari. Tidak boleh < TanggalPinjam.", "Wajib", "Dihitung sistem", "2026-10-26", "2026-10-18 (sebelum TanggalPinjam)"),
 "TanggalKembali": ("Tanggal eksemplar diterima kembali.", "Tanggal", "YYYY-MM-DD (10)", ">= TanggalPinjam.", "Kosong selama dipinjam; wajib saat Selesai", "Dihitung sistem", "2026-10-28", "2026-10-10 (sebelum TanggalPinjam)"),
 "TanggalBayar": ("Tanggal denda dilunasi.", "Tanggal", "YYYY-MM-DD (10)", ">= TanggalKembali.", "Kosong bila belum/ tidak ada denda", "Diinput aktor (petugas) / tanggal sistem", "2026-10-28", "2026-10-01 (sebelum kembali)"),
 "TanggalLaporan": ("Tanggal laporan dibuat.", "Tanggal", "YYYY-MM-DD (10)", "Tanggal kalender valid.", "Wajib", "Dihitung sistem", "2026-10-30", "30-10-2026"),
 "StatusAnggota": ("Hak layanan anggota.", "Enumerasi", "Teks, maks 8", "[Aktif | Nonaktif]", "Wajib", "Disimpan di D1 (awal Aktif)", "Aktif", "Diblokir (bukan domain)"),
 "StatusAkademik": ("Status civitas menurut Sistem Akademik.", "Enumerasi", "Teks, maks 14", "[Aktif | TidakAktif | Cuti | TidakTerdaftar]", "Wajib", "Dari Sistem Akademik", "Cuti", "Lulus (bukan domain)"),
 "StatusProses": ("Hasil umum pemrosesan permintaan.", "Enumerasi", "Teks, maks 8", "[Berhasil | Ditolak]", "Wajib", "Dihitung sistem", "Ditolak", "Pending"),
 "AlasanPenolakan": ("Sebab permintaan ditolak (diturunkan dari error condition event table).", "Enumerasi", "Teks, maks 30", "Lihat struktur (11 nilai).", "Wajib bila Ditolak", "Dihitung sistem", "KuotaPinjamPenuh", "Error"),
 "KataKunci": ("Teks yang dicari anggota.", "Teks", "1{karakter}100", "Tidak boleh kosong/spasi saja.", "Wajib", "Diinput aktor", "basis data", '"" (kosong)'),
 "JenisPencarian": ("Atribut buku yang dicocokkan dengan KataKunci.", "Enumerasi", "Teks, maks 9", "[Judul | Pengarang | ISBN | Subjek]", "Wajib (default Judul)", "Dipilih aktor", "Pengarang", "Penerbit"),
 "KodeEksemplar": ("Kode barcode unik setiap eksemplar fisik.", "Teks", '"SIL-BK-" + 4{angka}4 (11)', "Unik di D2.", "Wajib", "Diinput aktor (pindai barcode) / dibaca D2", "SIL-BK-0012", "SIL-0012 (prefix salah)"),
 "ISBN": ("Nomor buku standar internasional (ISBN-13).", "Teks numerik", "13{angka}13", "13 digit.", "Wajib", "Diinput aktor", "9786020332956", "978602033 (9 digit)"),
 "JudulBuku": ("Judul resmi buku.", "Teks", "1{karakter}200", "Tidak kosong (lihat TBD-04 untuk batas panjang).", "Wajib", "Diinput aktor / dibaca D2", "Rekayasa Perangkat Lunak", '"" (kosong)'),
 "Pengarang": ("Nama penulis buku; satu buku 1-3 pengarang.", "Teks", "1{karakter}100", "Tidak kosong.", "Wajib (min 1)", "Diinput aktor", "Roger S. Pressman", '"" (kosong)'),
 "Penerbit": ("Nama penerbit buku.", "Teks", "1{karakter}100", "Tidak kosong.", "Wajib", "Diinput aktor", "Andi Offset", '"" (kosong)'),
 "TahunTerbit": ("Tahun buku diterbitkan.", "Bilangan", "4{angka}4", "1900 <= TahunTerbit <= tahun berjalan.", "Wajib", "Diinput aktor", "2020", "2099 (masa depan)"),
 "Subjek": ("Topik utama buku untuk pencarian.", "Teks", "1{karakter}50", "Tidak kosong.", "Wajib", "Diinput aktor", "Rekayasa Perangkat Lunak", '"" (kosong)'),
 "LokasiRak": ("Posisi rak penyimpanan eksemplar.", "Teks", '"R" + 2{angka}2 + "-" + 1{hurufKapital}1 (5)', "Rak 01-99, baris A-Z.", "Wajib", "Diinput aktor", "R03-B", "Rak 3 B"),
 "StatusEksemplar": ("Ketersediaan/kondisi eksemplar.", "Enumerasi", "Teks, maks 8", "[Tersedia | Dipinjam | Rusak | Hilang]", "Wajib", "Diinput aktor (2.2) / diubah sistem (3.1, 3.2)", "Tersedia", "Pinjam (singkatan)"),
 "JumlahTersedia": ("Banyak eksemplar berstatus Tersedia untuk satu judul.", "Bilangan bulat", "1{angka}3", ">= 0.", "Wajib", "Dihitung sistem", "2", "-1"),
 "JenisPerubahan": ("Jenis pengelolaan koleksi yang dilakukan petugas.", "Enumerasi", "Teks, maks 6", "[Tambah | Ubah | Hapus]", "Wajib", "Dipilih aktor", "Tambah", "Edit"),
 "IDTransaksi": ("Nomor unik satu transaksi peminjaman satu eksemplar.", "Teks", '"TRX-" + YYYYMMDD + "-" + 3{angka}3 (16)', "Unik di D3; tanggal = TanggalPinjam; nomor urut 001-999 per hari.", "Wajib", "Dihitung sistem", "TRX-20261019-001", "TRX123"),
 "JumlahPerpanjangan": ("Berapa kali transaksi sudah diperpanjang.", "Bilangan bulat", "1{angka}1", "0 <= nilai <= BatasPerpanjangan (TBD-01).", "Wajib (awal 0)", "Dihitung sistem", "1", "-1"),
 "JumlahHariTerlambat": ("Selisih hari kalender TanggalKembali dengan TanggalJatuhTempo.", "Bilangan bulat", "1{angka}3", ">= 1 bila terlambat.", "Kosong bila tidak terlambat", "Dihitung sistem", "3", "0 pada dataKeterlambatan"),
 "JumlahDenda": ("Nilai denda keterlambatan dalam rupiah.", "Bilangan bulat (Rp)", "1{angka}7", "= JumlahHariTerlambat x 1.000; kelipatan 1.000.", "Kosong bila tidak ada denda", "Dihitung sistem", "3000", "2500 (bukan kelipatan 1.000)"),
 "JumlahDibayar": ("Nominal pembayaran denda yang diterima petugas.", "Bilangan bulat (Rp)", "1{angka}7", "Harus = JumlahDenda (tidak dicicil).", "Kosong bila belum dibayar", "Diinput aktor (petugas)", "3000", "1000 (kurang dari denda)"),
 "StatusTransaksi": ("Tahap transaksi peminjaman.", "Enumerasi", "Teks, maks 9", "[Aktif | Terlambat | Selesai]", "Wajib", "Dihitung sistem", "Selesai", "Pending"),
 "StatusDenda": ("Status kewajiban denda transaksi.", "Enumerasi", "Teks, maks 10", "[TanpaDenda | BelumLunas | Lunas]", "Wajib (awal TanpaDenda)", "Dihitung sistem", "Lunas", "Hutang"),
 "PeriodeLaporan": ("Bulan yang direkap.", "Teks", "YYYY-MM (7)", "Bulan valid, tidak di masa depan.", "Wajib", "Diinput aktor / dihitung sistem (EV-07)", "2026-10", "Oktober"),
 "Tahun": ("Komponen tahun pada tanggal.", "Teks numerik", "4{angka}4", "2000-2100 untuk tanggal transaksi.", "Wajib", "-", "2026", "26"),
 "Bulan": ("Komponen bulan pada tanggal.", "Teks numerik", "2{angka}2", "01-12.", "Wajib", "-", "09", "13"),
 "Hari": ("Komponen hari pada tanggal.", "Teks numerik", "2{angka}2", "01-31, sesuai jumlah hari bulan.", "Wajib", "-", "28", "32"),
}
for t, ket in [("TotalPeminjaman", "transaksi peminjaman"), ("TotalPengembalian", "pengembalian"), ("TotalPerpanjangan", "perpanjangan"),
               ("TotalKeterlambatan", "pengembalian terlambat"), ("TotalEksemplar", "eksemplar tercatat"), ("TotalTersedia", "eksemplar Tersedia"),
               ("TotalDipinjam", "eksemplar Dipinjam"), ("TotalRusakHilang", "eksemplar Rusak atau Hilang")]:
    ELEMEN[t] = (f"Jumlah {ket} pada periode laporan.", "Bilangan bulat", "1{angka}6", ">= 0.", "Wajib", "Dihitung sistem", "145", "-10")
for t, ket in [("TotalDendaTercatat", "denda yang timbul"), ("TotalDendaLunas", "denda yang dilunasi"), ("TotalDendaBelumLunas", "denda belum lunas")]:
    ELEMEN[t] = (f"Jumlah rupiah {ket} pada periode laporan.", "Bilangan bulat (Rp)", "1{angka}9", ">= 0; kelipatan 1.000.", "Wajib", "Dihitung sistem", "45000", "-5000")

# ---------------------------------------------------------------------------
# 5. ALIAS, TBD, PARAMETER
# ---------------------------------------------------------------------------
ALIAS = [
 ("NomorIdentitas", "NIM, NIP, ID Anggota, ID Anggota Digital (EV-01)", "Satu identitas anggota; NIM/NIP adalah bentuknya (struktur [NIM | NIP])."),
 ("KodeEksemplar", "Kode Buku, Kode Eksemplar Buku, Barcode Buku", "Membedakan eksemplar fisik dari judul (ISBN)."),
 ("catatanDenda", "Konfirmasi Denda (CD, M02-M03); buktiKonfirmasiDenda (M05 v0.1)", "Nama baku mengikuti DFD hasil revisi M04. CD perlu direvisi (AUD-B-01)."),
 ("informasiKoleksiBuku", "Informasi Katalog (CD); Info Katalog/Ketersediaan; infoKatalogKoleksi", "PR-03."),
 ("laporanBulanan", "Laporan Bulanan Sirkulasi & Denda (CD); laporanSirkulasiBulanan (M05 v0.1)", "Nama baku = DFD."),
 ("statusKeaktifan", "Status Keaktifan Mahasiswa (CD); statusKeaktifanMahasiswa (M05 v0.1)", "Nama baku = DFD."),
 ("dataVerifikasi", "Data Verifikasi Mahasiswa (CD)", "Nama baku = DFD."),
 ("dataKoleksiBaru", "Data Koleksi Buku (CD)", "Nama baku = DFD."),
 ("statusTransaksiDanBukti", "Status Transaksi (CD); Status transaksi (L1 lama)", "AI-02."),
 ("dataTransaksiPeminjaman", "formTransaksiPinjam (M05 v0.1)", "Nama baku = DFD L1-P3."),
 ("dataTransaksiPengembalian", "formTransaksiKembali (M05 v0.1)", "Nama baku = DFD L1-P3."),
 ("D3 Transaksi Fisik", "dataTransaksiSirkulasi (M05 v0.1); Transaksi Peminjaman (M03)", "Nama baku = DFD."),
 ("JumlahDenda", "Nilai Denda, Denda", "Sesuai contoh Modul 5 §1.8 (NilaiDenda untuk data)."),
]

TBD = [
 ("TBD-01", "BatasPerpanjangan", "EV-05 menyebut 'misal max 2 kali', M05 v0.1 menulis 3 kali, catatan optimasi menyebut 3. Belum ada keputusan.", "Wildan", "Sebelum M06 (process spec 3.4)"),
 ("TBD-02", "Lama perpanjangan", "Apakah perpanjangan menambah 7 hari dari jatuh tempo lama atau dari tanggal pengajuan?", "Sahizidan", "Sebelum M06"),
 ("TBD-03", "Cakupan dosen", "EV-01 menyebut mahasiswa atau dosen; M05 v0.1 hanya NIM. Struktur [NIM | NIP] dipakai sementara.", "Wildan", "Sebelum M06"),
 ("TBD-04", "Panjang JudulBuku", "200 karakter atau tanpa batas (TBD lama M05 v0.1).", "Sahizidan", "Sebelum M06"),
 ("TBD-05", "Retensi D1 & D3", "Berapa lama data anggota nonaktif dan riwayat transaksi disimpan.", "Irfan", "Sebelum M06"),
 ("TBD-06", "Nomor bukti denda", "Apakah bukti pembayaran denda punya nomor sendiri atau memakai IDTransaksi (TBD lama M05 v0.1).", "Irfan", "Sebelum M06"),
 ("TBD-07", "Sumber aturan 7 hari & Rp1.000/hari", "Dipakai sejak M05 v0.1 sebagai kesepakatan kelompok; belum dirujuk ke event table/charter.", "Rere", "Sebelum M06"),
]

PARAMETER = [
 ("LamaPinjam", "7 hari kalender", "Kesepakatan kelompok M05 v0.1 (TBD-07)"),
 ("TarifDendaHarian", "Rp1.000 per hari per eksemplar", "Kesepakatan kelompok M05 v0.1 (TBD-07)"),
 ("MaksEksemplarDipinjam", "3 eksemplar per anggota", "M05 v0.1 aturan formTransaksiPinjam; EV-03 error 3 (kuota)"),
 ("BatasPerpanjangan", "TBD", "TBD-01"),
]

# urutan entri komposit di dokumen
URUT_FLOW = [r[0] for r in INVENTARIS if r[1] == "Flow"]
URUT_STORE = [r[0] for r in INVENTARIS if r[1] == "Store"]
