# 🛡️ CLAIRE SHIELD

> **Open-Source Anti-DDoS Gateway** — Inspired by Cloudflare and DDoS-Guard. Built for real-world attack mitigation.

<p align="center">
  <img src="https://img.shields.io/github/license/Rehannnaja/CLAIRE-SHIELD?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/Rehannnaja/CLAIRE-SHIELD?style=for-the-badge" alt="Stars">
  <img src="https://img.shields.io/github/issues/Rehannnaja/CLAIRE-SHIELD?style=for-the-badge" alt="Issues">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Rehannnaja/CLAIRE-SHIELD/main/assets/logo.svg" width="200" alt="Claire Shield Logo" />
</p>

---

## 🚀 Apa Itu Claire Shield?

Claire Shield adalah sistem **anti-DDoS open-source kelas enterprise**, dengan fitur lengkap mulai dari firewall L3/L4, WAF L7, sampai challenge bot protection. Dirancang untuk proteksi skala besar seperti Cloudflare, namun bisa kamu host sendiri dan kendalikan penuh.

---

## 📦 Fitur Unggulan

- 🔥 **Firewall Otomatis** (iptables, nftables, XDP ready)
- 🧠 **Smart Traffic Detection** (signature & anomaly)
- 🕵️‍♂️ **Bot Challenge System** (JS, Cookie, CAPTCHA)
- 🌐 **Reverse Proxy Built-in** (NGINX, Node.js, ModSecurity)
- 📊 **Dashboard Admin Modern** (Next.js + Tailwind)
- 📍 **GeoIP Rules & Blacklist**
- 🔐 **TLS Termination Ready** (Cloud-native)

---

## 🧱 Struktur Proyek

Lihat [struktur folder proyek »](#)

---

## 🧪 Instalasi & Jalankan

```bash
git clone https://github.com/Rehannnaja/CLAIRE-SHIELD.git
cd CLAIRE-SHIELD
docker-compose up --build
```

Atau instalasi manual:
```bash
bash scripts/install.sh
npm install && npm run dev  # untuk dashboard
```

---

## 📈 Dashboard

Pantau status IP, trafik masuk, firewall status, dan challenge logs dari **UI berbasis Next.js**.

---

## 🧩 Modul Modular

- `core/` - Mesin utama pendeteksi dan pelindung
- `proxy/` - Layer reverse proxy (NGINX/OpenResty/Node)
- `dashboard/` - Web admin panel
- `services/` - GeoIP, log service, auto-updater
- `config/` - Pengaturan dan policy

---

## 📜 Lisensi

Proyek ini dilindungi oleh:

**GNU Affero General Public License v3.0 (AGPL-3.0)**  
Kamu **wajib membuka modifikasi** jika menjalankan Claire Shield di server publik. 

---

## 🤝 Kontribusi

Kami terbuka untuk semua kontribusi:
- Pull request untuk fitur / patch
- Laporan bug
- Pembuatan rule baru

```bash
# Fork, buat branch, commit & PR 💻
```

---

## 🌐 Dibangun Dengan

- 🔧 Node.js / Python
- 🧱 NGINX / OpenResty
- 🚦 Redis / iptables
- 📡 Prometheus + Grafana
- ⚙️ Docker + Compose

---

<p align="center">
  Dibangun oleh <a href="https://github.com/Rehannnaja">Rehannnaja</a> — Powered by open source 💚
</p>
