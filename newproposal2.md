# NEW PROPOSAL 2 — INTEGRATED CONCEPT
## Sistem IoT-Edge Terintegrasi untuk SPKLU AC 22kW Berbasis Solar Hybrid dan Prediksi Beban Cerdas Menggunakan YOLOv8 dengan Pipeline Anonimisasi

*Integrasi proposal2.md + hybrid-solar-panel.md + bagaskoro-saputro-publications.md + turnad-lenggo-ginta-publications.md*

---

## A. INTISARI INTEGRASI

Proposal ini menggabungkan **IoT-Edge SPKLU AC 22kW** (proposal2) dengan **spesifikasi teknis hybrid off-grid solar panel** (hybrid-solar-panel.md), diperkuat oleh publikasi riset **Bagaskoro Saputro** pada fast charger dan bifacial PV, serta konteks kebijakan energi rendah karbon dari **Turnad Lenggo Ginta** (BRIN).

### Integrasi Kunci:

| Komponen | Dari Proposal2 | Dari hybrid-solar-panel.md | Dari Publikasi |
|----------|---------------|---------------------------|----------------|
| **Sumber Daya** | Grid PLN + Solar Hybrid | PV 4-100 kWp + BESS 48V LFP/NMC | Bifacial PV gain 25-30% (Widiyawati et al., 2026) |
| **MPPT** | Smart load balancing | HHO algorithm 99.53% | HHO outperform P&O, INC, GA (Aprilianto et al., 2025) |
| **DC-DC Charger** | - | IBC 2-phase 20 kHz | IBC PI-FLC 57.75 min (Subiyanto et al., 2026) |
| **Charger Output** | AC 22kW | DC 72V/20A (E2W) + AC 22kW | 1 C rate NMC (Subiyanto et al., 2026) |
| **Edge AI** | YOLOv8 occupancy | - | AMD/Xilinx deployable |
| **EMS** | Load balancing hybrid | Hierarchical PI-FLC 3-level | Microgrid optimization (Syah et al., 2025) |
| **Kebijakan** | UU PDP, Perpres EV | LCOE USD 0.08-0.15/kWh | Low-carbon pathway (Farabi, Ginta et al., 2025) |
| **OCPP Bridge** | WS→MQTT | Modbus/CAN for BMS | - |

---

## B. JUDUL PENELITIAN

**Pengembangan Sistem IoT-Edge Terintegrasi untuk SPKLU AC 22kW Berbasis Solar Hybrid dan Prediksi Beban Cerdas Menggunakan YOLOv8 dengan Pipeline Anonimisasi: Integrasi HHO MPPT, Interleaved Buck Converter, dan Fast Charging untuk Mendukung Ekosistem EV Rendah Karbon di Indonesia**

---

## C. LATAR BELAKANG (Enhanced)

### C.1 Konteks Energi, EV, dan Kebijakan

Indonesia menargetkan 2 juta mobil listrik dan 13 juta motor listrik pada 2030 (Perpres 55/2019, PP 28/2025). Namun, 73% SPKLU dikuasai PLN dengan fokus DC fast charging yang mahal. Charger AC 22kW menawarkan CAPEX terjangkau dan cocok untuk pola parkir 3-4 jam di kampus, kantor, mall, dan hotel.

Farabi, **Ginta** et al. (2025) — "Promoting a Low-carbon Indonesia" — mengkonfirmasi bahwa pengembangan energi dan kebijakan finansial berkontribusi signifikan pada reduksi emisi, memperkuat urgensi investasi infrastruktur charging berbasis energi terbarukan. **DOI:** 10.32479/ijeep.18292

### C.2 Peluang Integrasi Solar Hybrid

Penelitian Ibezim et al. (2026) menunjukkan konfigurasi solar hybrid mencapai **30-50% reduksi kebutuhan baterai** dan **LCOE USD 0.08-0.15/kWh**. Pasar off-grid solar EV charging global bernilai USD 512 juta (2024) menuju USD 2.31 miliar (2033, CAGR 18.4%).

Integrasi solar hybrid pada SPKLU AC 22kW menjawab tiga masalah:
1. **Ketergantungan grid** — solar PV + BESS sebagai sumber mandiri
2. **Biaya operasional** — LCOE 15-25% lebih rendah dari grid-only
3. **Keandalan** — intelligent EMS dengan hierarchical PI-FLC

### C.3 State of the Art dari UNNES Research Group

**Subiyanto et al. (2026)** — High-Performance E2W Fast Charger:
- IBC dengan PI-FLC, charging 0-100% SoC dalam **57.75 menit**
- Ripple cancellation 11.56%, efisiensi >94%
- **DOI:** 10.14313/jamris-2026-030

**Widiyawati, Subiyanto, Syah, Saputro et al. (2026)** — Bifacial PV Ray Tracing:
- Bifacial gain 25-30% rear-side
- Konfigurasi checkerboard 5% lebih tinggi dari tilt 35°
- **DOI:** 10.23960/jtepl.v15i2.510-524

**Aprilianto, Subiyanto, Syah & Nugroho (2025)** — HHO-based MPPT:
- Efisiensi 99.53% pada STC
- **DOI:** 10.1109/ISMEE68179.2025.11473059

---

## D. RUMUSAN MASALAH

1. Bagaimana merancang arsitektur IoT-Edge yang mengintegrasikan OCPP 1.6J, Modbus inverter, MPPT HHO, dan IBC fast charger dalam satu sistem solar hybrid terpadu?
2. Bagaimana mengimplementasikan pipeline edge-AI YOLOv8 dengan anonimisasi real-time untuk prediksi okupansi 15-60 menit (MAPE <15%) tanpa mengirim data biometrik ke cloud?
3. Bagaimana mengintegrasikan hierarchical EMS (PI-FLC) dengan HHO MPPT dan smart load balancing berbasis irradiance, SoC, tarif TOU?
4. Apakah prototipe sistem layak diuji pada skala pilot (TKT 5-6) di 3 lokasi parkir publik dwell-time tinggi?

---

## E. SPESIFIKASI TEKNIS SISTEM INTEGRATED

### E.1 Solar PV Array

| Parameter | Spesifikasi | Sumber |
|-----------|-------------|--------|
| Kapasitas PV | 4-100 kWp (modular) | hybrid-solar-panel.md |
| Tipe modul | Monocrystalline / Bifacial | Widiyawati et al., 2026 |
| Efisiensi modul | ≥ 20% | hybrid-solar-panel.md |
| Bifacial gain | 25-30% rear-side | Widiyawati et al., 2026 |
| MPPT algorithm | Horse Herd Optimization (HHO) | Aprilianto et al., 2025 |
| Efisiensi MPPT | 99.53% | Aprilianto et al., 2025 |

### E.2 Energy Storage System (BESS)

| Parameter | Spesifikasi |
|-----------|-------------|
| Kimia baterai | Lithium NMC / LFP |
| Tegangan nominal | 48 V DC |
| Kapasitas | 10-50 kWh (modular) |
| Efisiensi R/T | ≥ 92% |
| Cycle life | ≥ 4000 cycles pada 80% DoD |
| BMS | CAN/Modbus, thermal monitoring, SoC/SoH estimation |

### E.3 Fast Charger — Interleaved Buck Converter (for E2W)

| Parameter | Spesifikasi | Sumber |
|-----------|-------------|--------|
| Topologi | Two-phase IBC | Subiyanto et al., 2026 |
| Frekuensi switching | 20-50 kHz | Subiyanto et al., 2026 |
| Output voltage | 72 V DC (adjustable) | Subiyanto et al., 2026 |
| Output current | 20 A (1 C rate) | Subiyanto et al., 2026 |
| Charging time | 57.75 min (0-100% SoC) | Subiyanto et al., 2026 |
| Ripple cancellation | < 12% | Subiyanto et al., 2026 |
| Efisiensi | > 94% | Subiyanto et al., 2026 |

### E.4 Hybrid Inverter & AC Charger

| Parameter | Spesifikasi |
|-----------|-------------|
| Daya inverter | 5-15 kW (modular, parallel hingga 150 kW) |
| AC output charger | 22 kW, 3-phase, Type 2 |
| MPPT voltage range | 330-800 V DC |
| UPS switchover | < 10 ms |
| Efisiensi maks | 97.5% |
| Proteksi | IP65, Type II SPD |

### E.5 IoT-Edge Gateway

| Parameter | Spesifikasi |
|-----------|-------------|
| Edge Controller | ESP32 + NVIDIA Jetson / Raspberry Pi 5 |
| Connectivity | WiFi 802.11 b/g/n + 4G LTE Cat-4 (failover) |
| Protocol Bridge | OCPP 1.6J (WebSocket) → MQTT, Modbus RTU/TCP |
| Power metering | ±1% akurasi, real-time kWh |
| Touchscreen | 10" Android, kiosk mode |

### E.6 Edge-AI: YOLOv8 + Anonimisasi Pipeline

| Parameter | Spesifikasi |
|-----------|-------------|
| Model | YOLOv8 (Ultralytics) |
| Task | Vehicle occupancy detection & duration estimation |
| Inferensi | 100% edge (Jetson/RPi 5 via TensorRT/OpenVINO) |
| Latensi | <200ms per frame |
| Anonimisasi | Frame blurring + metadata-only export |
| Storage | Zero raw image/video storage |
| Output | Metadata agregat: count, timestamp, estimated duration |
| Kepatuhan | UU PDP No. 27/2022, Perka BRIN No. 22/2022 |

### E.7 Smart Energy Management System (EMS)

**Three-level hierarchical control:**

| Level | Fungsi | Algoritma | Update Rate |
|-------|--------|-----------|-------------|
| Primary | IBC regulation | PI-FLC | < 1 ms |
| Secondary | Load balancing & SoC mgmt | Rule-based + PI | 1-10 s |
| Tertiary | Scheduling & grid interaction | LSTM/Prophet + TOU | 15-60 min |

**Input EMS:**
- Irradiance solar real-time (pyranometer / PV string sensor)
- SoC baterai (BMS via Modbus)
- Tarif TOU PLN (API/configuration)
- Okupansi terprediksi dari edge-AI (YOLOv8 metadata)

**Output:**
- Set-point daya solar ke grid / battery / charger
- Jadwal switching solar-grid optimal
- Notifikasi prediksi beban puncak ke operator

---

## F. PUBLIKASI RISET TERKAIT

### F.1 Bagaskoro Saputro (UNNES/BINUS) — Kontribusi pada Hardware Fast Charger & PV

1. **Subiyanto, S.**, Aprilianto, R.A., Syah, M.N., **Saputro, B.**, et al. (2026). High-Performance Electric Two-Wheeler Fast Charger Based on Intelligent Control Algorithm. *JAMRIS*, 20(2), 175-184. **DOI:** 10.14313/jamris-2026-030
   → Mendukung modul IBC fast charger (E.3) dan validasi kecepatan charging 57.75 menit.

2. Widiyawati, E., Subiyanto, S., Ridloah, S., Sunarko, B., **Saputro, B.**, et al. (2026). Ray Tracing-Based Modeling of Bifacial Photovoltaic Systems in Greenhouse Agrivoltaics. *JTP Lampung*, 15(2), 510-524. **DOI:** 10.23960/jtepl.v15i2.510-524
   → Mendukung spesifikasi solar PV bifacial (E.1) dengan gain 25-30%.

### F.2 Turnad Lenggo Ginta (BRIN) — Kontribusi pada Kebijakan Energi & Justifikasi

1. Farabi, A., Kurniadi, A.P., Salim, Z., **Ginta, T.L.**, et al. (2025). Promoting a Low-carbon Indonesia: How Energy Consumption and Financial Development Shape its Path. *IJEEP*, 15(5), 114-126. **DOI:** 10.32479/ijeep.18292
   → Mendukung latar belakang kebijakan (C.1) dan justifikasi investasi infrastruktur charging energi terbarukan.

2. Rusli, Jufriadi, Hasannuddin, T., Daud, M., Nurhasnah, S., Fadhil, M., **Ginta, T.L.** (2023). Development of the Renewable Energy-Based Distributed Generation Electricity System at Politeknik Negeri Lhokseumawe. ResearchGate.
   → Mendukung desain distributed generation / microgrid untuk SPKLU hybrid.

---

## G. LUARAN

| No | Luaran | Target |
|----|--------|--------|
| 1 | Prototipe SPKLU AC 22kW + Solar Hybrid + IBC Fast Charger | 3 unit terpasang |
| 2 | CSMS Go + EMQX Gateway, terintegrasi Modbus/CAN | Uptime >99% |
| 3 | Pipeline YOLOv8 anonim (100% edge, zero biometric storage) | MAPE <15%, latency <200ms |
| 4 | Publikasi Ilmiah Internasional Q3 | 2 KTI accepted + 1 under review |
| 5 | Paten Sederhana (IBC + Hybrid EMS + Edge-AI) | 1 paten terdaftar DJKI |
| 6 | Dataset telemetri & metadata anonim | Publik di Zenodo/GitHub |
| 7 | SOP instalasi & maintenance | 1 dokumen teknis |
| 8 | Policy brief interoperabilitas & privasi | 1 policy brief |

---

## H. TKT ROADMAP INTEGRATED

| Periode | Target TKT | Kegiatan Inti | Luaran Utama |
|---------|------------|---------------|--------------|
| **Tahun 1** | 3 → 4 | Desain arsitektur, setup CSMS Go & EMQX, kustomisasi YOLOv8 + anonimisasi, integrasi IBC + HHO MPPT, TimescaleDB + RLS, uji lab (QoS, akurasi billing, failover, efisiensi MPPT) | 1 prototipe lab fungsional, 1 draf Paten, 1 KTI under review (Q3) |
| **Tahun 2** | 5 → 6 | Instalasi 3 unit di mitra, monitoring 3 bulan, validasi switching solar-grid, kalibrasi load balancing HHO-IBC, SOP & SDK rilis | 3 unit terpasang, 1 Paten terdaftar, 2 KTI accepted/under review, 1 SOP + policy brief |

---

## I. DAFTAR PUSTAKA INTEGRATED

1. Subiyanto, S., Aprilianto, R.A., Syah, M.N., Saputro, B., et al. (2026). High-Performance Electric Two-Wheeler Fast Charger. *JAMRIS*, 20(2), 175-184. https://doi.org/10.14313/jamris-2026-030
2. Widiyawati, E., Subiyanto, S., Ridloah, S., Sunarko, B., Saputro, B., et al. (2026). Ray Tracing-Based Modeling of Bifacial PV. *JTP Lampung*, 15(2), 510-524. https://doi.org/10.23960/jtepl.v15i2.510-524
3. Aprilianto, R.A., Subiyanto, Syah, M.N., & Nugroho, D.B. (2025). HHO MPPT for PV-Battery. *IEEE ISMEE 2025*. https://doi.org/10.1109/ISMEE68179.2025.11473059
4. Syah, M.N., Aprilianto, R.A., Suryanto, A., & Al-Azhari, A.H. (2025). Hybrid Renewable Energy Microgrid Design. *IEEE IES 2025*.
5. Syah, M.N., Aprilianto, R.A., & Suryanto, A. (2024). PID Controller Enhancement of IBC. *IEEE ICT-PEP 2024*.
6. Aprilianto, R.A., Syah, M.N., & Suryanto, A. (2024). Novel High Gain Modified SEPIC Converter. *IEEE ICT-PEP 2024*.
7. Farabi, A., Ginta, T.L., et al. (2025). Promoting a Low-carbon Indonesia. *IJEEP*, 15(5), 114-126. https://doi.org/10.32479/ijeep.18292
8. Ibezim, O., Prasad, K., & Kilby, J. (2026). Intelligent Hybrid Solar–Wind Off-Grid EV Charging Stations. *Electronics*, 15(11), 2253. https://doi.org/10.3390/electronics15112253
9. Singla, P., Boora, S., & Singhal, P. (2024). Design and Simulation of 4 kW Solar Power-Based Hybrid EV Charging Station. *Scientific Reports*, 14, 7336. https://doi.org/10.1038/s41598-024-56833-5
10. Erdemir, D., & Dincer, I. (2023). Solar-Driven Charging Station with Liquid CO2 Storage. *Journal of Energy Storage*, 73(C), 109080. https://doi.org/10.1016/j.est.2023.109080
11. He, L., & Wu, Z. (2024). Hybrid Solar-Wind Fast Charging Station with Demand Response. *Renewable Energy*, 237(C), 121843. https://doi.org/10.1016/j.renene.2024.121843
12. Open Charge Alliance. (2022). *OCPP 1.6J specification*. https://openchargealliance.org
13. Jocher, G., et al. (2023). *Ultralytics YOLOv8*. https://github.com/ultralytics/ultralytics
14. Peraturan Pemerintah No. 28 Tahun 2025.
15. Undang-Undang No. 27 Tahun 2022 tentang Perlindungan Data Pribadi.

---

*Dokumen ini merupakan integrasi dari proposal2.md (IoT-Edge SPKLU AC 22kW + YOLOv8), hybrid-solar-panel.md (technical spec off-grid solar), bagaskoro-saputro-publications.md, dan turnad-lenggo-ginta-publications.md — diformat ulang sebagai konsep terpadu untuk proposal RIIM/BRIN.*
