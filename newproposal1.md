# NEW PROPOSAL 1 — INTEGRATED CONCEPT
## Hybrid Off-Grid Solar-Powered SPKLU Cerdas Berbasis IoT Terintegrasi MyPLN

*Integrasi proposal1.md + hybrid-solar-panel.md + bagaskoro-saputro-publications.md + turnad-lenggo-ginta-publications.md*

---

## A. INTISARI INTEGRASI

Proposal ini menggabungkan konsep **SPKLU Cerdas Berbasis IoT** (proposal1) dengan **spesifikasi teknis hybrid off-grid solar panel** (hybrid-solar-panel.md), diperkuat oleh publikasi riset **Bagaskoro Saputro** (UNNES/BINUS) pada fast charger E2W dan bifacial PV, serta konteks kebijakan energi rendah karbon dari **Turnad Lenggo Ginta** (BRIN).

### Integrasi Kunci:

| Komponen | Dari Proposal1 | Dari hybrid-solar-panel.md | Dari Publikasi |
|----------|---------------|---------------------------|----------------|
| **Sumber Daya** | Grid PLN | Solar PV 4-100 kWp + BESS | Bifacial PV gain 25-30% (Widiyawati et al., 2026) |
| **DC-DC Converter** | - | Interleaved Buck Converter 2-phase | IBC PI-FLC 57.75 min charging (Subiyanto et al., 2026) |
| **MPPT** | - | HHO algorithm 99.53% efisiensi | HHO outperforms P&O, INC, GA (Aprilianto et al., 2025) |
| **Charger Output** | 4.4 kW AC | 72V/20A DC fast charge | 1 C rate, NMC battery (Subiyanto et al., 2026) |
| **Connectivity** | WiFi + 4G, OCPP, MQTT | CAN/Modbus untuk BMS | - |
| **EMS** | Smart charging scheduling | Hierarchical PI-FLC + load balancing | Microgrid optimization (Syah et al., 2025) |
| **Kebijakan** | Target EV nasional | LCOE USD 0.08-0.15/kWh | Low-carbon pathway Indonesia (Farabi, Ginta et al., 2025) |

---

## B. JUDUL PENELITIAN

**Pengembangan Hybrid Off-Grid Solar-Powered SPKLU Cerdas Berbasis IoT dengan Fast Charging Interleaved Buck Converter dan Integrasi MyPLN untuk Mendukung Ekosistem Kendaraan Listrik di Indonesia**

---

## C. LATAR BELAKANG (Enhanced)

### C.1 Konteks Energi dan Transportasi

Indonesia berkomitmen menurunkan emisi GRK 29-41% pada 2030 (Perpres 55/2019). Sektor transportasi menyumbang 24% emisi CO2 global. Target 2 juta mobil listrik dan 13 juta motor listrik pada 2030 membutuhkan infrastruktur charging yang masif. Namun, 78% SPKLU terkonsentrasi di Jawa dengan rasio 1:150 terhadap kendaraan listrik.

### C.2 Peluang Solar Hybrid

Penelitian terbaru (Ibezim et al., 2026) menunjukkan konfigurasi solar hybrid mencapai **30-50% reduksi kebutuhan baterai** dan **LCOE USD 0.08-0.15/kWh** — 15-25% lebih rendah dibanding sistem single-source. Pasar off-grid solar EV charging global bernilai USD 512 juta (2024) dan diproyeksikan mencapai USD 2.31 miliar pada 2033 (CAGR 18.4%).

Integrasi solar hybrid pada SPKLU menjawab tiga masalah sekaligus:
1. **Ketergantungan grid** — dikurangi dengan sumber energi mandiri
2. **Biaya operasional** — diturunkan dengan LCOE kompetitif
3. **Keandalan** — ditingkatkan dengan BESS dan intelligent EMS

### C.3 State of the Art dari UNNES Research Group

**Subiyanto et al. (2026)** — High-Performance Electric Two-Wheeler Fast Charger Based on Intelligent Control Algorithm:
- Interleaved Buck Converter (IBC) dengan PI-FLC
- Charging 0-100% SoC dalam **57.75 menit** (vs PID CC-CV: 180 menit)
- Ripple cancellation 11.56%, efisiensi >94%
- **DOI:** 10.14313/jamris-2026-030

**Widiyawati, Subiyanto, Syah, Saputro et al. (2026)** — Ray Tracing-Based Modeling of Bifacial PV:
- Bifacial PV gain 25-30% rear-side energy capture
- Konfigurasi checkerboard 5% lebih tinggi dari tilt 35°
- **DOI:** 10.23960/jtepl.v15i2.510-524

**Aprilianto, Subiyanto, Syah & Nugroho (2025)** — HHO-based MPPT:
- Efisiensi 99.53% pada STC, outperform P&O, INC, GA
- **DOI:** 10.1109/ISMEE68179.2025.11473059

### C.4 Konteks Kebijakan Energi

Farabi, **Ginta** et al. (2025) dalam "Promoting a Low-carbon Indonesia" mengkonfirmasi bahwa pengembangan energi dan kebijakan finansial berkontribusi signifikan pada reduksi emisi di Indonesia, memperkuat justifikasi investasi infrastruktur charging berbasis energi terbarukan.
**DOI:** 10.32479/ijeep.18292

---

## D. RUMUSAN MASALAH

1. Bagaimana merancang SPKLU hybrid yang mengintegrasikan solar PV (4-100 kWp), BESS, IBC fast charger, dan konektivitas IoT dalam satu sistem terpadu?
2. Bagaimana mengimplementasikan MPPT berbasis HHO (99.53% efisiensi) dan IBC PI-FLC (57.75 menit fast charging) pada SPKLU komersial?
3. Bagaimana mengintegrasikan sistem dengan MyPLN untuk autentikasi, pembayaran, dan manajemen energi real-time?
4. Bagaimana memvalidasi performa sistem di lokasi parkir publik dwell-time tinggi dengan skema bisnis dual revenue?

---

## E. SPESIFIKASI TEKNIS SISTEM INTEGRATED

### E.1 Solar PV Array

| Parameter | Spesifikasi |
|-----------|-------------|
| Kapasitas PV | 4-100 kWp (modular, scalable) |
| Tipe modul | Monocrystalline / Bifacial |
| Efisiensi modul | ≥ 20% |
| Bifacial gain | 25-30% rear-side (Widiyawati et al., 2026) |
| MPPT algorithm | Horse Herd Optimization (HHO) |
| Efisiensi MPPT | 99.53% (Aprilianto et al., 2025) |

### E.2 Energy Storage System (BESS)

| Parameter | Spesifikasi |
|-----------|-------------|
| Kimia baterai | Lithium NMC / LFP |
| Tegangan nominal | 48 V DC (400 V DC untuk fast charging) |
| Efisiensi R/T | ≥ 92% |
| Cycle life | ≥ 4000 cycles pada 80% DoD |
| BMS | CAN/Modbus, thermal monitoring, SoC/SoH estimation |

### E.3 Fast Charger — Interleaved Buck Converter

| Parameter | Spesifikasi | Sumber |
|-----------|-------------|--------|
| Topologi | Two-phase IBC | Subiyanto et al. (2026) |
| Frekuensi switching | 20-50 kHz | Subiyanto et al. (2026) |
| Output voltage | 72 V DC (adjustable) | Subiyanto et al. (2026) |
| Output current | 20 A (1 C rate) | Subiyanto et al. (2026) |
| Charging time | 57.75 min (0-100% SoC) | Subiyanto et al. (2026) |
| Ripple cancellation | < 12% | Subiyanto et al. (2026) |
| Efisiensi | > 94% | Subiyanto et al. (2026) |

### E.4 Hybrid Inverter

| Parameter | Spesifikasi |
|-----------|-------------|
| Daya | 5-15 kW (modular, parallel hingga 150 kW) |
| MPPT voltage range | 330-800 V DC |
| AC output | 220/380 V, 3-phase |
| UPS switchover | < 10 ms |
| Efisiensi maks | 97.5% |
| Proteksi | IP65, Type II SPD |

### E.5 IoT & Connectivity

| Parameter | Spesifikasi |
|-----------|-------------|
| Controller | ESP32 + Edge AI (Jetson/RPi 5) |
| Connectivity | WiFi 802.11 b/g/n + 4G LTE Cat-4 (failover) |
| Protocol | OCPP 1.6J, MQTT, Modbus |
| Power metering | Akurasi ±1%, real-time |
| Tablet | 10" Android, kiosk mode |

### E.6 Smart Energy Management System (EMS)

Three-level hierarchical control:
1. **Primary:** PI-FLC untuk IBC regulation
2. **Secondary:** Load balancing dan SoC management
3. **Tertiary:** Scheduling optimasi dan grid interaction

Dengan prediksi beban 15-60 menit menggunakan algoritma hybrid (LSTM/Prophet) yang mempertimbangkan:
- Irradiance solar real-time
- SoC baterai
- Tarif TOU PLN
- Okupansi terprediksi dari edge AI

---

## F. PUBLIKASI RISET TERKAIT

### F.1 Bagaskoro Saputro (UNNES/BINUS)

1. **Subiyanto, S.**, Aprilianto, R.A., Syah, M.N., **Saputro, B.**, et al. (2026). High-Performance Electric Two-Wheeler Fast Charger Based on Intelligent Control Algorithm. *JAMRIS*, 20(2), 175-184. **DOI:** 10.14313/jamris-2026-030

2. Widiyawati, E., Subiyanto, S., Ridloah, S., Sunarko, B., **Saputro, B.**, et al. (2026). Ray Tracing-Based Modeling of Bifacial Photovoltaic Systems in Greenhouse Agrivoltaics. *JTP Lampung*, 15(2), 510-524. **DOI:** 10.23960/jtepl.v15i2.510-524

### F.2 Turnad Lenggo Ginta (BRIN)

1. Farabi, A., Kurniadi, A.P., Salim, Z., **Ginta, T.L.**, et al. (2025). Promoting a Low-carbon Indonesia: How Energy Consumption and Financial Development Shape its Path. *IJEEP*, 15(5), 114-126. **DOI:** 10.32479/ijeep.18292

2. Rusli, Jufriadi, Hasannuddin, T., Daud, M., Nurhasnah, S., Fadhil, M., **Ginta, T.L.** (2023). Development of the Renewable Energy-Based Distributed Generation Electricity System at Politeknik Negeri Lhokseumawe. ResearchGate.

---

## G. LUARAN

| No | Luaran | Target |
|----|--------|--------|
| 1 | Prototipe SPKLU Solar Hybrid + IBC Fast Charger | 10 unit |
| 2 | Sistem Backend & Cloud terintegrasi MyPLN | Uptime >99% |
| 3 | Publikasi Ilmiah Internasional Q1-Q3 | 2 artikel |
| 4 | Paten Sederhana (IBC + Hybrid EMS) | 2 paten |
| 5 | Pilot Project di 3 lokasi | Terpasang & operasional |
| 6 | Dataset telemetri teranonimisasi | Publik di Zenodo/GitHub |

---

## H. DAFTAR PUSTAKA INTEGRATED

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

---

*Dokumen ini merupakan integrasi dari proposal1.md (IoT SPKLU MyPLN), hybrid-solar-panel.md (technical spec off-grid solar), bagaskoro-saputro-publications.md, dan turnad-lenggo-ginta-publications.md — diformat ulang sebagai konsep terpadu untuk proposal RIIM/BRIN.*
