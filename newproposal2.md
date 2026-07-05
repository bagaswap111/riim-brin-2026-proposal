# PROPOSAL RIIM KOMPETISI 2026
**FOKUS RISET:** Elektronika dan Informatika / Energi
**JUDUL:** Pengembangan Sistem IoT-Edge Terintegrasi untuk SPKLU AC 22kW Berbasis Solar Hybrid dan Prediksi Beban Cerdas Menggunakan YOLOv8 dengan Pipeline Anonimisasi: Integrasi HHO MPPT, Interleaved Buck Converter, dan Fast Charging untuk Mendukung Ekosistem EV Rendah Karbon di Indonesia

**KETUA PERISET:** Prof. Dr. Subiyanto
**ANGGOTA PERISET:**
1. Bagaskoro Saputro, S.Kom., M.Kom. — Ilmu Komputer / IoT dan Sistem Cerdas (BINUS University)
2. Mario Norman Syah, S.T., M.T. — Teknik Elektro / Power Electronics dan Konversi Energi
3. Adhe Lingga Dewi, S.Si., M.Si. — Ilmu Komputer / IoT dan Sensor
4. Dr. Turnad Lenggo Ginta — Teknik Mesin / Kebijakan Energi

**NAMA UNIT KERJA – INSTANSI PENGUSUL:** Universitas Negeri Semarang (UNNES)
**BADAN RISET DAN INOVASI NASIONAL**
**TAHUN 2026**

---

## HALAMAN PENGESAHAN
**PROPOSAL PENDANAAN RIIM KOMPETISI**
1. **Judul Proposal** : Pengembangan Sistem IoT-Edge Terintegrasi untuk SPKLU AC 22kW Berbasis Solar Hybrid dan Prediksi Beban Cerdas Menggunakan YOLOv8 dengan Pipeline Anonimisasi: Integrasi HHO MPPT, Interleaved Buck Converter, dan Fast Charging untuk Mendukung Ekosistem EV Rendah Karbon di Indonesia
2. **Ketua Periset** :
   a. Nama Lengkap : Prof. Dr. Subiyanto
   b. Jenis Kelamin : [L/P]
   c. NIP/NIK/KTP : [NIP Ketua]
   d. Jabatan Struktural : [Jabatan]
   e. Jabatan Fungsional : Guru Besar/Profesor
   f. Institusi Periset : Universitas Negeri Semarang (UNNES)
   g. Alamat : Jl. Sekaran, Gunungpati, Semarang 50229
   h. HP/Telepon/Faks : [No. Telp/HP]
   i. Alamat Rumah : [Alamat Rumah]
   j. Telpon/Faks/Email : [Email Institusi]
3. **Mitra Riset** : [Mitra: Pengelola Kampus/Mall/PLN UID/Startup EV]
   **Anggota Riset**
   | No | Nama | NIP/NIK | Asal Institusi |
   |---|---|---|---|
   | 1 | Bagaskoro Saputro, S.Kom., M.Kom. | [NIK] | BINUS University |
   | 2 | Mario Norman Syah, S.T., M.T. | [NIK] | UNNES |
   | 3 | Adhe Lingga Dewi, S.Si., M.Si. | [NIK] | BINUS University |
   | 4 | Dr. Turnad Lenggo Ginta | [NIP] | BRIN / OR Energi |
4. **Pendanaan** :
   | No | Uraian | BRIN/LPDP (Tahun 1) | BRIN/LPDP (Tahun 2) | Sharing Mitra (Tahun 1) | Sharing Mitra (Tahun 2) | Total |
   |---|---|---|---|---|---|---|
   | 1 | Periode/Tahun 1 | Rp [...] | - | Rp [...] | - | Rp [...] |
   | 2 | Periode/Tahun 2 | Rp [...] | Rp [...] | Rp [...] | Rp [...] | Rp [...] |

**Menyetujui, Pimpinan Institusi Pengusul,** | **Tempat, dd-mm-yy Ketua Periset,**
---|---

---

## ABSTRAK
Penelitian ini mengembangkan prototipe sistem manajemen SPKLU AC 22kW berbasis arsitektur IoT-Edge terintegrasi untuk lokasi parkir publik dwell-time tinggi (kampus, kantor, mall, hotel), dengan integrasi solar hybrid dan HHO MPPT. Permasalahan strategis yang diangkat adalah ketergantungan grid PLN, fragmentasi vendor, ketiadaan prediksi okupansi yang patuh privasi, serta belum adanya integrasi IBC fast charger dengan edge-AI untuk prediksi beban. Solusi mencakup: (1) CSMS terbuka dengan bridge OCPP 1.6J dan Modbus ke MQTT, (2) Edge-AI YOLOv8 untuk deteksi okupansi dengan anonimisasi real-time (frame blurring + metadata-only, kepatuhan UU PDP), (3) integrasi solar hybrid dengan MPPT HHO (99.53% efisiensi) dan IBC PI-FLC (57.75 menit fast charging E2W), (4) smart EMS tiga-level dengan prediksi ANN/LSTM 15-60 menit, dan (5) pipeline AI diproses 100% di edge device tanpa mengirim data biometrik ke cloud. Penelitian diperkuat oleh track record tim: IBC fast charger (Subiyanto et al., 2026), bifacial PV (Widiyawati et al., 2026), HHO MPPT (Aprilianto et al., 2025), IoT multi-sensor ESP32 (Dewi et al., 2024), kalibrasi sensor (Dewi et al., 2025), dan kebijakan low-carbon (Farabi, Ginta et al., 2025). Target: TKT 3→6, 3 unit pilot, 2 KTI Q3, 1 paten, dataset publik.
**Kata Kunci:** SPKLU, AC 22kW, OCPP 1.6J, MQTT, YOLOv8, Edge AI, Solar Hybrid, HHO MPPT, IBC, ANN, UU PDP, TKT 3-6

---

## PENDAHULUAN

### 1. Latar Belakang
Indonesia menargetkan 2 juta mobil listrik dan 13 juta motor listrik pada 2030 (Perpres 55/2019, PP 28/2025). Namun, 73% SPKLU dikuasai PLN dengan fokus DC fast charging yang mahal. Charger AC 22kW menawarkan CAPEX terjangkau dan cocok untuk pola parkir 3-4 jam. Tiga hambatan utama: (1) ketergantungan penuh pada grid, (2) ekosistem vendor tertutup (vendor lock-in), (3) ketiadaan prediksi okupansi yang patuh privasi.

Penelitian Ibezim et al. (2026) menunjukkan konfigurasi solar hybrid mencapai 30-50% reduksi kebutuhan baterai dan LCOE USD 0.08-0.15/kWh. Dari sisi kebijakan, Farabi, Ginta et al. (2025) mengkonfirmasi kontribusi pengembangan energi pada reduksi emisi Indonesia.

Tim periset UNNES memiliki rekam jejak terdepan: Subiyanto et al. (2026) — IBC PI-FLC fast charger 57.75 menit; Widiyawati et al. (2026) — bifacial PV gain 25-30%; Aprilianto et al. (2025) — HHO MPPT 99.53%. Dari sisi IoT, Dewi et al. (2024) telah membangun sistem monitoring udara berbasis ESP32 multi-sensor dengan cloud platform (cited 22), serta studi kalibrasi sensor MQ (Dewi et al., 2025) dan ANN untuk prediksi time-series (Dewi et al., 2024) — membuktikan kapabilitas dalam pengembangan IoT gateway, validasi sensor, dan model prediktif.

### 2. Rumusan Masalah dan Hipotesis Solusi
**Rumusan Masalah:**
(1) Bagaimana merancang arsitektur IoT-Edge yang mengintegrasikan OCPP 1.6J, Modbus inverter, MPPT HHO, dan IBC fast charger dalam satu sistem solar hybrid?
(2) Bagaimana mengimplementasikan pipeline edge-AI YOLOv8 dengan anonimisasi real-time untuk prediksi okupansi 15-60 menit (MAPE <15%) tanpa mengirim data biometrik ke cloud, serta menjamin kepatuhan UU PDP No. 27/2022?
(3) Bagaimana mengintegrasikan hierarchical EMS tiga-level (PI-FLC + ANN/LSTM) dengan HHO MPPT dan smart load balancing berbasis irradiance, SoC, tarif TOU?
(4) Apakah prototipe sistem layak diuji pada skala pilot TKT 5-6 di 3 lokasi parkir publik dwell-time tinggi?

**Hipotesis Solusi:**
Arsitektur modular edge gateway dengan pola `OCPP/Modbus → MQTT Bridge` + YOLOv8 anonimisasi real-time akan menurunkan latensi <200ms, MAPE <15%, utilisasi solar ≥35%, dan strain puncak grid ≥20%. Integrasi IBC PI-FLC + MPPT HHO memberikan efisiensi charging >94% dan MPPT >99%. Pipeline edge 100% lokal menjamin zero biometric storage.

### 3. State of the Art dan Kebaruan
CSMS komersial masih tertutup dengan biaya lisensi tinggi dan bersifat reaktif. Penggunaan kamera untuk prediksi di ruang publik terkendala regulasi privasi. MPPT konvensional (P&O/INC) <95% efisiensi. Charger E2W konvensional membutuhkan 180 menit untuk full charge.

Kebaruan penelitian:
1. **IBC PI-FLC Fast Charger** — 57.75 menit, ripple <12%, efisiensi >94% (Subiyanto et al., 2026)
2. **MPPT HHO** — 99.53% efisiensi (Aprilianto et al., 2025)
3. **Solar PV Bifacial** — 25-30% rear gain (Widiyawati et al., 2026)
4. **Privacy-by-Design Edge Vision** — YOLOv8 + anonimisasi real-time, metadata-only, zero biometric storage/transmission
5. **IoT-ESP32 Multi-sensor Gateway** — Berbasis pengalaman monitoring udara IoT (Dewi et al., 2024, cited 22)
6. **Sensor Calibration Methodology** — Validasi akurasi sensor untuk metering SPKLU (Dewi et al., 2025)
7. **Predictive EMS with ANN** — Prediksi beban 15-60 menit menggunakan ANN/LSTM, didukung studi komparasi fungsi ANN (Dewi et al., 2024)
8. **Bridge OCPP-WS → MQTT** untuk charger AC 22kW yang tidak mendukung native MQTT

### 4. Tujuan dan Sasaran Riset
**Tujuan Umum:** Mengembangkan prototipe CSMS interoperabel berbasis OCPP-MQTT + Edge-AI YOLOv8 untuk charger AC 22kW hybrid off-grid yang patuh privasi.

**Tujuan Khusus:**
(1) Menguji akurasi metering, stabilitas koneksi, performa load balancing, dan keamanan data di lab & lapangan
(2) Memvalidasi pipeline AI edge terhadap akurasi prediksi, latensi inferensi, dan audit kepatuhan PDP
(3) Mengintegrasikan IBC PI-FLC, MPPT HHO, dan solar hybrid dalam satu platform IoT-Edge
(4) Menyusun SOP, API terbuka, dan blueprint operasional untuk hilirisasi

**Sasaran:** TKT 3→6 dalam 2 tahun, 2 KTI Q3, 1 Paten terdaftar, 3 unit pilot.

---

## PETA JALAN DAN NILAI STRATEGIS
| Periode | Target TKT | Kegiatan Inti | Luaran Utama |
|---------|------------|---------------|--------------|
| **Tahun 1 (2026)** | 3 → 4 | Desain arsitektur, CSMS Go & EMQX, YOLOv8 + anonimisasi, integrasi IBC + HHO MPPT, setup TimescaleDB + RLS, uji lab (QoS, akurasi billing, efisiensi MPPT/IBC) | 1 prototipe lab, 1 draf Paten, 1 KTI under review (Q3) |
| **Tahun 2 (2027)** | 5 → 6 | Instalasi 3 unit mitra, monitoring 3 bulan, validasi switching solar-grid, kalibrasi load balancing, SOP & SDK rilis | 3 unit terpasang, 1 Paten terdaftar, 2 KTI accepted/under review, 1 SOP + policy brief |

**Nilai Strategis:** Riset menjawab kebutuhan SPKLU terjangkau, interoperabel, dan ramah grid. Integrasi solar hybrid + HHO MPPT + IBC menurunkan ketergantungan grid dan waktu charging. Edge-AI anonim membuka standar etis baru untuk IoT publik. Pipeline privacy-by-design menjadi referensi nasional kepatuhan UU PDP.

---

## METODOLOGI
Pendekatan: Research & Development Iteratif dengan validasi teknis dan uji lapangan terbatas.

**Work Packages (WP):**
- **WP1 Arsitektur & Backend:** CSMS Go, EMQX WS→MQTT, PostgreSQL/TimescaleDB/Redis, RLS & TOTP 2FA
- **WP2 Edge-AI & Anonimisasi:** YOLOv8 untuk deteksi okupansi, pipeline anonymisasi real-time (frame blurring, metadata-only), optimasi TensorRT/OpenVINO pada Jetson/RPi 5
- **WP3 Integrasi Solar Hybrid + IBC + MPPT:** PV array 4-100 kWp bifacial, BESS LFP/NMC, IBC two-phase PI-FLC, MPPT HHO, hierarchical EMS tiga-level dengan ANN/LSTM untuk prediksi 15-60 menit
- **WP4 Validasi Lab:** QoS 0/1/2, akurasi MeterValues, failover, uji beban 50 charger, audit keamanan & PDP, validasi kalibrasi sensor (metodologi Dewi et al., 2025)
- **WP5 Pilot & Evaluasi:** Instalasi 3 unit mitra, monitoring real-time, kalibrasi revenue-share, SOP, diseminasi

**Detail Metodologi Tahun 1:** Fokus desain arsitektur, firmware gateway, integrasi IBC-MPPT-YOLOv8, validasi lab. Data simulator OCPP, energy logger, log inferensi edge. Analisis: compliance OCPP 1.6J, packet loss/latency, MAPE prediksi, audit privasi, efisiensi konverter, efisiensi MPPT.

**Teknik Pengumpulan Data:** Telemetri charger, log inverter solar, metadata okupansi anonim, log inferensi edge.
**Teknik Analisis:** MAPE <15%, latency <200ms, akurasi kWh ±1%, uptime ≥95%, efisiensi IBC >94%, MPPT >99%, verifikasi zero raw-image storage.

---

## JANGKA WAKTU PELAKSANAAN RISET
24 bulan (2 tahun), terbagi dalam 2 periode evaluasi tahunan.

---

## LUARAN DAN INDIKATOR KINERJA
| Luaran | Status Luaran Tahun 1 | Status Luaran Tahun 2 |
|--------|----------------------|----------------------|
| Jurnal Internasional (min. Q3) | 1 KTI under review | 1 KTI accepted + 1 KTI under review |
| Kekayaan Intelektual | 1 draf Paten Sederhana (IBC + Hybrid EMS + Edge-AI) | 1 Paten Sederhana terdaftar di DJKI |
| Prototipe | TKT 4 (fungsional di lab) | TKT 6 (terpasang & beroperasi di 3 lokasi mitra) |

**Indikator Kinerja Kegiatan Tahun 1:**
| No | Indikator | Target |
|----|-----------|--------|
| 1 | KTI | 100% — 1 naskah jurnal Q3 under review (arsitektur OCPP-MQTT bridge + YOLOv8 anonim + IBC-HHO) |
| 2 | KI | 100% — 1 draf klaim Paten Sederhana (metode prediksi beban berbasis okupansi edge + IBC + EMS) |

**Indikator Kinerja Kegiatan Tahun 2:**
| No | Indikator | Target |
|----|-----------|--------|
| 1 | KTI | 100% — 1 accepted (validasi pilot) + 1 under review (optimasi hybrid load balancing) |
| 2 | KI | 100% — 1 Paten terdaftar, 1 SOP instalasi & maintenance, 1 policy brief interoperabilitas & privasi |

---

## JADWAL KEGIATAN
**TAHUN/PERIODE 1**
| No | Aktivitas | Deskripsi | Waktu |
|----|-----------|-----------|-------|
| 1 | Desain Arsitektur & Setup Infrastruktur | CSMS Go, EMQX, DB schema, algoritma hybrid load balancing, desain IBC + MPPT HHO | Bulan ke-1–3 |
| 2 | Integrasi Multi-Protokol & IBC-MPPT | Bridge OCPP-WS & Modbus→MQTT, simulator, uji IBC (ripple, efisiensi), uji MPPT HHO | Bulan ke-4–6 |
| 3 | Pengembangan Edge-AI & Anonimisasi | YOLOv8, pipeline metadata-only, optimasi TensorRT/OpenVINO, integrasi kamera | Bulan ke-5–7 |
| 4 | Smart EMS & Prediksi ANN/LSTM | Hierarchical EMS tiga-level, ANN/LSTM prediksi 15-60 menit, load balancing | Bulan ke-6–8 |
| 5 | Validasi Lab & Kalibrasi | QoS, akurasi billing, beban 50 charger, audit PDP, validasi kalibrasi sensor | Bulan ke-9–11 |
| 6 | Publikasi & Paten Tahun 1 | KTI, draf paten, audit internal | Bulan ke-10–12 |

**TAHUN/PERIODE 2**
| No | Aktivitas | Deskripsi | Waktu |
|----|-----------|-----------|-------|
| 1 | Persiapan Pilot & MoU Mitra | Koordinasi lokasi, instalasi listrik & panel surya, provisioning charger | Bulan ke-1–2 |
| 2 | Instalasi & Pilot Lapangan | 3 unit, monitoring 3 bulan, kalibrasi billing & switching solar-grid | Bulan ke-3–8 |
| 3 | Evaluasi, SOP & Diseminasi | Analisis utilisasi, SOP, SDK, policy brief, publikasi jurnal | Bulan ke-9–12 |

---

## ANGGARAN
*(Struktur mengikuti Sublampiran IV RIIM. Semua komponen patuh ketentuan: ≤10% modal, tanpa honor tim, tanpa APC jurnal, fokus bahan/uji/lapangan)*

| Komponen Biaya | Indikator Kinerja | Volume | Frekuensi | Harga Satuan (Rp) | Satuan | Jumlah | LPDP | Mitra |
|---------------|-------------------|--------|-----------|-------------------|--------|--------|------|-------|
| **A. Pengadaan Bahan** | | | | | | | | |
| A.1 Prototipe & Pengembangan | Prototipe lab TKT 4 | | | | | | | |
| 1. Panel Surya Bifacial 500Wp + Inverter Hybrid | Integrasi solar hybrid | 4 | 1 | [Harga] | unit | [Isi] | 100% | 0% |
| 2. BESS LFP 48V 100Ah + BMS | Energy storage | 2 | 1 | [Harga] | set | [Isi] | 100% | 0% |
| 3. NVIDIA Jetson / Raspberry Pi 5 + Kamera | Edge-AI YOLOv8 | 3 | 1 | [Harga] | set | [Isi] | 100% | 0% |
| 4. ESP32 Dev Kit + Sensor PZEM-004T + DHT11 | IoT gateway & metering | 5 | 1 | [Harga] | set | [Isi] | 100% | 0% |
| 5. Komponen IBC (Mosfet, Induktor, Driver) | Fast charger | 3 | 1 | [Harga] | set | [Isi] | 100% | 0% |
| 6. Enclosure IP65 + Kabel Power | Integrasi fisik | 3 | 1 | [Harga] | paket | [Isi] | 100% | 0% |
| **Sub Total A.1** | | | | | | | **[Isi]** | **0%** |
| A.2 Pengujian & Validasi | Laporan uji | | | | | | | |
| 1. Sewa Cloud Server (Fly.io/Supabase/EMQX) | Hosting CSMS & time-series | 12 | 1 | [Harga] | bulan | [Isi] | 100% | 0% |
| 2. Sewa Simulator OCPP & Energy Logger | Validasi protokol & metering | 6 | 1 | [Harga] | bulan | [Isi] | 100% | 0% |
| **Sub Total A.2** | | | | | | | **[Isi]** | **0%** |
| **Sub Total A** | | | | | | | **[Isi]** | **0%** |
| **B. Honor Tenaga Lapangan** | Instalasi & monitoring | 72 | 1 | 150.000 | OH | [Isi] | 100% | 0% |
| **Sub Total B** | | | | | | | **[Isi]** | **0%** |
| **C. Perjalanan Dinas** | Validasi lapangan | | | | | | | |
| 1. Transportasi & Akomodasi (Semarang–Mitra) | Uji konektivitas & instalasi | 9 | 2 | [SBM] | trip | [Isi] | 100% | 0% |
| 2. Uang Harian Perjalanan | Kegiatan lapangan | 18 | 2 | [SBM] | OH | [Isi] | 100% | 0% |
| **Sub Total C** | | | | | | | **[Isi]** | **0%** |
| **TOTAL BIAYA TAHUN 1** | | | | | | **[Isi]** | **100%** | **0%** |

*(Tahun 2 mengikuti struktur serupa dengan penyesuaian volume pilot & publikasi)*

---

## DAFTAR PUSTAKA
1. Subiyanto, S., Aprilianto, R.A., Syah, M.N., Saputro, B., et al. (2026). High-Performance Electric Two-Wheeler Fast Charger Based on Intelligent Control Algorithm. *JAMRIS*, 20(2), 175-184. https://doi.org/10.14313/jamris-2026-030
2. Widiyawati, E., Subiyanto, S., Ridloah, S., Sunarko, B., Saputro, B., et al. (2026). Ray Tracing-Based Modeling of Bifacial Photovoltaic Systems in Greenhouse Agrivoltaics. *JTP Lampung*, 15(2), 510-524. https://doi.org/10.23960/jtepl.v15i2.510-524
3. Aprilianto, R.A., Subiyanto, Syah, M.N., & Nugroho, D.B. (2025). HHO MPPT for PV-Battery Systems Under Partial Shading Conditions. *IEEE ISMEE 2025*. https://doi.org/10.1109/ISMEE68179.2025.11473059
4. Easterline, L.M., Putri, A.A.-Z.R., Atmaja, P.S., Dewi, A.L., & Prasetyo, A. (2024). Smart Air Monitoring with IoT-based MQ-2, MQ-7, MQ-8, and MQ-135 Sensors using NodeMCU ESP32. *Procedia Computer Science*, 245, 815-824. https://doi.org/10.1016/j.procs.2024.10.308
5. Dewi, A.L., Adi, C.G.S., & Prasetyo, A. (2025). Datsheet-based Calibration Study of the MQ-135 Sensors for Carbon Dioxide (CO2) and MQ-8 Sensors for Hydrogen (H2). *Engineering Research Express*. https://doi.org/10.1088/2631-8695/adbcc6
6. Dewi, A.L., Adi, C.G.S., Prasetyo, A., & Sari, R.K. (2024). Comparison of Training Function, Adaption Learning Function, and Transfer Function of Hidden Layers in Artificial Neural Network in Weather Prediction. *Proc. ICIMTech 2024*.
7. Farabi, A., Kurniadi, A.P., Salim, Z., Ginta, T.L., et al. (2025). Promoting a Low-carbon Indonesia: How Energy Consumption and Financial Development Shape its Path. *IJEEP*, 15(5), 114-126. https://doi.org/10.32479/ijeep.18292
8. Syah, M.N., Aprilianto, R.A., Suryanto, A., & Al-Azhari, A.H. (2025). Hybrid Renewable Energy Microgrid Design with AI-Based Energy Management. *IEEE IES 2025*.
9. Syah, M.N., Aprilianto, R.A., & Suryanto, A. (2024). PID Controller Enhancement of Interleaved Buck Converter for DC-DC Conversion. *IEEE ICT-PEP 2024*.
10. Aprilianto, R.A., Syah, M.N., & Suryanto, A. (2024). Novel High Gain Modified SEPIC Converter for Renewable Energy Applications. *IEEE ICT-PEP 2024*.
11. Ibezim, O., Prasad, K., & Kilby, J. (2026). Intelligent Hybrid Solar–Wind Off-Grid EV Charging Stations: A Techno-Economic Assessment. *Electronics*, 15(11), 2253. https://doi.org/10.3390/electronics15112253
12. Singla, P., Boora, S., & Singhal, P. (2024). Design and Simulation of 4 kW Solar Power-Based Hybrid EV Charging Station. *Scientific Reports*, 14, 7336. https://doi.org/10.1038/s41598-024-56833-5
13. Erdemir, D., & Dincer, I. (2023). Solar-Driven Charging Station with Liquid CO2 Storage. *Journal of Energy Storage*, 73(C), 109080. https://doi.org/10.1016/j.est.2023.109080
14. He, L., & Wu, Z. (2024). Hybrid Solar-Wind Fast Charging Station with Demand Response. *Renewable Energy*, 237(C), 121843. https://doi.org/10.1016/j.renene.2024.121843
15. Open Charge Alliance. (2022). *OCPP 1.6J specification*. https://openchargealliance.org
16. Jocher, G., et al. (2023). *Ultralytics YOLOv8*. https://github.com/ultralytics/ultralytics
17. Peraturan Pemerintah No. 28 Tahun 2025 tentang Percepatan Pengembangan dan Pemanfaatan KBLBB.
18. Undang-Undang No. 27 Tahun 2022 tentang Perlindungan Data Pribadi.
19. Peraturan Presiden No. 55 Tahun 2019 tentang Percepatan Program KBLBB.

---

## DAFTAR RIWAYAT HIDUP (DRH) TIM PERISET
*(Lampirkan dalam format bebas sesuai ketentuan BRIN, wajib mencantumkan:)*
- Identitas lengkap & NIP/NIK
- Riwayat pendidikan (S1–S3)
- Daftar publikasi ilmiah 5 tahun terakhir (Scopus/SINTA)
- HKI/Paten yang pernah dihasilkan
- Pengalaman riset relevan
- Tautan profil Scopus/Google Scholar/ID SINTA

**Prof. Dr. Subiyanto** — Ketua Periset
- S3 Teknik Elektro, Universitas Gadjah Mada
- Guru Besar UNNES, bidang Power Electronics & Energy Conversion
- Scopus Author ID: [ID]; SINTA ID: [ID]
- Publikasi utama: IBC fast charger (JAMRIS 2026), Microgrid AI (IEEE IES 2025), PID IBC (IEEE ICT-PEP 2024)

**Bagaskoro Saputro, S.Kom., M.Kom.** — Anggota Periset
- S2 Ilmu Komputer, BINUS University
- Dosen BINUS University, bidang IoT dan Sistem Cerdas
- Scopus Author ID: [ID]; SINTA ID: [ID]
- Kontribusi: Co-author IBC fast charger (JAMRIS 2026) dan bifacial PV modeling (JTP Lampung 2026)
- Email: bagaskoro.saputro@binus.ac.id / bagaskoro@mail.unnes.ac.id

**Mario Norman Syah, S.T., M.T.** — Anggota Periset
- S2 Teknik Elektro, Universitas Gadjah Mada
- Dosen / Peneliti UNNES, bidang Power Electronics, DC-DC Converter, dan Renewable Energy Systems
- Scopus Author ID: [ID]; SINTA ID: [ID]
- Publikasi utama: IBC fast charger (JAMRIS 2026), HHO MPPT (ISMEE 2025), Microgrid Optimization (IES 2025), PID IBC (ICT-PEP 2024), Interleaved Bidirectional DC-DC Converter (ICPEA 2022)
- Kontribusi: Co-author pada 4+ publikasi inti tim, spesialis topologi konverter dan algoritma kontrol

**Adhe Lingga Dewi, S.Si., M.Si.** — Anggota Periset
- S2 Ilmu Komputer, BINUS University
- Dosen Computer Science, BINUS University, Kampus Semarang
- SINTA ID: 6838447; Research Fields: IoT, Sensors, ANN, Computational Physics, Photonic
- Scopus: 12 articles, H-Index 3 | Google Scholar: 46 articles, H-Index 5
- Publikasi relevan: IoT Air Monitoring ESP32 (Procedia CS 2024, cited 22), Sensor Calibration MQ-135/8 (Eng. Res. Express 2025), ANN Weather Prediction (ICIMTech 2024), DNN Classification (AIP 2026)
- Afiliasi: adhe.dewi@binus.ac.id

**Dr. Turnad Lenggo Ginta** — Anggota Periset
- Senior Researcher, BRIN — Pusat Riset [OR / Bidang Energi]
- Scopus: 77 documents, H-Index 17
- Publikasi relevan: Low-carbon Indonesia (IJEEP 2025), PLTS Distributed Generation (2023)

---

## DATA MANAGEMENT PLAN (DMP)
- **Data yang Dikumpulkan:** Telemetri charger (OCPP 1.6J), log inverter solar (Modbus), metadata okupansi anonim, log inferensi edge, metrik utilisasi
- **Format & Struktur:** JSON/CSV (TimescaleDB), Relational (PostgreSQL), Cache (Redis Stack). Metadata AI hanya berisi bounding-box agregat, timestamp, estimasi durasi
- **Penyimpanan & Akses:** Cloud terenkripsi (Fly.io/Supabase Pro), backup harian, akses RBAC + Row Level Security. Tidak ada penyimpanan citra/video mentah
- **Privasi & Kepatuhan:** Pipeline 100% di edge, zero biometric storage/transmission, plakat consent di lokasi, klirens etik riset sesuai Perka BRIN No. 22/2022 & UU PDP No. 27/2022
- **Sharing & Retensi:** Dataset telemetri & metadata anonim dipublikasikan di Zenodo/GitHub 12 bulan pasca proyek. Data mentah (log inferensi) disimpan 3 tahun untuk audit & replikasi riset

---

*Dokumen ini merupakan integrasi dari proposal2.md (IoT-Edge SPKLU AC 22kW + YOLOv8), hybrid-solar-panel.md (technical spec off-grid solar), bagaskoro-saputro-publications.md, adhe-lingga-dewi-publications.md, dan turnad-lenggo-ginta-publications.md — diformat ulang mengikuti sistematika Sublampiran I Pedoman RIIM.*
