# NotePRPL: Manajemen Tugas SILAPUS (Kelompok 6 / RajinBelajar, 2B)

Catatan kerja tugas bertahap PRPL (Polban D3 TI) untuk studi kasus SILAPUS. Repo ini hanya berisi folder `manajemen/`. Artefak (PDF, docx, `.bpm`) tetap disimpan lokal.

| File | Isi |
|---|---|
| [BACKLOG.md](BACKLOG.md) | To-do & status per modul |
| [revisions-recommendations/](revisions-recommendations/README.md) | **Rekomendasi revisi per modul** (M01–M06), dengan checklist yang bisa dicentang |
| [BASELINE_PENAMAAN.md](BASELINE_PENAMAAN.md) | Nama resmi proses, flow, store. Cek di sini sebelum menulis nama apa pun |
| [AUDIT_BALANCING.md](AUDIT_BALANCING.md) | Audit balancing lintas modul (AUD-A/B/C/D) + rencana perbaikan |
| [EVALUASI_DATA_DICTIONARY.md](EVALUASI_DATA_DICTIONARY.md) | List flow per diagram vs kamus data, koreksi hasil Gemini |
| [TEMUAN_DAN_REVISI.md](TEMUAN_DAN_REVISI.md) | Peer review, audit internal, revision history |
| [generator/](generator/) | `m05_data.py` (isi kamus data) → `build_m05.py` (xlsx + docx); `build_validasi_k4.py` |

Generator menulis ke `../progress/` dan `../validasi-silang/`, jadi jalankan dari folder kerja lokal yang berisi folder-folder itu:

```
python manajemen/generator/build_m05.py
```
