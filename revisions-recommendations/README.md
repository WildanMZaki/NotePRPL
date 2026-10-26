# Rekomendasi Revisi per Modul

Satu file per modul. Setiap item punya ID `RV-M0x-nn`, checkbox, prioritas, lokasi, isi **sekarang → seharusnya**, acuan, dan dampak ke modul lain.
Rujukan audit asal (AUD-xx) ada di [`../AUDIT_BALANCING.md`](../AUDIT_BALANCING.md).

**Cara pakai:** centang `[x]` kalau sudah diterapkan di dokumen, isi kolom PIC di tabel di bawah, lalu commit. Rename apa pun tetap ikut alur `BASELINE_PENAMAAN.md` → `TEMUAN_DAN_REVISI.md` → artefak.

## Siap Timpa (2026-10-26) — pakai ini dulu

Teks pengganti lengkap per bagian dokumen, tinggal salin dan timpa. Perubahan tiap bagian ada di "Catatan Perubahan" di bawah masing-masing file.

| Modul | File |
|---|---|
| M01 Project Charter | [siap-timpa/M01-charter.md](siap-timpa/M01-charter.md) |
| M02 Event Context | [siap-timpa/M02-event-context.md](siap-timpa/M02-event-context.md) |
| M03 DFD Level 0 | [siap-timpa/M03-dfd-level0.md](siap-timpa/M03-dfd-level0.md) |
| M04 DFD Decomposition | [siap-timpa/M04-dfd-decomposition.md](siap-timpa/M04-dfd-decomposition.md) |
| M05 | belum (sedang diedit kelompok); kebutuhan dari M04/M06: [siap-timpa/KEBUTUHAN-DARI-M05.md](siap-timpa/KEBUTUHAN-DARI-M05.md) |
| M06 | draft lengkap di `progress/PRPL_M06_2B_RajinBelajar_ProcessSpecification_draft.docx` (+ `_DecisionTable.xlsx`, `_DecisionTree_3.4.png`), dibangkitkan dari `generator/m06_data.py` |

File per item (RV-M0x-nn) di bawah tetap disimpan sebagai rujukan alasan.

## Tracker

| Modul | File | Item | P1 | P2 | P3 | PIC | Status |
|---|---|---|---|---|---|---|---|
| M01 Project Charter | [M01-charter.md](M01-charter.md) | 8 | 0 | 5 | 3 | | ⏳ |
| M02 Event & Context | [M02-event-context.md](M02-event-context.md) | 11 | 6 | 3 | 2 | | ⏳ |
| M03 DFD Level 0 | [M03-dfd-level0.md](M03-dfd-level0.md) | 7 | 4 | 3 | 0 | | ⏳ |
| M04 DFD Decomposition | [M04-dfd-decomposition.md](M04-dfd-decomposition.md) | 12 | 8 | 3 | 1 | | ⏳ |
| M05 Data Dictionary | [M05-data-dictionary.md](M05-data-dictionary.md) | 20 | 13 | 6 | 1 | | 🔄 v0.2 (generator) vs v0.1b (`updates/`); +11 item 2026-10-21 |
| M06 Process Spec (persiapan) | [M06-process-spec-prep.md](M06-process-spec-prep.md) | 5 | 3 | 2 | 0 | | ⏳ |

P1 = memblokir balancing/keterlacakan, kerjakan dulu · P2 = sebelum M06 · P3 = kerapian

## Urutan pengerjaan yang disarankan

Urutannya penting karena perubahan mengalir dari hulu ke hilir:

1. **Keputusan kelompok dulu**: Bagian Keuangan (RV-M02-01), flow tambahan DFD (RV-M04-11), keputusan desain kamus data (RV-M05-02), TBD-01 batas perpanjangan.
2. **DFD (.bpm)**: terapkan flow tambahan, ekspor ulang semua gambar.
3. **Context Diagram**: gambar ulang (RV-M02-09). Dipakai di M02 dan M03.
4. **M02**: event list & event table (RV-M02-02..07).
5. **M03**: pengelompokan, tabel proses, matriks CD→L0.
6. **M04**: matriks balancing, daftar koreksi, audit, peer review.
7. **M05**: pindahkan draft v0.2 ke dokumen utama.
8. **M06**: mulai dari inventaris proses primitif.
