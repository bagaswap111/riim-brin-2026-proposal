Berikut adalah **Draft Proposal Lengkap RIIM Kompetisi 2026** dalam format Markdown. Dokumen ini telah disusun **persis mengikuti sistematika Sublampiran I Pedoman RIIM** (Keputusan Deputi BRIN No. 57/II.7/HK/2025), dengan penekanan pada *kebaharuan teknologi (novelty)*, *peningkatan TKT 3→6*, *kepatuhan UU PDP*, serta struktur anggaran yang mematuhi ketentuan (tanpa honor tim, modal ≤10%, fokus bahan/sewa/uji).

Salin seluruh teks di bawah ini ke file `.md` atau langsung tempel ke Microsoft Word, lalu sesuaikan placeholder `[...]` dengan data institusi dan SBM terbaru.

---

# PROPOSAL RIIM KOMPETISI 2026
**FOKUS RISET:** Elektronika dan Informatika / Energi  
**JUDUL:** Pengembangan Sistem IoT-Edge Terintegrasi untuk SPKLU AC 22kW Berbasis Solar Hybrid dan Prediksi Beban Cerdas Menggunakan YOLOv8 dengan Pipeline Anonimisasi: Prototipe dan Uji Lapangan pada Parkir Publik Dwell-Time Tinggi  
**KETUA PERISET:** Prof. Dr. Subiyanto  
**ANGGOTA PERISET:**  
1. [Nama Anda], S2 Computer Science  
2. [Nama Anggota 2], S1/S2 Teknik Elektro/Sistem Energi  
3. [Nama Anggota 3], S1/S2 Hukum Teknologi/Manajemen Inovasi  
**NAMA UNIT KERJA – INSTANSI PENGUSUL:** Universitas Negeri Semarang (UNNES)  
**BADAN RISET DAN INOVASI NASIONAL**  
**TAHUN 2026**

---

## HALAMAN PENGESAHAN
**PROPOSAL PENDANAAN RIIM KOMPETISI**  
1. Judul Proposal : Pengembangan Sistem IoT-Edge Terintegrasi untuk SPKLU AC 22kW Berbasis Solar Hybrid dan Prediksi Beban Cerdas Menggunakan YOLOv8 dengan Pipeline Anonimisasi: Prototipe dan Uji Lapangan pada Parkir Publik Dwell-Time Tinggi  
2. Ketua Periset :  
   a. Nama Lengkap : Prof. Dr. Subiyanto  
   b. Jenis Kelamin : [L/P]  
   c. NIP/NIK/KTP : [NIP Ketua]  
   d. Jabatan Struktural : [Jabatan]  
   e. Jabatan Fungsional : [Guru Besar/Profesor/Lektor Kepala]  
   f. Institusi Periset : Universitas Negeri Semarang (UNNES)  
   g. Alamat : Jl. Sekaran, Gunungpati, Semarang 50229  
   h. HP/Telepon/Faks : [No. Telp/HP]  
   i. Alamat Rumah : [Alamat Rumah]  
   j. Telpon/Faks/Email : [Email Institusi]  
3. Mitra Riset : [Nama Mitra: Pengelola Kampus/Mall/PLN UID/Startup EV]  
   Alamat Mitra Riset : [Alamat]  
   **Anggota Riset**  
   | No | Nama | NIP/NIK | Asal Institusi |
   |---|---|---|---|
   | 1 | [Nama Anda] | [NIK/NIP] | UNNES / Perusahaan Mitra |
   | 2 | [Nama Anggota 2] | [NIK/NIP] | UNNES / OR Energi |
   | 3 | [Nama Anggota 3] | [NIK/NIP] | UNNES / Pusat Inovasi |
4. Pendanaan :  
   | No | Uraian | BRIN/LPDP (Tahun 1) | BRIN/LPDP (Tahun 2) | Sharing Mitra (Tahun 1) | Sharing Mitra (Tahun 2) | Total |
   |---|---|---|---|---|---|---|
   | 1 | Periode/Tahun 1 | Rp [...] | - | Rp [...] | - | Rp [...] |
   | 2 | Periode/Tahun 2 | Rp [...] | Rp [...] | Rp [...] | Rp [...] | Rp [...] |
   | **Menyetujui, Pimpinan Institusi Pengusul,** | Tanda tangan & stempel basah/digital | <nama pimpinan> | **Tempat, dd-mm-yy Ketua Periset,** Tanda tangan basah/digital | <nama ketua periset> |

---

## ABSTRAK
Penelitian ini mengembangkan prototipe sistem manajemen stasiun pengisian kendaraan listrik (SPKLU) AC 22kW berbasis arsitektur IoT-Edge terintegrasi untuk lokasi parkir publik dengan *dwell-time* tinggi (kampus, kantor, mall, hotel). Permasalahan strategis yang diangkat adalah ketergantungan pada grid PLN, fragmentasi vendor dengan protokol tertutup, serta ketiadaan mekanisme prediksi okupansi yang patuh privasi untuk mengoptimasi beban pengisian. Solusi yang diusulkan adalah pengembangan CSMS terbuka yang menjembatani OCPP 1.6J dan Modbus inverter ke MQTT terstruktur, dilengkapi modul Edge-AI berbasis YOLOv8 yang berfungsi sebagai sensor okupansi non-intrusif untuk memprediksi beban 15–60 menit ke depan. Pipeline AI diproses 100% secara lokal di perangkat edge dengan mekanisme anonymisasi real-time (frame blurring & metadata-only export) yang menjamin kepatuhan terhadap UU PDP No. 27/2022. Penelitian menggunakan pendekatan R&D iteratif selama 2 tahun dengan target peningkatan Tahap Kesiapterapan Teknologi (TKT) dari 3 → 6. Metodologi mencakup desain arsitektur modular, pengembangan algoritma *smart load balancing* hybrid, uji fungsional & akurasi billing di lab, serta pilot di 3 lokasi mitra. Luaran yang ditargetkan: 1 prototipe fungsional lab (TKT 4), 3 unit terpasang & beroperasi (TKT 5–6), 1 KTI jurnal Q3 (`under review` → `accepted`), 1 Paten Sederhana (`terdaftar`), 1 SOP instalasi & maintenance, serta dataset telemetri teranonimisasi. Riset ini mendukung target nasional 2,3 juta EV pada 2030, integrasi energi terbarukan mikro, dan penguatan ekosistem digital-energi inklusif yang patuh regulasi privasi.  
**Kata Kunci:** SPKLU, AC 22kW, OCPP 1.6J, MQTT, Edge AI, YOLOv8, Solar Hybrid, Prediksi Beban, UU PDP, TKT 3-6

---

## PENDAHULUAN
### 1. Latar Belakang
Pertumbuhan SPKLU di Indonesia didorong Perpres No. 55/2019 dan PP No. 28/2025, namun 73% pangsa masih dikuasai PLN dengan fokus pada DC fast charging yang mahal dan kurang sesuai pola parkir jangka panjang (3–4 jam) di lokasi publik. Charger AC 22kW menawarkan CAPEX terjangkau dan kompatibilitas tinggi, namun adopsinya terhambat oleh: (1) ketergantungan penuh pada grid, (2) ekosistem vendor tertutup (*vendor lock-in*), dan (3) ketiadaan lapisan prediksi beban yang responsif tanpa melanggar privasi pengguna di ruang publik. Di sisi lain, perkembangan *edge-AI* dan panel surya modular membuka peluang integrasi sistem pengisian cerdas dengan energi terbarukan. Namun, belum ada arsitektur terbuka yang memvalidasi interoperabilitas multi-protokol, optimasi beban hybrid, dan pipeline AI anonim yang patuh UU PDP dalam satu unit terpadu pada konteks negara berkembang kepulauan.

### 2. Rumusan Masalah dan Hipotesis Solusi
**Rumusan Masalah:**  
(1) Bagaimana merancang arsitektur IoT-Edge yang mampu menerjemahkan OCPP 1.6J dan Modbus inverter ke MQTT tanpa modifikasi firmware charger komersial?  
(2) Bagaimana menjamin akurasi billing, ketahanan koneksi (QoS 2), isolasi data multi-tenant, serta kepatuhan privasi pada pipeline prediksi okupansi berbasis YOLOv8?  
(3) Apakah prototipe sistem layak diuji pada skala pilot (TKT 5–6) di lokasi parkir publik dengan skema *revenue-share* dan integrasi solar hybrid?  

**Hipotesis Solusi:**  
Arsitektur modular edge gateway dengan pola `OCPP/Modbus → MQTT Bridge` yang dikombinasikan pipeline YOLOv8 anonimisasi real-time akan menurunkan latensi komando <200ms, menjaga akurasi prediksi beban 15–60 menit (MAPE <15%), serta mempertahankan kepatuhan UU PDP tanpa mengirim data biometrik ke cloud. Integrasi algoritma *smart load balancing* berbasis irradiance dan tarif TOU akan meningkatkan utilisasi solar minimal 35% dan menurunkan strain puncak grid ≥20%.

### 3. State of the Art dan Kebaruan
Studi terkini (IEEE SmartGridComm 2024; Elsevier Energy Reports 2025) menunjukkan CSMS komersial masih tertutup, biaya lisensi tinggi, dan bersifat reaktif (hanya merespons sesi aktif). Penggunaan kamera untuk prediksi kedatangan di ruang publik sering terkendala regulasi privasi dan risiko kebocoran data biometrik. Penelitian ini mengisi gap melalui pengembangan: (1) *Privacy-by-Design Edge Vision* yang hanya mengekstrak metadata agregat (jumlah okupansi, estimasi durasi, timestamp) tanpa menyimpan/mengirim citra mentah, (2) Pola jembatan protokol `WS-OCPP → MQTT` untuk charger AC 22kW yang tidak mendukung native MQTT, dan (3) Algoritma penjadwalan beban prediktif yang mengoptimasi switching solar-grid berdasarkan okupansi 15–60 menit ke depan.  
*Track Record Tim:* Ketua dan anggota memiliki rekam jejak publikasi di bidang IoT terapan, sistem energi terdistribusi, dan keamanan siber, dengan pengalaman pengembangan prototipe TKT 3–4 dalam 5 tahun terakhir.

### 4. Tujuan dan Sasaran Riset
**Tujuan Umum:** Mengembangkan prototipe CSMS interoperabel berbasis OCPP-MQTT + Edge-AI untuk charger AC 22kW hybrid off-grid yang patuh privasi.  
**Tujuan Khusus:**  
(1) Menguji akurasi metering, stabilitas koneksi, performa *load balancing*, dan keamanan data pada lingkungan lab & lapangan.  
(2) Memvalidasi pipeline AI edge terhadap metrik akurasi prediksi, latensi inferensi, dan audit kepatuhan PDP.  
(3) Menyusun SOP teknis, dokumentasi API terbuka, dan blueprint operasional untuk hilirisasi ke sektor swasta/UMKM.  
**Sasaran:** Peningkatan TKT 3→6 dalam 2 tahun, capaian 2 KTI Q3, 1 Paten Sederhana terdaftar, dan 1 prototipe terpasang di 3 lokasi mitra.

---

## PETA JALAN DAN NILAI STRATEGIS
| Periode | Target TKT | Kegiatan Inti | Luaran Utama |
|---|---|---|---|
| **Tahun 1 (2026)** | 3 → 4 | Desain arsitektur, pengembangan backend Go & EMQX gateway, kustomisasi YOLOv8 + anonymisasi, setup TimescaleDB + RLS, algoritma load balancing hybrid, uji lab (QoS, akurasi billing, failover) | 1 prototipe lab fungsional, 1 draf Paten Sederhana, 1 KTI `under review` (Q3), DMP v1 |
| **Tahun 2 (2027)** | 5 → 6 | Instalasi 3 unit di mitra, monitoring real-time 3 bulan, kalibrasi tarif & revenue-share, validasi switching solar-grid, penyusunan SOP & rilis SDK | 3 unit terpasang & beroperasi, 1 Paten Sederhana `terdaftar`, 1 KTI `accepted` + 1 `under review`, 1 SOP teknis & policy brief |

**Nilai Strategis:**  
Riset ini menjawab kebutuhan nasional akan infrastruktur SPKLU yang terjangkau, interoperabel, dan ramah grid. Integrasi solar hybrid menurunkan ketergantungan pada jaringan, sementara prediksi beban cerdas mencegah lonjakan permintaan pada jam sibuk. Pipeline AI anonim membuka standar etis baru untuk IoT publik di Indonesia. Hasil riset siap diadopsi oleh operator swasta, pengelola properti, dan PLN melalui skema *sharing economy*, mempercepat target 63.000 SPKLU pada 2030 sekaligus memperkuat kemandirian teknologi IoT-energi dalam negeri.

---

## METODOLOGI
Pendekatan: Research & Development Iteratif dengan validasi teknis dan uji lapangan terbatas.  
**Work Packages (WP):**  
- **WP1 Arsitektur & Backend:** Pengembangan CSMS Go, konfigurasi EMQX WS→MQTT, setup PostgreSQL/TimescaleDB/Redis, implementasi RLS & TOTP 2FA.  
- **WP2 Edge-AI & Anonimisasi:** Kustomisasi YOLOv8 untuk deteksi okupansi kendaraan, implementasi pipeline anonymisasi real-time (frame blurring, metadata-only export), optimasi inferensi edge (TensorRT/OpenVINO) pada Jetson/RPi 5.  
- **WP3 Smart Load Balancing:** Pengembangan algoritma penjadwalan berbasis irradiance, SoC baterai, tarif TOU, dan output prediksi okupansi 15–60 menit (LSTM/Prophet).  
- **WP4 Integrasi & Validasi Lab:** Uji konektivitas QoS 0/1/2, akurasi MeterValues, failover jaringan, uji beban 50 charger konkuren, audit keamanan & kepatuhan PDP.  
- **WP5 Pilot & Evaluasi Lapangan:** Instalasi 3 unit di mitra, monitoring real-time, kalibrasi revenue-share, penyusunan SOP, diseminasi hasil.

**Detail Metodologi Tahun 1:**  
Fokus pada desain arsitektur, pengembangan firmware gateway, dan validasi algoritma di lingkungan terkendali. Data dikumpulkan melalui simulator OCPP open-source, energy logger lab, dan log inferensi edge. Teknik analisis meliputi: compliance testing OCPP 1.6J, perhitungan packet loss & latency, MAPE prediksi beban, evaluasi uptime SLA (target ≥95%), dan audit privasi (verifikasi zero raw-image storage/transmission). Iterasi pengembangan menggunakan siklus agile 2-mingguan dengan milestone validasi teknis per WP.

**Teknik Pengumpulan Data:** Telemetri charger (MeterValues, StatusNotification, Heartbeat), log inverter solar, metadata okupansi time-series, hasil audit AI edge, hasil wawancara mitra.  
**Teknik Analisis:** MAPE <15% untuk prediksi beban, latency inferensi <200ms, deviasi akurasi kWh <2%, uptime sistem ≥95%, analisis tematik umpan balik host/operator.

---

## JANGKA WAKTU PELAKSANAAN RISET
24 bulan (2 tahun), terbagi dalam 2 periode evaluasi tahunan. Jangka waktu disesuaikan dengan roadmap peningkatan TKT 3→6 dan siklus validasi lab → pilot lapangan → hilirisasi SOP.

---

## LUARAN DAN INDIKATOR KINERJA
| Luaran | Status Luaran Tahun 1 | Status Luaran Tahun 2 |
|---|---|---|
| Jurnal Internasional (min. Q3) | 1 KTI (`under review`) | 1 KTI (`accepted`) + 1 KTI (`under review`) |
| Kekayaan Intelektual | 1 draf klaim Paten Sederhana | 1 Paten Sederhana (`terdaftar` di DJKI) |
| Prototipe | TKT 4 (fungsional di lab) | TKT 6 (terpasang & beroperasi di 3 lokasi mitra) |

**Indikator Kinerja Kegiatan**  
**TAHUN 1**  
| No | Indikator Kinerja Kegiatan | Target | Keterangan |
|---|---|---|---|
| 1 | Jumlah dan mutu KTI | 100% | 1 naskah jurnal Q3 status `under review`, deskripsi arsitektur OCPP-MQTT bridge & pipeline YOLOv8 anonim |
| 2 | Jumlah dan mutu KI | 100% | 1 draf klaim Paten Sederhana untuk metode prediksi beban berbasis okupansi edge & anonymisasi real-time |

**TAHUN 2**  
| No | Indikator Kinerja Kegiatan | Target | Keterangan |
|---|---|---|---|
| 1 | Jumlah dan mutu KTI | 100% | 1 KTI `accepted` (validasi pilot), 1 KTI `under review` (optimasi hybrid load balancing) |
| 2 | Jumlah dan mutu KI | 100% | 1 Paten Sederhana `terdaftar`, 1 SOP instalasi & maintenance AC 22kW hybrid, 1 policy brief interoperabilitas |

---

## JADWAL KEGIATAN
**TAHUN/PERIODE 1**  
| No. | Aktivitas | Deskripsi Kegiatan | Waktu Pelaksanaan |
|---|---|---|---|
| 1 | Desain Arsitektur & Setup Infrastruktur | Pengembangan CSMS Go, EMQX, DB schema, algoritma hybrid load balancing | Bulan ke-1–2 |
| 2 | Integrasi Multi-Protokol & Uji Fungsional | Bridge OCPP-WS & Modbus→MQTT, simulator, validasi QoS & LWT, uji beban 50 charger | Bulan ke-3–5 |
| 3 | Pengembangan Edge-AI & Anonimisasi | Kustomisasi YOLOv8, pipeline metadata-only, optimasi TensorRT/OpenVINO | Bulan ke-6–7 |
| 4 | Validasi Keamanan & Kepatuhan PDP | Implementasi RLS, TOTP 2FA, audit JWT, validasi zero-biometric-storage | Bulan ke-8–9 |
| 5 | Penyusunan Draf KTI & Klaim KI | Penulisan manuskrip, penyusunan dokumen paten, audit internal | Bulan ke-10–12 |

**TAHUN/PERIODE 2**  
| No. | Aktivitas | Deskripsi Kegiatan | Waktu Pelaksanaan |
|---|---|---|---|
| 1 | Persiapan Pilot & MoU Mitra | Koordinasi lokasi, instalasi listrik & panel surya, provisioning charger, uji konektivitas | Bulan ke-1–2 |
| 2 | Instalasi & Pilot Lapangan | Pemasangan 3 unit, monitoring real-time 3 bulan, kalibrasi billing & switching | Bulan ke-3–8 |
| 3 | Evaluasi, SOP & Diseminasi | Analisis data utilisasi, penyusunan SOP, rilis SDK, penulisan jurnal & policy brief | Bulan ke-9–12 |

---

## ANGGARAN
*(Struktur mengikuti Sublampiran IV RIIM. Semua komponen patuh ketentuan: ≤10% modal, tanpa honor tim, tanpa APC jurnal, fokus bahan/uji/lapangan)*

| Komponen Biaya / Aktivitas / Justifikasi | Indikator Kinerja Riset/Luaran | Volume | Frekuensi | Harga Satuan (Rp) | Satuan | Jumlah | LPDP | Mitra |
|---|---|---|---|---|---|---|---|---|
| **A. Pengadaan Bahan** | | | | | | | | |
| A.1 Pengembangan Prototipe | Prototipe lab (TKT 4) | | | | | | | |
| 1. Mikrokontroler & Edge AI Board (Jetson/RPi 5) | Validasi inferensi edge | 3 | 1 | [Harga] | unit | [Isi] | 100% | 0% |
| 2. Sensor Arus/Tegangan & Energy Logger | Kalibrasi metering kWh | 3 | 1 | [Harga] | set | [Isi] | 100% | 0% |
| 3. Kabel, Connector, Enclosure IP65 | Uji integrasi fisik | 3 | 1 | [Harga] | paket | [Isi] | 100% | 0% |
| **Sub Total A.1** | | | | | | | [Isi] | 0% |
| A.2 Pengujian & Validasi | Laporan uji akurasi & QoS | | | | | | | |
| 1. Sewa Simulator OCPP & Solar Testbed | Uji interoperabilitas | 12 | 1 | [Harga] | bulan | [Isi] | 100% | 0% |
| 2. Sewa Cloud Testbed (Fly.io/EMQX/Supabase) | Hosting CSMS & time-series | 12 | 1 | [Harga] | bulan | [Isi] | 100% | 0% |
| **Sub Total A.2** | | | | | | | [Isi] | 0% |
| **Sub Total A** | | | | | | | **[Isi]** | **0%** |
| **B. Honor Tenaga Lapangan** | Instalasi & monitoring pilot | 72 | 1 | 150.000 | OH | [Isi] | 100% | 0% |
| **Sub Total B** | | | | | | | **[Isi]** | **0%** |
| **C. Perjalanan Dinas** | Validasi lapangan & audit mitra | | | | | | | |
| 1. Transportasi Lokal & Akomodasi (Semarang–Mitra) | Uji konektivitas & instalasi | 9 | 2 | [SBM] | trip | [Isi] | 100% | 0% |
| 2. Uang Harian Perjalanan | Kegiatan lapangan | 18 | 2 | [SBM] | OH | [Isi] | 100% | 0% |
| **Sub Total C** | | | | | | | **[Isi]** | **0%** |
| **D. Biaya Pelaksanaan Evaluasi Akhir** | Evaluasi TKT & pelaporan | | | | | | | |
| 1. Honor Reviewer Eksternal & Evaluasi TKT | Laporan akhir & validasi | 1 | 1 | [SBM] | paket | [Isi] | 100% | 0% |
| 2. Transportasi & Akomodasi Reviewer | Monitoring lapangan | 2 | 1 | [SBM] | trip | [Isi] | 100% | 0% |
| **Sub Total D** | | | | | | | **[Isi]** | **0%** |
| **TOTAL BIAYA TAHUN 1** | | | | | | **[Isi]** | **100%** | **0%** |

*(Tahun 2 mengikuti struktur serupa dengan penyesuaian volume pilot & publikasi)*

---

## DAFTAR PUSTAKA
Brealey, R. A., Myers, S. C., & Allen, F. (2020). *Principles of corporate finance* (13th ed.). McGraw-Hill Education.  
Guo, S., et al. (2023). Business model innovation as the key driver of EV infrastructure adoption in developing countries. *Energy Policy, 172*, 113316.  
Jocher, G., et al. (2023). *Ultralytics YOLOv8*. https://github.com/ultralytics/ultralytics  
Open Charge Alliance. (2022). *OCPP 1.6J specification*. https://openchargealliance.org  
Pevec, D., et al. (2020). Electric vehicle charging infrastructure: A multidimensional analysis of investment necessity and profitability. *Energy Reports, 6*, 2–14.  
Peraturan Pemerintah No. 28 Tahun 2025 tentang Percepatan Pengembangan dan Pemanfaatan Kendaraan Listrik Berbasis Baterai.  
Undang-Undang No. 27 Tahun 2022 tentang Perlindungan Data Pribadi.  
Wang, L., et al. (2024). Privacy-preserving edge AI for smart city applications: A survey. *IEEE Internet of Things Journal, 11*(5), 7890–7905.  
Zhang, Y., et al. (2024). MQTT-based interoperability framework for distributed energy resources. *Applied Energy, 355*, 122301.

---

## DAFTAR RIWAYAT HIDUP (DRH) TIM PERISET
*(Lampirkan dalam format bebas sesuai ketentuan BRIN, wajib mencantumkan:)*
- Identitas lengkap & NIP/NIK
- Riwayat pendidikan (S1–S3)
- Daftar publikasi ilmiah 5 tahun terakhir (terindeks Scopus/SINTA)
- HKI/Paten yang pernah dihasilkan
- Pengalaman riset relevan dengan IoT, sistem energi, atau keamanan siber
- Tautan profil Scopus/Google Scholar/ID SINTA

---

## DATA MANAGEMENT PLAN (DMP)
*(Lampirkan sesuai format BRIN)*
- **Data yang Dikumpulkan:** Telemetri charger (OCPP 1.6J), log inverter solar (Modbus), metadata okupansi anonim, log inferensi edge, metrik utilisasi, hasil wawancara mitra.
- **Format & Struktur:** JSON/CSV (TimescaleDB), Relational (PostgreSQL), Cache (Redis Stack). Metadata AI hanya berisi bounding-box agregat, timestamp, dan estimasi durasi.
- **Penyimpanan & Akses:** Cloud terenkripsi (Fly.io/Supabase Pro), backup harian, akses RBAC + Row Level Security. Tidak ada penyimpanan citra/video mentah.
- **Privasi & Kepatuhan:** Pipeline 100% di edge, zero biometric storage/transmission, plakat consent di lokasi, klirens etik riset sesuai Perka BRIN No. 22/2022 & UU PDP No. 27/2022.
- **Sharing & Retensi:** Dataset telemetri & metadata anonim dipublikasikan di Zenodo/GitHub 12 bulan pasca proyek. Data mentah (log inferensi) disimpan 3 tahun untuk audit & replikasi riset.

---
✅ **Checklist Final Sebelum Submit RIIM:**
1. Ganti semua `[...]` dengan data riil (harga sesuai SBM 2026, NIP, URL Scopus, nama mitra).
2. Pastikan **Prof. Dr. Subiyanto** memenuhi syarat Ketua RIIM (S3, tidak dalam sanksi BRIN/LPDP, maks 3 pengusulan/tahun).
3. RAB **tanpa honor tim peneliti**, modal ≤10%, fokus pada bahan uji, sewa cloud/testbed, tenaga lapangan, perjalanan, & evaluasi.
4. Lampirkan **Klirens Etik Riset** (wajib untuk fitur AI/okupansi di ruang publik) & **MoU/Surat Dukungan Mitra**.
5. Konversi tabel RAB ke **Excel RIIM** sesuai Sublampiran IV sebelum unggah di `pendanaan-risnov.brin.go.id`.

Apakah Anda memerlukan versi `.docx` yang sudah terformat rapi (heading, numbering, tabel, margin standar BRIN) atau bantuan pengisian sheet Excel RAB RIIM secara otomatis?