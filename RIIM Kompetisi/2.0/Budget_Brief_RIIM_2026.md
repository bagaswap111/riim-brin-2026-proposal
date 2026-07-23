# Budget Brief — RIIM Kompetisi 2026

## Acuan

- **SBM (Standar Biaya Masukan):** PMK terbaru + Keputusan Kepala BRIN
- **UNNES status:** PTN — Non PKP → tidak dikenakan PPN/PPh 23
- **Pagu:** Rp200–300 juta/tahun (belum final — perlu konfirmasi Feddy)
- **Durasi:** 2 tahun (Tahun I: hardware + pipeline; Tahun II: pilot + diseminasi)

---

## 1. Struktur Anggaran (BRIN Format)

| Komponen | Proporsi | Th I (Rp) | Th II (Rp) | Keterangan |
|----------|----------|-----------|------------|------------|
| **BLP** (Biaya Langsung Personil) | ≤ 25% | — | — | Honor ketua/anggota (jika diizinkan) |
| **BLNP** (Biaya Langsung Non-Personil) | ~70% | — | — | Bahan, perjalanan, sewa, modal |
| **BTL** (Biaya Tidak Langsung) | ~5% | — | — | Monev institusi |
| **Total** | 100% | **250.000.000** | **250.000.000** | **500.000.000** |

---

## 2. Estimasi Biaya Langsung Personil (BLP) — Opsional

> **Catatan:** Beberapa sumber menyebut honor ketua/anggota tidak diizinkan di RIIM Kompetisi, namun sosialisasi BRIN 2026 mencantumkan satuan biaya berikut. Perlu klarifikasi dengan PMO.

| Peran | Satuan | Volume | Satuan (Rp/bln) | Th I (12 bln) | Th II (12 bln) |
|-------|--------|--------|-----------------|---------------|----------------|
| Ketua | orang/bln | 1 | 3.600.000 | 43.200.000 | 43.200.000 |
| Anggota (4 org × 2.400.000) | orang/bln | 4 | 2.400.000 | 115.200.000 | 115.200.000 |
| Tenaga lapangan (2 org) | orang/bln | 2 | 1.500.000 | 18.000.000 | 18.000.000 |
| **Subtotal BLP** | | | | **176.400.000** | **176.400.000** |

> **Alternatif (tanpa honor tim):** BLP diisi hanya tenaga lapangan → Rp18 juta/tahun

---

## 3. Estimasi Biaya Langsung Non-Personil (BLNP)

### 3.1 Hardware Utama (Tahun I) — Belanja Modal ≤ 10%

| Item | Spesifikasi | Estimasi (Rp) | Keterangan |
|------|------------|---------------|------------|
| Panel surya monokristalin | 5,5 kWp (~15 pcs × 370 Wp) | 20.000.000 | ~Rp3,6 jt/panel |
| Inverter hybrid 5 kW | On-grid + battery ready, 2 MPPT | 14.000.000 | Merek Growatt/Solis/SE |
| BESS LiFePO₄ 10 kWh | 48V, termasuk BMS | 32.000.000 | ~Rp3,2 jt/kWh |
| Charger AC 22 kW | — | 0 | Dari mitra (in-kind) |
| IoT gateway + edge computer | Raspberry Pi 5 / industrial PC | 5.000.000 | |
| Sensor cuaca + pyranometer | Suhu, iradiasi, kelembaban | 6.000.000 | |
| Panel distribusi + proteksi | MCB, SPD, enclosure, kabel | 4.000.000 | |
| **Subtotal Hardware** | | **81.000.000** | |

> **Catatan belanja modal:** Jika hardware diklasifikasikan sebagai belanja modal (bukan bahan habis pakai), maka maksimal 10% × Rp500 jt = **Rp50 jt**. Namun komponen seperti panel surya, BESS, inverter biasanya dapat diklasifikasikan sebagai **bahan baku purwarupa** (masuk BLNP) selama merupakan bagian integral dari riset. **Klarifikasi dengan BRIN.**

### 3.2 Bahan Habis Pakai

| Item | Th I | Th II | Satuan |
|------|------|-------|--------|
| Kabel, konektor, MC4, conduit | 3.000.000 | 1.500.000 | |
| Modul komunikasi (RS485/WiFi/4G) | 3.000.000 | 1.000.000 | |
| Enclosure, panel box | 2.000.000 | — | |
| Tools instalasi | 1.500.000 | 500.000 | |
| ATK + cetak | 1.000.000 | 1.000.000 | |
| **Subtotal Bahan** | **10.500.000** | **4.000.000** | |

### 3.3 Cloud & Infrastruktur

| Item | Th I | Th II | Keterangan |
|------|------|-------|------------|
| VPS cloud (4 GB RAM, 60 GB SSD) | 3.240.000 | 3.240.000 | Rp270 rb/bln × 12 |
| Object storage backup | 960.000 | 960.000 | Rp80 rb/bln × 12 |
| Domain + SSL | 500.000 | 500.000 | |
| **Subtotal Cloud** | **4.700.000** | **4.700.000** | |

### 3.4 Perjalanan

| Kegiatan | Th I | Th II | Keterangan |
|----------|------|-------|------------|
| Survei lokasi mitra (Sleman) | 3.000.000 | — | 2 org, 2 hari |
| Instalasi & commissioning | 5.000.000 | 2.000.000 | Tim ke lokasi |
| Monitoring lapangan (4×) | — | 8.000.000 | 2 org × 4 kali |
| Seminar/konferensi | — | 10.000.000 | 1 org, nasional |
| **Subtotal Perjalanan** | **8.000.000** | **20.000.000** | |

### 3.5 Diseminasi & Publikasi

| Item | Th I | Th II | Keterangan |
|------|------|-------|------------|
| Biaya publikasi jurnal Q2 | — | 8.000.000 | OA fee |
| Pendaftaran paten sederhana | 3.500.000 | 3.500.000 | |
| FGD/workshop hasil riset | — | 5.000.000 | |
| **Subtotal Diseminasi** | **3.500.000** | **16.500.000** | |

### 3.6 Lain-lain

| Item | Th I | Th II |
|------|------|-------|
| Konsumsi rapat tim | 2.000.000 | 1.000.000 |
| Dokumentasi & pelaporan | 1.000.000 | 1.000.000 |
| **Subtotal Lain** | **3.000.000** | **2.000.000** |

---

## 4. Biaya Tidak Langsung (BTL)

| Item | Th I | Th II |
|------|------|-------|
| Monitoring & evaluasi institusi (5%) | 12.500.000 | 12.500.000 |

---

## 5. Rekapitulasi — Hasil Optimasi

### RAB Final (Rp — ribuan)

| Komponen | Th I | Th II | 2 Tahun | % |
|----------|------|-------|---------|---|
| **BLP** (Ketua 4 OB + 4 Anggota 4 OB) | 52.800 | 52.800 | 105.600 | 21,9% |
| **BLNP — Ind 1: Pipeline & Platform** | 111.100 | 89.700 | 200.800 | 41,6% |
| • Sewa PV 5,5kWp/BESS 10kWh/inverter 5kW | 50.000 | 55.000 | 105.000 | |
| • Belanja modal instrumentasi | 29.000 | 22.500 | 51.500 | |
| • Bahan purwarupa | 32.100 | 12.200 | 44.300 | |
| **BLNP — Ind 2: AI Software & Testing** | 71.000 | 80.000 | 151.000 | 31,3% |
| • Jasa pengembangan pipeline/EMS/dashboard | 45.000 | 41.000 | 86.000 | |
| • Uji integrasi, lapangan, luaran | 26.000 | 39.000 | 65.000 | |
| **BTL** (Monev & evaluasi) | 12.500 | 12.500 | 25.000 | 5,2% |
| **Total** | **247.400** | **235.000** | **482.400** | 100% |

---

## 6. Item Kritis Perlu Klarifikasi

| No | Pertanyaan | Dampak |
|----|-----------|--------|
| 1 | Apakah honor ketua/anggota tim diizinkan? | BLP bisa 0–176 jt/tahun |
| 2 | Apakah hardware (PV, BESS, inverter) dianggap belanja modal atau bahan baku riset? | Jika modal → max 50 jt total |
| 3 | Berapa pagu maksimal per tahun? | 200, 250, atau 300 jt? |
| 4 | Apakah UNNES PKP atau Non PKP? | Mempengaruhi PPN/PPh |

---

## 7. Tindak Lanjut

1. **Konfirmasi Feddy:** pagu per tahun, apakah honor tim diizinkan
2. **Konsultasi LPPM UNNES:** klasifikasi hardware (modal vs bahan)
3. **Finalisasi RAB** di template xlsx BRIN setelah angka fix
4. **Isi ke Proposal** halaman pendangan (line 48–52 `[DIISI]`)
