# Logika Proses 1, 3.1, 3.4 tanpa Structured English

Pengganti bagian "Structured English" + "Decision Table/Tree" pada Proses 1, 3.1, dan 3.4 di M06. Setelah ini ketiga proses hanya memakai satu bentuk logika:

| Proses | Bentuk logika |
|---|---|
| 1 Mengelola Keanggotaan | Decision table (DT-1) |
| 3.1 Memproses Peminjaman Buku | Decision table (DT-2) |
| 3.4 Memperpanjang Peminjaman | Decision tree (DTree-1) |

Proses lain (2.1, 2.2, 3.2, 3.3, 4) tetap Structured English, tidak berubah.

Karena Structured English dihapus, semua yang tadinya hanya ada di SE (jalur EV-09, perulangan per eksemplar, isi data yang ditulis ke store) sekarang dimasukkan ke dalam tabel/tree.

---

## Cara membaca decision table

- **Baris atas = kondisi (C)**, baris bawah = tindakan (A).
- **Setiap kolom R = satu aturan.** Baca satu kolom dari atas ke bawah: "kalau kondisinya seperti ini, maka tindakan yang bertanda X dijalankan".
- **Isi sel kondisi:**
  - `Y` = kondisi terpenuhi (ya)
  - `T` = kondisi tidak terpenuhi (tidak)
  - nilai lain (mis. `Aktif`, `EV-01`) = kondisi bernilai itu
  - `-` = kondisi tidak diperiksa / tidak berpengaruh di aturan ini (biasanya karena kondisi di atasnya sudah gagal)
- **Isi sel tindakan:** `X` = tindakan dijalankan; kosong = tidak dijalankan. Bila satu aturan punya beberapa X, tindakan dijalankan berurutan sesuai nomor A dari atas ke bawah.
- **Urutan pemeriksaan kondisi** = urutan nomor C (C1 dulu, lalu C2, dst.).
- **Pemeriksaan kelengkapan** di bawah tabel membuktikan setiap kombinasi kondisi tertutup tepat satu aturan (tidak ada yang terlewat, tidak ada yang dobel).

Contoh baca DT-1 kolom R3: pemicu EV-01, data lengkap (Y), NoIdentitas belum terdaftar (T), Sistem Akademik membalas Aktif → jalankan A1, A2, A3 (kirim dataVerifikasi, simpan anggota, kirim Berhasil).

## Cara membaca decision tree

- Mulai dari **simpul [1]** paling atas, jawab pertanyaannya dengan data yang ada.
- Ikuti cabang **Ya** atau **Tidak** ke simpul berikutnya.
- Berhenti saat sampai di **daun (L1, L2, ...)**: itu hasil akhir dan tindakan yang dijalankan.
- Urutan simpul penting: pemeriksaan pertama yang gagal menentukan alasan penolakan yang dikirim ke anggota. Karena itu bentuk tree dipakai di Proses 3.4, bukan tabel.

---

## Proses 1 Mengelola Keanggotaan: Decision Table DT-1

**Data yang dipakai:** dataPendaftaran (dari Anggota Perpustakaan) atau statusKeaktifan (dari Sistem Akademik); dataAnggota dibaca dari D1 Data Anggota untuk memeriksa NoIdentitas.

| Kondisi atau Tindakan | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|---|---|---|---|---|---|---|---|---|
| C0 Pemicu | EV-01 | EV-01 | EV-01 | EV-01 | EV-01 | EV-09 | EV-09 | EV-09 |
| C1 Data pendaftaran lengkap (NoIdentitas, NamaLengkap, ProgramStudi, EmailKampus) dan EmailKampus berdomain polban.ac.id | T | Y | Y | Y | Y | - | - | - |
| C2 NoIdentitas sudah ada di D1 Data Anggota | - | Y | T | T | T | Y | Y | T |
| C3 StatusAkademik pada statusKeaktifan dari Sistem Akademik | - | - | Aktif | Nonaktif | Tidak Terdaftar | Aktif | Nonaktif / Tidak Terdaftar | - |
| A1 Kirim dataVerifikasi (NoIdentitas, NamaLengkap, ProgramStudi, EmailKampus) ke Sistem Akademik, lalu terima statusKeaktifan |  |  | X | X | X |  |  |  |
| A2 Simpan dataAnggota baru ke D1 (StatusKeaktifan = Aktif, TanggalDaftar = tanggal hari ini) |  |  | X |  |  |  |  |  |
| A3 Kirim statusPendaftaran Berhasil (NoIdentitas, TanggalDaftar) ke Anggota |  |  | X |  |  |  |  |  |
| A4 Kirim statusPendaftaran Gagal + KeteranganGagal ke Anggota; D1 tidak berubah | X | X |  | X | X |  |  |  |
| A5 Ubah StatusKeaktifan anggota di D1 menjadi Aktif |  |  |  |  |  | X |  |  |
| A6 Ubah StatusKeaktifan anggota di D1 menjadi Nonaktif |  |  |  |  |  |  | X |  |
| A7 Abaikan; D1 tidak berubah |  |  |  |  |  |  |  | X |
| Keterangan gagal | Data pendaftaran tidak lengkap | NIM/NIP sudah terdaftar | - | Status akademik tidak aktif | NIM/NIP tidak terdaftar di Sistem Akademik | - | - | - |

**Catatan urutan:** pada EV-01, C3 baru diketahui setelah A1 dijalankan (dataVerifikasi dikirim dan Sistem Akademik membalas). Jadi urutannya C1 → C2 → A1 → C3 → tindakan sisa. A1 tidak dijalankan bila C1 atau C2 sudah gagal (R1, R2).

**Pemeriksaan kelengkapan:**
- EV-01: C1 (2) x C2 (2) x C3 (3) = 12 kombinasi. R1 menutup 6 (C1 = T), R2 menutup 3 (C1 = Y, C2 = Y), R3–R5 menutup 3 sisanya. Total 12.
- EV-09: C2 (2) x C3 (3) = 6 kombinasi. R6 menutup 1, R7 menutup 2, R8 menutup 3 (C2 = T). Total 6.
- Tidak ada aturan ganda atau bertentangan, dan setiap tindakan dijalankan oleh minimal satu aturan.

---

## Proses 3.1 Memproses Peminjaman Buku: Decision Table DT-2

**Data yang dipakai:** dataTransaksiPeminjaman (NoIdentitas + 1 sampai 3 KodeEksemplar) dari Petugas Perpustakaan; statusAnggota dari D1; peminjamAktif dari D3; dataEksemplar dari D2.

| Kondisi atau Tindakan | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| C1 statusAnggota (D1) = Aktif | T | Y | Y | Y | Y |
| C2 peminjamAktif (D3) memuat StatusDenda = Belum Lunas atau StatusTransaksi = Terlambat | - | Y | T | T | T |
| C3 Jumlah pinjaman berstatus Aktif + jumlah KodeEksemplar yang diminta <= 3 (KuotaPinjam) | - | - | T | Y | Y |
| C4 StatusEksemplar (D2) dari KodeEksemplar ini = Tersedia | - | - | - | T | Y |
| A1 Buat IDTransaksi dan NoBukti; TanggalPinjam = tanggal hari ini; TanggalJatuhTempo = TanggalPinjam + 7 hari |  |  |  |  | X |
| A2 Tulis dataPeminjamanBaru ke D3 (IDTransaksi, NoIdentitas, KodeEksemplar, TanggalPinjam, TanggalJatuhTempo, StatusTransaksi = Aktif, StatusDenda = Tanpa Denda, JumlahPerpanjangan = 0) |  |  |  |  | X |
| A3 Tulis pembaruanEksemplar ke D2 (KodeEksemplar, StatusEksemplar = Dipinjam) |  |  |  |  | X |
| A4 Catat bukti Berhasil untuk eksemplar ini (KodeEksemplar, NoBukti, IDTransaksi, TanggalJatuhTempo) |  |  |  |  | X |
| A5 Tolak seluruh permintaan: statusTransaksiDanBukti Gagal + KeteranganGagal; D2 dan D3 tidak berubah | X | X | X |  |  |
| A6 Catat bukti Gagal untuk eksemplar ini + KeteranganGagal (eksemplar lain tetap diproses) |  |  |  | X |  |
| A7 Kirim statusTransaksiDanBukti ke Petugas Perpustakaan | X | X | X | X | X |
| Keterangan gagal | Anggota tidak aktif | Masih memiliki denda atau pinjaman terlambat | Kuota pinjam penuh | Eksemplar tidak tersedia | - |

**Catatan urutan (pengganti FOR EACH):**
1. C1, C2, C3 diperiksa **sekali per permintaan** (berlaku untuk anggota). Bila salah satu gagal → R1, R2, atau R3: seluruh permintaan ditolak.
2. Bila C1–C3 lolos, C4 diperiksa **untuk setiap KodeEksemplar** (1 sampai 3 kali). Setiap eksemplar jatuh ke R4 atau R5 sendiri-sendiri, jadi satu permintaan bisa berisi campuran Berhasil dan Gagal.
3. A7 dijalankan **sekali** di akhir, setelah semua eksemplar diperiksa, berisi bukti semua eksemplar.

**Pemeriksaan kelengkapan:** 2^4 = 16 kombinasi. R1 menutup 8 (C1 = T), R2 menutup 4, R3 menutup 2, R4 dan R5 masing-masing 1. Total 16, tidak ada aturan ganda atau bertentangan, dan setiap tindakan dijalankan oleh minimal satu aturan.

---

## Proses 3.4 Memperpanjang Peminjaman: Decision Tree DTree-1

**Data yang dipakai:** permintaanPerpanjangan (NoIdentitas, IDTransaksi) dari Anggota Perpustakaan; peminjamAktif dari D3; statusAnggota dari D1.

```
[1] IDTransaksi ada di peminjamAktif milik NoIdentitas dan masih aktif?
 ├─ Tidak ─> L1 GAGAL "Transaksi tidak ditemukan"
 └─ Ya ──> [2] statusAnggota (D1) = Aktif?
            ├─ Tidak ─> L2 GAGAL "Anggota tidak aktif"
            └─ Ya ──> [3] Tanggal hari ini <= TanggalJatuhTempo?
                       ├─ Tidak ─> L3 GAGAL "Sudah melewati tanggal jatuh tempo"
                       └─ Ya ──> [4] Tidak ada StatusDenda = Belum Lunas di peminjamAktif?
                                  ├─ Tidak ─> L4 GAGAL "Memiliki denda aktif"
                                  └─ Ya ──> [5] JumlahPerpanjangan < 2 (BatasPerpanjangan)?
                                             ├─ Tidak ─> L5 GAGAL "Batas perpanjangan tercapai"
                                             └─ Ya ──> L6 BERHASIL
```

| Simpul | Pertanyaan | Bila Tidak | Bila Ya |
|---|---|---|---|
| 1 | IDTransaksi ada di peminjamAktif milik NoIdentitas dan masih aktif? | L1 Gagal: Transaksi tidak ditemukan | ke simpul 2 |
| 2 | statusAnggota = Aktif? | L2 Gagal: Anggota tidak aktif | ke simpul 3 |
| 3 | Tanggal hari ini <= TanggalJatuhTempo? | L3 Gagal: Sudah melewati tanggal jatuh tempo | ke simpul 4 |
| 4 | Tidak ada denda belum lunas? | L4 Gagal: Memiliki denda aktif | ke simpul 5 |
| 5 | JumlahPerpanjangan < 2? | L5 Gagal: Batas perpanjangan tercapai | L6 Berhasil |

**Tindakan di daun:**
- **L1–L5 (Gagal):** kirim statusPerpanjangan (StatusHasil = Gagal, KeteranganGagal sesuai daun) ke Anggota Perpustakaan. D3 tidak berubah.
- **L6 (Berhasil):**
  1. TanggalJatuhTempo = TanggalJatuhTempo lama + 7 hari (TambahanPerpanjangan)
  2. JumlahPerpanjangan = JumlahPerpanjangan + 1
  3. Tulis pembaruanMasaPinjam (IDTransaksi, TanggalJatuhTempo, JumlahPerpanjangan) ke D3
  4. Kirim statusPerpanjangan (StatusHasil = Berhasil, IDTransaksi, TanggalJatuhTempo baru) ke Anggota Perpustakaan

Gambar tree yang sudah ada (`progress/PRPL_M06_2B_RajinBelajar_DecisionTree_3.4.png`) tetap bisa dipakai; isinya sama, label L1–L6 opsional.

---

## Bagian M06 lain yang ikut menyesuaikan

Ini bukan perubahan baru, hanya teks yang menyebut Structured English untuk tiga proses ini.

**1. Tabel inventaris, kolom Bentuk Logika**

| No. Proses | Lama | Baru |
|---|---|---|
| 1 | Decision table + Structured English | Decision table |
| 3.1 | Decision table + Structured English | Decision table |
| 3.4 | Decision tree + Structured English | Decision tree |

**2. Tabel Memilih Bentuk Logika, kolom Bentuk Logika + Alasan**

| No. Proses | Bentuk Logika | Alasan Pemilihan |
|---|---|---|
| 1 | Decision table | Tiga kondisi independen (kelengkapan data, sudah terdaftar, status dari Sistem Akademik) menentukan hasil pendaftaran; jalur EV-09 dimasukkan sebagai pemicu kedua di tabel yang sama. Decision table memastikan semua kombinasi tertangani. |
| 3.1 | Decision table | Empat kondisi independen membentuk 16 kombinasi; decision table menjamin tidak ada kombinasi yang terlewat. Pemeriksaan per eksemplar ditulis sebagai catatan urutan di bawah tabel. |
| 3.4 | Decision tree | Pemeriksaan berurutan; pemeriksaan pertama yang gagal menentukan alasan penolakan, sehingga urutan cabang perlu terlihat. |

**3. Baris "Bentuk logika dan alasan" di process specification**

| Proses | Isi baru |
|---|---|
| 1 | Decision table (DT-1). Tiga kondisi independen menentukan hasil pendaftaran (EV-01); pembaruan status dari Sistem Akademik (EV-09) ditangani aturan R6–R8. |
| 3.1 | Decision table (DT-2). Empat kondisi independen; C4 diperiksa untuk setiap eksemplar. |
| 3.4 | Decision tree (DTree-1). Urutan pemeriksaan menentukan alasan penolakan yang dikirim. |

**4. Contoh uji: kolom Aturan atau Jalur dan Hasil Penelusuran** (kolom lain tetap)

| ID Uji | Aturan atau Jalur | Hasil Penelusuran |
|---|---|---|
| TC-01 | DT-1 R1 (BR-01) | EV-01, C1 = T → R1 → A4 'Data pendaftaran tidak lengkap' |
| TC-02 | DT-1 R1 (BR-02) | EV-01, email bukan polban.ac.id → C1 = T → R1 → A4 |
| TC-03 | DT-1 R2 (BR-03) | EV-01, C1 = Y, C2 = Y → R2 → A4 'NIM/NIP sudah terdaftar' |
| TC-04 | DT-1 R3 (BR-04) | EV-01, C1 = Y, C2 = T, C3 = Aktif → R3 → A1, A2, A3 |
| TC-05 | DT-1 R4 (BR-04) | EV-01, C3 = Nonaktif → R4 → A1, A4 |
| TC-06 | DT-1 R5 (BR-04) | EV-01, C3 = Tidak Terdaftar → R5 → A1, A4 |
| TC-07 | DT-1 R7 (BR-25) | EV-09, C2 = Y, C3 = Nonaktif → R7 → A6 |
| TC-08 | DT-1 R8 (BR-25) | EV-09, C2 = T → R8 → A7 (diabaikan) |
| TC-18 | DT-2 R1 (BR-08) | C1 = T → R1 → A5, A7 |
| TC-19 | DT-2 R2 (BR-09) | C1 = Y, C2 = Y → R2 → A5, A7 |
| TC-20 | DT-2 R3 (BR-10) | 2 + 2 = 4 > 3 → C3 = T → R3 → A5, A7 |
| TC-21 | DT-2 R4 (BR-11) | C1–C3 lolos; C4 = T untuk 101202-2 → R4 → A6, A7 |
| TC-22 | DT-2 R5 (BR-10, BR-12) | 1 + 2 = 3 → C3 = Y; C4 = Y untuk kedua eksemplar → R5 dua kali (A1–A4), lalu A7 |
| TC-31 | DTree-1 L6 (BR-19, BR-20) | Simpul 1–5 Ya → L6 Berhasil |
| TC-32 | DTree-1 L6 (BR-19) | Simpul 5: 1 < 2 Ya → L6 |
| TC-33 | DTree-1 L5 (BR-19) | Simpul 5: 2 < 2 Tidak → L5 |
| TC-34 | DTree-1 L6 (BR-18) | Simpul 3: 2026-10-26 <= 2026-10-26 Ya → lanjut → L6 |
| TC-35 | DTree-1 L3 (BR-18) | Simpul 3: 2026-10-26 <= 2026-10-25 Tidak → L3 |
| TC-36 | DTree-1 L4 (BR-18) | Simpul 4 Tidak → L4 |
| TC-37 | DTree-1 L2 (BR-08) | Simpul 2 Tidak → L2 |
| TC-38 | DTree-1 L1 (BR-17) | Simpul 1 Tidak → L1 |
