# Yang Dibutuhkan M04 & M06 dari Kamus Data (M05)

Ini **bukan** revisi M05. Isinya daftar yang dipakai M04 (matriks balancing) dan M06 (process spec) supaya keduanya tetap terlacak ke kamus data. Untuk dicek oleh yang sedang mengedit M05 (`updates/`, versi 2026-10-26).

## A. Karena DFD berubah (2026-10-26)

| Flow | Yang perlu ada di M05 |
|---|---|
| dataAnggota | Arah jadi dua arah (Proses 1 ↔ D1 Data Anggota) |
| peminjamAktif | Tujuan + Proses 3.1 dan 3.3 (sekarang 3.1, 3.2, 3.3, 3.4) |
| dataKoleksiBuku | Di 2.2 dua arah (baca + tulis) |
| statusPengelolaanKoleksi | **Entri baru**: Proses 2 / 2.2 → Petugas Perpustakaan. Struktur usulan: `StatusHasil + KodeBuku + (KeteranganGagal)` |

## B. Supaya matriks balancing M04 sah (baris 4 & 10)

- `dataTransaksiFisik = [dataTransaksiPeminjaman | dataTransaksiPengembalian]`
- `dataPeminjaman = [dataPeminjamanBaru | pembaruanPengembalian | dataDenda | pembaruanMasaPinjam]`, ditambah **4 entri baru**: dataPeminjamanBaru, pembaruanPengembalian, dataDenda, pembaruanMasaPinjam

## C. Elemen yang dipakai M06 tetapi belum ada atau beda

| Elemen | Dipakai di | Catatan |
|---|---|---|
| KodeEksemplar (bukan KodeBuku) di dataTransaksiPeminjaman, dataTransaksiPengembalian, permintaanPerpanjangan | 3.1, 3.2, 3.4 | Yang dipinjam adalah eksemplar fisik. dataTransaksiPeminjaman = NoIdentitas + 1{KodeEksemplar}3 |
| IDTransaksi di permintaanPerpanjangan | 3.4 | Untuk menunjuk transaksi yang diperpanjang |
| JumlahPerpanjangan | 3.1, 3.4 | Di record D3 dan peminjamAktif |
| StatusDenda, TotalDenda, StatusTransaksi, JumlahPerpanjangan di peminjamAktif | 3.1, 3.3, 3.4 | Sekarang peminjamAktif hanya NoIdentitas + {IDTransaksi + KodeEksemplar + TanggalJatuhTempo} |
| StatusDenda = [Tanpa Denda \| Belum Lunas \| Lunas] | 3.1, 3.3, 3.4 | Sekarang ada dua domain berbeda (catatanDenda vs tabel elemen) |
| JumlahDibayar, TanggalBayar | 3.3 | Isi catatanDenda = IDTransaksi + JumlahDibayar + TanggalBayar (RV-M05-10) |
| StatusHasil = [Berhasil \| Gagal] | semua output status | Sekarang memakai nama StatusTransaksi, bentrok dengan StatusTransaksi [Aktif \| Selesai \| Terlambat] di D3 (homonim) |
| KeteranganGagal | semua output status | Aturan M05 "transaksi gagal wajib disertai keterangan alasan" |
| JenisPerubahan = [Tambah \| Ubah \| Hapus] | 2.2 | EV-08 mencakup tambah, ubah, hapus |
| KataKunci | 2.1 | Isi dataPencarian |
| statusKeaktifan dari Sistem Akademik: + nilai "Tidak Terdaftar" | 1 | EV-01 error 1 |
| StatusEksemplar: + Rusak, Hilang | 3.2 | KondisiBuku Rusak/Hilang mengubah status eksemplar |
| dataKoleksiBuku memuat eksemplar ({KodeEksemplar + StatusEksemplar}) | 2.1 | Untuk menghitung StatusKetersediaan |
| NamaLengkap vs NamaAnggota | 1 | Pilih satu (dataPendaftaran vs dataAnggota) |
| IDPetugas | - | Tidak dipakai proses mana pun dan tidak tersimpan di store; hapus atau simpan di D3 |
| TanggalJatuhTempo di dataTransaksiPeminjaman | - | Nilai ini dihitung sistem (3.1), bukan input Petugas; hapus dari input |

## D. Parameter yang dipakai M06

LamaPinjam 7 hari · TarifDenda Rp1.000/hari · KuotaPinjam 3 · BatasPerpanjangan 2 (dari EV-05) · TambahanPerpanjangan 7 hari (asumsi, perlu dikonfirmasi).
