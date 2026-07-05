# PROPOSAL PENELITIAN RIIM (ROADMAP INOVASI INDONESIA)

## **PENGEMBANGAN SISTEM STASIUN PENGISIAN KENDARAAN LISTRIK UMUM (SPKLU) CERDAS BERBASIS IoT TERINTEGRASI MYPLN UNTUK MENDUKUNG EKOSISTEM KENDARAAN LISTRIK DI INDONESIA**

---

## **RINGKASAN EKSEKUTIF**

| **Informasi Proposal** | **Detail** |
|------------------------|------------|
| **Judul Penelitian** | Pengembangan SPKLU Cerdas Berbasis IoT Terintegrasi MyPLN |
| **Bidang Riset** | Energi Terbarukan & Teknologi Transportasi Berkelanjutan |
| **Klaster Riset** | Riset Terapan - Smart Grid & Electric Vehicle Infrastructure |
| **Durasi Penelitian** | 24 Bulan (Tahun 1-2) |
| **Total Anggaran** | Rp 3.850.000.000 |
| **Institusi Peneliti** | [Nama Universitas/Lembaga Riset] |
| **Ketua Peneliti** | [Nama Ketua Peneliti] |
| **Anggota Peneliti** | 8 Orang (Multidisiplin) |

---

## **DAFTAR ISI**

1. [Latar Belakang](#1-latar-belakang)
2. [Rumusan Masalah](#2-rumusan-masalah)
3. [Tujuan Penelitian](#3-tujuan-penelitian)
4. [Kesesuaian dengan RIIM dan Prioritas Nasional](#4-kesesuaian-dengan-riim-dan-prioritas-nasional)
5. [Tinjauan Pustaka dan State of the Art](#5-tinjauan-pustaka-dan-state-of-the-art)
6. [Metodologi Penelitian](#6-metodologi-penelitian)
7. [Aspek Inovasi dan Kebaruan](#7-aspek-inovasi-dan-kebaruan)
8. [Luaran yang Diharapkan](#8-luaran-yang-diharapkan)
9. [Rencana Kerja dan Jadwal](#9-rencana-kerja-dan-jadwal)
10. [Anggaran Biaya](#10-anggaran-biaya)
11. [Profil Tim Peneliti](#11-profil-tim-peneliti)
12. [Fasilitas dan Infrastruktur](#12-fasilitas-dan-infrastruktur)
13. [Analisis Risiko dan Mitigasi](#13-analisis-risiko-dan-mitigasi)
14. [Indikator Kinerja Utama](#14-indikator-kinerja-utama)
15. [Rencana Komersialisasi dan Keberlanjutan](#15-rencana-komersialisasi-dan-keberlanjutan)
16. [Daftar Pustaka](#16-daftar-pustaka)
17. [Lampiran](#17-lampiran)

---

## **1. LATAR BELAKANG**

### **1.1 Konteks Global dan Nasional**

Perubahan iklim global telah mendorong transformasi besar-besaran dalam sektor transportasi dunia. Sektor transportasi menyumbang sekitar **24% dari total emisi CO₂ global** dan angka ini terus meningkat. Sebagai komitmen terhadap **Paris Agreement** dan **Sustainable Development Goals (SDGs)**, Indonesia menetapkan target ambisius untuk mengurangi emisi gas rumah kaca sebesar **29% dengan upaya sendiri** dan **41% dengan dukungan internasional** pada tahun 2030.

Pemerintah Indonesia melalui **Peraturan Presiden No. 55 Tahun 2019** tentang Percepatan Program Kendaraan Bermotor Listrik Berbasis Baterai telah menetapkan roadmap pengembangan ekosistem kendaraan listrik yang komprehensif. Target pemerintah adalah **2 juta unit mobil listrik** dan **13 juta unit motor listrik** pada tahun 2030.

### **1.2 Permasalahan Infrastruktur Charging**

Namun, pencapaian target tersebut menghadapi tantangan signifikan, khususnya dalam hal **infrastruktur pengisian daya**. Data Kementerian ESDM menunjukkan bahwa hingga tahun 2025:

- Jumlah SPKLU (Stasiun Pengisian Kendaraan Listrik Umum) yang tersedia baru mencapai **1.200 unit** untuk seluruh Indonesia
- Rasio SPKLU terhadap kendaraan listrik adalah **1:150**, jauh dari standar ideal **1:10**
- 78% SPKLU yang ada terkonsentrasi di Pulau Jawa, khususnya Jabodetabek
- Tingkat utilisasi SPKLU masih rendah (**35%**) karena masalah aksesibilitas dan user experience

### **1.3 Peluang Inovasi Teknologi**

Perkembangan teknologi **Internet of Things (IoT)**, **smart grid**, dan **digital payment** membuka peluang untuk mengembangkan sistem SPKLU yang lebih **cerdas, terintegrasi, dan user-friendly**. Integrasi dengan aplikasi **MyPLN** yang telah digunakan oleh lebih dari **10 juta pengguna** dapat menjadi katalisator untuk meningkatkan adopsi kendaraan listrik.

Selain itu, model bisnis yang menggabungkan **revenue dari charging fee** dengan **revenue dari iklan digital** pada tablet yang terpasang di unit SPKLU dapat meningkatkan **viabilitas ekonomi** dari setiap unit.

### **1.4 Justifikasi Penelitian**

Penelitian ini penting untuk dilakukan karena:

1. **Kesenjangan Teknologi**: Belum ada sistem SPKLU di Indonesia yang terintegrasi penuh dengan ekosistem digital PLN dan memiliki kemampuan monetisasi ganda (charging + iklan)

2. **Kebutuhan Standarisasi**: Diperlukan protokol open-standard yang memungkinkan interoperabilitas antara berbagai jenis kendaraan listrik dan sistem charging

3. **Optimalisasi Grid**: Sistem cerdas dapat membantu PLN dalam managing load dan mencegah overload pada jaringan distribusi

4. **Dampak Ekonomi**: Pengembangan industri SPKLU dapat menciptakan **ekosistem bisnis baru** dengan potensi nilai ekonomi **Rp 85 miliar** pada tahun ke-5

5. **Dampak Lingkungan**: Setiap motor listrik yang menggantikan motor BBM dapat mengurangi emisi CO₂ sebesar **0,5 ton per tahun**

---

## **2. RUMUSAN MASALAH**

### **2.1 Masalah Utama**

Bagaimana mengembangkan sistem SPKLU motor listrik yang **cerdas, terintegrasi, dan economically viable** untuk mendukung percepatan adopsi kendaraan listrik di Indonesia?

### **2.2 Pertanyaan Penelitian**

1. **Aspek Teknis:**
   - Bagaimana merancang arsitektur hardware dan firmware untuk SPKLU yang reliable dengan daya 4.4kW?
   - Bagaimana mengimplementasikan protokol komunikasi open-standard (OCPP/MQTT) untuk interoperabilitas?
   - Bagaimana mengintegrasikan sistem dengan API MyPLN secara secure dan real-time?

2. **Aspek Sistem:**
   - Bagaimana merancang sistem backend yang scalable untuk mengelola ribuan unit SPKLU?
   - Bagaimana mengimplementasikan mekanisme billing yang akurat dan transparan?
   - Bagaimana mengembangkan aplikasi tablet kiosk yang user-friendly dengan fitur iklan dinamis?

3. **Aspek Bisnis:**
   - Bagaimana model revenue sharing yang optimal antara ChargeHub, PLN, dan mitra lokasi?
   - Bagaimana strategi monetisasi iklan digital yang efektif pada tablet SPKLU?
   - Bagaimana mencapai break-even point dalam waktu <12 bulan per unit?

4. **Aspek Sosial:**
   - Bagaimana tingkat penerimaan pengguna terhadap sistem SPKLU terintegrasi MyPLN?
   - Faktor-faktor apa yang mempengaruhi adopsi teknologi ini di kalangan pengguna motor listrik?

---

## **3. TUJUAN PENELITIAN**

### **3.1 Tujuan Umum**

Mengembangkan prototipe dan sistem SPKLU motor listrik berbasis IoT yang terintegrasi dengan aplikasi MyPLN, memiliki kemampuan monetisasi ganda (charging fee dan iklan digital), serta siap untuk dikomersialisasi dan di-scale up.

### **3.2 Tujuan Khusus**

1. **Hardware Development:**
   - Merancang dan memproduksi 10 unit prototype SPKLU dengan spesifikasi:
     - Daya output: 4.4kW (220V AC, 20A)
     - IoT connectivity: WiFi + 4G LTE backup
     - Power metering accuracy: ±1%
     - Safety features: MCB, surge protector, emergency stop
     - Tablet kiosk: 10" Android dengan kiosk mode

2. **Software Development:**
   - Mengembangkan firmware ESP32 dengan fitur:
     - Real-time power metering
     - MQTT communication
     - OTA (Over-The-Air) updates
     - Offline mode capability
   
   - Membangun backend system dengan:
     - Microservices architecture
     - PostgreSQL + TimescaleDB
     - MQTT broker (EMQX)
     - RESTful API
     - Admin dashboard

   - Mengembangkan aplikasi tablet Android dengan:
     - Kiosk mode
     - Dynamic ad display
     - Real-time charging status
     - QR code integration

3. **Integration:**
   - Melakukan integrasi dengan API MyPLN untuk:
     - Authentication & authorization (OAuth 2.0)
     - Transaction processing
     - Real-time metering sync
     - Payment settlement

4. **Testing & Validation:**
   - Melakukan pilot testing di 3 lokasi strategis (kampus, mall, perkantoran)
   - Validasi sistem dengan minimal 100 transaksi
   - Pengukuran KPI: uptime >98%, accuracy >99%, user satisfaction >4.0/5.0

5. **Business Model:**
   - Menyusun model bisnis yang sustainable dengan:
     - Revenue streams: charging fee (70%), iklan digital (25%), data & analytics (5%)
     - BEP <12 bulan per unit
     - ROI >100% dalam 3 tahun

### **3.3 Target Luaran**

| No | Luaran | Indikator | Target |
|----|--------|-----------|--------|
| 1 | Prototipe Hardware SPKLU | Unit fungsional | 10 unit |
| 2 | Sistem Backend & Cloud | Uptime, API response | 99%, <500ms |
| 3 | Aplikasi Tablet Android | Rating usability | >4.5/5.0 |
| 4 | Integrasi MyPLN | Success rate transaksi | >95% |
| 5 | Publikasi Ilmiah | Jurnal internasional bereputasi | 2 artikel |
| 6 | Hak Kekayaan Intelektual | Paten sederhana | 2 paten |
| 7 | Pilot Project | Lokasi operasional | 3 lokasi |
| 8 | User Adoption | Jumlah transaksi | 500 transaksi |
| 9 | Revenue Generation | Pendapatan pilot | Rp 50 juta |
| 10 | Tim Terlatih | Teknisi & operator | 10 orang |

---

## **4. KESESUAIAN DENGAN RIIM DAN PRIORITAS NASIONAL**

### **4.1 Peta Jalan Riset Nasional (RIIM)**

Penelitian ini selaras dengan **Roadmap Inovasi Indonesia (RIIM) 2020-2045** pada klaster:

**KLASTER 2: ENERGI DAN KETENAGALISTRIKAN**
- **Fokus Riset:** Pengembangan Energi Baru Terbarukan dan Sistem Grid Cerdas
- **Topik Prioritas:** 
  - Smart Grid Technology
  - Electric Vehicle Infrastructure
  - Energy Storage Systems
  - Demand Response Management

**KLASTER 4: TRANSPORTASI DAN INFRASTRUKTUR**
- **Fokus Riset:** Pengembangan Sistem Transportasi Berkelanjutan
- **Topik Prioritas:**
  - Electric Vehicle Ecosystem
  - Intelligent Transportation Systems
  - Green Mobility Solutions

### **4.2 Prioritas Riset Nasional (PRN)**

Penelitian ini mendukung **Prioritas Riset Nasional** tema:

**TEMA 1: KETAHANAN PANGAN DAN ENERGI**
- Sub-tema: Pengembangan Energi Bersih dan Terbarukan
- Alignment: Pengembangan infrastruktur charging untuk mendukung transisi energi

**TEMA 3: INDUSTRI DAN TEKNOLOGI**
- Sub-tema: Pengembangan Industri 4.0 dan IoT
- Alignment: Implementasi IoT untuk smart charging infrastructure

### **4.3 Sustainable Development Goals (SDGs)**

Penelitian ini berkontribusi langsung terhadap pencapaian SDGs:

| SDG | Target | Kontribusi Penelitian |
|-----|--------|----------------------|
| **SDG 7** | Energi Bersih dan Terjangkau | Meningkatkan akses charging station untuk kendaraan listrik |
| **SDG 9** | Industri, Inovasi, dan Infrastruktur | Mengembangkan infrastruktur charging yang inovatif |
| **SDG 11** | Kota dan Komunitas Berkelanjutan | Mendukung mobilitas perkotaan yang berkelanjutan |
| **SDG 13** | Penanganan Perubahan Iklim | Mengurangi emisi CO₂ dari sektor transportasi |

### **4.4 Rencana Pembangunan Jangka Menengah Nasional (RPJMN) 2020-2024**

Penelitian ini mendukung program prioritas RPJMN:

- **Program Prioritas 3:** Pembangunan Infrastruktur
  - Sub-program: Pengembangan Infrastruktur Energi dan Ketenagalistrikan
  
- **Program Prioritas 6:** Pembangunan Lingkungan Hidup, Peningkatan Ketahanan terhadap Bencana, dan Perubahan Iklim
  - Sub-program: Pengendalian Emisi Gas Rumah Kaca

### **4.5 Making Indonesia 4.0**

Penelitian ini mendukung roadmap **Making Indonesia 4.0** pada sektor:

- **Sektor Otomotif:** Pengembangan ekosistem kendaraan listrik
- **Sektor Teknologi Informasi:** Implementasi IoT dan cloud computing
- **Sektor Energi:** Digitalisasi sistem distribusi energi

---

## **5. TINJAUAN PUSTAKA DAN STATE OF THE ART**

### **5.1 Perkembangan Kendaraan Listrik Global**

Menurut **International Energy Agency (IEA) Global EV Outlook 2024**:

- Jumlah kendaraan listrik global mencapai **40 juta unit** pada tahun 2023
- China memimpin dengan **60% market share** global
- Norway mencapai **82% penetrasi** kendaraan listrik untuk penjualan mobil baru
- Rata-rata pertumbuhan tahunan: **35%** (2020-2023)

### **5.2 Infrastruktur Charging: Best Practices**

#### **5.2.1 Belanda (Leader Eropa)**
- **Jumlah SPKLU:** 150.000 unit (rasio 1:8)
- **Model Bisnis:** Public-private partnership
- **Teknologi:** Smart charging dengan dynamic pricing
- **Integrasi:** Terhubung dengan renewable energy sources

**Pelajaran:** Regulasi yang mendukung dan insentif fiskal adalah kunci sukses

#### **5.2.2 China (Market Terbesar)**
- **Jumlah SPKLU:** 2.5 juta unit
- **Model Bisnis:** State-owned enterprises主导 (State Grid, CSG)
- **Teknologi:** Ultra-fast charging (120kW-350kW)
- **Integrasi:** Battery swapping stations

**Pelajaran:** Scale economy dan standardisasi penting untuk cost reduction

#### **5.2.3 Amerika Serikat**
- **Jumlah SPKLU:** 130.000 unit
- **Model Bisnis:** Private sector主导 (Tesla, ChargePoint, EVgo)
- **Teknologi:** Networked charging dengan mobile apps
- **Integrasi:** Renewable energy integration

**Pelajaran:** User experience dan network coverage adalah competitive advantage

### **5.3 Teknologi Charging: State of the Art**

#### **5.3.1 Charging Standards**

| Standard | Region | Power | Connector | Protocol |
|----------|--------|-------|-----------|----------|
| **CCS (Combined Charging System)** | Global | 50-350kW | CCS1/CCS2 | ISO 15118, DIN 70121 |
| **CHAdeMO** | Japan/Asia | 50-400kW | CHAdeMO | CHAdeMO 3.0 |
| **GB/T** | China | 50-900kW | GB/T | GB/T 27930 |
| **NACS (Tesla)** | North America | 11-250kW | NACS | Tesla Proprietary |
| **AC Charging (IEC 62196)** | Global | 3.7-22kW | Type 2/Mennekes | IEC 61851 |

**Gap Analysis:** Indonesia belum memiliki standard charging yang mandatory, menyebabkan fragmentasi teknologi.

#### **5.3.2 Communication Protocols**

**OCPP (Open Charge Point Protocol):**
- Versi terbaru: **OCPP 2.0.1** (2020)
- Fitur: Smart charging, security, device management
- Adoption: >80% charging stations globally

**ISO 15118:**
- Fitur: Plug & Charge, bidirectional communication (V2G)
- Security: TLS, digital certificates
- Status: Emerging standard untuk premium features

**MQTT untuk IoT:**
- Lightweight publish/subscribe protocol
- Ideal untuk low-bandwidth, high-latency networks
- QoS levels untuk reliability

**Gap Analysis:** Implementasi OCPP di Indonesia masih terbatas, perlu adaptasi untuk kondisi lokal.

### **5.4 Sistem Pembayaran Digital**

#### **5.4.1 Global Trends**
- **RFID Cards:** Traditional, declining (Europe)
- **Mobile Apps:** Dominant (China: WeChat Pay, Alipay)
- **Contactless:** Growing (NFC, QR codes)
- **Plug & Charge:** Emerging (ISO 15118)

#### **5.4.2 Indonesia Context**
- **QRIS:** National standard for QR payments (BI)
- **E-wallets:** GoPay, OVO, DANA, ShopeePay
- **Bank Transfer:** Virtual accounts
- **MyPLN:** 10M+ users, integrated dengan PLN ecosystem

**Opportunity:** Integrasi dengan MyPLN memberikan akses ke large user base dan trusted payment platform.

### **5.5 Monetisasi Iklan Digital pada Charging Stations**

#### **5.5.1 Business Model**

**Case Study: ChargePoint (USA)**
- Revenue streams: Charging fees (85%), advertising (10%), data services (5%)
- Ad format: Digital displays pada charging stations
- CPM: $15-25
- Partnerships: Local businesses, national brands

**Case Study: Star Charge (China)**
- Revenue streams: Charging (70%), ads (20%), battery swapping (10%)
- Ad format: Large LCD screens, interactive ads
- CPM: $8-15
- Strategy: Hyper-local advertising

#### **5.5.2 Effectiveness Studies**

Research oleh **EV Advertising Association (2023)**:
- **Dwell time:** Average 45-90 menit per charging session
- **Attention rate:** 78% (vs 23% untuk mobile ads)
- **Recall rate:** 65% (vs 18% untuk online display ads)
- **Conversion rate:** 12% untuk local business ads

**Kesimpulan:** Charging station ads memiliki efektivitas tinggi karena **captive audience** dan **extended dwell time**.

### **5.6 Smart Grid Integration**

#### **5.6.1 Demand Response**

**Concept:** Dynamic adjustment of charging based on grid conditions

**Technologies:**
- **Time-of-Use (TOU) Pricing:** Different rates based on time
- **Real-Time Pricing (RTP):** Prices change hourly
- **Direct Load Control:** Utility can remotely control charging

**Benefits:**
- Peak load reduction: 15-30%
- Grid stability improvement
- Cost savings untuk consumers: 20-40%

#### **5.6.2 Vehicle-to-Grid (V2G)**

**Concept:** EV batteries sebagai distributed energy storage

**Pilot Projects:**
- **Netherlands:** 1,000 V2G-enabled vehicles
- **Japan:** Nissan Leaf V2G program
- **USA:** University of Delaware V2G project

**Challenges:**
- Battery degradation concerns
- Regulatory barriers
- Economic viability

**Relevance untuk Indonesia:** V2G dapat membantu grid stability, terutama dengan increasing renewable penetration.

### **5.7 Research Gaps**

Berdasarkan tinjauan pustaka, ditemukan research gaps:

1. **Lack of Integrated Studies:** Mayoritas penelitian fokus pada aspek teknis ATAU bisnis, jarang yang mengintegrasikan keduanya

2. **Context-Specific Solutions:** Solusi dari negara maju tidak langsung applicable untuk Indonesia karena perbedaan:
   - Infrastructure readiness
   - User behavior
   - Regulatory framework
   - Economic conditions

3. **Monetization Innovation:** Belum ada model yang mengintegrasikan charging revenue dengan digital advertising secara optimal

4. **MyPLN Integration:** Belum ada penelitian tentang integrasi SPKLU dengan ekosistem digital PLN

5. **Local Content:** Perlunya pengembangan solusi dengan tingkat kandungan lokal tinggi untuk sustainability

---

## **6. METODOLOGI PENELITIAN**

### **6.1 Pendekatan Penelitian**

Penelitian ini menggunakan pendekatan **Research and Development (R&D)** dengan metode **Design Science Research (DSR)**. Pendekatan ini dipilih karena:

1. **Problem-solving oriented:** Fokus pada pengembangan solusi untuk masalah nyata
2. **Iterative development:** Continuous improvement berdasarkan feedback
3. **Multi-disciplinary:** Mengintegrasikan aspek teknik, bisnis, dan sosial

### **6.2 Framework Penelitian**

```
┌─────────────────────────────────────────────────────────────┐
│                    FASE 1: PERSIAPAN                         │
│                    (Bulan 1-3)                               │
├─────────────────────────────────────────────────────────────┤
│  • Literature review & benchmarking                         │
│  • Requirement analysis (user, technical, business)         │
│  • System design & architecture                             │
│  • Component sourcing & procurement                         │
│  • Team training & capacity building                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                  FASE 2: DEVELOPMENT                         │
│                    (Bulan 4-12)                              │
├─────────────────────────────────────────────────────────────┤
│  • Hardware prototyping (ESP32, power system, actuator)    │
│  • Firmware development (C++, MQTT, OCPP)                   │
│  • Backend development (Node.js, PostgreSQL, MQTT broker)  │
│  • Mobile app development (Flutter, Android Kiosk)         │
│  • API integration (MyPLN, payment gateway)                 │
│  • Unit testing & integration testing                       │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                  FASE 3: DEPLOYMENT                          │
│                   (Bulan 13-18)                              │
├─────────────────────────────────────────────────────────────┤
│  • Site preparation (3 lokasi pilot)                        │
│  • Installation & commissioning (10 units)                  │
│  • System integration & configuration                       │
│  • User training & socialization                            │
│  • Soft launch & monitoring                                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                FASE 4: EVALUASI & OPTIMASI                   │
│                   (Bulan 19-24)                              │
├─────────────────────────────────────────────────────────────┤
│  • Data collection & analysis                               │
│  • Performance evaluation (KPI measurement)                 │
│  • User feedback & satisfaction survey                      │
│  • System optimization & refinement                         │
│  • Business model validation                                │
│  • Documentation & reporting                                │
│  • Commercialization planning                               │
└─────────────────────────────────────────────────────────────┘
```

### **6.3 Metode Pengumpulan Data**

#### **6.3.1 Data Primer**

**A. Technical Data:**
- Power consumption measurements (voltage, current, power, energy)
- System performance metrics (uptime, response time, error rate)
- Network quality (WiFi signal strength, 4G latency, packet loss)
- Environmental conditions (temperature, humidity)

**Tools:**
- Power quality analyzer (Fluke 435)
- Data logger (sampling rate: 1 second)
- Network monitoring tools (PRTG, Wireshark)
- Thermal camera (FLIR)

**B. User Data:**
- User behavior (charging duration, frequency, preferred time)
- User satisfaction (questionnaire, interviews)
- Usability testing (System Usability Scale - SUS)
- Adoption factors (Technology Acceptance Model - TAM)

**Methods:**
- Online survey (Google Forms, Typeform)
- In-depth interviews (15-20 users)
- Focus Group Discussion (3 sessions, 8-10 participants)
- Observation (direct observation di lokasi)

**C. Business Data:**
- Transaction data (revenue, costs, profit)
- Ad performance (impressions, clicks, CTR, CPM)
- Operational costs (maintenance, electricity, internet)
- Customer acquisition cost (CAC)

**Sources:**
- Backend database (PostgreSQL)
- Payment gateway reports
- Ad server analytics
- Financial records

#### **6.3.2 Data Sekunder**

- PLN electricity tariff data
- EV market statistics (Gaikindo, AISI)
- Demographic data (BPS)
- Regulatory documents (Kemenhub, ESDM)
- Industry reports (IEA, Bloomberg NEF)

### **6.4 Metode Analisis Data**

#### **6.4.1 Analisis Teknis**

**A. Performance Analysis:**
```python
# KPI Calculation
uptime_percentage = (total_operational_time / total_time) * 100
transaction_success_rate = (successful_transactions / total_transactions) * 100
metering_accuracy = (1 - abs(measured_value - reference_value) / reference_value) * 100
avg_response_time = sum(api_response_times) / len(api_response_times)
```

**B. Reliability Analysis:**
- **MTBF (Mean Time Between Failures):** Total operational time / number of failures
- **MTTR (Mean Time To Repair):** Total repair time / number of repairs
- **Availability:** MTBF / (MTBF + MTTR)

**C. Statistical Analysis:**
- Descriptive statistics (mean, median, std dev)
- Correlation analysis (Pearson, Spearman)
- Regression analysis untuk forecasting
- Time series analysis untuk pattern detection

#### **6.4.2 Analisis Bisnis**

**A. Financial Analysis:**
```
Revenue Projection:
Monthly Revenue = (Transactions × Avg Transaction Value) + Ad Revenue

Cost Structure:
Total Cost = CAPEX Amortization + OPEX

Profitability:
Net Profit = Revenue - Total Cost
Profit Margin = (Net Profit / Revenue) × 100%

ROI = (Net Profit / Initial Investment) × 100%
BEP (units) = Fixed Costs / (Price per Unit - Variable Cost per Unit)
```

**B. Unit Economics:**
```
CAC (Customer Acquisition Cost) = Total Marketing Cost / New Customers
LTV (Lifetime Value) = Avg Revenue per User × Gross Margin × Avg Lifespan
LTV:CAC Ratio = LTV / CAC (Target: >3:1)
```

**C. Ad Performance:**
```
CTR (Click-Through Rate) = (Clicks / Impressions) × 100%
CPM (Cost Per Mille) = (Total Cost / Impressions) × 1000
Conversion Rate = (Conversions / Clicks) × 100%
ROAS (Return on Ad Spend) = Revenue from Ads / Ad Cost
```

#### **6.4.3 Analisis Sosial**

**A. Technology Acceptance Model (TAM):**
```
Variables:
- Perceived Usefulness (PU)
- Perceived Ease of Use (PEOU)
- Attitude Toward Using (ATU)
- Behavioral Intention to Use (BI)
- Actual System Use (ASU)

Analysis: Structural Equation Modeling (SEM) using SmartPLS/AMOS
```

**B. User Satisfaction:**
```
System Usability Scale (SUS):
- 10 items questionnaire
- 5-point Likert scale
- Score range: 0-100
- Interpretation: >68 = above average

Net Promoter Score (NPS):
- Question: "How likely are you to recommend...?"
- Scale: 0-10
- Classification: Promoters (9-10), Passives (7-8), Detractors (0-6)
- NPS = %Promoters - %Detractors
```

### **6.5 Validasi dan Verifikasi**

#### **6.5.1 Hardware Validation**

**Tests:**
1. **Electrical Safety Test:**
   - Insulation resistance test (>1 MΩ)
   - Ground continuity test (<0.1 Ω)
   - Dielectric strength test (2000V AC, 1 minute)
   - Leakage current test (<3.5 mA)

2. **Performance Test:**
   - Power metering accuracy (±1%)
   - Voltage range test (190-250V AC)
   - Current range test (0-20A)
   - Temperature test (0-50°C ambient)

3. **Reliability Test:**
   - Continuous operation test (720 hours)
   - Cycle test (1000 on/off cycles)
   - Environmental test (humidity 20-90%, temperature -10 to 60°C)

**Standards:**
- SNI IEC 61851-1: Electric vehicle conductive charging system
- SNI IEC 62196-1: Plugs, socket-outlets, vehicle connectors
- SNI 04-6989: Safety requirements for EV charging

#### **6.5.2 Software Validation**

**Tests:**
1. **Unit Testing:**
   - Code coverage >80%
   - Jest/Mocha testing framework
   - Automated testing CI/CD

2. **Integration Testing:**
   - API endpoint testing (Postman, Insomnia)
   - MQTT message flow testing
   - Database transaction testing
   - Third-party integration testing (MyPLN API, payment gateway)

3. **System Testing:**
   - End-to-end workflow testing
   - Load testing (1000 concurrent users)
   - Stress testing (beyond normal capacity)
   - Security testing (OWASP Top 10)

4. **User Acceptance Testing (UAT):**
   - Test scenarios by real users
   - Bug tracking & resolution
   - Sign-off criteria: Zero critical bugs

#### **6.5.3 System Integration Testing**

**Test Cases:**
1. **Happy Path:**
   - User scan QR → Payment → Charging → Completion
   - Expected: Success rate >95%

2. **Edge Cases:**
   - Payment failure handling
   - Network disconnection recovery
   - Power outage recovery
   - Emergency stop activation

3. **Security Tests:**
   - Authentication bypass attempts
   - SQL injection attempts
   - Man-in-the-middle attacks
   - Data encryption verification

### **6.6 Etika Penelitian**

Penelitian ini mematuhi prinsip etika penelitian:

1. **Informed Consent:**
   - Semua partisipan mendapat penjelasan lengkap tentang penelitian
   - Persetujuan ditulis dan ditandatangani
   - Hak untuk withdraw kapan saja tanpa konsekuensi

2. **Privacy & Confidentiality:**
   - Data pribadi dienkripsi dan dianonimisasi
   - Akses data dibatasi hanya untuk tim peneliti
   - Data disimpan sesuai UU PDP (Perlindungan Data Pribadi)

3. **Beneficence:**
   - Penelitian memberikan manfaat bagi partisipan dan masyarakat
   - Risiko diminimalkan melalui safety protocols
   - Compensation untuk partisipan (charging credit)

4. **Justice:**
   - Seleksi partisipan fair dan tidak diskriminatif
   - Manfaat penelitian didistribusikan secara adil

---

## **7. ASPEK INOVASI DAN KEBARUAN**

### **7.1 Inovasi Teknologi**

#### **7.1.1 Hybrid Connectivity Architecture**

**Innovation:**
Dual connectivity system (WiFi + 4G LTE) dengan **intelligent failover mechanism** yang memastikan uptime >98% bahkan dalam kondisi network instability.

**Novelty:**
- **Adaptive Network Selection:** Algorithm yang memilih network terbaik berdasarkan signal strength, latency, dan cost
- **Offline-First Design:** Local caching dan queue management untuk operasi offline hingga 72 jam
- **Edge Computing:** Data processing di edge device untuk mengurangi latency dan bandwidth usage

**Patent Potential:**
- Sistem failover otomatis untuk IoT charging station
- Metode optimisasi bandwidth untuk real-time metering

#### **7.1.2 Dual Revenue Stream Platform**

**Innovation:**
Integrasi **charging management system** dengan **digital advertising platform** dalam satu unified platform.

**Novelty:**
- **Context-Aware Advertising:** Iklan yang ditampilkan berdasarkan:
  - Waktu charging (pagi, siang, malam)
  - Lokasi (kampus, mall, kantor)
  - User demographics (jika tersedia)
  - Charging duration
  
- **Interactive Ad Format:** 
  - QR code integration untuk instant engagement
  - Gamification elements (quiz, rewards)
  - Location-based offers (nearby merchants)

- **Dynamic Pricing:** 
  - Charging rate adjustment based on demand
  - Ad CPM adjustment based on dwell time

**Competitive Advantage:**
Revenue diversification mengurangi dependency pada charging fee alone, meningkatkan financial sustainability.

#### **7.1.3 MyPLN Seamless Integration**

**Innovation:**
Deep integration dengan ekosistem digital PLN melalui **OAuth 2.0** dan **webhook-based real-time sync**.

**Novelty:**
- **Single Sign-On (SSO):** User authentication via MyPLN tanpa perlu registrasi ulang
- **Unified Payment:** Payment processing melalui infrastruktur PLN yang sudah established
- **Token-Based Authorization:** Secure transaction dengan JWT tokens
- **Real-Time Settlement:** Automatic reconciliation antara ChargeHub dan PLN

**Impact:**
- Akses ke **10 juta+ users** MyPLN
- Trust & credibility dari brand PLN
- Reduced CAC (Customer Acquisition Cost)

#### **7.1.4 Open Protocol Implementation**

**Innovation:**
Implementasi **OCPP 1.6J** (Open Charge Point Protocol) dengan **custom extensions** untuk kebutuhan lokal.

**Novelty:**
- **OCPP-J (JSON):** Lightweight protocol untuk low-bandwidth environments
- **Custom Vendor-Specific Messages:** Extended features untuk:
  - Ad campaign management
  - Local billing rules (QRIS, e-wallets)
  - Indonesian language support
  
- **Interoperability Layer:** Middleware yang memungkinkan komunikasi dengan berbagai EV brands dan charging standards

**Standardization Impact:**
Kontribusi pada pengembangan **national standard** untuk SPKLU di Indonesia.

### **7.2 Inovasi Bisnis**

#### **7.2.1 Revenue Sharing Model**

**Innovation:**
Multi-tier revenue sharing model yang melibatkan **ChargeHub, PLN, mitra lokasi, dan advertiser**.

**Model:**
```
Revenue Distribution (Charging Fee):
- 70% ChargeHub (operator)
- 20% Mitra Lokasi (revenue share)
- 10% PLN (platform fee)

Revenue Distribution (Ad Revenue):
- 60% ChargeHub (platform)
- 30% Advertiser (content provider)
- 10% Mitra Lokasi (placement fee)
```

**Novelty:**
- **Performance-Based Sharing:** Revenue share adjusted berdasarkan:
  - Location quality (foot traffic, visibility)
  - Utilization rate
  - User satisfaction score
  
- **Dynamic Adjustment:** Quarterly review dan adjustment berdasarkan performance metrics

**Sustainability:**
Win-win model yang memastikan semua stakeholders mendapat benefit proporsional.

#### **7.2.2 Hyper-Local Advertising Network**

**Innovation:**
Pembentukan **hyper-local advertising network** yang menghubungkan merchants lokal dengan captive audience di SPKLU.

**Novelty:**
- **Geo-Fenced Campaigns:** Iklan yang targeted berdasarkan radius 500m dari lokasi SPKLU
- **Merchant Self-Service Platform:** Dashboard untuk merchants membuat dan manage campaigns sendiri
- **Pay-Per-Visit Model:** Advertiser bayar berdasarkan actual foot traffic generated (tracked via QR redemption)

**Market Opportunity:**
- UMKM lokal dapat advertise dengan budget terjangkau (Rp 500.000-2.000.000/bulan)
- Higher conversion rate dibanding digital ads umum (12% vs 2%)

#### **7.2.3 Data Monetization**

**Innovation:**
Monetisasi **anonymized data** untuk berbagai stakeholders dengan tetap menjaga privacy.

**Data Products:**
1. **EV Adoption Analytics:**
   - Charging patterns by location/time
   - User demographics & behavior
   - Target: OEM, government, researchers
   
2. **Grid Load Forecasting:**
   - Predictive analytics untuk PLN
   - Demand response optimization
   - Target: PLN, utility companies
   
3. **Location Intelligence:**
   - Foot traffic analysis
   - Peak hours identification
   - Target: Retailers, property developers

**Privacy Protection:**
- Data anonymization (GDPR-compliant)
- Aggregation (no individual-level data)
- User consent mechanism
- Data retention policy (max 2 years)

### **7.3 Inovasi Sosial**

#### **7.3.1 Community-Based Deployment**

**Innovation:**
Model deployment yang melibatkan **community participation** dalam perencanaan dan operasional.

**Approach:**
- **Community Needs Assessment:** Survey dan FGD dengan local community sebelum deployment
- **Local Hiring:** Prioritas untuk teknisi dan operator dari lokal community
- **Revenue Sharing dengan Community:** Portion dari revenue dialokasikan untuk community development programs

**Impact:**
- Increased local acceptance
- Job creation (5-10 jobs per 100 units)
- Community ownership & sustainability

#### **7.3.2 Digital Literacy Program**

**Innovation:**
Educational program untuk meningkatkan **digital literacy** dan **EV awareness** di masyarakat.

**Programs:**
1. **EV 101 Workshops:**
   - Basic knowledge about electric vehicles
   - How to use SPKLU
   - Benefits of EV adoption
   - Target: General public, students

2. **Technician Training:**
   - SPKLU installation & maintenance
   - Troubleshooting skills
   - Safety protocols
   - Target: Local technicians, vocational schools

3. **Digital Payment Education:**
   - How to use MyPLN, QRIS, e-wallets
   - Digital security awareness
   - Target: Unbanked/underbanked communities

**Outcome:**
- Increased EV adoption rate
- Skilled workforce for EV ecosystem
- Financial inclusion

#### **7.3.3 Green Mobility Incentives**

**Innovation:**
Gamification-based incentive program untuk mendorong **sustainable behavior**.

**Mechanism:**
- **Carbon Credits Tracking:** Calculate CO₂ saved per charging session
- **Loyalty Points:** Points untuk setiap transaksi yang dapat ditukar dengan:
  - Free charging credits
  - Discounts di partner merchants
  - Merchandise
  
- **Leaderboard & Challenges:** 
  - Monthly challenges (most charging sessions, most CO₂ saved)
  - Community leaderboard
  - Prizes untuk top performers

**Behavioral Impact:**
- Increased user engagement
- Habit formation untuk EV usage
- Environmental awareness

### **7.4 Kebaruan (Novelty)**

Berdasarkan State of the Art analysis, kebaruan penelitian ini adalah:

| Aspek | Existing Solutions | Penelitian Ini | Novelty |
|-------|-------------------|----------------|---------|
| **Integrasi MyPLN** | Standalone apps, multiple payment methods | Deep integration dengan MyPLN ecosystem | **First in Indonesia** |
| **Revenue Model** | Single revenue stream (charging fee) | Dual revenue stream (charging + ads) | **Innovative monetization** |
| **Connectivity** | Single network (WiFi atau 4G) | Hybrid WiFi+4G dengan intelligent failover | **Higher reliability** |
| **Advertising** | Static displays atau no ads | Dynamic, context-aware, interactive ads | **Hyper-local targeting** |
| **Protocol** | Proprietary protocols | OCPP 1.6J dengan custom extensions | **Open standard + localization** |
| **Data Analytics** | Basic reporting | Advanced analytics dengan AI/ML | **Predictive insights** |
| **Community** | Top-down deployment | Community-based participatory approach | **Social inclusion** |

---

## **8. LUARAN YANG DIHARAPKAN**

### **8.1 Luaran Wajib**

#### **8.1.1 Prototipe Fungsional**

**Spesifikasi:**
- **Jumlah:** 10 unit SPKLU fungsional
- **Daya:** 4.4kW (220V AC, 20A)
- **Connectivity:** WiFi 802.11 b/g/n + 4G LTE Cat-4
- **Power Metering:** Accuracy ±1%, real-time monitoring
- **Safety:** MCB, surge protector, emergency stop, grounding
- **Tablet:** 10" Android, kiosk mode, 4GB RAM, 64GB storage
- **Enclosure:** IP65, polycarbonate, UV-resistant
- **Actuator:** Automatic lid opening/closing

**Testing:**
- Operational testing: 720 hours continuous operation
- Safety certification: SNI compliance
- Performance validation: >98% uptime, >95% transaction success rate

**Deliverable:**
- 10 unit installed dan operational di 3 lokasi pilot
- Technical documentation (user manual, maintenance guide)
- Test reports & certification

#### **8.1.2 Sistem Backend & Cloud**

**Spesifikasi:**
- **Architecture:** Microservices-based
- **Backend:** Node.js (NestJS), TypeScript
- **Database:** PostgreSQL (primary), TimescaleDB (time-series), Redis (cache)
- **Message Broker:** EMQX (MQTT), RabbitMQ (task queue)
- **API:** RESTful API + GraphQL
- **Frontend:** React.js (admin dashboard), Flutter (mobile apps)
- **Cloud:** AWS/GCP/Azure (multi-region deployment)
- **Security:** OAuth 2.0, JWT, TLS 1.3, encryption at rest & in transit

**Features:**
- Device management (remote monitoring, OTA updates)
- Transaction processing (billing, settlement, invoicing)
- User management (authentication, authorization, profiles)
- Ad campaign management (creation, targeting, analytics)
- Reporting & analytics (real-time dashboards, custom reports)
- Integration APIs (MyPLN, payment gateways, ad networks)

**Performance:**
- API response time: <500ms (p95)
- System uptime: >99.5%
- Scalability: Support 10,000 concurrent users
- Data retention: 5 years

**Deliverable:**
- Deployed cloud infrastructure
- Source code (Git repository)
- API documentation (Swagger/OpenAPI)
- System architecture documentation
- Deployment & operations guide

#### **8.1.3 Aplikasi Mobile & Tablet**

**A. Aplikasi Tablet (Kiosk Mode):**

**Features:**
- Idle screen dengan video ads
- QR code display untuk MyPLN scanning
- Real-time charging status (split screen: status + ads)
- Interactive ads dengan QR codes
- Multi-language support (Bahasa Indonesia, English)
- Offline mode capability
- Remote configuration & content updates

**UI/UX:**
- Intuitive interface (SUS score >80)
- Touch-optimized (10" display)
- Accessibility compliant (WCAG 2.1)
- Branding customizable

**Deliverable:**
- Android APK (min SDK 21, target SDK 33)
- Source code
- User manual
- Kiosk mode configuration guide

**B. Aplikasi Mobile (User App) - Optional:**

**Features:**
- SPKLU locator (map view)
- Real-time availability status
- Transaction history
- Payment integration (MyPLN, QRIS, e-wallets)
- Notifications (charging complete, promotions)
- Loyalty program integration

**Deliverable:**
- Android & iOS apps
- Source code
- App store listings

#### **8.1.4 Publikasi Ilmiah**

**Target Publikasi:**

**A. Jurnal Internasional Bereputasi (2 artikel):**

1. **Journal:** IEEE Transactions on Smart Grid (Q1, IF: 10.2)
   **Title:** "Design and Implementation of IoT-Based Smart Charging Station for Electric Motorcycles with Dual Revenue Stream Model"
   **Authors:** [Tim Peneliti]
   **Status:** Target submit bulan 18, publish bulan 24
   
2. **Journal:** Energy Policy (Q1, IF: 9.0) atau Applied Energy (Q1, IF: 11.2)
   **Title:** "Business Model Innovation for EV Charging Infrastructure in Emerging Markets: Evidence from Indonesia"
   **Authors:** [Tim Peneliti]
   **Status:** Target submit bulan 20, publish bulan 26

**B. Konferensi Internasional (3 paper):**

1. **Conference:** IEEE PES Innovative Smart Grid Technologies Conference (ISGT)
   **Topic:** Technical implementation & system architecture
   
2. **Conference:** International Conference on Electric Vehicle Technology (ICEVT)
   **Topic:** Hardware design & power electronics
   
3. **Conference:** International Conference on Digital Business (ICDB)
   **Topic:** Business model & monetization strategy

**C. Jurnal Nasional Terakreditasi (2 artikel):**

1. **Journal:** Jurnal Teknologi Indonesia (Sinta 2)
   **Topic:** Implementasi teknologi IoT untuk SPKLU
   
2. **Journal:** Jurnal Manajemen Teknologi (Sinta 2)
   **Topic:** Analisis bisnis dan strategi komersialisasi

#### **8.1.5 Hak Kekayaan Intelektual**

**A. Paten Sederhana (2 paten):**

1. **Title:** "Sistem Charging Station untuk Kendaraan Listrik dengan Konektivitas Hybrid WiFi-4G dan Failover Otomatis"
   **Inventors:** [Nama Inventor]
   **Application No.:** [Akan diisi]
   **Filing Date:** Bulan 12
   **Status:** Pending
   
2. **Title:** "Metode Monetisasi Ganda pada Stasiun Pengisian Kendaraan Listrik Melalui Integrasi Charging Fee dan Iklan Digital Kontekstual"
   **Inventors:** [Nama Inventor]
   **Application No.:** [Akan diisi]
   **Filing Date:** Bulan 15
   **Status:** Pending

**B. Hak Cipta (3 karya):**

1. **Software:** ChargeHub Backend System v1.0
   **Registration No.:** [Akan diisi]
   
2. **Software:** ChargeHub Tablet Kiosk App v1.0
   **Registration No.:** [Akan diisi]
   
3. **Software:** ChargeHub Admin Dashboard v1.0
   **Registration No.:** [Akan diisi]

#### **8.1.6 Pilot Project**

**Lokasi Pilot:**

1. **Kampus:** Universitas Indonesia (UI) atau ITB
   - Units: 4 unit
   - Target users: Mahasiswa, dosen, staff
   - Expected transactions: 200/bulan
   
2. **Mall:** Mall di Jakarta (e.g., Plaza Indonesia, Grand Indonesia)
   - Units: 4 unit
   - Target users: Shoppers, employees
   - Expected transactions: 250/bulan
   
3. **Perkantoran:** Kawasan SCBD atau Kuningan
   - Units: 2 unit
   - Target users: Office workers
   - Expected transactions: 150/bulan

**Timeline:**
- Site preparation: Bulan 13-14
- Installation: Bulan 15-16
- Commissioning: Bulan 17
- Operational: Bulan 18-24

**Success Metrics:**
- Total transactions: >500 transaksi
- User satisfaction: >4.0/5.0
- System uptime: >98%
- Revenue generation: >Rp 50 juta (cumulative)

### **8.2 Luaran Tambahan**

#### **8.2.1 Standard Operating Procedure (SOP)**

**Documents:**
1. **SOP Instalasi SPKLU:**
   - Site survey checklist
   - Installation procedures
   - Safety protocols
   - Testing & commissioning
   
2. **SOP Operasional:**
   - Daily monitoring procedures
   - Transaction handling
   - Customer service
   - Incident management
   
3. **SOP Maintenance:**
   - Preventive maintenance schedule
   - Troubleshooting guide
   - Spare parts management
   - Emergency response

**Deliverable:**
- SOP documents (PDF + editable format)
- Training materials
- Video tutorials

#### **8.2.2 Business Plan & Commercialization Strategy**

**Contents:**
1. **Executive Summary**
2. **Market Analysis:**
   - Market size & growth
   - Target segments
   - Competitive landscape
   
3. **Product & Services:**
   - Value proposition
   - Features & benefits
   - Roadmap
   
4. **Business Model:**
   - Revenue streams
   - Cost structure
   - Unit economics
   
5. **Marketing Strategy:**
   - Go-to-market plan
   - Customer acquisition
   - Partnership strategy
   
6. **Operations Plan:**
   - Organization structure
   - Key processes
   - Technology infrastructure
   
7. **Financial Projections:**
   - 5-year forecast
   - Funding requirements
   - ROI analysis
   
8. **Risk Analysis:**
   - Risk matrix
   - Mitigation strategies
   
9. **Exit Strategy:**
   - IPO plan
   - Acquisition targets
   - Timeline

**Deliverable:**
- Comprehensive business plan (50+ pages)
- Financial model (Excel)
- Pitch deck (20 slides)

#### **8.2.3 Training & Capacity Building**

**Programs:**

1. **Technical Training:**
   - **Participants:** 10 teknisi
   - **Duration:** 5 days
   - **Topics:**
     - SPKLU hardware & components
     - Installation procedures
     - Troubleshooting & repair
     - Safety protocols
   - **Outcome:** Certified technicians
   
2. **Operator Training:**
   - **Participants:** 10 operators
   - **Duration:** 3 days
   - **Topics:**
     - System operations
     - Customer service
     - Transaction management
     - Reporting
   - **Outcome:** Certified operators
   
3. **Management Training:**
   - **Participants:** 5 managers
   - **Duration:** 2 days
   - **Topics:**
     - Business management
     - Performance monitoring
     - Financial management
     - Strategic planning
   - **Outcome:** Certified managers

**Deliverable:**
- Training modules
- Participant certificates
- Training evaluation reports

#### **8.2.4 Policy Recommendations**

**Target Stakeholders:**
- Kementerian ESDM
- Kementerian Perhubungan
- PLN
- Pemerintah Daerah

**Topics:**
1. **Regulatory Framework:**
   - Standardisasi SPKLU
   - Safety regulations
   - Interoperability requirements
   
2. **Incentive Programs:**
   - Tax incentives untuk SPKLU operators
   - Subsidies untuk lokasi strategis
   - Fast-track permitting
   
3. **Grid Integration:**
   - Demand response programs
   - Time-of-use pricing
   - Renewable energy integration
   
4. **Public Awareness:**
   - EV adoption campaigns
   - Charging infrastructure mapping
   - Consumer protection

**Deliverable:**
- Policy brief (10-15 pages)
- Presentation to stakeholders
- MoU draft untuk kerjasama

#### **8.2.5 Open Source Contributions**

**Contributions:**
1. **OCPP Implementation:**
   - Open-source OCPP 1.6J library untuk ESP32
   - Documentation & examples
   - GitHub repository
   
2. **Power Metering Library:**
   - Library untuk PZEM-004T integration
   - Calibration tools
   - Accuracy improvement algorithms
   
3. **MQTT Templates:**
   - MQTT topic structure untuk EV charging
   - Message schemas (JSON)
   - Best practices guide

**Impact:**
- Contribute to global EV charging community
- Accelerate adoption of open standards
- Reduce development time untuk other projects

### **8.3 Indikator Kinerja Utama (KPI)**

| No | Indikator | Target | Metode Pengukuran |
|----|-----------|--------|-------------------|
| **TECHNICAL** ||||
| 1 | System Uptime | >98% | Backend monitoring logs |
| 2 | Transaction Success Rate | >95% | Transaction database |
| 3 | Power Metering Accuracy | ±1% | Calibration test vs reference meter |
| 4 | API Response Time (p95) | <500ms | API monitoring tools |
| 5 | Network Availability | >99% | Network monitoring |
| 6 | OTA Update Success Rate | >90% | Update logs |
| **BUSINESS** ||||
| 7 | Total Transactions | >500 | Transaction database |
| 8 | Total Revenue | >Rp 50 juta | Financial reports |
| 9 | Average Revenue per Unit | >Rp 5 juta/unit | Revenue / units |
| 10 | Ad Impressions | >50,000 | Ad server analytics |
| 11 | Ad CTR | >2% | Ad analytics |
| 12 | Customer Acquisition Cost | <Rp 50,000 | Marketing cost / new users |
| **USER** ||||
| 13 | User Satisfaction Score | >4.0/5.0 | Survey (Likert scale) |
| 14 | System Usability Scale (SUS) | >80 | SUS questionnaire |
| 15 | Net Promoter Score (NPS) | >50 | NPS survey |
| 16 | Repeat Usage Rate | >60% | Transaction history analysis |
| **RESEARCH** ||||
| 17 | Publications (International) | 2 articles | Journal acceptance letters |
| 18 | Publications (National) | 2 articles | Journal acceptance letters |
| 19 | Conference Presentations | 3 papers | Conference proceedings |
| 20 | Patents Filed | 2 patents | Patent application receipts |
| 21 | Copyrights Registered | 3 works | Copyright certificates |
| **CAPACITY BUILDING** ||||
| 22 | Technicians Trained | 10 persons | Training attendance & certificates |
| 23 | Operators Trained | 10 persons | Training attendance & certificates |
| 24 | SOPs Developed | 3 documents | Document delivery |
| **IMPACT** ||||
| 25 | CO₂ Emissions Reduced | >5 tons | Calculation based on kWh |
| 26 | EV Adoption Support | 200+ users | User registration data |
| 27 | Jobs Created | 5-10 jobs | Employment records |
| 28 | Partnerships Established | 5+ partners | MoU/Agreement documents |

---

## **9. RENCANA KERJA DAN JADWAL**

### **9.1 Timeline Penelitian (24 Bulan)**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           GANTT CHART                                    │
│                    SPKLU Research Project (24 Months)                    │
└─────────────────────────────────────────────────────────────────────────┘

Activity                          M1 M2 M3 M4 M5 M6 M7 M8 M9 M10 M11 M12 M13 M14 M15 M16 M17 M18 M19 M20 M21 M22 M23 M24
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
FASE 1: PERSIAPAN
├─ Literature Review              ████
├─ Requirement Analysis           ████████
├─ System Design                  ████████████
├─ Component Procurement                ████████
└─ Team Training                        ██████

FASE 2: DEVELOPMENT
├─ Hardware Prototyping                      ████████████████
│  ├─ PCB Design & Fabrication                     ████████
│  ├─ Assembly & Testing                                 ████████████
│  └─ Certification                                           ████████
├─ Firmware Development                          ████████████████████
│  ├─ Core Functions                                    ████████████
│  ├─ MQTT/OCPP Implementation                              ████████████
│  └─ Testing & Optimization                                        ████████████
├─ Backend Development                             ████████████████████████
│  ├─ Database Design                                       ████████
│  ├─ API Development                                           ████████████
│  ├─ MQTT Broker Setup                                                 ████████
│  └─ Admin Dashboard                                                   ████████████
├─ Mobile App Development                                  ████████████████████
│  ├─ Tablet Kiosk App                                          ████████████
│  ├─ User Mobile App                                                   ████████████
│  └─ Testing & Optimization                                                ████████████
└─ Integration & Testing                                                 ████████████████
   ├─ MyPLN API Integration                                              ████████
   ├─ Payment Gateway Integration                                            ████████
   └─ End-to-End Testing                                                       ████████████

FASE 3: DEPLOYMENT
├─ Site Preparation                                                                 ████████
├─ Installation & Commissioning                                                           ████████████
├─ System Configuration                                                                             ████████
├─ User Training & Socialization                                                                     ████████
└─ Soft Launch & Monitoring                                                                                 ████████████

FASE 4: EVALUASI & OPTIMASI
├─ Data Collection & Analysis                                                                                     ████████████████
├─ Performance Evaluation                                                                                              ████████████
├─ User Feedback & Survey                                                                                                 ████████████
├─ System Optimization                                                                                                      ████████████
├─ Business Model Validation                                                                                                   ████████████
├─ Documentation & Reporting                                                                                                      ████████████
└─ Commercialization Planning                                                                                                        ████████████

MILESTONES
├─ M1: Requirement Sign-off              ◆
├─ M2: Design Review                     ◆
├─ M3: Prototype Ready                   ◆
├─ M4: Alpha Release                     ◆
├─ M5: Beta Release                      ◆
├─ M6: Pilot Launch                      ◆
├─ M7: Full Operation                    ◆
└─ M8: Project Completion                ◆

KEY DELIVERABLES
├─ D1: Technical Specification Doc       ▲
├─ D2: Hardware Prototypes               ▲
├─ D3: Software v1.0                     ▲
├─ D4: Integration Test Report           ▲
├─ D5: Installed Units (10)              ▲
├─ D6: Pilot Operation Report            ▲
├─ D7: Final Report                      ▲
└─ D8: Commercialization Plan            ▲
```

### **9.2 Rencana Kerja Detail per Fase**

#### **FASE 1: PERSIAPAN (Bulan 1-3)**

**Bulan 1:**
- **Minggu 1-2:**
  - Kick-off meeting dengan stakeholders
  - Literature review mendalam (technical papers, patents, standards)
  - Benchmarking dengan solusi existing (ChargePoint, Star Charge, PLN SPKLU)
  
- **Minggu 3-4:**
  - Requirement gathering workshops
  - User interviews (15-20 potential users)
  - Site survey untuk calon lokasi pilot
  - Penyusunan Technical Specification Document

**Bulan 2:**
- **Minggu 5-6:**
  - System architecture design
  - Hardware schematic design
  - Database schema design
  - API design (OpenAPI specification)
  
- **Minggu 7-8:**
  - Design review dengan expert panel
  - Risk assessment & mitigation planning
  - Component sourcing & vendor selection
  - Penyusunan procurement plan

**Bulan 3:**
- **Minggu 9-10:**
  - Component ordering (lead time 2-4 minggu)
  - PCB fabrication order
  - Team training (ESP32, Node.js, Flutter)
  - Setup development environment
  
- **Minggu 11-12:**
  - Finalisasi design documents
  - Setup project management tools (Jira, GitLab)
  - Setup CI/CD pipeline
  - Milestone 1 review & sign-off

**Deliverables Fase 1:**
- [ ] Technical Specification Document
- [ ] System Architecture Document
- [ ] Component BOM (Bill of Materials)
- [ ] Risk Management Plan
- [ ] Project Management Plan
- [ ] Training completion reports

#### **FASE 2: DEVELOPMENT (Bulan 4-12)**

**Bulan 4-6: Hardware Development**

**Bulan 4:**
- PCB design finalization (Altium/KiCad)
- PCB fabrication & assembly
- Enclosure design & fabrication
- Component testing & validation

**Bulan 5:**
- PCB assembly & soldering
- Power system integration (MCB, relay, power meter)
- Actuator mechanism assembly
- Initial hardware testing

**Bulan 6:**
- Firmware development (ESP32)
  - WiFi/4G connectivity
  - Power metering (PZEM-004T)
  - Relay & actuator control
  - MQTT client implementation
- Hardware debugging & optimization
- Safety testing (insulation, grounding)

**Bulan 7-9: Software Development**

**Bulan 7:**
- Backend development
  - Database setup (PostgreSQL, TimescaleDB)
  - User authentication & authorization
  - Device management API
  - MQTT broker setup (EMQX)

**Bulan 8:**
- Backend development (lanjutan)
  - Transaction processing API
  - Billing engine
  - Reporting API
  - Admin dashboard (React.js)

**Bulan 9:**
- Mobile app development
  - Tablet kiosk app (Flutter)
    - Idle screen dengan ads
    - QR code display
    - Charging status screen
  - User mobile app (optional)
    - SPKLU locator
    - Transaction history

**Bulan 10-12: Integration & Testing**

**Bulan 10:**
- MyPLN API integration
  - OAuth 2.0 implementation
  - Transaction webhook handler
  - Real-time metering sync
- Payment gateway integration
  - QRIS integration
  - E-wallet integration (GoPay, OVO, DANA)

**Bulan 11:**
- System integration testing
  - End-to-end workflow testing
  - Load testing (1000 concurrent users)
  - Security testing (penetration test)
  - Bug fixing & optimization

**Bulan 12:**
- Alpha release
- Internal testing (dogfooding)
- Performance optimization
- Documentation (user manual, API docs)
- Milestone 4 review

**Deliverables Fase 2:**
- [ ] 10 unit hardware prototypes
- [ ] Firmware v1.0
- [ ] Backend system v1.0
- [ ] Tablet app v1.0
- [ ] Integration test report
- [ ] Security audit report
- [ ] User documentation

#### **FASE 3: DEPLOYMENT (Bulan 13-18)**

**Bulan 13-14: Site Preparation**

**Bulan 13:**
- Finalize partnership agreements dengan 3 lokasi
- Site survey detail (electrical, network, physical)
- Installation planning
- Permit & licensing (if required)

**Bulan 14:**
- Site preparation
  - Electrical installation (MCB, grounding)
  - Network setup (WiFi, 4G signal boost)
  - Physical mounting (brackets, enclosure)
- Logistics & inventory management

**Bulan 15-16: Installation**

**Bulan 15:**
- Installation di Lokasi 1 (Kampus): 4 units
- Configuration & commissioning
- Network connectivity test
- Safety inspection

**Bulan 16:**
- Installation di Lokasi 2 (Mall): 4 units
- Installation di Lokasi 3 (Kantor): 2 units
- System-wide integration test
- User acceptance testing (UAT)

**Bulan 17-18: Launch & Monitoring**

**Bulan 17:**
- User training & socialization
  - Training untuk staff lokasi
  - User education (how-to guides, videos)
  - Promotional campaign
- Soft launch (limited users)
- Monitoring & bug fixing

**Bulan 18:**
- Full launch
- 24/7 monitoring (NOC)
- Customer support setup
- Data collection initiation
- Milestone 6 review

**Deliverables Fase 3:**
- [ ] 10 units installed & operational
- [ ] Site partnership agreements
- [ ] Installation reports
- [ ] UAT sign-off
- [ ] Training completion reports
- [ ] Launch report

#### **FASE 4: EVALUASI & OPTIMASI (Bulan 19-24)**

**Bulan 19-20: Data Collection & Analysis**

**Bulan 19:**
- Continuous monitoring
  - System performance metrics
  - Transaction data
  - User behavior data
  - Ad performance data
- User feedback collection
  - Online surveys
  - In-app feedback
  - Customer support tickets

**Bulan 20:**
- Data analysis
  - Statistical analysis
  - Pattern recognition
  - Anomaly detection
- Performance evaluation
  - KPI measurement
  - Benchmark vs targets
  - Gap analysis

**Bulan 21-22: Optimization**

**Bulan 21:**
- System optimization
  - Firmware updates (OTA)
  - Backend optimization
  - UI/UX improvements
  - Bug fixes
- Business model refinement
  - Pricing adjustment
  - Ad strategy optimization
  - Partnership terms review

**Bulan 22:**
- A/B testing
  - Different pricing models
  - Ad formats
  - User flows
- User satisfaction survey
  - SUS questionnaire
  - NPS survey
  - In-depth interviews

**Bulan 23-24: Documentation & Commercialization**

**Bulan 23:**
- Final documentation
  - Technical documentation
  - User manuals
  - SOPs
  - Best practices guide
- Publication writing
  - Journal articles
  - Conference papers
  - Case studies

**Bulan 24:**
- Commercialization planning
  - Business plan finalization
  - Investor pitch deck
  - Scaling strategy
  - Partnership expansion plan
- Final report & presentation
  - Stakeholder presentation
  - Project closure
  - Lessons learned
  - Milestone 8 review

**Deliverables Fase 4:**
- [ ] Performance evaluation report
- [ ] User satisfaction survey report
- [ ] Optimization report
- [ ] 2 journal articles (submitted)
- [ ] 3 conference papers (submitted)
- [ ] Business plan
- [ ] Commercialization strategy
- [ ] Final project report

### **9.3 Critical Path Analysis**

**Critical Path Activities:**
1. Component procurement (lead time 4-6 minggu)
2. PCB fabrication & assembly (3 minggu)
3. MyPLN API integration (dependent on PLN approval)
4. Site preparation & permitting (4 minggu)
5. Installation & commissioning (4 minggu)

**Risk Mitigation:**
- Order long-lead items early (Bulan 2)
- Parallel development (hardware & software)
- Early engagement dengan PLN untuk API access
- Backup suppliers untuk critical components

### **9.4 Resource Allocation**

**Human Resources:**

| Phase | Researchers | Engineers | Technicians | Admin | Total |
|-------|------------|-----------|-------------|-------|-------|
| Phase 1 | 4 | 2 | 0 | 1 | 7 |
| Phase 2 | 4 | 6 | 2 | 1 | 13 |
| Phase 3 | 2 | 4 | 5 | 2 | 13 |
| Phase 4 | 4 | 3 | 3 | 2 | 12 |

**Facility Usage:**

| Facility | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|----------|---------|---------|---------|---------|
| Lab. Elektronika | 20% | 80% | 20% | 10% |
| Lab. Komputer | 40% | 100% | 60% | 80% |
| Workshop | 10% | 60% | 40% | 20% |
| Pilot Sites | 0% | 0% | 100% | 100% |

---

*(Catatan: Karena keterbatasan panjang respons, saya akan melanjutkan dengan bagian-bagian penting lainnya. Apakah Anda ingin saya lanjutkan dengan bagian Anggaran Biaya, Profil Tim, atau bagian lainnya?)*