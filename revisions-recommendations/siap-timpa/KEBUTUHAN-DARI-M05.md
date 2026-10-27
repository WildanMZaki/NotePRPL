# Rekomendasi Perubahan M05 (Blocker M04 & M06)

> **Status 2026-10-27: #1–#26 sudah diterapkan di `updates/` M05** (lihat `M05-data-dictionary.md`). File ini disimpan sebagai rujukan alasan.

Bukan versi siap-timpa M05; M05 masih diedit kelompok. Isinya hanya perubahan yang **dibutuhkan M04 (matriks balancing) dan M06 (process spec)** supaya keduanya terlacak ke kamus data.

Dicek terhadap: `updates/PRPL_M05_2B_RajinBelajar_DataDictionary.pdf` (2026-10-26 22:28).
Status: ✅ sudah ada di M05 · ⏳ belum · ⚠️ ada tapi bentrok

Catatan yang sama, dikelompokkan per proses, ada di [`../../m06/PROCESS_SPEC_M06.md`](../../m06/PROCESS_SPEC_M06.md) (kotak "Catatan penyesuaian M05").

## A. Sudah dikerjakan kelompok

| Item | Status |
|---|---|
| Store D1, D2, D3 masuk inventaris (Jenis = Data Store) | ✅ |
| Flow store (dataAnggota, peminjamAktif, dll.) berjenis Flow | ✅ |
| `dataKoleksiBuku` di 2.2 dua arah (arus D2 → 2.1 dan 2.2) | ✅ |
| Entri store D1, D2, D3 dengan struktur record | ✅ |

## B. Masih memblokir (prioritas)

| # | Entri | Sekarang | Seharusnya | Dibutuhkan oleh | Status |
|---|---|---|---|---|---|
| 1 | Nama store D3 | `D3 Data Transaksi` | `D3 Transaksi Fisik` (sama dengan DFD) | semua | ⚠️ |
| 2 | `catatanDenda` | Proses 3.3 → Petugas; `NoIdentitas + KodeBuku + JumlahHariTerlambat + TarifDenda + TotalDenda + StatusDenda` | Petugas → 3.3; `IDTransaksi + JumlahDibayar + TanggalBayar` | 3.3 | ⏳ |
| 3 | `infoKatalog/Ketersediaan` | masih ada (inventaris no 7, entri, penguraian) | hapus; isinya digabung ke `informasiKoleksiBuku` | 2.1, M04 balancing | ⏳ |
| 4 | `dataTransaksiFisik` | `NoIdentitas + KodeBuku + JenisTransaksi + TanggalTransaksi + IDPetugas` | `[dataTransaksiPeminjaman \| dataTransaksiPengembalian]` | M04 matriks P3 baris 4 | ⏳ |
| 5 | `dataPeminjaman` | record tunggal (`IDTransaksi + ... + StatusTransaksi`) | `[dataPeminjamanBaru \| pembaruanPengembalian \| dataDenda \| pembaruanMasaPinjam]` | M04 matriks P3 baris 10 | ⏳ |
| 6 | Entri baru `dataPeminjamanBaru` | - | `IDTransaksi + NoIdentitas + KodeEksemplar + TanggalPinjam + TanggalJatuhTempo + StatusTransaksi + StatusDenda + JumlahPerpanjangan` (3.1 → D3) | 3.1 | ⏳ |
| 7 | Entri baru `pembaruanPengembalian` | - | `IDTransaksi + TanggalKembali + StatusTransaksi` (3.2 → D3) | 3.2 | ⏳ |
| 8 | Entri baru `dataDenda` | - | `IDTransaksi + JumlahHariTerlambat + TotalDenda + StatusDenda + (TanggalBayar)` (3.3 → D3) | 3.3 | ⏳ |
| 9 | Entri baru `pembaruanMasaPinjam` | - | `IDTransaksi + TanggalJatuhTempo + JumlahPerpanjangan` (3.4 → D3) | 3.4 | ⏳ |
| 10 | Entri baru `statusPengelolaanKoleksi` | - | `StatusHasil + KodeBuku + (KeteranganGagal)` (Proses 2 / 2.2 → Petugas; juga CD) | 2.2 | ⏳ |
| 11 | `dataTransaksiPeminjaman` | `NoIdentitas + KodeBuku + TanggalPinjam + TanggalJatuhTempo + IDPetugas` | `NoIdentitas + 1{KodeEksemplar}3` | 3.1 | ⏳ |
| 12 | `dataTransaksiPengembalian` | `NoIdentitas + KodeBuku + TanggalKembali + KondisiBuku + IDPetugas` | `1{KodeEksemplar + KondisiBuku}3` | 3.2 | ⏳ |
| 13 | `permintaanPerpanjangan` | `NoIdentitas + KodeBuku + TanggalPengajuan` | `NoIdentitas + IDTransaksi` | 3.4 | ⏳ |
| 14 | `peminjamAktif` | tujuan 3.2, 3.4; `NoIdentitas + {IDTransaksi + KodeEksemplar + TanggalJatuhTempo}` | tujuan 3.1, 3.2, 3.3, 3.4; `NoIdentitas + {IDTransaksi + KodeEksemplar + TanggalJatuhTempo + StatusTransaksi + StatusDenda + TotalDenda + JumlahPerpanjangan}` | 3.1, 3.3, 3.4 | ⏳ |
| 15 | Record D3 | `IDTransaksi + NoIdentitas + KodeEksemplar + TanggalPinjam + TanggalJatuhTempo + TanggalKembali + TotalDenda + StatusTransaksi` | + `StatusDenda + JumlahPerpanjangan + (TanggalBayar)`; `@IDTransaksi` | 3.1, 3.3, 3.4 | ⏳ |
| 16 | `dataAnggota` (arus D1) | Proses 1 → D1 saja | dua arah (D1 ↔ Proses 1) | 1 | ⏳ |

## C. Definisi yang belum ada atau bentrok

| # | Elemen / entri | Masalah | Usulan | Dibutuhkan oleh |
|---|---|---|---|---|
| 17 | `statusPendaftaran`, `statusPerpanjangan`, `statusAnggota`, `dataPencarian`, `permintaanLaporan` | Ditandai Elementer, tapi tidak punya entri maupun definisi elemen | `statusPendaftaran = StatusHasil + NoIdentitas + (TanggalDaftar) + (KeteranganGagal)`; `statusPerpanjangan = StatusHasil + IDTransaksi + (TanggalJatuhTempo) + (KeteranganGagal)`; `statusAnggota = NoIdentitas + StatusKeaktifan`; `dataPencarian = KataKunci`; `permintaanLaporan = Periode` | 1, 2.1, 3.1, 3.4, 4 |
| 18 | `StatusTransaksi` | Homonim: `[Berhasil \| Gagal]` di statusTransaksiDanBukti vs `[Aktif \| Selesai \| Terlambat]` di D3 | Hasil proses pakai `StatusHasil = [Berhasil \| Gagal]` | semua output status |
| 19 | `StatusDenda` | `[Belum Dibayar \| Lunas]` vs `[Tanpa Denda \| Belum Lunas \| Lunas]`; `StatusPembayaran` di bukti | Satu domain `[Tanpa Denda \| Belum Lunas \| Lunas]` | 3.1, 3.3, 3.4 |
| 20 | `StatusEksemplar` | `[Tersedia \| Dipinjam \| Rusak]`, `[... \| Hilang/Rusak]` | `[Tersedia \| Dipinjam \| Rusak \| Hilang]` | 3.1, 3.2 |
| 21 | `KodeEksemplar` | Penguraian `KodeBuku + "-" + 1{angka}3`, tabel elemen `SIL-BK-0012` | Pilih satu, samakan contoh | semua |
| 22 | `StatusKeaktifan` / `statusKeaktifan` | Beda kapitalisasi; tabel elemen masih `StatusAnggota [Aktif \| Bebas Denda \| Diblokir]` | `StatusKeaktifan = [Aktif \| Nonaktif]`; respons Sistem Akademik + `Tidak Terdaftar` | 1, 3.1, 3.4 |
| 23 | Elemen baru | Belum ada | `JumlahPerpanjangan = 1{angka}1`; `JumlahDibayar = 1{angka}8`; `TanggalBayar = Tahun-Bulan-Hari`; `KeteranganGagal = 1{karakter}100`; `JenisPerubahan = [Tambah \| Ubah \| Hapus]`; `KataKunci = 1{karakter}100` | 2.1, 2.2, 3.3, 3.4 |
| 24 | `dataKoleksiBaru` | Tidak ada jenis perubahan | + `JenisPerubahan` | 2.2 |
| 25 | `Jurusan`, `TipeAnggota` di D1 | Tidak dikirim `dataPendaftaran` | Tambahkan ke `dataPendaftaran`, atau hapus dari D1 | 1 |
| 26 | `IDPetugas` | Tidak dipakai proses mana pun, tidak tersimpan | Hapus dari flow | - |

## D. Parameter yang dipakai M06

LamaPinjam 7 hari · TarifDenda Rp1.000/hari · KuotaPinjam 3 · BatasPerpanjangan 2 (dari EV-05) · TambahanPerpanjangan 7 hari (asumsi, perlu dikonfirmasi).
