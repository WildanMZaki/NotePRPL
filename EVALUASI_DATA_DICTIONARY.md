# Evaluasi Data Dictionary (M05) — 2026-10-21

Pembanding: **M05 v0.1** = `baselines/PRPL_M05_2B_RajinBelajar_DataDictionary.pdf` (yang sudah dikumpulkan), terhadap DFD master `Silapus Latest.bpm` dan Context Diagram di `baselines/PRPL_M03_...DFD-2.pdf`.

Legenda: ✅ ada di inventaris M05 v0.1 dengan nama sama · ≈ ada tapi namanya beda (tidak balance) · ❌ belum ada
Kolom "v0.2" = sudah ditambahkan di kamus data baru (`progress/PRPL_M05_2B_RajinBelajar_DataDictionary.xlsx`).

## Ringkasan

| | Jumlah |
|---|---|
| Flow unik di DFD (L0 + L1) | 31 |
| Data store | 3 |
| Ada di inventaris M05 v0.1 dengan nama sama | 4 flow (dataPendaftaran, dataPencarian, informasiKoleksiBuku, permintaanPerpanjangan) |
| Ada tapi beda nama | 5 flow (`statusKeaktifanMahasiswa`, `formTransaksiPinjam`, `formTransaksiKembali`, `buktiKonfirmasiDenda`, `laporanSirkulasiBulanan`) + 3 store (dinamai `dataAnggota`, `dataKoleksiBuku`, `dataTransaksiSirkulasi` — dua nama pertama sebenarnya nama flow) |
| Belum ada sebagai flow | 22 flow |
| Punya entri komposit di M05 v0.1 | 7 (itu pun 4 di antaranya pakai nama lama) |
| Bagian "Menguraikan Struktur Data" & "Validasi Silang" di M05 v0.1 | **Kosong** |

---

## List Flow

### Context Diagram (dari M03, digambar di draw.io — tidak ada di .bpm)

| Flow di CD | Arah | Padanan DFD L0 | Status |
|---|---|---|---|
| Data Pendaftaran | Anggota → Sistem | dataPendaftaran | ≈ hanya beda format penulisan |
| Data Pencarian | Anggota → Sistem | dataPencarian | ≈ format |
| Permintaan Perpanjangan | Anggota → Sistem | permintaanPerpanjangan | ≈ format |
| Status Pendaftaran | Sistem → Anggota | statusPendaftaran | ≈ format |
| Informasi Katalog | Sistem → Anggota | informasiKoleksiBuku | ≈ **beda nama** |
| Status Perpanjangan | Sistem → Anggota | statusPerpanjangan | ≈ format |
| Data Transaksi Fisik | Petugas → Sistem | dataTransaksiFisik | ≈ format |
| Data Koleksi Buku | Petugas → Sistem | dataKoleksiBaru | ≈ **beda nama** |
| Konfirmasi Denda | Petugas → Sistem | catatanDenda | ≈ **beda nama** |
| Status Transaksi | Sistem → Petugas | statusTransaksiDanBukti | ≈ **beda nama** |
| Bukti Pengembalian dan Denda | Sistem → Petugas | buktiPengembalianDanDenda | ≈ format |
| **Laporan Operasional** | Sistem → Petugas | **tidak ada** | ❌ **CD tidak balance dengan L0** |
| Permintaan Laporan | Kepala → Sistem | permintaanLaporan | ≈ format |
| Laporan Bulanan Sirkulasi & Denda | Sistem → Kepala | laporanBulanan | ≈ **beda nama** |
| Status Keaktifan Mahasiswa | Sistem Akademik → Sistem | statusKeaktifan | ≈ **beda nama** |
| Data Verifikasi Mahasiswa | Sistem → Sistem Akademik | dataVerifikasi | ≈ **beda nama** |

→ Context Diagram harus direvisi ke nama baseline dan "Laporan Operasional" dihapus (lihat AUDIT_BALANCING AUD-B-01, AUD-B-02).

### DFD Level 0

**Tipe 1: entitas → proses / proses → entitas (tanpa data store)**

| Flow | Arah | Inventaris M05 v0.1 | v0.2 |
|---|---|---|---|
| dataPendaftaran | Anggota → 1 | ✅ (tapi Tujuan tertulis "Proses 1.1", padahal proses 1 tidak didekomposisi) | ✅ |
| statusPendaftaran | 1 → Anggota | ❌ | ✅ |
| dataVerifikasi | 1 → Sistem Akademik | ❌ | ✅ |
| statusKeaktifan | Sistem Akademik → 1 | ≈ `statusKeaktifanMahasiswa` | ✅ |
| dataPencarian | Anggota → 2 | ✅ (tapi tidak ada entri komposit) | ✅ |
| informasiKoleksiBuku | 2 → Anggota | ✅ | ✅ |
| dataKoleksiBaru | Petugas → 2 | ❌ | ✅ |
| dataTransaksiFisik | Petugas → 3 | ❌ (di v0.1 langsung pecah jadi `formTransaksiPinjam` + `formTransaksiKembali`) | ✅ sebagai komposit [pilih] |
| statusTransaksiDanBukti | 3 → Petugas | ❌ | ✅ |
| catatanDenda | Petugas → 3 | ≈ `buktiKonfirmasiDenda` | ✅ |
| buktiPengembalianDanDenda | 3 → Petugas | ❌ | ✅ |
| permintaanPerpanjangan | Anggota → 3 | ✅ (tapi Tujuan tertulis "Proses 3.3"; yang benar 3.4) | ✅ |
| statusPerpanjangan | 3 → Anggota | ❌ | ✅ |
| permintaanLaporan | Kepala → 4 | ❌ | ✅ |
| laporanBulanan | 4 → Kepala | ≈ `laporanSirkulasiBulanan` | ✅ |

**Tipe 2: melibatkan data store**

| Flow | Arah | Inventaris M05 v0.1 | v0.2 |
|---|---|---|---|
| dataAnggota | 1 → D1 (tulis) | ≈ dicatat sebagai **nama store**, bukan flow | ✅ |
| dataKoleksiBuku | D2 ↔ 2 (baca + tulis) | ≈ dicatat sebagai **nama store** | ✅ |
| statusAnggota | D1 → 3 (baca) | ❌ | ✅ |
| dataEksemplar | D2 → 3 (baca) | ❌ | ✅ |
| pembaruanEksemplar | 3 → D2 (tulis) | ❌ | ✅ |
| peminjamAktif | D3 → 3 (baca) | ❌ | ✅ |
| dataPeminjaman | 3 → D3 (tulis) | ❌ | ✅ sebagai komposit [pilih] |
| dataTransaksi | D3 → 4 (baca) | ❌ | ✅ |
| dataKoleksi | D2 → 4 (baca) | ❌ | ✅ |

**Data store**

| Store | Inventaris M05 v0.1 | v0.2 |
|---|---|---|
| D1 Data Anggota | ≈ `dataAnggota` | ✅ |
| D2 Data Koleksi | ≈ `dataKoleksiBuku` | ✅ |
| D3 Transaksi Fisik | ≈ `dataTransaksiSirkulasi` | ✅ |

### DFD Level 1 Proses 2 (Mencari Katalog Buku, Mengelola Data Koleksi)

**Tipe 1**

| Flow | Arah | Inventaris M05 v0.1 | v0.2 |
|---|---|---|---|
| dataPencarian | Anggota → 2.1 | ✅ | ✅ |
| informasiKoleksiBuku | 2.1 → Anggota | ✅ | ✅ |
| dataKoleksiBaru | Petugas → 2.2 | ❌ | ✅ |

**Tipe 2**

| Flow | Arah | Inventaris M05 v0.1 | v0.2 |
|---|---|---|---|
| dataKoleksiBuku | D2 → 2.1 (baca) | ≈ (sebagai store) | ✅ |
| dataKoleksiBuku | 2.2 → D2 (tulis) | ≈ (sebagai store) | ✅ |

### DFD Level 1 Proses 3 (Memproses Sirkulasi dan Denda)

**Tipe 1**

| Flow | Arah | Inventaris M05 v0.1 | v0.2 |
|---|---|---|---|
| dataTransaksiPeminjaman | Petugas → 3.1 | ≈ `formTransaksiPinjam` | ✅ |
| statusTransaksiDanBukti | 3.1 → Petugas | ❌ | ✅ |
| dataTransaksiPengembalian | Petugas → 3.2 | ≈ `formTransaksiKembali` | ✅ |
| statusTransaksiDanBukti | 3.2 → Petugas | ❌ (flow yang sama dengan 3.1, satu entri) | ✅ |
| dataKeterlambatan | 3.2 → 3.3 (internal) | ❌ | ✅ |
| catatanDenda | Petugas → 3.3 | ≈ `buktiKonfirmasiDenda` (v0.1 menulis tujuannya "3.4", yang benar 3.3) | ✅ |
| buktiPengembalianDanDenda | 3.3 → Petugas | ❌ | ✅ |
| permintaanPerpanjangan | Anggota → 3.4 | ✅ | ✅ |
| statusPerpanjangan | 3.4 → Anggota | ❌ | ✅ |

**Tipe 2**

| Flow | Arah | Inventaris M05 v0.1 | v0.2 |
|---|---|---|---|
| statusAnggota | D1 → 3.1, D1 → 3.4 | ❌ | ✅ |
| dataEksemplar | D2 → 3.1 | ❌ | ✅ |
| pembaruanEksemplar | 3.1 → D2, 3.2 → D2 | ❌ | ✅ |
| peminjamAktif | D3 → 3.2, D3 → 3.4 | ❌ | ✅ |
| dataPeminjamanBaru | 3.1 → D3 | ❌ | ✅ |
| pembaruanPengembalian | 3.2 → D3 | ❌ | ✅ |
| dataDenda | 3.3 → D3 | ❌ | ✅ |
| pembaruanMasaPinjam | 3.4 → D3 | ❌ | ✅ |

---

## Koreksi terhadap hasil Gemini (Irfan + Rere)

Sebagian besar hasil Gemini sudah benar, terutama hitungan 15 flow Tipe 1 di Level 0. Yang perlu dikoreksi:

1. **`buktiKonfirmasiDenda` padanannya `catatanDenda`, bukan `buktiPengembalianDanDenda`.** Di M05 v0.1, `buktiKonfirmasiDenda` arahnya Petugas → Proses (input pembayaran denda). Sedangkan `buktiPengembalianDanDenda` adalah output Proses → Petugas. Arahnya beda, jadi bukan sinonim. Akibatnya `buktiPengembalianDanDenda` statusnya **belum ada**.
2. **`infoKatalog/Ketersediaan` di L1 Proses 2 sudah tidak berlaku.** Itu nama dari file Rere sebelum merge. Di DFD master sudah `informasiKoleksiBuku`, jadi sudah balance.
3. **Tipe 2 (flow ke/dari data store) belum dihitung sama sekali**, padahal Modul 5 §1.11 mewajibkan seluruh flow dan store ada di inventaris. Jumlahnya 9 flow di L0 dan 8 flow di L1 Proses 3 (lihat tabel di atas).
4. **Context Diagram belum dicek.** Hasilnya ada flow `Laporan Operasional` yang tidak punya padanan sama sekali.
5. **Tanda "✅" belum tentu benar.** `dataPencarian` memang ada di inventaris, tapi tidak punya entri komposit. `dataPendaftaran` dan `permintaanPerpanjangan` ada, tapi nomor proses tujuannya salah.

---

## Kepatuhan M05 v0.1 terhadap Instruksi Modul 5

| # | Ketentuan Modul 5 | Kondisi M05 v0.1 | Status v0.2 |
|---|---|---|---|
| K-01 | §1.11 / Langkah 1: seluruh flow & store pada DFD tercatat di inventaris | 12 dari 34 | ✅ 34/34 |
| K-02 | Langkah 1.2: salin nama **tanpa mengubah ejaan** | Banyak nama dikarang ulang (`formTransaksiPinjam`, `buktiKonfirmasiDenda`, ...) | ✅ nama = DFD |
| K-03 | Langkah 1.3: lokasi, sumber, tujuan, proses terkait benar | Nomor proses salah: "1.1", "1.2" (proses 1 tidak didekomposisi), 3.3/3.4 tertukar | ✅ |
| K-04 | Kolom "Status Entri" | Diisi Komposit/Elementer/Store, bercampur dan tidak sejajar | ✅ Baku / Baku (dulu: ...) |
| K-05 | §1.6: entri komposit untuk setiap flow (nama, alias, bentuk, arus, penjelasan, periode, volume, struktur, aturan) | 7 entri | ✅ 31 entri |
| K-06 | §1.3: entri store berisi deskripsi, record, kunci, retensi, sumber, akses | Tidak ada di PDF (hanya di xlsx, tanpa retensi/akses) | ✅ 3 entri (retensi = TBD-05) |
| K-07 | Langkah 3: struktur diuraikan sampai elemen elementer, tidak sirkular | **Bagian kosong** | ✅ sheet `4_Penguraian` + docx (dicek otomatis tidak sirkular) |
| K-08 | §1.7 / Langkah 4: elemen punya definisi, tipe, format, panjang, domain, null, sumber nilai, contoh valid & tidak valid | 10 elemen; kolom null & sumber nilai tidak ada di PDF | ✅ 55 elemen lengkap |
| K-09 | Format, domain, dan contoh tidak boleh bertentangan | `KodeEksemplar` An(10) tapi contohnya 11 karakter; `IDTransaksi` An(12) tapi contohnya 16 karakter | ✅ format diperbaiki |
| K-10 | Langkah 4.4: `@` untuk elemen kunci | `@` dipakai di flow untuk rujukan (`@IDTransaksi + @NIM + @KodeEksemplar`) | ✅ `@` hanya di record store |
| K-11 | §1.8: satu konsep satu nama; sinonim dicatat sebagai alias | `NIM` vs NIM/NIP di event; PascalCase vs camelCase | ✅ sheet `6_Alias` |
| K-12 | §1.8 & Modul 4 §1.8: tanpa detail implementasi | Alias `tb_anggota`, `tb_koleksi`, `tb_transaksi`; "terminal OPAC" | ✅ dihapus |
| K-13 | §1.9: TBD punya pemilik & batas waktu, bukan tebakan | 2 TBD; aturan "max 3 kali perpanjangan" ditulis sebagai fakta padahal bentrok dengan EV-05 | ✅ 7 TBD |
| K-14 | Aturan bisnis tidak boleh di luar cakupan DFD | "eksemplar direservasi", "top 10 buku", "status Bebas Denda", "kondisi fisik buku" — tidak ada di DFD | ✅ dihapus |
| K-15 | Langkah 5: validasi silang (telusuri satu proses) | **Bagian kosong**; matriks di xlsx menulis "Digunakan di Process Spec: Ya" padahal M06 belum ada | ✅ lihat bagian berikut |
| K-16 | Pengumpulan: `.pdf` + `.xlsx` + `_Review.pdf` dengan nama `PRPL_M05_[Kelas]_[Kelompok]_...` | xlsx bernama `Kelompok6`; Review.pdf belum ada | ⏳ xlsx baru sudah memakai `RajinBelajar`; Review.pdf belum |
| K-17 | Pertanyaan refleksi Modul 5 | Belum dijawab | ⏳ |

---

## Validasi Silang Internal (Modul 5 Langkah 5) — Proses 3.1 Memproses Peminjaman Buku

| Langkah | Hasil |
|---|---|
| 1. Telusuri input-output 3.1 | Input: `dataTransaksiPeminjaman`, `statusAnggota`, `dataEksemplar`. Output: `statusTransaksiDanBukti`, `pembaruanEksemplar`, `dataPeminjamanBaru`. Keenamnya punya entri di kamus data v0.2. |
| 2. Elemen yang akan dipakai process spec terdefinisi | `NomorIdentitas`, `KodeEksemplar`, `StatusAnggota`, `StatusEksemplar`, `IDTransaksi`, `TanggalPinjam`, `TanggalJatuhTempo`, `StatusTransaksi`, `StatusDenda`, `AlasanPenolakan`, `JumlahPerpanjangan` sudah ada. |
| 3. Sinonim / homonim | `Status` dipisah jadi `StatusAnggota`, `StatusEksemplar`, `StatusTransaksi`, `StatusDenda`, `StatusProses`, `StatusAkademik`. Sinonim NIM/NIP/IDAnggota disatukan di alias `NomorIdentitas`. |
| 4. Store punya record & kunci jelas | D1 `@NomorIdentitas`, D2 `@KodeEksemplar`, D3 `@IDTransaksi`. |
| 5. **Masalah yang asalnya dari DFD** | Aturan EV-03 "kuota 3 eksemplar" dan "anggota memiliki denda" butuh data transaksi aktif anggota. Masalahnya, **3.1 tidak membaca D3** (hanya menulis), jadi aturan itu tidak bisa dijalankan (gray hole). Perlu tambah flow `peminjamAktif` D3 → 3.1. Balance tetap aman karena `peminjamAktif` sudah ada di Level 0. → AUD-B-07 |
| 6. TBD | TBD-01 (batas perpanjangan) dan TBD-07 (sumber aturan 7 hari/Rp1.000) memengaruhi 3.1 & 3.4. |

---

## Yang Perlu Dikerjakan Berikutnya (dari evaluasi ini)

1. **Review isi v0.2 oleh kelompok.** Terutama keputusan desain yang kuambil:
   - `NomorIdentitas = [NIM | NIP]`
   - 1 transaksi = 1 eksemplar (kuota 3 dicek lewat jumlah transaksi aktif)
   - `StatusAnggota` hanya [Aktif | Nonaktif]; denda dicek dari D3, bukan dari status anggota
   - Elemen tanggal diurai jadi `Tahun-Bulan-Hari`
2. **Zidan (penguraian atom):** cek sheet `4_Penguraian`. Penguraian dibangkitkan otomatis dari definisi struktur, jadi yang perlu dicek adalah domain dan panjang tiap elemen. Kalau mau ubah, edit `manajemen/generator/m05_data.py` lalu jalankan `python manajemen/generator/build_m05.py`, supaya xlsx & docx tetap sinkron.
3. **Irfan + Rere:** cocokkan tabel di atas dengan hasil Gemini. Isi Periode/Volume yang masih berupa asumsi bila ada data lebih baik.
4. Revisi Context Diagram (AUD-B-01/02), lalu alias "(CD)" di sheet Alias bisa dihapus.
5. Pindahkan isi `..._DataDictionary_draft.docx` ke dokumen utama, ekspor PDF, buat `_Review.pdf`.
