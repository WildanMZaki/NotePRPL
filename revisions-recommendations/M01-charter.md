# M01 — Project Charter

File: `baselines/PRPL_M01_2B_RajinBelajar_Charter-1.pdf`

Charter jarang perlu diubah. Yang direvisi di sini hanya bagian yang **bertentangan** dengan artefak setelahnya, atau yang menjadi **sumber aturan** untuk kamus data dan process spec.

- [ ] RV-M01-01 · Placeholder nama kelompok masih tertinggal · P2
- [ ] RV-M01-02 · Tujuan tidak selaras dengan masalah prioritas · P2
- [ ] RV-M01-03 · Out of scope "pengadaan koleksi" vs proses 2.2 · P2
- [ ] RV-M01-04 · Asumsi mahasiswa/dosen vs dependensi "cukup NIM" · P2
- [ ] RV-M01-05 · Mekanisme perubahan belum dijalankan · P2
- [ ] RV-M01-06 · Penjadwalan berhenti di 7 Okt · P3
- [ ] RV-M01-07 · Tabel deliverable bergeser · P3
- [ ] RV-M01-08 · Typo · P3

---

### RV-M01-01 · Placeholder nama kelompok · P2
- **Lokasi:** A. Identitas Proyek, paragraf 2
- **Sekarang:** "Proyek dikerjakan oleh **[Nama Kelompok, misalnya Kelompok 1]** dari kelas 2B - D3"
- **Seharusnya:** "Proyek dikerjakan oleh **Kelompok 6 (RajinBelajar)** dari kelas 2B - D3"

### RV-M01-02 · Tujuan vs masalah prioritas · P2
- **Lokasi:** C. Problem Statement (paragraf pemilihan) dan D. Tujuan
- **Sekarang:** Prioritas yang dipilih P_02, P_03, P_04. Tapi Tujuan 1 = pencarian katalog (itu P_01, yang tidak dipilih), sedangkan P_02 (validasi Sistem Akademik) tidak muncul di Tujuan (hanya di Kriteria Keberhasilan 1).
- **Seharusnya:** Tujuan 1 = validasi status keanggotaan terintegrasi Sistem Akademik (P_02); Tujuan 2 = denda (P_03); Tujuan 3 = laporan (P_04). Pencarian katalog disebut sebagai fitur pendukung dalam ruang lingkup.
- **Acuan:** keterlacakan masalah → tujuan → kriteria keberhasilan (Kriteria Keberhasilan 4 charter sendiri).

### RV-M01-03 · Pengadaan koleksi vs Proses 2.2 · P2
- **Lokasi:** F. Ruang Lingkup
- **Sekarang:** Out of Scope "Modul pengadaan koleksi buku baru", sementara DFD punya Proses 2.2 Mengelola Data Koleksi dengan flow `dataKoleksiBaru` (EV-08).
- **Seharusnya:** Tambahkan di In Scope: "Pengelolaan data katalog koleksi (tambah, ubah, hapus data buku & eksemplar)". Pertegas Out of Scope: "Proses pengadaan/pembelian koleksi (pemesanan, anggaran, vendor)".
- **Dampak:** menjustifikasi EV-08 dan Proses 2.2.

### RV-M01-04 · Mahasiswa/dosen vs "cukup NIM" · P2
- **Lokasi:** F. Ruang Lingkup, kolom Asumsi dan Dependensi
- **Sekarang:** Asumsi "anggota mahasiswa atau dosen", tetapi asumsi integrasi "cukup dengan NIM".
- **Seharusnya:** "cukup dengan NIM/NIP". Atau, bila dosen dikeluarkan, ubah asumsi jadi mahasiswa saja.
- **Dampak:** TBD-03 kamus data (`NomorIdentitas = [NIM | NIP]`), EV-01.

### RV-M01-05 · Mekanisme perubahan belum dijalankan · P2
- **Lokasi:** J. Mekanisme Perubahan
- **Sekarang:** Charter mewajibkan setiap perubahan dicatat (bagian, alasan, pengedit, disetujui minimal satu anggota lain), tetapi M02–M05 tidak punya revision history.
- **Seharusnya:** Tidak perlu mengubah charter. Terapkan di M04–M06: tabel revision history dengan kolom Reviewer yang terisi (lihat `TEMUAN_DAN_REVISI.md` bagian D).
- **Catatan sumber aturan:** bagian Batasan menyebut "pembayaran cash maupun non-cash, tidak menerima hutang". Ini sumber aturan `JumlahDibayar = JumlahDenda` di kamus data, jadi rujuk ini untuk menutup sebagian TBD-07.

### RV-M01-06 · Penjadwalan · P3
- **Lokasi:** I. Penjadwalan
- **Sekarang:** berhenti di penyusunan DFD (7 Okt 2026).
- **Seharusnya:** tambah baris M04 (dekomposisi), M05 (kamus data), M06 (process spec), validasi silang.

### RV-M01-07 · Tabel deliverable · P3
- **Lokasi:** G. Deliverable
- **Sekarang (di PDF):** isi kolom Keterangan bergeser dari barisnya (keterangan "Model Analisis Terstruktur" tercampur dengan "Model Berorientasi Objek").
- **Seharusnya:** periksa tabel di file sumber, rapikan per baris. Perbaiki juga typo "Beroirentasi", "Spesifikasi Spesial".

### RV-M01-08 · Typo · P3
"Layaanan", "kolekasi", "datannya", "msaih", "spreasheet", "statu", "perpustakkan", "berrdiskusi", "kelompomi", "sebegai", "mengembailikan", "Menperoleh", "Asusmsi", "mempertimbangan", "Resiko" (baku: Risiko), "telat direvisi" (maksudnya: telah).
