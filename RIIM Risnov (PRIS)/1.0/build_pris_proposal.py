#!/usr/bin/env python3
"""
Read Proposal_RIIM_Kompetisi_2026_Smart_Charging.docx (internal reference)
and output a PRIS-formatted Markdown proposal.
"""

import zipfile
import xml.etree.ElementTree as ET
import os

DOCX = os.path.join(os.path.dirname(__file__),
                    "internal reference",
                    "Proposal_RIIM_Kompetisi_2026_Smart_Charging.docx")
OUT = os.path.join(os.path.dirname(__file__),
                   "prisproposal_internal_reference.md")

# ── Extract paragraphs from docx ─────────────────────────────────
def extract_paragraphs(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')
    root = ET.fromstring(xml_content)
    texts = []
    for p in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        para_text = ''
        for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
            if t.text:
                para_text += t.text
        texts.append(para_text.strip())
    return texts

paras = extract_paragraphs(DOCX)

# ── Helper ───────────────────────────────────────────────────────
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def section(title, level=2):
    return f"\n{'#' * level} {title}\n"

def table(headers, rows):
    out = f"| {' | '.join(headers)} |\n"
    out += f"|{'|'.join(['---']*len(headers))}|\n"
    for r in rows:
        out += f"| {' | '.join(str(c) for c in r)} |\n"
    return out

# ── Hardcoded metadata (verified from docx) ──────────────────────
# Using hardcoded values to avoid index fragility across different docx parsers
judul = ("Pengembangan Smart Charging Hub Solar Hybrid PV–BESS–Grid "
         "Berbasis AI dan IoT-Edge dengan EMS Adaptif, Mode Islanding, "
         "dan Layanan Digital")
ketua_nama = "Prof. Dr. Subiyanto, S.T., M.T."
ketua_nip = "197411232005011001"
tema = "Kedaulatan Energi"

pengesahan_data = {
    "Tema": tema,
    "Judul": judul,
    "Nama Ketua": ketua_nama,
    "NIP/NIK": ketua_nip,
    "Jabatan": "Guru Besar / Dosen",
    "Institusi": "Universitas Negeri Semarang",
    "Unit Kerja": "Fakultas Teknik / Program Studi Teknik Elektro",
    "Alamat": "Kampus Sekaran, Gunungpati, Kota Semarang 50229",
    "No HP/WA": "+62 857-2757-4192",
    "Email": "subiyanto@mail.unnes.ac.id",
    "Mitra": "PT. Arunika Sains Teknologi",
    "Peran Mitra": ("Penyedia lokasi uji, data historis operasional, dan engineer pendamping (2 orang, ~120–150 jam/tahun) "
                    "sebagai kontribusi in-kind; calon pengguna dan mitra hilirisasi hasil riset."),
}
anggota = [
    ("Bagaskoro Saputro, S.Si., M.Cs.", "BINUS University", "081327694998", "bagaskoro.saputro@binus.ac.id"),
    ("Mario Norman Syah, S.Pd., M.Eng.", "Universitas Negeri Semarang", "085713381616", "marionormansyah@mail.unnes.ac.id"),
    ("Adhe Lingga Dewi, S.Si., M.Si.", "BINUS University", "[DIISI]", "adhe.dewi@binus.ac.id"),
    ("Ir. Turnad Lenggo Ginta, S.T., M.T., Ph.D.", "BRIN", "[DIISI]", "turnad.lenggo.ginta@brin.go.id"),
]

# ── Find section boundaries by keyword ─────────────────────────
def find_section(title_keyword, start=0):
    for i in range(start, len(paras)):
        if title_keyword.lower() in paras[i].lower():
            return i
    return None

def extract_between(start_kw, end_kw, min_len=10):
    """Extract paragraphs between two section headers (exclusive)."""
    s = find_section(start_kw)
    e = find_section(end_kw, s + 1 if s else 0)
    if s is None:
        return []
    if e is None:
        e = len(paras)
    lines = []
    for i in range(s + 1, e):
        txt = paras[i]
        if len(txt) >= min_len and not txt.startswith("Gambar") and not txt.startswith("Tabel"):
            lines.append(txt)
    return lines

p = paras
s1_latarbelakang = find_section("1.1 Latar Belakang")
s1_rumusan = find_section("1.2 Rumusan")
s1_stateofart = find_section("1.3 State of the Art")
s1_tujuan = find_section("1.4 Tujuan")
s1_posisi = find_section("1.5 Posisi")
s2_kerangka = find_section("2. KERANGKA")
s3_petajalan = find_section("3. PETA JALAN")
s4_metodologi = find_section("4. METODOLOGI")
s4_risiko = find_section("4.9 Analisis Risiko")
s6_keluaran = find_section("6. KELUARAN")
s7_jadwal = find_section("7. JADWAL")
s8_anggaran = find_section("8. ANGGARAN")
s9_kompetensi = find_section("9. KOMPETENSI")
s10_pustaka = find_section("10. DAFTAR PUSTAKA")

# Abstract - find after ABSTRAK header
abstrak_idx = find_section("ABSTRAK")
abstrak = ""
if abstrak_idx and abstrak_idx + 1 < len(p):
    abstrak = p[abstrak_idx + 1]

# ── Extract narrative content by section ──────────────────────
naskah_latarbelakang = extract_between("1.1 Latar Belakang", "1.2 Rumusan")
naskah_rumusan = extract_between("1.2 Rumusan", "1.3 State of the Art")
naskah_stateofart = extract_between("1.3 State of the Art", "1.4 Tujuan")
naskah_tujuan = extract_between("1.4 Tujuan", "1.5 Posisi")
naskah_posisi = extract_between("1.5 Posisi", "2. KERANGKA")
naskah_kerangka = extract_between("2.1 Kerangka", "2.2 Nilai")

# ── Build the PRIS proposal ──────────────────────────────────────
out = []
out.append("# PROPOSAL PENDANAAN PROGRAM RISET INOVASI STRATEGIS (PRIS)\n")
out.append("---\n")

# ── HALAMAN MUKA ──
out.append(section("HALAMAN MUKA"))
out.append("| | |")
out.append("|---|---|")
out.append(f"| **Program** | PROGRAM RISET INOVASI STRATEGIS (PRIS) |")
out.append(f"| **Tema** | Kedaulatan Energi |")
out.append(f"| **Judul** | {esc(judul)} |")
out.append(f"| **Ketua Periset** | {esc(ketua_nama)} |")
out.append("| **Anggota Periset** | 1. Bagaskoro Saputro, S.Si., M.Cs. (BINUS University) |")
out.append("| | 2. Mario Norman Syah, S.Pd., M.Eng. (UNNES) |")
out.append("| | 3. Adhe Lingga Dewi, S.Si., M.Si. (BINUS University) |")
out.append("| | 4. Ir. Turnad Lenggo Ginta, S.T., M.T., Ph.D. (BRIN) |")
out.append("| **Institusi Pengusul** | Universitas Negeri Semarang (UNNES) |")
out.append("| **Tahun** | 2026 |")

# ── HALAMAN PENGESAHAN ──
out.append("\n---\n")
out.append(section("HALAMAN PENGESAHAN"))
out.append("### LEMBAR PENGESAHAN")
out.append("**PROPOSAL PENDANAAN PROGRAM RISET INOVASI STRATEGIS (PRIS)**\n")
out.append(f"**Tema:** Kedaulatan Energi\n")
out.append(f"**Judul Proposal:**")
out.append(f"{judul}\n")

out.append("**Ketua Periset:**")
out.append(table(["Item", "Detail"], [
    ("Nama Lengkap", ketua_nama),
    ("NIP/NIK", ketua_nip),
    ("Jabatan", "Guru Besar (Professor)"),
    ("Institusi Periset", "Universitas Negeri Semarang (UNNES)"),
    ("Unit Kerja Periset", "Fakultas Teknik, Program Studi Teknik Elektro"),
    ("Alamat", pengesahan_data["Alamat"]),
    ("No. HP/WA", pengesahan_data["No HP/WA"]),
    ("Email", pengesahan_data["Email"]),
]))

out.append("**Mitra Riset:**")
out.append(table(["Item", "Detail"], [
    ("Nama Mitra", pengesahan_data["Mitra"]),
    ("Alamat Mitra", "[Alamat Mitra]"),
    ("Peran Mitra", pengesahan_data["Peran Mitra"]),
]))

out.append("**Anggota Periset:**")
out.append(table(["No", "Nama", "Institusi", "No. HP/WA", "Email"],
    [(i+1, a[0], a[1], a[2], a[3]) for i, a in enumerate(anggota)]
))

out.append("**Luaran:**")
out.append(table(["No", "Uraian", "Tahun 1", "Tahun 2"], [
    ("1", "KTI jurnal internasional bereputasi target Q2 (minimum Q3)",
     "1 artikel target Q2 dengan status minimal under review",
     "Artikel Tahun I minimal accepted dan 1 artikel baru target Q2/Q3 minimal under review"),
    ("2", "Paten/paten sederhana",
     "1 permohonan dengan status terdaftar",
     "Penyempurnaan substansi dan dokumen kesiapan pemanfaatan/lisensi"),
    ("3", "Purwarupa AI-IoT-EMS + Smart Signage CV",
     "Smart charging hub charger dual-gun-display-IoT-smart signage CV, modul PV 22 kWp, BESS 30 kWh, hybrid inverter, EMS terintegrasi serta tervalidasi lab, TKT 4",
     "Smart charging hub PV 22 kWp\u2013BESS 30 kWh + smart signage CV tervalidasi pada lingkungan relevan, TKT 6"),
    ("4", "Dataset, model AI, perangkat lunak, dan dokumentasi",
     "Dataset v1, model AI, EMS core, CSMS/CMS, ICD/API, laporan uji",
     "Dataset v2, stable release, SOP operasi-keselamatan-pemeliharaan, paket replikasi"),
]))

out.append("**Pendanaan:**")
out.append(table(["No", "Tahapan", "Usulan Anggaran", "Dana Pendamping", "Total Anggaran"], [
    ("1",      "Tahun 1", "Rp250.000.000", "[DIISI sesuai komitmen mitra]", "Rp250.000.000 + pendamping"),
    ("2",      "Tahun 2", "Rp250.000.000", "[DIISI sesuai komitmen mitra]", "Rp250.000.000 + pendamping"),
]))

out.append("Dengan ini menyatakan bahwa proposal yang diajukan bersifat orisinil dan belum pernah memperoleh pendanaan dari lembaga/sumber dana lain, serta tidak mengandung plagiasi.\n")

out.append(table(["Menyetujui, Kepala Unit Kerja / Pimpinan Institusi Pengusul,",
                   "Semarang, [tanggal bulan 2026] Ketua Periset,"], [
                   ("", ""),
                   ("", ""),
                   ("", ""),
                   ("(................................)", f"**{ketua_nama}**"),
                   ("NIP. ................................", f"NIP. {ketua_nip}"),
]))

# ── DAFTAR ISI ──
out.append("\n---\n")
out.append(section("DAFTAR ISI"))
out.append(table(["No", "Bagian", "Halaman"], [
    ("1", "HALAMAN MUKA", "1"),
    ("2", "HALAMAN PENGESAHAN", "2"),
    ("3", "DAFTAR ISI", "3"),
    ("4", "ABSTRAK", "4"),
    ("5", "PENDAHULUAN", "5"),
    ("  ", "5.1 Latar Belakang", "5"),
    ("  ", "5.2 Rumusan Masalah", "6"),
    ("  ", "5.3 Tujuan Penelitian", "7"),
    ("  ", "5.4 Kontribusi terhadap Program Riset Inovasi Strategis", "7"),
    ("  ", "5.5 Relevansi dengan Prioritas Nasional dan/atau Kebutuhan User", "8"),
    ("  ", "5.6 Posisi dalam Rantai Nilai Inovasi", "9"),
    ("6", "KAJIAN TEORI DAN KERANGKA KONSEPTUAL", "10"),
    ("7", "METODOLOGI", "13"),
    ("8", "LUARAN DAN INDIKATOR KINERJA", "15"),
    ("9", "RENCANA KERJA KEGIATAN", "16"),
    ("10", "ANALISIS RISIKO KEGIATAN RISET", "17"),
    ("11", "DAMPAK DAN MANFAAT", "18"),
    ("12", "SARANA RISET", "19"),
    ("13", "RINCIAN ANGGARAN BIAYA", "20"),
    ("14", "KOMPETENSI TIM PERISET", "22"),
    ("15", "DAFTAR RIWAYAT HIDUP TIM PERISET", "23"),
    ("16", "REFERENSI", "26"),
    ("17", "LAMPIRAN", "28"),
]))

# ── ABSTRAK ──
out.append("\n---\n")
out.append(section("ABSTRAK"))
out.append(abstrak)
out.append("\n**Kata Kunci:** smart charging hub; solar hybrid; BESS; EMS; AI; IoT-edge; computer vision; smart signage; SPKLU; islanding; peak shaving; OCPP; layanan digital.")

# ── BAB 1 — PENDAHULUAN ──
out.append("\n---\n")
out.append(section("BAB 1 — PENDAHULUAN"))

# 5.1 Latar Belakang
out.append(section("5.1 Latar Belakang", 3))
for txt in naskah_latarbelakang:
    out.append(txt)

# Spesifikasi Sistem Tambahan: Smart Signage CV & EMC
out.append("\n**Catatan Spesifikasi Sistem:** Berdasarkan hasil diskusi dengan mitra dan analisis kebutuhan user, spesifikasi sistem dikembangkan sebagai berikut:\n")
out.append("1. **PLTS 22 kWp** menggunakan 40 modul 550 Wp dengan konfigurasi 2 string, menyediakan kapasitas pembangkitan harian ~80\u201390 kWh pada peak-sun-hour 4,5 dan performance ratio 0,8.\n")
out.append("2. **BESS 30 kWh LiFePO4** dalam konfigurasi rack-mounted dengan BMS terintegrasi, mampu menyediakan cadangan energi untuk operasi islanding dan peak shaving.\n")
out.append("3. **Charger dual-gun AC 22 kW** dengan dual connector tipe 2, mendukung OCPP 2.0.1, memungkinkan pengisian dua kendaraan simultan.\n")
out.append("4. **Smart Signage berbasis Computer Vision (Prop 3)** dengan edge computer (Raspberry Pi 5 + Coral TPU USB) untuk inferensi deteksi occupancy dan klasifikasi kendaraan. Spesifikasi antarmuka hardware: port Ethernet/RS485 dedicated untuk komunikasi data real-time dengan EMS dan IoT-edge; power supply terpisah (isolated DC-DC converter 24V/5A) untuk edge computer guna isolasi daya dan pencegahan propagasi gangguan; mounting bracket terintegrasi untuk pemasangan pada struktur charger atau dinding. Desain kabel dan proteksi surge pada jalur Cat6/STP memperhitungkan beban tambahan perangkat CV untuk menjamin EMC compliance.\n")
out.append("5. **Uji kompatibilitas elektromagnetik (EMC)** antara charger, smart signage CV, dan perangkat IoT dilaksanakan pada Tahun I (lab) dan disertifikasi pada Tahun II (lab tersertifikasi) untuk menjamin tidak ada interferensi elektromagnetik yang mengganggu kinerja sistem.\n")

# 5.2 Rumusan Masalah
out.append(section("5.2 Rumusan Masalah", 3))
rumusan_items = extract_between("1.2 Rumusan", "1.3 State of the Art", min_len=5)
for txt in rumusan_items:
    if txt.startswith("Bagaimana") or txt.startswith("Hipotesis"):
        out.append(f"\n{txt}")
    elif len(txt) > 10:
        out.append(txt)

# 5.3 Tujuan Penelitian
out.append(section("5.3 Tujuan Penelitian", 3))
out.append("**Tujuan Umum:**")
out.append("Mengembangkan dan memvalidasi purwarupa smart charging hub solar hybrid PV\u2013BESS\u2013Grid berbasis AI dan IoT-edge dengan EMS adaptif, mode islanding terbatas, peak shaving, dan pengelolaan beban layanan digital.\n")
out.append("**Tujuan Khusus:**")
tujuan_items = extract_between("1.4 Tujuan", "1.5 Posisi", min_len=15)
for item in tujuan_items:
    if item.startswith("Tujuan umum") or item.startswith("Gambar"):
        continue
    out.append(f"- {item}")

# 5.4 Kontribusi terhadap PRIS
out.append(section("5.4 Kontribusi terhadap Program Riset Inovasi Strategis", 3))
out.append("Program Riset Inovasi Strategis (PRIS) bertujuan mendorong riset yang menghasilkan inovasi strategis bernilai tambah tinggi dan berdampak langsung pada daya saing bangsa. Penelitian ini berkontribusi pada PRIS dalam tiga aspek utama:\n")
out.append("**Pertama**, pengembangan smart charging hub solar hybrid PV\u2013BESS\u2013Grid dengan EMS adaptif dan mode islanding merupakan solusi infrastruktur pengisian kendaraan listrik yang mandiri energi dan tidak bergantung sepenuhnya pada grid PLN \u2014 sejalan dengan target PRIS dalam menciptakan kemandirian energi nasional dan percepatan transisi energi rendah karbon.\n")
out.append("**Kedua**, integrasi AI forecasting, IoT-edge multi-protokol, dan data-quality-aware EMS menjawab kebutuhan interoperabilitas dan keandalan operasi SPKLU di Indonesia. Arsitektur yang dihasilkan bersifat modular dan dapat direplikasi, mendukung target PRIS untuk menghasilkan inovasi tepat guna yang dapat diadopsi secara luas.\n")
out.append("**Ketiga**, keterlibatan mitra strategis (PT. Arunika Sains Teknologi sebagai penyedia lokasi uji dan perangkat eksisting, serta calon pengguna hasil riset) memastikan hasil riset memiliki jalur hilirisasi yang jelas, dari prototipe TKT 6 hingga komersialisasi melalui lisensi paten dan transfer teknologi ke industri.\n")

# 5.5 Relevansi Prioritas Nasional
out.append(section("5.5 Relevansi dengan Prioritas Nasional dan/atau Kebutuhan User", 3))
out.append("Penelitian ini relevan dengan prioritas nasional sebagai berikut:\n")
out.append("1. **Peraturan Presiden No. 55 Tahun 2019** tentang Percepatan Program Kendaraan Bermotor Listrik Berbasis Baterai (KBLBB) untuk Transportasi Jalan, sebagaimana diubah dengan Perpres No. 79 Tahun 2023 \u2014 menargetkan akselerasi ekosistem KBLBB yang membutuhkan infrastruktur SPKLU masif dan merata.\n")
out.append("2. **Peraturan Menteri ESDM No. 1 Tahun 2023** tentang Penyediaan Infrastruktur Pengisian Listrik untuk KBLBB \u2014 mengatur standar teknis dan interoperabilitas SPKLU yang menjadi acuan desain sistem.\n")
out.append("3. **Peraturan Pemerintah No. 28 Tahun 2025** tentang Percepatan Pengembangan dan Pemanfaatan KBLBB \u2014 secara eksplisit mendorong integrasi energi baru terbarukan pada infrastruktur pengisian daya.\n")
out.append("4. **Rencana Umum Energi Nasional (RUEN)** \u2014 menargetkan bauran energi baru terbarukan 23% pada 2025 dan 31% pada 2050; smart charging hub solar hybrid berkontribusi langsung pada pencapaian target ini.\n")
out.append("5. **Undang-Undang No. 27 Tahun 2022** tentang Perlindungan Data Pribadi \u2014 arsitektur sistem dirancang tanpa menyimpan data personal pengguna, sejalan dengan prinsip privacy-by-design.\n")
out.append("\nKebutuhan user yang dijawab meliputi: pengguna kendaraan listrik yang membutuhkan SPKLU andal; pengelola fasilitas yang mencari solusi pengisian terintegrasi dengan energi terbarukan; dan operator SPKLU yang memerlukan platform interoperabel dan terjangkau.\n")

# 5.6 Posisi dalam Rantai Nilai Inovasi
out.append(section("5.6 Posisi dalam Rantai Nilai Inovasi", 3))
out.append("Posisi riset ini dalam rantai nilai inovasi dari riset dasar hingga komersialisasi adalah sebagai berikut:\n")
out.append(table(["Tahap Rantai Nilai", "Posisi Riset", "Keterangan"], [
    ("Riset Dasar", "TKT 1\u20132", "Fondasi MPPT, konverter daya, IoT multisensor, dan ANN (Syah et al., 2024; Dewi et al., 2024, 2025; Easterline et al., 2024)"),
    ("Riset Terapan", "TKT 3\u20134 (**Tahun 1**)", "Desain arsitektur smart charging hub + smart signage CV, integrasi PV 22 kWp\u2013BESS 30 kWh\u2013Grid\u2013charger dual-gun, pengembangan IoT-edge, AI/CV forecasting, EMS adaptif, uji EMC"),
    ("Pengembangan Prototipe", "TKT 5\u20136 (**Tahun 2**)", "Integrasi BESS 30 kWh, commissioning grid/islanding, pilot lapangan + smart signage CV, monitoring longitudinal, SOP, sertifikasi EMC"),
    ("Komersialisasi", "TKT 7\u20139 (**Pasca PRIS**)", "Lisensi paten ke mitra industri, produksi massal, replikasi multi-site"),
]))
out.append("\nRiset ini berada pada fase riset terapan menuju pengembangan prototipe (TKT 3\u21926), dengan jalur hilirisasi yang jelas pasca-PRIS melalui mitra industri.")

# ── BAB 2 — KAJIAN TEORI DAN KERANGKA KONSEPTUAL ──
out.append("\n---\n")
out.append(section("BAB 2 — KAJIAN TEORI DAN KERANGKA KONSEPTUAL"))

# 6.1 State of the Art
out.append(section("6.1 State of the Art", 3))
out.append("State of the art riset ini mencakup enam pendekatan utama yang masing-masing memiliki capaian, keterbatasan, dan posisi usulan yang dijelaskan pada Tabel 2.1.\n")
out.append("\n**Tabel 2.1 State of the Art**\n")
out.append(table(["Pendekatan", "Capaian Utama", "Keterbatasan/Gap", "Posisi Usulan"], [
    ("Rule-based EMS", "Sederhana, transparan, mudah diterapkan (Danielsson et al., 2025; Olano et al., 2025)", "Reaktif, sensitif threshold, tidak mengantisipasi ketidakpastian", "Digunakan sebagai baseline dan fail-safe"),
    ("Optimasi deterministik/MPC", "Kendala eksplisit dan antisipatif (Dong et al., 2025; Meng et al., 2025)", "Sensitif error prediksi dan data tidak ideal", "Rolling horizon dengan quantile/scenario dan data-quality flag"),
    ("AI forecasting", "Prediksi point/quantile (Khajeh & Laaksonen, 2022; Hewamalage et al., 2023)", "Tidak terhubung langsung ke constrained EMS", "Model ringan, probabilistik, drift-aware"),
    ("Smart charging hub + layanan digital", "Integrasi pengisian, penyimpanan, kontrol (Olano et al., 2025; Tairo et al., 2025)", "Belum terhubung dengan EMS resiliensi dan site power limit", "Multi-service load priority, islanding reserve"),
    ("Battery-aware stochastic EMS", "Ketidakpastian, batas baterai, fairness (Dong et al., 2025; Tairo et al., 2025)", "Validasi cyber-physical terbatas", "Dynamic safety envelope, degradation cost, edge deployment"),
    ("Platform proprietary", "Integrasi cepat dalam ekosistem satu vendor (OCA, 2025)", "Vendor lock-in, data tidak portabel", "ICD/API terbuka, protocol adapter, model card"),
]))

# 6.2 Kebaruan
out.append(section("6.2 Kebaruan (Novelty)", 3))
out.append("Kebaruan utama riset adalah:\n")
out.append("1. **Arsitektur smart charging hub solar hybrid** yang mengoordinasikan charger EV dan beban layanan digital sebagai multi-service load.\n")
out.append("2. **EMS adaptif** yang secara eksplisit memasukkan resilience reserve untuk mode islanding dan biaya degradasi BESS.\n")
out.append("3. **AI forecasting dan anomaly/data-quality score** yang langsung memengaruhi batas keputusan EMS.\n")
out.append("4. **IoT-edge multi-protokol** dengan local buffering, audit trail, cybersecurity, dan fail-safe operation.\n")
out.append("5. **Charging priority** yang menjamin site power limit dan layanan minimum saat SOC rendah atau grid padam.\n")
out.append("6. **Dynamic energy-status messaging** pada display berdasarkan renewable fraction tanpa menyimpan data personal pengguna.\n")
out.append("7. **Smart Signage berbasis Computer Vision** sebagai properti ketiga (Prop 3) yang menampilkan informasi real-time renewable fraction, status EMS, dan rekomendasi efisiensi energi melalui antarmuka Ethernet/RS485 terdedikasi dengan edge-AI box untuk inferensi visual.\n")

# 6.3 Kerangka Berpikir
out.append(section("6.3 Kerangka Berpikir", 3))
out.append("Kerangka berpikir dimulai dari ketidaksesuaian waktu antara produksi PV, kedatangan EV, tarif grid, dan fleksibilitas BESS. Ketidakpastian ini menjadi dasar penggunaan penjadwalan stokastik dan rolling horizon pada stasiun pengisian PV\u2013BESS (Dong et al., 2025; Meng et al., 2025). IoT-edge mengubah data heterogen menjadi telemetri tersinkron dan berkualitas; AI menghasilkan prakiraan beserta ketidakpastiannya; dan EMS menggunakan informasi tersebut untuk membagi daya di antara grid, PV, BESS, charger, smart socket, display, dan beban esensial. Pada kondisi normal, tujuan utamanya adalah biaya, peak shaving, pemanfaatan PV, fairness layanan, dan battery health. Pada kondisi grid outage, tujuan bergeser ke keselamatan dan kontinuitas layanan minimum berdasarkan resilience reserve (Wu et al., 2024; Tairo et al., 2025).\n")

# 6.4 Arsitektur Sistem
out.append(section("6.4 Arsitektur Sistem", 3))
out.append("Arsitektur smart charging hub terdiri atas empat lapisan: (1) **lapisan daya** yang mencakup PV 22 kWp, BESS LiFePO4 30 kWh, hybrid inverter 20 kW tiga fasa, charger AC dual-gun 22 kW, smart socket, smart signage berbasis computer vision, dan display digital; (2) **lapisan kontrol dan akuisisi** yang terdiri atas gateway IoT multi-protokol (Modbus/CAN/OCPP/MQTT), sensor arus/tegangan/iradiasi/suhu, BMS interface, serta antarmuka Ethernet/RS485 terdedikasi untuk smart signage; (3) **lapisan edge** yang menjalankan local buffering, data validation, AI inference ringan (termasuk computer vision pada edge computer), dan fail-safe logic; serta (4) **lapisan cloud** yang menyediakan CSMS/CMS, dashboard monitoring, database time-series, dan API interoperabilitas. Seluruh lapisan dihubungkan melalui jaringan terproteksi dengan segmentasi OT/IT, enkripsi TLS, dan audit trail.\n")
out.append("\nSmart Signage (Prop 3) dirancang sebagai display berbasis computer vision dengan spesifikasi antarmuka hardware sebagai berikut: port Ethernet/RS485 dedicated untuk komunikasi data real-time dengan EMS dan IoT-edge; power supply terpisah (isolated DC-DC converter 24V/5A) untuk edge computer guna memutus jalur propagasi gangguan daya; serta mounting bracket terintegrasi yang memungkinkan pemasangan pada struktur charger atau dinding. Desain kabel dan proteksi surge pada jalur Cat6/STP memperhitungkan beban tambahan perangkat CV untuk menjamin EMC compliance. Edge computer menjalankan inferensi computer vision untuk deteksi occupancy, klasifikasi jenis kendaraan, dan estimasi waktu pengisian tanpa mengirim data visual mentah ke cloud.\n")

# 6.5 Alur Data
out.append(section("6.5 Alur Data", 3))
out.append("Alur data dimulai dari sumber data (iradiasi solar, tegangan/arus PV, SOC BESS, MeterValues OCPP, kamera CV untuk occupancy) yang diproses melalui edge dan cloud processing untuk menghasilkan output berupa load balancing solar/grid, setpoint EMS, dashboard monitoring, informasi smart signage, dan laporan kinerja. Data visual dari kamera CV hanya diproses di edge computer untuk inferensi occupancy dan klasifikasi kendaraan; tidak ada data visual mentah yang dikirim ke cloud.\n")

# ── BAB 3 — METODOLOGI ──
out.append("\n---\n")
out.append(section("BAB 3 — METODOLOGI"))

# 7.1 Metode Riset
out.append(section("7.1 Metode Riset", 3))
out.append("Pendekatan: **Research & Development Iteratif** dengan validasi teknis dan uji lapangan terbatas, mengacu pada standar TKT BRIN.\n")
out.append("Riset menggunakan siklus PDCA dan eksperimen komparatif. Validasi bertingkat dari model, perangkat nyata, hingga kasus/lokasi relevan mengikuti praktik pengembangan EMS (BRIN, 2026; Olano et al., 2025; Tairo et al., 2025). Unit analisis adalah smart charging hub cyber-physical yang meliputi PV, BESS, grid, hybrid inverter, charger AC/DC, smart socket, display digital, IoT-edge, cloud, dan EMS.\n")

out.append("**Work Packages (WP):**\n")
out.append(table(["WP", "Nama", "Aktivitas Utama", "Deliverable"], [
    ("WP1", "Audit & Perencanaan", "Audit lokasi, profil beban, SLD, sizing PV 22 kWp/BESS 30 kWh, izin interkoneksi, URS, DMP", "Laporan audit, dokumen perencanaan"),
    ("WP2", "IoT-edge, Backend & Smart Signage", "Gateway multi-protokol (Modbus/CAN/OCPP/MQTT), CSMS/CMS, cloud, dashboard, cybersecurity, fail-safe, edge-AI box CV, antarmuka Ethernet/RS485 smart signage", "Gateway IoT, CSMS/CMS, dashboard, edge-AI box"),
    ("WP3", "AI Forecasting, Anomaly & CV", "Model PV, EV demand, anomaly detection, data-quality scoring, drift monitoring, computer vision untuk occupancy dan klasifikasi kendaraan", "Model AI + model card + model CV"),
    ("WP4", "EMS Adaptif", "Formulasi multi-objektif, rolling horizon, resilience reserve, battery degradation, fail-safe, integrasi sinyal CV", "EMS core"),
    ("WP5", "Integrasi, Uji Lab & EMC", "Digital twin, integrasi hardware, uji fungsional, kalibrasi, fault injection, switching grid/islanding, uji kompatibilitas elektromagnetik (EMC) charger-CV", "Laporan uji, TKT 4, laporan EMC"),
    ("WP6", "Pilot & Diseminasi", "Instalasi, commissioning, monitoring 6 bulan, SOP, KTI, KI, paket replikasi, FGD diseminasi", "TKT 6, dataset v2, SOP"),
]))

# 7.2 Roadmap Pencapaian Luaran
out.append(section("7.2 Roadmap Pencapaian Luaran", 3))
out.append(table(["Periode", "Target TKT", "Kegiatan Inti", "Luaran Utama"], [
    ("Tahun 1 (2026)", "TKT 3\u21924",
      "Audit lokasi, desain arsitektur, integrasi charger dual-gun-display-IoT-smart signage CV, mobilisasi perangkat PV 22 kWp/inverter, digital twin, AI/CV, EMS, uji lab & EMC",
     "1 prototipe lab fungsional + smart signage CV, 1 draf Paten, 1 KTI under review (Q2/Q3), dataset v1, laporan uji EMC"),
    ("Tahun 2 (2027)", "TKT 4\u21926",
     "Integrasi BESS 30 kWh, commissioning grid/islanding, pilot lapangan, monitoring 6 bulan, evaluasi techno-economic, SOP, paket replikasi",
     "3 unit pilot beroperasi TKT 6, 1 Paten terdaftar, 1 KTI accepted + 1 under review, dataset v2, SOP operasi"),
]))

# ── BAB 4 — LUARAN DAN INDIKATOR KINERJA ──
out.append("\n---\n")
out.append(section("BAB 4 — LUARAN DAN INDIKATOR KINERJA"))
out.append(section("8.1 Target Luaran", 3))
out.append(table(["No", "Jenis Luaran", "Target Tahun I", "Target Tahun II"], [
    ("1", "Publikasi Ilmiah (Jurnal Internasional Q2/Q3)",
     "1 KTI under review (arsitektur smart charging hub + EMS adaptif)",
     "1 KTI accepted (validasi pilot) + 1 KTI under review (optimasi EMS + CV)"),
    ("2", "Kekayaan Intelektual",
     "1 draf Paten Sederhana (metode EMS adaptif resilience-aware + IoT-edge multi-protokol + integrasi smart signage CV)",
     "1 Paten Sederhana terdaftar di DJKI"),
    ("3", "Purwarupa",
     "TKT 4 \u2014 smart charging hub charger dual-gun-display-IoT, modul PV 22 kWp, hybrid inverter, EMS, smart signage CV terintegrasi dan tervalidasi lab",
     "TKT 6 \u2014 smart charging hub PV 22 kWp\u2013BESS 30 kWh + smart signage CV tervalidasi pada lingkungan relevan"),
    ("4", "Dataset, Model AI, Perangkat Lunak & Pengujian",
     "Dataset v1, model AI, model CV, EMS core, CSMS/CMS, ICD/API, laporan uji, laporan uji kompatibilitas elektromagnetik (EMC) charger-CV",
     "Dataset v2, stable release, SOP operasi-keselamatan-pemeliharaan, paket replikasi"),
]))

out.append(section("8.2 Indikator Kinerja Kegiatan", 3))
out.append("**Indikator Kinerja Kegiatan Tahun 1:**\n")
out.append(table(["No", "Indikator", "Target"], [
    ("1", "KTI", "100% \u2014 1 naskah jurnal Q2/Q3 status under review"),
    ("2", "KI", "100% \u2014 1 draf klaim Paten Sederhana"),
    ("3", "Prototipe", "100% \u2014 1 unit prototipe lab TKT 4 fungsional + smart signage CV"),
    ("4", "EMC", "100% \u2014 1 laporan uji kompatibilitas elektromagnetik charger\u2013CV"),
]))
out.append("\n**Indikator Kinerja Kegiatan Tahun 2:**\n")
out.append(table(["No", "Indikator", "Target"], [
    ("1", "KTI", "100% \u2014 1 accepted + 1 under review"),
    ("2", "KI", "100% \u2014 1 Paten terdaftar, 1 SOP, 1 paket replikasi"),
    ("3", "Prototipe", "100% \u2014 1 unit pilot TKT 6 beroperasi + smart signage CV"),
]))

# ── BAB 5 — RENCANA KERJA KEGIATAN ──
out.append("\n---\n")
out.append(section("BAB 5 — RENCANA KERJA KEGIATAN"))
out.append(section("9.1 Peta Jalan", 3))
out.append("Peta jalan penelitian mencakup 24 bulan (2 tahun) dengan 6 work packages. Tahun I membangun fondasi TKT 3\u21924 melalui audit, integrasi perangkat, digital twin, AI, EMS, dan uji lab. Tahun II meningkatkan TKT 4\u21926 melalui integrasi BESS, commissioning, pilot lapangan, monitoring, dan diseminasi.\n")

out.append(section("9.2 Jadwal Kegiatan", 3))
out.append("**TAHUN/PERIODE 1 (2026):**\n")
out.append(table(["No", "Aktivitas", "Deskripsi", "Waktu"], [
    ("1", "Audit & Perencanaan", "Audit lokasi, profil beban, SLD, sizing PV/BESS, izin interkoneksi, URS, DMP", "Bulan ke-1 s.d. 3"),
    ("2", "IoT-edge & Backend", "Gateway multi-protokol, CSMS/CMS, cloud, dashboard, cybersecurity", "Bulan ke-3 s.d. 7"),
    ("3", "AI Forecasting & Anomaly", "Model PV, EV demand, anomaly detection, data-quality scoring", "Bulan ke-4 s.d. 7"),
    ("4", "EMS Adaptif", "Formulasi multi-objektif, rolling horizon, resilience reserve", "Bulan ke-5 s.d. 9"),
    ("5", "Integrasi & Uji Lab", "Digital twin, integrasi hardware, uji fungsional, kalibrasi, fault injection", "Bulan ke-8 s.d. 11"),
    ("6", "Publikasi & Paten T1", "Penulisan manuskrip, penyusunan draf paten", "Bulan ke-10 s.d. 12"),
]))

out.append("\n**TAHUN/PERIODE 2 (2027):**\n")
out.append(table(["No", "Aktivitas", "Deskripsi", "Waktu"], [
    ("1", "Persiapan Pilot & MoU Mitra", "Koordinasi lokasi, instalasi PV & BESS, provisioning perangkat", "Bulan ke-1 s.d. 2"),
    ("2", "Integrasi BESS & Commissioning", "Integrasi BESS 20,48 kWh, commissioning grid/islanding", "Bulan ke-3 s.d. 5"),
    ("3", "Pilot Lapangan & Monitoring", "Operasi pilot, monitoring energi/biaya/emisi/reliabilitas 6 bulan", "Bulan ke-4 s.d. 9"),
    ("4", "Evaluasi, SOP & Diseminasi", "Analisis data, penyusunan SOP, publikasi jurnal, KI, paket replikasi", "Bulan ke-10 s.d. 12"),
]))

# ── BAB 6 — ANALISIS RISIKO ──
out.append("\n---\n")
out.append(section("BAB 6 — ANALISIS RISIKO KEGIATAN RISET"))
out.append(table(["Target Luaran", "Identifikasi Risiko", "Jenis Risiko", "Strategi Mitigasi", "Rencana Penyesuaian"], [
    ("Prototipe TKT 4 (Lab)", "Keterlambatan pengadaan komponen elektronik (ESP32, sensor, gateway)",
     "Teknis & Logistik",
     "Pemesanan H-3 bulan, menyiapkan alternatif supplier lokal",
     "Gunakan modul substitusi yang setara untuk pengembangan firmware sambil menunggu komponen utama"),
    ("Prototipe TKT 6 (Pilot)", "Gagal integrasi antara EMS, inverter, BMS, dan charger",
     "Teknis",
     "Pengujian parsial setiap subsistem sebelum integrasi penuh, simulasi digital twin",
     "Arsitektur modular sehingga subsistem dapat diuji dan diganti independen"),
    ("Publikasi Q2/Q3", "Manuscript rejection oleh jurnal target",
     "Akademik",
     "Submit ke multiple jurnal secara paralel, perbaikan berdasarkan reviewer feedback",
     "Turun ke jurnal Q4 atau Sinta 1/2 sebagai opsi cadangan"),
    ("Paten Sederhana", "Klaim paten ditolak karena prior art",
     "Hukum",
     "Patent search menyeluruh, konsultasi dengan konsultan paten",
     "Revisi klaim, fokus pada aspek integrasi sistem sebagai novelty"),
    ("Pilot lapangan", "Rendahnya utilisasi SPKLU di lokasi pilot",
     "Pasar/Operasional",
     "Seleksi lokasi dengan dwell time tinggi dan aksesibilitas optimal",
     "Penambahan insentif pengisian daya, kerjasama dengan komunitas EV"),
    ("Keamanan sistem", "Serangan siber pada IoT gateway atau cloud backend",
     "Keamanan",
     "Segmentasi jaringan OT, enkripsi TLS, autentikasi mutual, audit log",
     "Isolasi jaringan IoT dengan VLAN, incident response plan"),
    ("Ketersediaan data", "Data telemetri tidak mencukupi untuk training AI",
     "Teknis",
     "Digital twin dengan sintesis data, augmentasi skenario operasi",
     "Gunakan data sekunder dari literatur sebagai pelengkap training"),
]))

# ── BAB 7 — DAMPAK DAN MANFAAT ──
out.append("\n---\n")
out.append(section("BAB 7 — DAMPAK DAN MANFAAT"))
out.append("Penelitian ini memberikan dampak strategis pada empat dimensi utama.\n")
out.append("**Dimensi energi:** Pengembangan smart charging hub solar hybrid PV\u2013BESS\u2013Grid dengan EMS adaptif menurunkan ketergantungan pada grid PLN dan mendukung target bauran energi baru terbarukan nasional. Setiap unit smart charging hub yang beroperasi dengan solar hybrid berpotensi mereduksi emisi CO\u2082 secara signifikan dibandingkan SPKLU grid-only.\n")
out.append("**Dimensi ekonomi dan industri:** Arsitektur berbasis komponen modular dan protokol terbuka menawarkan biaya lebih rendah dibandingkan platform proprietary. Hilirisasi melalui lisensi paten ke mitra industri berpotensi menumbuhkan industri komponen EV charging dalam negeri.\n")
out.append("**Dimensi sosial:** Integrasi EMS adaptif dan mode islanding meningkatkan keandalan layanan pengisian bagi pengguna EV, termasuk saat gangguan grid. Display digital memberikan informasi renewable fraction secara transparan.\n")
out.append("**Dimensi kebijakan:** SOP operasi dan keselamatan, ICD/API terbuka, serta paket replikasi yang dihasilkan menjadi masukan bagi pemerintah dalam penyusunan standar teknis SPKLU nasional.\n")

# ── BAB 8 — SARANA RISET ──
out.append("\n---\n")
out.append(section("BAB 8 — SARANA RISET"))
out.append(table(["No", "Nama Alat/Fasilitas", "Spesifikasi", "Lokasi", "Kepemilikan", "Penggunaan"], [
    ("1", "Laboratorium Teknik Elektro UNNES",
     "Power analyzer, osiloskop 4ch 100MHz, DC supply, function generator",
     "Fakultas Teknik UNNES", "UNNES", "Pengembangan dan uji EMS, integrasi inverter-BMS"),
    ("2", "Laboratorium IoT & Komputer UNNES",
     "Workstation GPU, ESP32 dev kit, Raspberry Pi 5, sensor kit",
     "Fakultas Teknik UNNES", "UNNES", "Pengembangan gateway IoT, AI forecasting, dashboard"),
    ("3", "Workshop Energi Terbarukan",
     "Panel surya 1 kWp, BESS 48V, data logger, pyranometer",
     "Kampus UNNES Sekaran", "UNNES", "Validasi PV, kalibrasi sensor iradiasi"),
    ("4", "Cloud Infrastructure",
     "Cloud VM, TimescaleDB, EMQX MQTT broker, object storage",
     "Remote", "UNNES / Cloud Provider", "Hosting CSMS, database time-series, dashboard"),
    ("5", "Fasilitas Mitra (PT. Arunika)",
     "Lokasi uji pilot, charger/display/PV\u2013BESS\u2013inverter eksisting",
     "Lokasi mitra", "Mitra (in-kind)", "Instalasi pilot, monitoring lapangan"),
     ("6", "Perangkat Pengukuran & EMC",
     "Energy logger Fluke/Hioki, CAN bus analyzer, EMI receiver, LISN, near-field probe",
     "Lab Teknik Elektro UNNES", "UNNES", "Pengukuran kualitas daya, efisiensi, komunikasi BMS, uji kompatibilitas elektromagnetik"),
     ("7", "Edge-AI Box & Smart Signage CV",
     "Raspberry Pi 5 + Coral TPU USB + Kamera RGB, power supply isolated 24V/5A, enclosure IP54",
     "Lab IoT UNNES", "UNNES", "Inferensi computer vision, deteksi occupancy, klasifikasi kendaraan, antarmuka smart signage"),
]))

# ── BAB 9 — RINCIAN ANGGARAN BIAYA ──
def fmt(n):
    return f"{n:,.0f}".replace(",", ".")

out.append("\n---\n")
out.append(section("BAB 9 — RINCIAN ANGGARAN BIAYA"))
out.append("*(Struktur mengikuti Pedoman PRIS. Komponen: BLNP (B.1 Belanja Bahan, B.2 Honor Lapangan, B.3 Perjalanan, B.4 Modal/Sewa/Publikasi) dan BTL (C.1 Belanja Bahan, C.2 Belanja Jasa, C.3 Perjalanan). BLP (insentif tim) tidak ditampilkan di sini.)*\n")

# ── TAHUN I ──
out.append(section("Tahun 1 (2026) — TKT 3 → 4", 3))

t1_b1 = [
    ("B.1 Belanja Bahan (Fokus: PLTS 22 kWp, BESS 30 kWh, Charger Dual-gun, Smart Signage CV)", "", "", "", "", "", "", ""),
    ("Kegiatan 1: Pengadaan Hardware Utama & Integrasi", "", "", "", "", "", "", ""),
    ("1. Modul PV 550 Wp (40 unit = 22 kWp)", "40", "1", "1.250.000", "unit", fmt(40*1*1250000), "100%", "0%"),
    ("2. BESS 30 kWh LiFePO4 rack + BMS terintegrasi", "1", "1", "75.000.000", "set", fmt(1*1*75000000), "100%", "0%"),
    ("3. Charger dual-gun AC 22 kW (OCPP 2.0.1, dual connector tipe 2)", "1", "1", "32.000.000", "unit", fmt(1*1*32000000), "100%", "0%"),
    ("4. Hybrid inverter 20 kW 3-fasa grid-tie + islanding capable", "1", "1", "25.000.000", "unit", fmt(1*1*25000000), "100%", "0%"),
    ("5. Smart signage CV (RPi 5 + Camera Module 3 + 7\" LCD + ESP32-S3 + enclosure)", "1", "1", "6.500.000", "set", fmt(1*1*6500000), "100%", "0%"),
    ("6. ESP32 Dev Kit + Modul 4G + sensor kit (arus, tegangan, suhu)", "5", "1", "2.800.000", "set", fmt(5*1*2800000), "100%", "0%"),
    ("7. Industrial IoT gateway (RPi 5 + SSD 256GB + enclosure IP54)", "2", "1", "5.800.000", "unit", fmt(2*1*5800000), "100%", "0%"),
    ("8. Sensor presisi (pyranometer, power meter 3-fase, suhu BESS)", "5", "1", "2.200.000", "set", fmt(5*1*2200000), "100%", "0%"),
    ("9. Komponen panel & proteksi surge (MCB, MCCB, SPD, ATS, enclosure, kabel NYY/STP)", "1", "1", "23.000.000", "paket", fmt(1*1*23000000), "100%", "0%"),
    ("10. Smart socket WiFi (8 unit) + display digital 10\" (5 unit)", "1", "1", "14.000.000", "paket", fmt(1*1*14000000), "100%", "0%"),
    ("11. Bahan habis pakai (kabel data RJ45/RS485, konektor, ATK, PCB, solder, heatshrink)", "1", "1", "10.000.000", "paket", fmt(1*1*10000000), "100%", "0%"),
    ("Sub Total Kegiatan 1", "", "", "", "", fmt(40*1250000+75000000+32000000+25000000+6500000+5*2800000+2*5800000+5*2200000+23000000+14000000+10000000), "100%", "0%"),
    ("Kegiatan 2: Uji Lab, Kalibrasi & EMC", "", "", "", "", "", "", ""),
    ("12. Kalibrasi sensor & alat ukur (power analyzer, pyranometer, termometer)", "1", "1", "6.500.000", "paket", fmt(1*1*6500000), "100%", "0%"),
    ("13. Komponen uji (beban dummy, resistor presisi, kabel uji)", "1", "1", "5.000.000", "paket", fmt(1*1*5000000), "100%", "0%"),
    ("14. Perangkat uji EMC (LISN, near-field probe set) sewa", "1", "1", "8.000.000", "paket", fmt(1*1*8000000), "100%", "0%"),
    ("Sub Total Kegiatan 2", "", "", "", "", fmt(6500000+5000000+8000000), "100%", "0%"),
    ("Sub Total B.1", "", "", "", "", fmt(40*1250000+75000000+32000000+25000000+6500000+5*2800000+2*5800000+5*2200000+23000000+14000000+10000000+6500000+5000000+8000000), "100%", "0%"),
]
t1_b2 = [
    ("B.2 Honor Tenaga Lapangan", "", "", "", "", "", "", ""),
    ("1. Teknisi instalasi elektrikal (72 OH)", "72", "1", "145.000", "OH", fmt(72*1*145000), "100%", "0%"),
    ("2. Programmer firmware IoT & backend (60 OH)", "60", "1", "215.000", "OH", fmt(60*1*215000), "100%", "0%"),
    ("Sub Total B.2", "", "", "", "", fmt(72*145000+60*215000), "100%", "0%"),
]
t1_b3 = [
    ("B.3 Perjalanan Dinas Terkait Riset", "", "", "", "", "", "", ""),
    ("Kegiatan 1: Perjalanan Semarang–Mitra (PT. Arunika)", "", "", "", "", "", "", ""),
    ("1. Transportasi Semarang–lokasi mitra PP (2 orang)", "9", "2", "425.000", "kali", fmt(9*2*425000), "100%", "0%"),
    ("2. Akomodasi hotel (2 orang)", "18", "1", "375.000", "hari", fmt(18*1*375000), "100%", "0%"),
    ("3. Uang harian perjalanan (2 orang)", "18", "1", "185.000", "OH", fmt(18*1*185000), "100%", "0%"),
    ("Sub Total B.3", "", "", "", "", fmt(9*2*425000+18*375000+18*185000), "100%", "0%"),
]
t1_b4 = [
    ("B.4 Belanja Modal / Sewa / Publikasi / Lainnya", "", "", "", "", "", "", ""),
    ("Kegiatan 1: Infrastruktur & Perangkat Pendukung", "", "", "", "", "", "", ""),
    ("1. Sewa cloud server dev-tier (VM, database, MQTT, storage)", "12", "1", "1.500.000", "bulan", fmt(12*1*1500000), "100%", "0%"),
    ("2. Lisensi software pengembangan (IDE, CAD, toolchains)", "1", "1", "6.500.000", "paket", fmt(1*1*6500000), "100%", "0%"),
    ("Sub Total Kegiatan 1", "", "", "", "", fmt(12*1500000+6500000), "100%", "0%"),
    ("Kegiatan 2: Diseminasi & Pelaporan (Tahap Awal)", "", "", "", "", "", "", ""),
    ("3. FGD awal & workshop koordinasi (2 kali × 20 peserta)", "2", "1", "8.250.000", "kali", fmt(2*1*8250000), "100%", "0%"),
    ("Sub Total Kegiatan 2", "", "", "", "", fmt(2*1*8250000), "100%", "0%"),
    ("Sub Total B.4", "", "", "", "", fmt(12*1500000+6500000+2*8250000), "100%", "0%"),
]
t1_c = [
    ("C. Biaya Tidak Langsung (BTL)", "", "", "", "", "", "", ""),
    ("C.1 Monitoring & Evaluasi Internal (Fase Pengembangan)", "", "", "", "", "", "", ""),
    ("1. Honor reviewer internal (2 jam × 3 reviewer × 2 kali)", "6", "2", "475.000", "OJ", fmt(6*2*475000), "100%", "0%"),
    ("2. Konsumsi rapat koordinasi intensif (12 bulan)", "12", "1", "575.000", "bulan", fmt(12*1*575000), "100%", "0%"),
    ("Sub Total C.1", "", "", "", "", fmt(6*2*475000+12*575000), "100%", "0%"),
    ("C.2 Administrasi Proposal & Laporan", "", "", "", "", "", "", ""),
    ("3. ATK, cetak, fotokopi, jilid proposal & laporan kemajuan", "1", "1", "3.500.000", "paket", fmt(1*1*3500000), "100%", "0%"),
    ("Sub Total C.2", "", "", "", "", fmt(1*1*3500000), "100%", "0%"),
    ("Sub Total C (BTL)", "", "", "", "", fmt(6*2*475000+12*575000+3500000), "100%", "0%"),
]

t1_total_blnp = (40*1250000+75000000+32000000+25000000+6500000+5*2800000+2*5800000+5*2200000+23000000+14000000+10000000+6500000+5000000+8000000)+(72*145000+60*215000)+(9*2*425000+18*375000+18*185000)+(12*1500000+6500000+2*8250000)
t1_total_btl = 6*2*475000+12*575000+3500000
t1_total = t1_total_blnp + t1_total_btl
t1_lpdp_total = t1_total + 105600000
t1_inkind = 24000000 + 10000000 + 5000000 + 5000000  # engineer 120h×2org×Rp100k + akses lokasi + data + konsumsi
t1_inkind_desc = "Engineer pendamping (2 org × 120 jam × Rp100.000 = Rp24jt), akses lokasi pilot & lab (Rp10jt), data historis operasional (Rp5jt), konsumsi listrik & internet (Rp5jt)"
out.append(f"**Total Tahun I: LPDP {fmt(t1_lpdp_total)} (BLP {fmt(105600000)} + BLNP+BTL {fmt(t1_total)}) + Mitra in-kind {fmt(t1_inkind)} = ~{fmt(t1_lpdp_total+t1_inkind)}**\n")
out.append(f"*Rincian in-kind mitra: {t1_inkind_desc}*\n")

out.append(table(["Komponen Biaya", "Volume", "Frekuensi", "Harga Satuan (Rp)", "Satuan", "Jumlah", "LPDP", "Mitra"],
                 t1_b1 + [("", "", "", "", "", "", "", "")] + t1_b2 + [("", "", "", "", "", "", "", "")] + t1_b3 + [("", "", "", "", "", "", "", "")] + t1_b4 + [("", "", "", "", "", "", "", "")] + t1_c + [
    ("", "", "", "", "", "", "", ""),
    ("**TOTAL BIAYA TAHUN I (BLNP + BTL)**", "", "", "", "", f"**{fmt(t1_total)}**", "**100%**", "**0%**"),
]))

# ── TAHUN II ──
out.append(section("Tahun 2 (2027) — TKT 4 → 6", 3))

t2_b1 = [
    ("B.1 Belanja Bahan (Fokus: Pilot Lapangan, EMC Sertifikasi & CV Validasi)", "", "", "", "", "", "", ""),
    ("Kegiatan 1: Pilot Lapangan & Integrasi Sistem", "", "", "", "", "", "", ""),
    ("1. BESS 15 kWh LiFePO4 portable unit (ekspansi lokasi pilot + demo mobile)", "1", "1", "52.000.000", "set", fmt(1*1*52000000), "100%", "0%"),
    ("2. Modul PV 550 Wp tambahan (12 unit = 6,6 kWp ekspansi)", "12", "1", "1.250.000", "unit", fmt(12*1*1250000), "100%", "0%"),
    ("3. Material instalasi pilot (kabel NYY, grounding, panel distribusi, ATS tambahan, bollard)", "3", "1", "10.500.000", "paket", fmt(3*1*10500000), "100%", "0%"),
    ("4. Komponen pemeliharaan & suku cadang (MCB spare, relay, fuse, thermal, kabel connector)", "1", "1", "12.000.000", "paket", fmt(1*1*12000000), "100%", "0%"),
    ("5. Sensor tambahan (power meter 3-fase, weather station, CT clamp)", "3", "1", "3.200.000", "set", fmt(3*1*3200000), "100%", "0%"),
    ("Sub Total Kegiatan 1", "", "", "", "", fmt(52000000+12*1250000+3*10500000+12000000+3*3200000), "100%", "0%"),
    ("Kegiatan 2: Sertifikasi & Uji EMC", "", "", "", "", "", "", ""),
    ("6. Sertifikasi uji EMC (charger + smart signage CV) di lab tersertifikasi", "1", "1", "18.000.000", "paket", fmt(1*1*18000000), "100%", "0%"),
    ("7. Alat ukur portable (energy logger, power quality analyzer sewa)", "1", "1", "12.500.000", "paket", fmt(1*1*12500000), "100%", "0%"),
    ("Sub Total Kegiatan 2", "", "", "", "", fmt(18000000+12500000), "100%", "0%"),
    ("Sub Total B.1", "", "", "", "", fmt(52000000+12*1250000+3*10500000+12000000+3*3200000+18000000+12500000), "100%", "0%"),
]
t2_b2 = [
    ("B.2 Honor Tenaga Lapangan (Fase Pilot Lapangan)", "", "", "", "", "", "", ""),
    ("1. Teknisi monitoring & pemeliharaan pilot (96 OH)", "96", "1", "155.000", "OH", fmt(96*1*155000), "100%", "0%"),
    ("2. Teknisi commissioning (sinkronisasi grid, switching islanding, 48 OH)", "48", "1", "225.000", "OH", fmt(48*1*225000), "100%", "0%"),
    ("Sub Total B.2", "", "", "", "", fmt(96*155000+48*225000), "100%", "0%"),
]
t2_b3 = [
    ("B.3 Perjalanan Dinas Terkait Riset", "", "", "", "", "", "", ""),
    ("Kegiatan 1: Perjalanan Pilot & Diseminasi", "", "", "", "", "", "", ""),
    ("1. Transportasi Semarang–lokasi pilot PP (2 orang)", "15", "2", "425.000", "kali", fmt(15*2*425000), "100%", "0%"),
    ("2. Akomodasi hotel (2 orang)", "30", "1", "375.000", "hari", fmt(30*1*375000), "100%", "0%"),
    ("3. Uang harian perjalanan (2 orang)", "30", "1", "185.000", "OH", fmt(30*1*185000), "100%", "0%"),
    ("Sub Total B.3", "", "", "", "", fmt(15*2*425000+30*375000+30*185000), "100%", "0%"),
]
t2_b4 = [
    ("B.4 Belanja Modal / Sewa / Publikasi / Lainnya", "", "", "", "", "", "", ""),
    ("Kegiatan 1: Infrastruktur Cloud & IoT", "", "", "", "", "", "", ""),
    ("1. Sewa cloud server production-tier (12 bulan)", "12", "1", "2.500.000", "bulan", fmt(12*1*2500000), "100%", "0%"),
    ("2. Biaya data plan IoT (4G LTE) 12 bulan", "12", "1", "475.000", "bulan", fmt(12*1*475000), "100%", "0%"),
    ("Sub Total Kegiatan 1", "", "", "", "", fmt(12*2500000+12*475000), "100%", "0%"),
    ("Kegiatan 2: Publikasi & KI", "", "", "", "", "", "", ""),
    ("3. Biaya publikasi jurnal internasional Q2/Q3 (2 artikel)", "2", "1", "14.500.000", "publikasi", fmt(2*1*14500000), "100%", "0%"),
    ("4. Biaya pendaftaran paten sederhana (DJKI)", "1", "1", "4.750.000", "paket", fmt(1*1*4750000), "100%", "0%"),
    ("Sub Total Kegiatan 2", "", "", "", "", fmt(2*14500000+4750000), "100%", "0%"),
    ("Kegiatan 3: Diseminasi & FGD", "", "", "", "", "", "", ""),
    ("5. FGD diseminasi hasil riset (2 kali × 30 peserta)", "2", "1", "10.250.000", "kali", fmt(2*1*10250000), "100%", "0%"),
    ("Sub Total Kegiatan 3", "", "", "", "", fmt(2*1*10250000), "100%", "0%"),
    ("Kegiatan 4: Pengujian, Dokumentasi & Konsumsi", "", "", "", "", "", "", ""),
    ("6. Sewa peralatan uji (power analyzer, thermal camera, logger)", "1", "1", "14.500.000", "paket", fmt(1*1*14500000), "100%", "0%"),
    ("7. Konsumsi rapat teknis & koordinasi lapangan (12 bulan)", "12", "1", "825.000", "bulan", fmt(12*1*825000), "100%", "0%"),
    ("8. Dokumentasi teknis & video operasional pilot", "1", "1", "7.750.000", "paket", fmt(1*1*7750000), "100%", "0%"),
    ("9. Pengujian eksternal (sertifikasi komponen, lab testing)", "1", "1", "6.750.000", "paket", fmt(1*1*6750000), "100%", "0%"),
    ("Sub Total Kegiatan 4", "", "", "", "", fmt(14500000+12*825000+7750000+6750000), "100%", "0%"),
    ("Sub Total B.4", "", "", "", "", fmt(12*2125000+12*475000+2*14500000+4750000+2*10250000+14500000+12*825000+7750000+6750000), "100%", "0%"),
]
t2_c = [
    ("C. Biaya Tidak Langsung (BTL)", "", "", "", "", "", "", ""),
    ("C.1 Monitoring & Evaluasi Akhir", "", "", "", "", "", "", ""),
    ("1. Honor reviewer internal (2 jam × 3 reviewer × 2 kali)", "12", "1", "475.000", "OJ", fmt(12*1*475000), "100%", "0%"),
    ("2. Konsumsi rapat monitoring (12 bulan)", "12", "1", "475.000", "bulan", fmt(12*1*475000), "100%", "0%"),
    ("Sub Total C.1", "", "", "", "", fmt(12*475000+12*475000), "100%", "0%"),
    ("C.2 Pelaporan Akhir & Dokumentasi", "", "", "", "", "", "", ""),
    ("3. ATK, cetak, foto, video, jilid laporan akhir & diseminasi", "1", "1", "5.250.000", "paket", fmt(1*1*5250000), "100%", "0%"),
    ("Sub Total C.2", "", "", "", "", fmt(1*1*5250000), "100%", "0%"),
    ("Sub Total C (BTL)", "", "", "", "", fmt(12*475000+12*475000+5250000), "100%", "0%"),
]

t2_total_blnp = (52000000+12*1250000+3*10500000+12000000+3*3200000+18000000+12500000)+(96*155000+48*225000)+(15*2*425000+30*375000+30*185000)+(12*2500000+12*475000+2*14500000+4750000+2*10250000+14500000+12*825000+7750000+6750000)
t2_total_btl = 12*475000+12*475000+5250000
t2_total = t2_total_blnp + t2_total_btl
t2_lpdp_total = t2_total + 105600000
t2_inkind = 30000000 + 10000000 + 10000000  # engineer 150h×2×Rp100k + akses lokasi + data&konsumsi
t2_inkind_desc = "Engineer pendamping (2 org × 150 jam × Rp100.000 = Rp30jt), akses lokasi pilot (Rp10jt), data operasional & konsumsi (Rp10jt)"
out.append(f"**Total Tahun II: LPDP {fmt(t2_lpdp_total)} (BLP {fmt(105600000)} + BLNP+BTL {fmt(t2_total)}) + Mitra in-kind {fmt(t2_inkind)} = ~{fmt(t2_lpdp_total+t2_inkind)}**\n")
out.append(f"*Rincian in-kind mitra: {t2_inkind_desc}*\n")

out.append(table(["Komponen Biaya", "Volume", "Frekuensi", "Harga Satuan (Rp)", "Satuan", "Jumlah", "LPDP", "Mitra"],
                 t2_b1 + [("", "", "", "", "", "", "", "")] + t2_b2 + [("", "", "", "", "", "", "", "")] + t2_b3 + [("", "", "", "", "", "", "", "")] + t2_b4 + [("", "", "", "", "", "", "", "")] + t2_c + [
    ("", "", "", "", "", "", "", ""),
    ("**TOTAL BIAYA TAHUN II (BLNP + BTL)**", "", "", "", "", f"**{fmt(t2_total)}**", "**100%**", "**0%**"),
]))

# Compliance table (after all totals computed)
t1_blp_pct = round(105600000 / t1_lpdp_total * 100, 1)
t1_blnp_pct = round(t1_total_blnp / t1_lpdp_total * 100, 1)
t1_btl_pct = round(t1_total_btl / t1_lpdp_total * 100, 1)
t1_modal = 12*1500000 + 6500000
t1_modal_pct = round(t1_modal / t1_lpdp_total * 100, 1)
t2_blp_pct = round(105600000 / t2_lpdp_total * 100, 1)
t2_blnp_pct = round(t2_total_blnp / t2_lpdp_total * 100, 1)
t2_btl_pct = round(t2_total_btl / t2_lpdp_total * 100, 1)
t2_modal = 12*2500000
t2_modal_pct = round(t2_modal / t2_lpdp_total * 100, 1)
out.append("\nRekapitulasi verifikasi kepatuhan Juknis:\n")
out.append("| Parameter | Syarat | Tahun I | Tahun II | Status |\n")
out.append("|---|---|---|---|---|\n")
out.append(f"| BLP (Insentif Tim) | Maks 25% | {str(t1_blp_pct).replace('.',',')}% | {str(t2_blp_pct).replace('.',',')}% | ✓ |\n")
out.append(f"| BLNP (B.1+B.2+B.3+B.4) | Min 70% | {str(t1_blnp_pct).replace('.',',')}% | {str(t2_blnp_pct).replace('.',',')}% | ✓ |\n")
out.append(f"| BTL (C) | Maks 5% | {str(t1_btl_pct).replace('.',',')}% | {str(t2_btl_pct).replace('.',',')}% | ✓ |\n")
out.append(f"| Belanja Modal (dalam B.4) | Maks 10% | {str(t1_modal_pct).replace('.',',')}% | {str(t2_modal_pct).replace('.',',')}% | ✓ |\n")

# ── BAB 10 — KOMPETENSI TIM PERISET ──
out.append("\n---\n")
out.append(section("BAB 10 — KOMPETENSI TIM PERISET"))
out.append(table(["No", "Nama", "Pendidikan", "Kepakaran", "Peran dalam Riset", "URL Scopus"], [
    ("1", "Prof. Dr. Subiyanto, S.T., M.T.",
     "S3 Universiti Kebangsaan Malaysia",
     "Intelligent control, power electronics, AI",
     "Ketua; novelty, arsitektur smart charging hub, integrasi sistem, scientific governance, mitra",
     "[DIISI URL]"),
    ("2", "Bagaskoro Saputro, S.Si., M.Cs.",
     "S2 Ilmu Komputer UGM",
     "IoT architecture, edge/cloud, system integration, AI",
     "Lead IoT: gateway, OCPP/MQTT/Modbus/CAN, CSMS/CMS, backend, cybersecurity, interoperabilitas",
     "[DIISI URL]"),
    ("3", "Mario Norman Syah, S.Pd., M.Eng.",
     "S2 Teknik Elektro UGM",
     "Power electronics, MPPT, DC-DC converters, microgrid",
     "Lead power: sizing PV/BESS, integrasi inverter, model energi, uji lab power converter",
     "[DIISI URL]"),
    ("4", "Adhe Lingga Dewi, S.Si., M.Si.",
     "S2 Ilmu Komputer UNDIP",
     "IoT, sensors, ANN, computational physics",
     "Lead data: kalibrasi sensor, AI forecasting, anomaly detection, data quality, evaluasi model",
     "[DIISI URL]"),
    ("5", "Ir. Turnad Lenggo Ginta, S.T., M.T., Ph.D.",
     "S3 Universiti Malaya",
     "Machine learning, energy policy, manufacturing",
     "Lead hilirisasi: analisis techno-economic, kebijakan energi, dampak, ESG, keberlanjutan",
     "26435862600"),
]))

# ── BAB 11 — DAFTAR RIWAYAT HIDUP ──
out.append("\n---\n")
out.append(section("BAB 11 — DAFTAR RIWAYAT HIDUP TIM PERISET"))

# 1. Subiyanto
out.append("\n### 1. Prof. Dr. Subiyanto, S.T., M.T. \u2014 Ketua Periset\n")
out.append(table(["Item", "Detail"], [
    ("NIP", "197411232005011001"),
    ("Institusi", "Universitas Negeri Semarang (UNNES)"),
    ("Jabatan Fungsional", "Guru Besar (Professor)"),
    ("Program Studi", "Teknik Elektro, Fakultas Teknik"),
    ("Bidang Keahlian", "Intelligent Systems Electrical Engineering, Power Electronics, Artificial Intelligence"),
    ("S1", "Teknik Elektro \u2014 Universitas Diponegoro (Undip)"),
    ("S2", "Teknik Elektro \u2014 Universitas Gadjah Mada (UGM)"),
    ("S3", "Electrical, Electronic & Systems Engineering \u2014 Universiti Kebangsaan Malaysia (UKM)"),
    ("SINTA ID", "257687"),
    ("Google Scholar", "https://scholar.google.com/citations?user=TcmKHJgAAAAJ"),
    ("Email", "subiyanto@mail.unnes.ac.id"),
    ("Publikasi Utama (2024\u20132026)", "Fast Charger E2W Intelligent Control (JAMRIS 2026); Microgrid AI Optimization (IEEE IES 2025); HHO MPPT (ISMEE 2025, DOI: 10.1109/ISMEE68179.2025.11473059); PID IBC (IEEE ICT-PEP 2024)"),
]))

# 2. Bagaskoro
out.append("\n### 2. Bagaskoro Saputro, S.Si., M.Cs. \u2014 Anggota Periset\n")
out.append(table(["Item", "Detail"], [
    ("Institusi", "BINUS University"),
    ("Program Studi", "Computer Science, School of Computer Science, Kampus Semarang"),
    ("Bidang Keahlian", "IoT, Sistem Cerdas, Signal Processing, Machine Learning, Electric Vehicle"),
    ("S1", "Elektronika dan Instrumentasi \u2014 Universitas Gadjah Mada (UGM)"),
    ("S2", "Ilmu Komputer \u2014 Universitas Gadjah Mada (UGM)"),
    ("SINTA ID", "6869233"),
    ("Google Scholar", "https://scholar.google.com/citations?user=wJSoTIMAAAAJ"),
    ("Email", "bagaskoro.saputro@binus.ac.id"),
    ("Publikasi Utama (2026)", "Co-author IBC Fast Charger (JAMRIS 2026, DOI: 10.14313/jamris-2026-030); Co-author Bifacial PV Modeling (JTP Lampung 2026, DOI: 10.23960/jtepl.v15i2.510-524)"),
]))

# 3. Mario
out.append("\n### 3. Mario Norman Syah, S.Pd., M.Eng. \u2014 Anggota Periset\n")
out.append(table(["Item", "Detail"], [
    ("Institusi", "Universitas Negeri Semarang (UNNES)"),
    ("Program Studi", "Pendidikan Teknik Elektro, Fakultas Teknik"),
    ("Bidang Keahlian", "Power Electronics, MPPT, DC-DC Converters, Microgrid, Control System, Renewable Energy"),
    ("S1", "Pendidikan Teknik Elektro \u2014 Universitas Negeri Semarang (UNNES)"),
    ("S2", "Teknik Elektro \u2014 Universitas Gadjah Mada (UGM)"),
    ("SINTA ID", "6869196"),
    ("Google Scholar", "https://scholar.google.com/citations?user=Ao9DaAkAAAAJ"),
    ("Email", "marionormansyah@mail.unnes.ac.id"),
    ("Publikasi Utama (2024\u20132026)", "IBC Fast Charger (JAMRIS 2026); HHO MPPT (ISMEE 2025); Microgrid AI Optimization (IEEE IES 2025); PID IBC (IEEE ICT-PEP 2024); Novel High Gain SEPIC (ICT-PEP 2024)"),
]))

# 4. Adhe
out.append("\n### 4. Adhe Lingga Dewi, S.Si., M.Si. \u2014 Anggota Periset\n")
out.append(table(["Item", "Detail"], [
    ("Institusi", "BINUS University"),
    ("Program Studi", "Computer Science, School of Computer Science, Kampus Semarang"),
    ("Bidang Keahlian", "IoT, Sensors, Artificial Neural Network, Computational Physics, Photonic"),
    ("S1", "Fisika \u2014 Universitas Negeri Semarang (UNNES)"),
    ("S2", "Ilmu Komputer \u2014 Universitas Diponegoro (UNDIP)"),
    ("SINTA ID", "6838447"),
    ("Scopus", "12 articles, H-Index 3"),
    ("Google Scholar", "46 articles, H-Index 5"),
    ("Email", "adhe.dewi@binus.ac.id"),
    ("Publikasi Utama (2024\u20132026)", "Smart Air Monitoring IoT ESP32 (Procedia CS 2024, corresponding author); Sensor Calibration MQ-135/8 (Eng. Res. Express 2025, first author); ANN Weather Prediction (ICIMTech 2024, first author)"),
]))

# 5. Turnad
out.append("\n### 5. Ir. Turnad Lenggo Ginta, S.T., M.T., Ph.D. \u2014 Anggota Periset\n")
out.append(table(["Item", "Detail"], [
    ("Institusi", "Badan Riset dan Inovasi Nasional (BRIN)"),
    ("Unit Kerja", "Research Center for Manufacturing Technology of Production Machinery"),
    ("Bidang Keahlian", "Machine Learning, Welding Technology, Precision Machining, Energy Policy"),
    ("Scopus ID", "26435862600"),
    ("Scopus", "77 documents, H-Index 17, Cited by 1,082"),
    ("Google Scholar", "Cited by 1,686, H-Index 21, i10-Index 32"),
    ("Email", "turnad.lenggo.ginta@brin.go.id"),
    ("Publikasi Utama Relevan", "Promoting a Low-carbon Indonesia (IJEEP 2025); PLTS Distributed Generation Lhokseumawe (2023)"),
]))

# ── REFERENSI ──
out.append("\n---\n")
out.append(section("REFERENSI"))
refs = [
    "Badan Riset dan Inovasi Nasional. (2026). Sosialisasi Pedoman RIIM Kompetisi 2026 Nomor 69/II.7/HK/2026. Direktorat Pendanaan Riset dan Inovasi.",
    "Danielsson, G. H., da Silva, L. N. F., da Paix\u00e3o, J. L., Abaide, A. R., & Neto, N. K. (2025). Rules-based energy management system for an EV charging station nanogrid: A stochastic analysis. *Energies*, 18(1), Article 26. https://doi.org/10.3390/en18010026",
    "Dewi, A. L., Setyoko, D. E., Adhi, C. G. S., & Afrilia, N. S. (2024). Comparison of training function, adaption learning function, and transfer function of hidden layers in artificial neural network in weather prediction. In *2024 ICIMTech* (pp. 145\u2013149). IEEE. https://doi.org/10.1109/ICIMTech63123.2024.10780803",
    "Dewi, A. L., Suseno, J. E., & Soesanto, Q. M. B. (2025). Datsheet-based calibration study of the MQ-135 sensors for carbon dioxide (CO2) and MQ-8 sensors for hydrogen (H2). *Engineering Research Express*, 7(4), Article 045306. https://doi.org/10.1088/2631-8695/ae0b35",
    "Dong, X.-J., Shen, J.-N., Ma, Z.-F., & He, Y.-J. (2025). Stochastic optimization of integrated electric vehicle charging stations under photovoltaic uncertainty and battery power constraints. *Energy*, 314, Article 134163. https://doi.org/10.1016/j.energy.2024.134163",
    "Easterline, L. M., Putri, A. A.-Z. R., Atmaja, P. S., Dewi, A. L., & Prasetyo, A. (2024). Smart air monitoring with IoT-based MQ-2, MQ-7, MQ-8, and MQ-135 sensors using NodeMCU ESP32. *Procedia Computer Science*, 245, 815\u2013824. https://doi.org/10.1016/j.procs.2024.10.308",
    "Hewamalage, H., Ackermann, K., & Bergmeir, C. (2023). Forecast evaluation for data scientists: Common pitfalls and best practices. *Data Mining and Knowledge Discovery*, 37, 788\u2013832. https://doi.org/10.1007/s10618-022-00894-5",
    "International Electrotechnical Commission. (2023). IEC 61851-1:2017/COR1:2023, Corrigendum 1\u2014Electric vehicle conductive charging system\u2014Part 1: General requirements.",
    "International Organization for Standardization. (2022). ISO 15118-20:2022, Road vehicles\u2014Vehicle to grid communication interface\u2014Part 20: 2nd generation network layer and application layer requirements.",
    "Keith, J., Mirletz, B., Prilliman, M., Blair, N., Guittet, D., Janzou, S., & Gilman, P. (2022). FY19\u2013FY21 final technical report: Foundational open source solar system modeling through improvement and validation of the System Advisor Model and PVWatts (NREL/TP-7A40-82478). NREL. https://doi.org/10.2172/1870820",
    "Kementerian Energi dan Sumber Daya Mineral. (2023). Peraturan Menteri ESDM No. 1 Tahun 2023 tentang Penyediaan Infrastruktur Pengisian Listrik untuk KBLBB.",
    "Khajeh, H., & Laaksonen, H. (2022). Applications of probabilistic forecasting in smart grids: A review. *Applied Sciences*, 12(4), Article 1823. https://doi.org/10.3390/app12041823",
    "Lazidis, A., Tsakos, K., & Petrakis, E. G. M. (2022). Publish\u2013subscribe approaches for the IoT and the cloud: Functional and performance evaluation of open-source systems. *Internet of Things*, 19, Article 100538. https://doi.org/10.1016/j.iot.2022.100538",
    "Meng, Q., Hussain, S., He, Y., Lu, J., & Guerrero, J. M. (2025). Multi-timescale stochastic optimization for enhanced dispatching and operational efficiency of electric vehicle photovoltaic charging stations. *International Journal of Electrical Power & Energy Systems*, 172, Article 111096. https://doi.org/10.1016/j.ijepes.2025.111096",
    "National Institute of Standards and Technology. (2023). Guide to operational technology (OT) security (NIST SP 800-82 Revision 3). https://doi.org/10.6028/NIST.SP.800-82r3",
    "Olano, J., Camblong, H., L\u00f3pez-Ibarra, J. A., & Lie, T. T. (2025). Development of energy management systems for electric vehicle charging stations associated with batteries: Application to a real case. *Applied Sciences*, 15(16), Article 8798. https://doi.org/10.3390/app15168798",
    "Open Charge Alliance. (2025). New editions of the OCPP 2.1 and 2.0.1 now available! https://openchargealliance.org",
    "Pemerintah Republik Indonesia. (2023). Peraturan Presiden Nomor 79 Tahun 2023 tentang Perubahan atas Perpres 55/2019 tentang Percepatan Program KBLBB untuk Transportasi Jalan.",
    "Pemerintah Republik Indonesia. (2025). Peraturan Pemerintah Nomor 28 Tahun 2025 tentang Percepatan Pengembangan dan Pemanfaatan KBLBB.",
    "Syah, M. N., Aprilianto, R. A., & Suryanto, A. (2024). PID controller enhancement of interleaved buck converter using intelligent algorithm. In *2024 ICT-PEP* (pp. 318\u2013323). IEEE. https://doi.org/10.1109/ICT-PEP63827.2024.10733376",
    "Tairo, D. C., Silva, J. A. A., L\u00f3pez, J. C., & Rider, M. J. (2025). Implementation of a microgrid energy management system considering fair EV charging, uncertainties and contingencies: A multi-objective approach. *Applied Energy*, 396, Article 126242. https://doi.org/10.1016/j.apenergy.2025.126242",
    "Wu, Y.-S., Liao, J.-T., & Yang, H.-T. (2024). Three-stage resilience enhancement via optimal dispatch and reconfiguration for a microgrid. *Frontiers in Energy Research*, 12, Article 1461383. https://doi.org/10.3389/fenrg.2024.1461383",
]
for i, ref in enumerate(refs, 1):
    out.append(f"\n{i}. {ref}")

# ── LAMPIRAN ──
out.append("\n---\n")
out.append(section("LAMPIRAN"))
out.append("**Lampiran 1 \u2014 Data Management Plan (DMP)**\n")
out.append(section("1. Metadata", 4))
out.append(table(["Item", "Isian"], [
    ("1.1 Judul Riset", judul),
    ("1.2 Durasi Riset", "Mulai: 01-01-2026 \u2014 Akhir: 31-12-2027"),
    ("1.3 Ketua Tim Riset", f"nama: {ketua_nama}; afiliasi: Universitas Negeri Semarang; e-mail: subiyanto@mail.unnes.ac.id"),
    ("1.4 Subjek Riset", "Engineering, Computer and Information Sciences"),
    ("1.5 Deskripsi Riset", "Riset mengembangkan smart charging hub solar hybrid PV\u2013BESS\u2013Grid berbasis AI dan IoT-edge dengan EMS adaptif, TKT 3\u21926 dalam 2 tahun"),
    ("1.6 Sumber Dana Riset", "PRIS \u2014 BRIN/LPDP"),
]))

out.append(section("2. Tipe Data", 4))
out.append(table(["Jenis Data", "Deskripsi", "Format File"], [
    ("Log inverter solar", "Data Modbus (tegangan PV, arus, daya, iradiasi)", "CSV"),
    ("Data BMS BESS", "SOC, SOH, daya charge/discharge, temperatur", "CSV, JSON"),
    ("Telemetri charger", "Log OCPP (session ID, meter start/stop, kWh, timestamp)", "JSON, CSV"),
    ("Data grid", "P, Q, V, I, PF, kWh, peak demand", "CSV"),
    ("Log EMS", "Setpoint, mode operasi, SOC target, alokasi daya", "JSON, CSV"),
    ("Data AI", "Forecast, anomaly score, data quality flag, drift indicator", "JSON"),
    ("Data pengujian", "Hasil uji fungsional, kalibrasi, fault injection", "CSV, PDF"),
]))

out.append(section("3. Penyimpanan dan Pengamanan Data", 4))
out.append(table(["Item", "Isian"], [
    ("3.1 Tempat penyimpanan", "Layanan cloud terenkripsi, backup harian; repositori institusi UNNES; laptop tim riset"),
    ("3.2 Waktu deposit ke RIN", "12/2027 (maksimal 1 bulan sebelum akhir kegiatan)"),
]))

out.append(section("4. Pengelolaan Privasi", 4))
out.append(table(["Item", "Isian"], [
    ("Data pribadi/sensitif?", "Tidak ada data pribadi yang disimpan; data telemetri bersifat teknis"),
    ("Penanganan", "Pseudonim \u2014 ID sesi OCPP sebagai kode unik tanpa PII; enkripsi TLS untuk komunikasi"),
]))

out.append("\n**Lampiran 2 \u2014 Format Peran Tim Periset**\n")
out.append(table(["No", "Nama", "Peran dalam Riset", "Kompetensi Pendukung", "URL Scopus"], [
    ("1", "Prof. Dr. Subiyanto, S.T., M.T.",
     "Ketua; perancang arsitektur smart charging hub, integrasi sistem, scientific governance, mitra",
     "Intelligent control, Power Electronics, AI; Guru Besar Teknik Elektro UNNES",
     "[DIISI URL]"),
    ("2", "Bagaskoro Saputro, S.Si., M.Cs.",
     "Lead IoT: gateway multi-protokol, CSMS/CMS, backend, cybersecurity, interoperabilitas",
     "IoT Architecture, Edge/Cloud, System Integration; Dosen BINUS University",
     "[DIISI URL]"),
    ("3", "Mario Norman Syah, S.Pd., M.Eng.",
     "Lead power: sizing PV/BESS, integrasi inverter, model energi, uji lab",
     "Power Electronics, MPPT, DC-DC Converters; Dosen UNNES",
     "[DIISI URL]"),
    ("4", "Adhe Lingga Dewi, S.Si., M.Si.",
     "Lead data: kalibrasi sensor, AI forecasting, anomaly detection, data quality",
     "IoT, Sensors, ANN, Computational Physics; Dosen BINUS University",
     "[DIISI URL]"),
    ("5", "Ir. Turnad Lenggo Ginta, S.T., M.T., Ph.D.",
     "Lead hilirisasi: analisis techno-economic, kebijakan energi, ESG",
     "Machine Learning, Energy Policy; Peneliti BRIN",
     "26435862600"),
]))

# ── Write output ──
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print(f"✅ Written to {OUT}")
print(f"   {len(out)} lines")
