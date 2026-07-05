# PROPOSAL RIIM KOMPETISI 2026
**FOKUS RISET:** Elektronika dan Informatika / Energi
**JUDUL:** Pengembangan Hybrid Off-Grid Solar-Powered SPKLU Cerdas dengan Fast Charging Interleaved Buck Converter dan Integrasi MyPLN untuk Mendukung Ekosistem Kendaraan Listrik Rendah Karbon di Indonesia

**KETUA PERISET:** Prof. Dr. Subiyanto
**ANGGOTA PERISET:**
1. Bagaskoro Saputro, S.Kom., M.Kom. — Ilmu Komputer / IoT dan Sistem Cerdas (BINUS University)
2. Mario Norman Syah, S.T., M.T. — Teknik Elektro / Power Electronics dan Konversi Energi
3. Adhe Lingga Dewi, S.Si., M.Si. — Ilmu Komputer / IoT dan Sensor
4. Yashella Tirana, S.Kom. — Information Systems / User Experience dan Sistem Informasi (BINUS University)
5. Dr. Turnad Lenggo Ginta — Teknik Mesin / Kebijakan Energi

**NAMA UNIT KERJA – INSTANSI PENGUSUL:** Universitas Negeri Semarang (UNNES)
**BADAN RISET DAN INOVASI NASIONAL**
**TAHUN 2026**

---

## HALAMAN PENGESAHAN
**PROPOSAL PENDANAAN RIIM KOMPETISI**
1. **Judul Proposal** : Pengembangan Hybrid Off-Grid Solar-Powered SPKLU Cerdas dengan Fast Charging Interleaved Buck Converter dan Integrasi MyPLN untuk Mendukung Ekosistem Kendaraan Listrik Rendah Karbon di Indonesia
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
3. **Mitra Riset** : [Mitra: PLN / Pengelola Parkir Publik / Startup EV]
   **Anggota Riset**
   | No | Nama | NIP/NIK | Asal Institusi |
   |---|---|---|---|
    | 1 | Bagaskoro Saputro, S.Kom., M.Kom. | [NIK] | BINUS University |
    | 2 | Mario Norman Syah, S.T., M.T. | [NIK] | UNNES |
    | 3 | Adhe Lingga Dewi, S.Si., M.Si. | [NIK] | BINUS University |
    | 4 | Yashella Tirana, S.Kom. | [NIK] | BINUS University |
    | 5 | Dr. Turnad Lenggo Ginta | [NIP] | BRIN / OR Energi |
4. **Pendanaan** :
   | No | Uraian | BRIN/LPDP (Tahun 1) | BRIN/LPDP (Tahun 2) | Sharing Mitra (Tahun 1) | Sharing Mitra (Tahun 2) | Total |
   |---|---|---|---|---|---|---|
   | 1 | Periode/Tahun 1 | Rp [...] | - | Rp [...] | - | Rp [...] |
   | 2 | Periode/Tahun 2 | Rp [...] | Rp [...] | Rp [...] | Rp [...] | Rp [...] |

**Menyetujui, Pimpinan Institusi Pengusul,** | **Tempat, dd-mm-yy Ketua Periset,**
---|---

---

## ABSTRAK
Penelitian ini mengembangkan prototipe SPKLU hybrid off-grid yang mengintegrasikan solar PV (4-100 kWp), BESS, Interleaved Buck Converter (IBC) dengan PI-FLC untuk fast charging 72V/20A, serta konektivitas IoT-Cloud yang terintegrasi MyPLN. Permasalahan strategis yang diangkat adalah ketergantungan pada grid PLN (78% SPKLU di Jawa), fragmentasi sistem pembayaran, dan belum adanya SPKLU hybrid yang mengintegrasikan MPPT berbasis HHO (efisiensi 99.53%) dengan IBC fast charger (charging 57.75 menit 0-100% SoC) dalam satu platform IoT. Solusi yang diusulkan mencakup: (1) arsitektur IoT berbasis ESP32 dengan konektivitas WiFi/4G dan protokol OCPP 1.6J/MQTT, (2) integrasi sistem backend cloud dengan MyPLN untuk autentikasi dan pembayaran, (3) smart EMS tiga-level dengan prediksi beban 15-60 menit menggunakan ANN/LSTM, serta (4) skema bisnis dual revenue (charging + advertising). Penelitian memperkuat integrasi dengan publikasi terkini tim periset pada fast charger E2W (Subiyanto et al., 2026; DOI: 10.14313/jamris-2026-030), bifacial PV modeling (Widiyawati et al., 2026; DOI: 10.23960/jtepl.v15i2.510-524), HHO MPPT (Aprilianto et al., 2025; DOI: 10.1109/ISMEE68179.2025.11473059), IoT sensor systems (Dewi et al., 2024; DOI: 10.1016/j.procs.2024.10.308), dan kebijakan energi rendah karbon (Farabi, Ginta et al., 2025; DOI: 10.32479/ijeep.18292). Target luaran: prototipe TKT 4→6 dalam 2 tahun, 2 publikasi Q3, 2 paten sederhana, dataset telemetri publik, dan 3 unit pilot di lokasi parkir publik.
**Kata Kunci:** SPKLU, Solar Hybrid, Interleaved Buck Converter, HHO MPPT, IoT, ESP32, MyPLN, OCPP 1.6J, Fast Charging, TKT 3-6

---

## PENDAHULUAN

### 1. Latar Belakang
Indonesia berkomitmen menurunkan emisi GRK 29-41% pada 2030 (Perpres 55/2019). Sektor transportasi menyumbang 24% emisi CO2 global. Target 2 juta mobil listrik dan 13 juta motor listrik pada 2030 membutuhkan infrastruktur SPKLU yang masif, namun 78% SPKLU terkonsentrasi di Jawa dengan rasio 1:150 terhadap kendaraan listrik (Kementerian ESDM, 2025). SPKLU eksisting mayoritas DC fast charging dengan CAPEX tinggi dan belum mengintegrasikan sumber energi terbarukan mandiri.

Penelitian Ibezim et al. (2026) menunjukkan konfigurasi solar hybrid mencapai 30-50% reduksi kebutuhan baterai dan LCOE USD 0.08-0.15/kWh — 15-25% lebih rendah dari sistem single-source. Pasar off-grid solar EV charging global bernilai USD 512 juta (2024) dan diproyeksikan USD 2.31 miliar (2033, CAGR 18.4%).

Tim periset UNNES telah menghasilkan publikasi terdepan di bidang ini. Subiyanto et al. (2026) mengembangkan IBC PI-FLC fast charger dengan charging time 57.75 menit — tiga kali lebih cepat dari PID CC-CV konvensional. Widiyawati et al. (2026) memvalidasi bifacial PV gain 25-30% melalui ray tracing. Aprilianto et al. (2025) mencapai efisiensi MPPT 99.53% menggunakan HHO algorithm.

Dari sisi IoT dan sensor, Dewi et al. (2024) telah mengimplementasikan sistem monitoring berbasis ESP32 dengan multi-sensor MQ dan DHT11 yang terintegrasi cloud platform, serta studi kalibrasi sensor MQ-135/MQ-8 untuk CO2 dan H2 (Dewi et al., 2025) — memberikan dasar pengalaman dalam pengembangan IoT gateway dan validasi sensor untuk sistem SPKLU. Komparasi fungsi aktivasi ANN untuk prediksi time-series (Dewi et al., 2024) juga relevan untuk pengembangan EMS prediktif.

Dari sisi pengalaman pengguna dan sistem informasi, Tirana & Sfenrianto (2023) mengidentifikasi faktor-faktor kepuasan pengguna aplikasi MyIndihome — platform serupa dengan MyPLN — menggunakan SEM-PLS dengan 417 responden, menunjukkan bahwa information quality, system quality, ease of use, dan chatbot effectiveness berpengaruh signifikan. Hal ini menjadi dasar pengembangan antarmuka pengguna MyPLN, chatbot layanan pelanggan, serta evaluasi kualitas sistem pada SPKLU terintegrasi.

Dari konteks kebijakan, Farabi, Ginta et al. (2025) mengkonfirmasi bahwa pengembangan energi dan kebijakan finansial berkontribusi signifikan pada reduksi emisi di Indonesia, memperkuat justifikasi investasi infrastruktur charging berbasis energi terbarukan. Tirana & Sfenrianto (2023) memberikan kontribusi dari sisi analisis faktor kepuasan pengguna platform digital — relevan untuk pengembangan antarmuka MyPLN dan chatbot service yang meningkatkan adopsi sistem charging.

### 2. Rumusan Masalah dan Hipotesis Solusi
**Rumusan Masalah:**
(1) Bagaimana merancang SPKLU hybrid off-grid yang mengintegrasikan solar PV (4-100 kWp), BESS, IBC PI-FLC fast charger, MPPT HHO, dan IoT gateway ESP32 dalam satu sistem terpadu?
(2) Bagaimana mengimplementasikan MPPT HHO (99.53% efisiensi) dan IBC PI-FLC (57.75 menit fast charging) pada SPKLU komersial yang terintegrasi MyPLN?
(3) Bagaimana mengembangkan smart EMS tiga-level dengan prediksi beban ANN/LSTM 15-60 menit yang mempertimbangkan irradiance, SoC, tarif TOU, dan okupansi?
(4) Bagaimana mengembangkan sistem antarmuka dan chatbot layanan yang memenuhi kebutuhan kepuasan pengguna berdasarkan faktor-faktor yang teridentifikasi pada platform digital serupa (Tirana & Sfenrianto, 2023)?
(5) Bagaimana memvalidasi performa sistem di lokasi parkir publik dwell-time tinggi dengan skema bisnis dual revenue?

**Hipotesis Solusi:**
Arsitektur modular berbasis ESP32 + edge AI dengan protokol OCPP 1.6J/MQTT, dikombinasikan IBC PI-FLC (ripple <12%, efisiensi >94%) dan MPPT HHO (99.53%), akan menurunkan waktu charging >65% vs konvensional, meningkatkan utilisasi solar ≥35%, dan menurunkan strain puncak grid ≥20% — dengan akurasi billing ±1% dan uptime sistem >99%.

### 3. State of the Art dan Kebaruan
Studi terkini menunjukkan CSMS komersial masih tertutup (vendor lock-in), charger AC/DC konvensional belum mengadopsi IBC dengan PI-FLC untuk fast charging E2W, dan MPPT masih menggunakan P&O/INC konvensional (efisiensi <95%). Integrasi sistem IoT-Cloud dengan MyPLN untuk autentikasi dan pembayaran terpadu juga belum ada di pasar.

Kebaruan penelitian ini:
1. **IBC PI-FLC Fast Charger** — Topologi two-phase IBC dengan PI-FLC, charging 0-100% dalam 57.75 menit, ripple cancellation <12% (Subiyanto et al., 2026)
2. **MPPT HHO** — Efisiensi 99.53%, outperform P&O, INC, GA (Aprilianto et al., 2025)
3. **Solar PV Bifacial** — Gain 25-30% rear-side, konfigurasi checkerboard (Widiyawati et al., 2026)
4. **IoT-Cloud Architecture** — ESP32 multi-sensor gateway dengan cloud pipeline real-time, berbasis pengalaman monitoring udara IoT (Dewi et al., 2024) dan kalibrasi sensor akurat (Dewi et al., 2025)
5. **Predictive EMS** — ANN/LSTM untuk prediksi beban 15-60 menit dengan input irradiance, SoC, TOU, okupansi
6. **MyPLN Integration** — Autentikasi dan pembayaran terpadu dengan skema dual revenue, didukung oleh analisis faktor kepuasan pengguna dan kualitas sistem informasi (Tirana & Sfenrianto, 2023)
7. **User Experience & Chatbot** — Evaluasi user experience dashboard MyPLN dan pengembangan chatbot untuk helpdesk SPKLU berbasis model kepuasan pengguna (Tirana & Sfenrianto, 2023)

### 4. Tujuan dan Sasaran Riset
**Tujuan Umum:** Mengembangkan prototipe SPKLU hybrid off-grid dengan IBC fast charger, MPPT HHO, dan IoT terintegrasi MyPLN yang siap hilirisasi.

**Tujuan Khusus:**
(1) Merancang dan menguji integrasi IBC PI-FLC dengan MPPT HHO pada SPKLU hybrid 4-100 kWp
(2) Mengembangkan dan memvalidasi IoT gateway ESP32 + cloud backend dengan protokol OCPP/MQTT dan integrasi MyPLN
(3) Mengimplementasikan smart EMS tiga-level dengan prediksi ANN/LSTM dan load balancing
(4) Mengembangkan antarmuka pengguna dan chatbot layanan SPKLU berbasis faktor kepuasan pengguna platform digital
(5) Memvalidasi performa sistem di 3 lokasi parkir publik dwell-time tinggi

**Sasaran:** Peningkatan TKT 3→6 dalam 2 tahun, 2 publikasi Q3, 2 paten sederhana, 3 unit pilot, 1 dashboard UX teruji.

---

## PETA JALAN DAN NILAI STRATEGIS
| Periode | Target TKT | Kegiatan Inti | Luaran Utama |
|---------|------------|---------------|--------------|
| **Tahun 1 (2026)** | 3 → 4 | Desain arsitektur hybrid solar + IBC, pengembangan firmware ESP32 gateway, integrasi MPPT HHO, setup cloud backend & MyPLN API, uji lab IBC (efisiensi, ripple), uji MPPT, validasi sensor via metode kalibrasi (Dewi et al., 2025), evaluasi UX dashboard MyPLN & chatbot (Tirana & Sfenrianto, 2023) | 1 prototipe lab fungsional, 1 draf Paten IBC-EMS, 1 KTI under review (Q3), 1 laporan UX |
| **Tahun 2 (2027)** | 5 → 6 | Instalasi 3 unit di mitra, monitoring 3 bulan, validasi switching solar-grid, kalibrasi revenue-share, penyusunan SOP, rilis dataset, evaluasi kepuasan pengguna | 3 unit terpasang & operasional, 1 Paten terdaftar, 1 KTI accepted + 1 under review, 1 SOP teknis, 1 policy brief UX |

**Nilai Strategis:** Riset ini menjawab kebutuhan nasional akan infrastruktur SPKLU yang terjangkau, mandiri energi, dan interoperabel. Integrasi solar hybrid + IBC fast charging menurunkan ketergantungan grid dan waktu charging, sementara integrasi MyPLN mempercepat adopsi melalui kemudahan pembayaran. Skema dual revenue menawarkan keberlanjutan bisnis. Hasil riset siap diadopsi oleh operator swasta, pengelola properti, dan PLN.

---

## METODOLOGI
Pendekatan: Research & Development Iteratif dengan validasi teknis dan uji lapangan terbatas.

**Work Packages (WP):**
- **WP1 Perancangan Sistem Hybrid Solar + IBC:** Desain PV array 4-100 kWp dengan bifacial gain 25-30%, BESS LFP/NMC 48V, IBC two-phase 20-50 kHz dengan PI-FLC, MPPT HHO 99.53%
- **WP2 Pengembangan IoT Gateway & Cloud:** Firmware ESP32 untuk multi-sensor (arus, tegangan, irradiance, suhu), protokol OCPP 1.6J / MQTT, backend Go, PostgreSQL/TimescaleDB, integrasi API MyPLN
- **WP2a UX MyPLN & Chatbot:** Evaluasi UX dashboard MyPLN berbasis SEM-PLS (Tirana & Sfenrianto, 2023), pengembangan chatbot helpdesk SPKLU, analisis faktor kepuasan pengguna
- **WP3 Smart EMS & Prediksi Beban:** Algoritma ANN/LSTM untuk prediksi 15-60 menit, hierarchical PI-FLC kontrol tiga-level, load balancing berbasis irradiance + SoC + TOU
- **WP4 Validasi Lab & Kalibrasi:** Uji QoS (latensi <200ms), akurasi metering ±1% (berbasis metodologi kalibrasi sensor — Dewi et al., 2025), efisiensi IBC >94%, ripple <12%, MPPT efisiensi >99%
- **WP5 Pilot & Diseminasi:** Instalasi 3 unit, monitoring 3 bulan, analisis utilisasi, penyusunan SOP, publikasi dan paten

**Detail Metodologi Tahun 1:** Fokus pada desain arsitektur, pengembangan firmware gateway, integrasi IBC-MPPT, dan validasi algoritma di lingkungan terkendali. Data dikumpulkan melalui simulator OCPP, energy logger lab, dan data logger irradiance. Teknik analisis: compliance testing OCPP 1.6J, perhitungan efisiensi konverter, MAPE prediksi, audit keamanan, dan analisis LCOE.

**Teknik Pengumpulan Data:** Telemetri charger (MeterValues, StatusNotification), log BMS, data irradiance solar, log inferensi edge, data transaksi MyPLN.
**Teknik Analisis:** Efisiensi konversi >94%, MAPE prediksi beban <15%, akurasi kWh ±1%, uptime ≥95%.

---

## JANGKA WAKTU PELAKSANAAN RISET
24 bulan (2 tahun), terbagi dalam 2 periode evaluasi tahunan. Jangka waktu disesuaikan dengan roadmap peningkatan TKT 3→6.

---

## LUARAN DAN INDIKATOR KINERJA
| Luaran | Status Luaran Tahun 1 | Status Luaran Tahun 2 |
|--------|----------------------|----------------------|
| Jurnal Internasional (min. Q3) | 1 KTI under review | 1 KTI accepted + 1 KTI under review |
| Kekayaan Intelektual | 1 draf Paten Sederhana (IBC + Hybrid EMS) | 1 Paten Sederhana terdaftar di DJKI |
| Prototipe | TKT 4 (fungsional di lab) | TKT 6 (terpasang & beroperasi di 3 lokasi mitra) |

**Indikator Kinerja Kegiatan Tahun 1:**
| No | Indikator | Target |
|----|-----------|--------|
| 1 | KTI | 100% — 1 naskah jurnal Q3 status under review (arsitektur IBC-MPPT-IoT) |
| 2 | KI | 100% — 1 draf klaim Paten Sederhana |

**Indikator Kinerja Kegiatan Tahun 2:**
| No | Indikator | Target |
|----|-----------|--------|
| 1 | KTI | 100% — 1 accepted (validasi pilot) + 1 under review (optimasi EMS) |
| 2 | KI | 100% — 1 Paten terdaftar, 1 SOP instalasi, 1 policy brief interoperabilitas |

---

## JADWAL KEGIATAN
**TAHUN/PERIODE 1**
| No | Aktivitas | Deskripsi | Waktu |
|----|-----------|-----------|-------|
| 1 | Desain Arsitektur Hybrid & IBC | Perancangan PV array, BESS, IBC two-phase PI-FLC, MPPT HHO | Bulan ke-1–3 |
| 2 | Pengembangan IoT Gateway ESP32 | Firmware multi-sensor, OCPP/MQTT bridge, integrasi sensor arus/tegangan | Bulan ke-4–6 |
| 3 | Pengembangan Cloud Backend & MyPLN API | Backend Go, TimescaleDB, integrasi autentikasi MyPLN, dashboard | Bulan ke-5–7 |
| 3a | UX Dashboard & Chatbot | Evaluasi UX dashboard MyPLN (SEM-PLS), pengembangan chatbot helpdesk | Bulan ke-5–8 |
| 4 | Smart EMS & Prediksi Beban | ANN/LSTM prediksi 15-60 menit, hierarchical PI-FLC control | Bulan ke-6–8 |
| 5 | Validasi Lab & Kalibrasi | Uji efisiensi IBC, ripple, akurasi MPPT, QoS jaringan, akurasi billing | Bulan ke-9–11 |
| 6 | Publikasi & Paten Tahun 1 | Penulisan manuskrip, penyusunan draf paten | Bulan ke-10–12 |

**TAHUN/PERIODE 2**
| No | Aktivitas | Deskripsi | Waktu |
|----|-----------|-----------|-------|
| 1 | Persiapan Pilot & MoU Mitra | Koordinasi 3 lokasi, instalasi listrik, panel surya, provisioning | Bulan ke-1–2 |
| 2 | Instalasi & Pilot Lapangan | Pemasangan 3 unit, monitoring 3 bulan, kalibrasi billing & switching | Bulan ke-3–8 |
| 3 | Evaluasi, SOP & Diseminasi | Analisis data, penyusunan SOP, publikasi jurnal, policy brief | Bulan ke-9–12 |

---

## ANGGARAN
*(Struktur mengikuti Sublampiran IV RIIM. Semua komponen patuh ketentuan: ≤10% modal, tanpa honor tim, tanpa APC jurnal, fokus bahan/uji/lapangan)*

| Komponen Biaya | Indikator Kinerja | Volume | Frekuensi | Harga Satuan (Rp) | Satuan | Jumlah | LPDP | Mitra |
|---------------|-------------------|--------|-----------|-------------------|--------|--------|------|-------|
| **A. Pengadaan Bahan** | | | | | | | | |
| A.1 Prototipe & Pengembangan | Prototipe lab TKT 4 | | | | | | | |
| 1. Panel Surya Bifacial 500Wp + Inverter Hybrid | Integrasi solar PV | 6 | 1 | [Harga] | unit | [Isi] | 100% | 0% |
| 2. BESS LFP 48V 100Ah + BMS | Energy storage | 2 | 1 | [Harga] | set | [Isi] | 100% | 0% |
| 3. ESP32 Dev Kit + Sensor Arus/Tegangan ACS712 + PZEM-004T | IoT gateway & metering | 5 | 1 | [Harga] | set | [Isi] | 100% | 0% |
| 4. Komponen IBC (Mosfet, Induktor, Driver, Dioda) | Rangkaian fast charger | 3 | 1 | [Harga] | set | [Isi] | 100% | 0% |
| 5. Enclosure IP65 + Kabel Power | Integrasi fisik | 3 | 1 | [Harga] | paket | [Isi] | 100% | 0% |
| **Sub Total A.1** | | | | | | | **[Isi]** | **0%** |
| A.2 Pengujian & Validasi | Laporan uji | | | | | | | |
| 1. Sewa Cloud Server (Fly.io/Supabase) | Hosting backend | 12 | 1 | [Harga] | bulan | [Isi] | 100% | 0% |
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
16. Peraturan Pemerintah No. 28 Tahun 2025 tentang Percepatan Pengembangan dan Pemanfaatan KBLBB.
17. Tirana, Y., & Sfenrianto. (2023). Factors on Mobile Application User Satisfaction in the Largest Indonesian Internet Service Provider (ISP). *CommIT Journal*, 17(2), 199-208. https://journal.binus.ac.id/index.php/commit/article/view/8518
18. Undang-Undang No. 27 Tahun 2022 tentang Perlindungan Data Pribadi.
19. Peraturan Presiden No. 55 Tahun 2019 tentang Percepatan Program KBLBB.

---

## DAFTAR RIWAYAT HIDUP (DRH) TIM PERISET

### 1. Prof. Dr. Subiyanto, ST, MT — Ketua Periset
| Item | Detail |
|------|--------|
| **NIP** | 132309137 |
| **Institusi** | Universitas Negeri Semarang (UNNES) |
| **Jabatan Fungsional** | Guru Besar (Professor) — terhitung 1 Desember 2020 |
| **Program Studi** | Teknik Elektro, Fakultas Teknik |
| **Bidang Keahlian** | Intelligent Systems Electrical Engineering, Power Electronics, Artificial Intelligence |
| **S1** | Teknik Elektro — Universitas Diponegoro (Undip) |
| **S2** | Teknik Elektro — Universitas Gadjah Mada (UGM) |
| **S3** | Electrical, Electronic & Systems Engineering — Universiti Kebangsaan Malaysia (UKM) |
| **SINTA ID** | 257687 |
| **Google Scholar** | https://scholar.google.com/citations?user=TcmKHJgAAAAJ |
| **Email** | subiyanto@mail.unnes.ac.id |
| **Publikasi Utama (2024-2026)** | IBC Fast Charger (JAMRIS 2026), Microgrid AI (IEEE IES 2025), PID IBC (IEEE ICT-PEP 2024), Electric Bus Scheduling (Majalah Ilmiah Teknologi Elektro 2024) |

### 2. Bagaskoro Saputro, S.Kom., M.Kom. — Anggota Periset
| Item | Detail |
|------|--------|
| **Institusi** | BINUS University |
| **Program Studi** | Computer Science, School of Computer Science, Kampus Semarang |
| **Bidang Keahlian** | IoT, Sistem Cerdas, Signal Processing, Machine Learning, Electric Vehicle |
| **S1** | Elektronika dan Instrumentasi — Universitas Gadjah Mada (UGM) |
| **S2** | Ilmu Komputer — Universitas Gadjah Mada (UGM) |
| **SINTA ID** | 6869233 |
| **Google Scholar** | https://scholar.google.com/citations?user=wJSoTIMAAAAJ |
| **Email** | bagaskoro.saputro@binus.ac.id |
| **Publikasi Utama (2026)** | Co-author IBC Fast Charger (JAMRIS 2026, DOI: 10.14313/jamris-2026-030); Co-author Bifacial PV Modeling (JTP Lampung 2026, DOI: 10.23960/jtepl.v15i2.510-524) |

### 3. Mario Norman Syah, S.T., M.T. — Anggota Periset
| Item | Detail |
|------|--------|
| **Institusi** | Universitas Negeri Semarang (UNNES) |
| **Program Studi** | Pendidikan Teknik Elektro, Fakultas Teknik |
| **Bidang Keahlian** | Power Electronics, MPPT, DC-DC Converters, Microgrid, Control System, Renewable Energy |
| **S1** | Pendidikan Teknik Elektro — Universitas Negeri Semarang (UNNES) |
| **S2** | Teknik Elektro — Universitas Gadjah Mada (UGM) |
| **SINTA ID** | 6869196 |
| **Google Scholar** | https://scholar.google.com/citations?user=Ao9DaAkAAAAJ |
| **Scopus H-index** | - (cited by 54 on GS) |
| **Email** | mario.norman@mail.unnes.ac.id |
| **Publikasi Utama (2024-2026)** | IBC Fast Charger (JAMRIS 2026), HHO MPPT (ISMEE 2025, DOI: 10.1109/ISMEE68179.2025.11473059), Microgrid Optimization (IEEE IES 2025), PID IBC (IEEE ICT-PEP 2024), Novel High Gain SEPIC (ICT-PEP 2024), Interleaved Bidirectional DC-DC Converter (ICPEA 2022), Fast MPPT Dynamic Scaling P&O (2025), Techno-economic Feasibility Study (Techné 2025) |

### 4. Adhe Lingga Dewi, S.Si., M.Si. — Anggota Periset
| Item | Detail |
|------|--------|
| **Institusi** | BINUS University |
| **Program Studi** | Computer Science, School of Computer Science, Kampus Semarang |
| **Bidang Keahlian** | IoT, Sensors, Artificial Neural Network, Computational Physics, Photonic |
| **S1** | Fisika — Universitas Negeri Semarang (UNNES) |
| **S2** | Ilmu Komputer — Universitas Diponegoro (UNDIP) |
| **SINTA ID** | 6838447 |
| **Scopus** | 12 articles, H-Index 3 |
| **Google Scholar** | 46 articles, H-Index 5 |
| **Email** | adhe.dewi@binus.ac.id |
| **Publikasi Utama (2024-2026)** | Smart Air Monitoring IoT ESP32 (Procedia CS 2024, DOI: 10.1016/j.procs.2024.10.308, cited 22 — sebagai corresponding author); Sensor Calibration MQ-135/8 (Eng. Res. Express 2025, DOI: 10.1088/2631-8695/adbcc6 — first author); ANN Weather Prediction (ICIMTech 2024 — first author); Workload & Stress Monitoring IoT GSR (Procedia CS 2025); #DEBITAAPPS ML Diabetes (E3S Web of Conferences 2026 — first author); Breast Cancer DNN (AIP Conf. Proc. 2026) |

### 5. Yashella Tirana, S.Kom. — Anggota Periset
| Item | Detail |
|------|--------|
| **Institusi** | BINUS University |
| **Program Studi** | Information Systems Management, BINUS Graduate Program |
| **Bidang Keahlian** | Information Systems, User Satisfaction, Chatbot Effectiveness, Machine Learning, Image Processing |
| **S1** | Bisnis Digital — BINUS University |
| **SINTA ID** | 6998018 |
| **Google Scholar** | https://scholar.google.com/citations?user= |
| **Email** | yashella.tirana@binus.ac.id |
| **Publikasi Utama (2023-2026)** | Factors on Mobile App User Satisfaction (CommIT Journal 2023, cited 8); Model Deteksi Misleading Visual Review (Hibah BINUS 2026) |

### 6. Ir. Turnad Lenggo Ginta, ST, MT, PhD — Anggota Periset
| Item | Detail |
|------|--------|
| **Institusi** | Badan Riset dan Inovasi Nasional (BRIN) |
| **Unit Kerja** | Research Center for Manufacturing Technology of Production Machinery |
| **Bidang Keahlian** | Machine Learning, Welding Technology, Precision Machining, Metal Casting, Surface Treatment, Energy Policy |
| **Scopus ID** | 26435862600 |
| **Scopus** | 77 documents, H-Index 17, Cited by 1,082 |
| **Google Scholar** | Cited by 1,686, H-Index 21, i10-Index 32 |
| **Email** | turnad.lenggo.ginta@brin.go.id |
| **Publikasi Utama Relevan** | Promoting a Low-carbon Indonesia (IJEEP 2025, DOI: 10.32479/ijeep.18292); PLTS Distributed Generation Lhokseumawe (2023); Optimization Briquette Performance (Eng. J. 2024); Additively Manufactured Inconel 718 (J. Mech. Eng. 2024) |

---

## DATA MANAGEMENT PLAN (DMP)
- **Data yang Dikumpulkan:** Telemetri charger (OCPP 1.6J), log inverter solar (Modbus), data irradiance, data transaksi MyPLN, log EMS, metrik utilisasi
- **Format & Struktur:** JSON/CSV (TimescaleDB), Relational (PostgreSQL)
- **Penyimpanan & Akses:** Cloud terenkripsi, backup harian, RBAC + Row Level Security
- **Privasi & Kepatuhan:** Data transaksi MyPLN dienkripsi, tidak menyimpan data pribadi pengguna, plakat informasi di lokasi
- **Sharing & Retensi:** Dataset telemetri anonim dipublikasikan di Zenodo/GitHub 12 bulan pasca proyek. Data mentah disimpan 3 tahun untuk audit dan replikasi riset

---

*Dokumen ini merupakan integrasi dari proposal1.md (IoT SPKLU MyPLN), hybrid-solar-panel.md (technical spec off-grid solar), dan publikasi tim periset — diformat ulang mengikuti sistematika Sublampiran I Pedoman RIIM.*
