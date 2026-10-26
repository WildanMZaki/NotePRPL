# M05 — Kamus Data (Revisi per Bagian)

Sumber: `updates/PRPL_M05_2B_RajinBelajar_DataDictionary.pdf` (final, 2026-10-26 22:44, 53 halaman).
Dokumen terlalu panjang untuk ditulis ulang. File ini hanya menyebut **bagian yang harus diubah**: nomor baris inventaris, nomor entri komposit (No. di "Daftar Entry Komposit"), dan nomor penguraian (No. di "Menguraikan Struktur Data"). Penomoran entri dan penguraian di dokumen sama (1–24).

Prioritas: **P1** = memblokir balancing M04 atau M06 · **P2** = konsistensi · **P3** = kerapian.
Kolom "Kode" merujuk ke [`KEBUTUHAN-DARI-M05.md`](KEBUTUHAN-DARI-M05.md) (#1–#26).

---

## 1. Membuat Inventaris Data

| Baris | Kolom | Sekarang | Ganti jadi | P | Kode |
|---|---|---|---|---|---|
| 1 dataPendaftaran | Lokasi DFD, Tujuan | `CD, DFD 0, DFD 1.1` · `Proses 1.1 (Pendaftaran)` | `CD, DFD 0` · `Proses 1` | P2 | - |
| 7 infoKatalog/Ketersediaan | seluruh baris | ada (Status: Sinonim) | **hapus baris**; nomor setelahnya maju satu | P1 | #3 |
| 6 informasiKoleksiBuku | Lokasi DFD, Sumber | `CD, DFD 0` · `Proses 2` | `CD, DFD 0, DFD 2.1` · `Proses 2, Proses 2.1` | P1 | #3 |
| 13 catatanDenda | Lokasi, Sumber, Tujuan | `DFD 0, DFD 3.3` · Sumber `Proses 3, Proses 3.3` · Tujuan `Petugas Perpustakaan` | `CD, DFD 0, DFD 3.3` · Sumber `Petugas Perpustakaan` · Tujuan `Proses 3, Proses 3.3` | P1 | #2 |
| 20 dataAnggota | Sumber/Tujuan | `Proses 1` → `D1 Data Anggota` | dua arah: `Proses 1 ↔ D1 Data Anggota` | P1 | #16 |
| 26 peminjamAktif | Lokasi, Tujuan | `DFD 3.2, 3.4` · `Proses 3 (3.2, 3.4)` | `DFD 3.1–3.4` · `Proses 3 (3.1, 3.2, 3.3, 3.4)` | P1 | #14 |
| 25 dataPeminjaman | Lokasi | `DFD 0, DFD 3.1 sampai 3.4` | `DFD 0` (di Level 1 diganti 4 aliran baru di bawah) | P1 | #5 |
| 31 D3 Data Transaksi | Nama | `D3 Data Transaksi` | `D3 Transaksi Fisik` (sama dengan DFD) | P1 | #1 |
| 2, 4, 5, 16, 17, 24 | Jenis Struktur | Elementer | Komposit (atau tetap Elementer **dan** didefinisikan di tabel elemen) | P2 | #17 |
| baru | — | — | `statusPengelolaanKoleksi` · Flow · CD, DFD 0, DFD 2.2 · Proses 2, Proses 2.2 · Petugas Perpustakaan · Komposit · baku | P1 | #10 |
| baru | — | — | `dataPeminjamanBaru` · Flow · DFD 3.1 · Proses 3.1 · D3 Transaksi Fisik · Komposit · baku | P1 | #6 |
| baru | — | — | `pembaruanPengembalian` · Flow · DFD 3.2 · Proses 3.2 · D3 Transaksi Fisik · Komposit · baku | P1 | #7 |
| baru | — | — | `dataDenda` · Flow · DFD 3.3 · Proses 3.3 · D3 Transaksi Fisik · Komposit · baku | P1 | #8 |
| baru | — | — | `pembaruanMasaPinjam` · Flow · DFD 3.4 · Proses 3.4 · D3 Transaksi Fisik · Komposit · baku | P1 | #9 |

## 2. Daftar Entry Komposit

| Entri | Atribut | Sekarang | Ganti jadi | P | Kode |
|---|---|---|---|---|---|
| 1 dataPendaftaran | Arus Data | `Anggota Perpustakaan -> Proses 1.1` | `Anggota Perpustakaan -> Proses 1` | P2 | - |
| 1 dataPendaftaran | Struktur | tanpa Jurusan, TipeAnggota | `+ Jurusan + TipeAnggota` (keduanya ada di D1), atau hapus dari D1 | P2 | #25 |
| 3 informasiKoleksiBuku | Arus Data | `Proses 2 -> Anggota` | `Proses 2, Proses 2.1 -> Anggota Perpustakaan`; gabungkan JumlahTersedia & LokasiRak dari entri 4 | P1 | #3 |
| 4 infoKatalog/Ketersediaan | seluruh entri | ada | **hapus** (nomor entri setelahnya maju satu) | P1 | #3 |
| 5 dataKoleksiBaru | Struktur | tanpa jenis perubahan | `JenisPerubahan + KodeBuku + Judul + ...` | P2 | #24 |
| 6 dataTransaksiFisik | Struktur | `NoIdentitas + KodeBuku + JenisTransaksi + TanggalTransaksi + IDPetugas` | `dataTransaksiFisik = [dataTransaksiPeminjaman \| dataTransaksiPengembalian]` | P1 | #4 |
| 7 dataTransaksiPeminjaman | Struktur | `NoIdentitas + KodeBuku + TanggalPinjam + TanggalJatuhTempo + IDPetugas` | `NoIdentitas + 1{KodeEksemplar}3` | P1 | #11 |
| 8 dataTransaksiPengembalian | Struktur | `NoIdentitas + KodeBuku + TanggalKembali + KondisiBuku + IDPetugas` | `1{KodeEksemplar + KondisiBuku}3` | P1 | #12 |
| 9 statusTransaksiDanBukti | Struktur | `StatusTransaksi + NoBukti + ...` | `StatusHasil + NoBukti + NoIdentitas + KodeEksemplar + TanggalTransaksi + (TanggalJatuhTempo) + (KeteranganGagal)` | P2 | #18 |
| 10 catatanDenda | Arus, Penjelasan, Struktur, Aturan | Proses 3.3 → Petugas; rincian denda | Petugas → Proses 3, 3.3; "catatan pembayaran denda dari petugas"; `IDTransaksi + JumlahDibayar + TanggalBayar`; aturan: JumlahDibayar = TotalDenda | P1 | #2 |
| 11 buktiPengembalianDanDenda | Struktur | `... + (StatusPembayaran)` | `... + (StatusDenda) + (KeteranganGagal)` | P2 | #19 |
| 12 permintaanPerpanjangan | Struktur | `NoIdentitas + KodeBuku + TanggalPengajuan` | `NoIdentitas + IDTransaksi` | P1 | #13 |
| 12 permintaanPerpanjangan | Aturan 3 | "Dibatasi jumlah maksimal perpanjangan per buku" | "Maksimal 2 kali per transaksi" (EV-05) | P2 | - |
| 14 dataAnggota | Arus Data | "Menerima aliran data masuk dari Proses 1" | `Proses 1 <-> D1 Data Anggota` (baca: cek terdaftar; tulis: anggota baru) | P1 | #16 |
| 15 dataKoleksiBuku | Struktur | hanya data buku | `+ {KodeEksemplar + StatusEksemplar + LokasiRak}` (dipakai 2.1 untuk hitung ketersediaan) | P2 | - |
| 18 dataPeminjaman | Struktur | record tunggal | `dataPeminjaman = [dataPeminjamanBaru \| pembaruanPengembalian \| dataDenda \| pembaruanMasaPinjam]` | P1 | #5 |
| 19 peminjamAktif | Arus, Struktur | `-> Proses 3 (3.2, 3.4)`; `NoIdentitas + {IDTransaksi + KodeEksemplar + TanggalJatuhTempo}` | `-> Proses 3 (3.1, 3.2, 3.3, 3.4)`; `NoIdentitas + {IDTransaksi + KodeEksemplar + TanggalJatuhTempo + StatusTransaksi + StatusDenda + TotalDenda + JumlahPerpanjangan}` | P1 | #14 |
| 22 D1 Data Anggota | Arus Data | `Proses 1 -> D1` | `Proses 1 <-> D1` | P1 | #16 |
| 22 D1 Data Anggota | Struktur | `{NoIdentitas + ...}` tanpa `@` | `{@NoIdentitas + ...}` | P2 | - |
| 23 D2 Data Koleksi | Struktur | tanpa `@` | `{@KodeBuku + ...} + {@KodeEksemplar + KodeBuku + ...}` | P2 | - |
| 24 D3 Data Transaksi | Nama, Struktur, Arus | nama `D3 Data Transaksi`; tanpa `@`; arus ke 3.2, 3.4 | `D3 Transaksi Fisik`; `{@IDTransaksi + ... + StatusDenda + JumlahPerpanjangan + (TanggalBayar)}`; arus ke 3.1–3.4 | P1 | #1, #15 |
| baru | entri komposit | — | `dataKeterlambatan` (entrinya hilang, padahal ada di inventaris baris 19): `IDTransaksi + NoIdentitas + KodeEksemplar + TanggalJatuhTempo + TanggalKembali + JumlahHariTerlambat` | P1 | - |
| baru | entri komposit | — | `statusPengelolaanKoleksi`, `dataPeminjamanBaru`, `pembaruanPengembalian`, `dataDenda`, `pembaruanMasaPinjam` (struktur di KEBUTUHAN #6–#10) | P1 | #6–#10 |
| baru | entri komposit | — | `statusPendaftaran`, `statusPerpanjangan`, `statusAnggota`, `dataPencarian`, `permintaanLaporan`, `statusKeaktifan` (kalau jadi Komposit; struktur di KEBUTUHAN #17) | P2 | #17 |

## 3. Menguraikan Struktur Data

| No | Masalah | Perbaikan | P |
|---|---|---|---|
| 4 infoKatalog/Ketersediaan | dihapus bersama entrinya | hapus penguraian | P1 |
| 6, 7, 8, 12, 18, 19 | ikut struktur baru di bagian 2 | uraikan ulang sesuai struktur baru | P1 |
| 8, 10, 11 | `KodeBuku = 3{angka}3 + 3{angka}3]` (ada `]` nyasar) | hapus `]` | P3 |
| 8 | `angka = [0 \| … \| 9` (kurung tidak ditutup) | `angka = [0 \| … \| 9]` | P3 |
| 6, 7, 8 | `hari = 2{angka}2` huruf kecil, di tempat lain `Hari` | `Hari` | P3 |
| 16 | `pembaruan Eksemplar = KodeEksemplar + Status Eksemplar`; `Status Eksemplar = [ ... \| Hilang/Rusak ]` | `pembaruanEksemplar = KodeEksemplar + StatusEksemplar`; `StatusEksemplar = [Tersedia \| Dipinjam \| Rusak \| Hilang]` | P2 |
| 17 | `StatusEksemplar = [ Tersedia \| Dipinjam \| Rusak ]` | `[Tersedia \| Dipinjam \| Rusak \| Hilang]` (sama dengan 16 dan 23) | P2 |
| 18, 19, 20 | `Noldentitas` (huruf L kecil, bukan I), `Tanggal Pinjam`, `TanggalJatuh Tempo`, `Status Transaksi`, `data Transaksi`, `Total Denda` (ada spasi) | `NoIdentitas`, `TanggalPinjam`, `TanggalJatuhTempo`, `StatusTransaksi`, `dataTransaksi`, `TotalDenda` | P2 |
| 15, 21 | `dataKoleksi Buku`, `Total Eksemplar`, `Eksemplar Tersedia` (ada spasi) | `dataKoleksiBuku`, `TotalEksemplar`, `EksemplarTersedia` | P2 |
| 23, 24 | `KodeEksemplar = @KodeBuku + "-" + 1{angka}3` | `@` di depan elemen, bukan di dalam definisi: `KodeEksemplar = KodeBuku + "-" + 1{angka}3`, dan `@KodeEksemplar` di record D2 | P2 |
| 10, 11 | `StatusDenda = [Belum Dibayar \| Lunas]`, `StatusPembayaran = [...]` | `StatusDenda = [Tanpa Denda \| Belum Lunas \| Lunas]` | P2 |
| 14, 22 | `statusKeaktifan` (14) vs `StatusKeaktifan` (22) | satu ejaan: `StatusKeaktifan` | P2 |
| 9 | `StatusTransaksi = [Berhasil \| Gagal]` | `StatusHasil = [Berhasil \| Gagal]` | P2 |
| baru | — | penguraian entri baru di bagian 2 | P1 |

## 4. Mendefinisikan Elemen

| Baris | Masalah | Perbaikan | P |
|---|---|---|---|
| NIM | Hanya NIM | Ganti/ tambah `NoIdentitas = [NIM \| NIP]` (dipakai di seluruh struktur) | P2 |
| KodeEksemplar | Format "Kode Barcode Buku", contoh `SIL-BK-0012`, sedangkan penguraian `KodeBuku + "-" + 1{angka}3` | Samakan dengan penguraian, mis. format `NNNNNN-N..NNN`, contoh `101202-1`, tidak valid `SIL-BK-0012` | P2 |
| StatusAnggota | `[Aktif \| Bebas Denda \| Diblokir]` tidak dipakai di struktur mana pun | Ganti dengan `StatusKeaktifan = [Aktif \| Nonaktif]` | P2 |
| StatusEksemplar | `[Tersedia \| Dipinjam \| Rusak]` | `[Tersedia \| Dipinjam \| Rusak \| Hilang]` | P2 |
| StatusDenda | sudah `[Tanpa Denda \| Belum Lunas \| Lunas]` | tetap; struktur 10 & 11 yang menyesuaikan | - |
| JumlahDenda | nama di struktur `TotalDenda` | ganti nama baris jadi `TotalDenda` | P2 |
| baru | belum ada | `JumlahPerpanjangan`, `JumlahDibayar`, `TanggalBayar`, `KeteranganGagal`, `StatusHasil`, `JenisPerubahan`, `KataKunci`, `KondisiBuku`, `TarifDenda`, `JumlahHariTerlambat`, `NoBukti` (dipakai M06; format di KEBUTUHAN #23) | P1 |
| semua | Kolom Nullability & Sumber Nilai tidak ada (wajib Modul 5 §1.7) | tambah dua kolom | P2 |

## 5. Validasi Silang

Bagian ini **masih kosong** (hal. 53). Isi dengan penelusuran satu proses (Modul 5 Langkah 5). Contoh siap pakai: tabel "Validasi Silang Internal — Proses 3.1" di [`../../EVALUASI_DATA_DICTIONARY.md`](../../EVALUASI_DATA_DICTIONARY.md). Cantumkan temuan DFD yang muncul (3.1 butuh baca D3), karena ini jawaban refleksi M05 no. 2. — **P1**

## 6. Bagian Wajib yang Belum Ada (Modul 5 Bagian IV)

| Bagian | Isi | P |
|---|---|---|
| Daftar Alias | Nama baku ↔ alias. Contoh: `NoIdentitas` ↔ NIM, NIP, ID Anggota; `KodeEksemplar` ↔ Kode Buku Fisik; `catatanDenda` ↔ Konfirmasi Denda (M02–M03); `D3 Transaksi Fisik` ↔ Data Transaksi | P1 |
| Daftar TBD | Mis. TambahanPerpanjangan (+7 hari dari jatuh tempo lama?), retensi D1/D3; masing-masing dengan pemilik dan tenggat | P1 |
| Revision History, Log Kontribusi | Lampiran A & B modul; catat juga penggunaan AI | P1 |
| Pertanyaan Refleksi | 3 pertanyaan Modul 5 | P2 |

---

## Catatan Perubahan

| Bagian | Ringkas | Alasan |
|---|---|---|
| Inventaris | 1 hapus, 5 tambah, 6 koreksi arah/lokasi, 1 ganti nama store | DFD final 2026-10-26 + balancing M04 |
| Entri Komposit | 7 entri baru, 1 hapus, 14 koreksi | Blocker M06 (struktur input/output process spec) |
| Penguraian | ikut entri + typo nama elemen | Konsistensi nama (Modul 5 §1.8) |
| Elemen | 11 elemen baru, 5 koreksi domain, 2 kolom wajib | Modul 5 §1.7, §1.10 |
| Validasi Silang, Alias, TBD, Revision | diisi / ditambah | Isi minimum dokumen utama Modul 5 Bagian IV |
