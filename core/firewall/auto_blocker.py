import time
from controller import FirewallController
import logging

# Threshold konfigurasi
REQUEST_LIMIT = 100        # Maksimal request
WINDOW_SECONDS = 10        # Dalam durasi berapa detik
BAN_DURATION = 3600        # Lama waktu IP diblok (dalam detik)

# Simulasi IP traffic log (bisa diganti dengan log parser)
sample_traffic_log = [
    ("192.168.1.20", 105),  # IP & jumlah request dalam 10 detik
    ("10.0.0.5", 99),
    ("45.77.88.11", 125),
]

# Penyimpan waktu banned sementara (bisa diganti Redis/DB)
temp_ban_db = {}

fw = FirewallController()
logging.basicConfig(level=logging.INFO)

def auto_block():
    global temp_ban_db
    now = time.time()

    for ip, count in sample_traffic_log:
        if fw.is_whitelisted(ip):
            logging.info(f"[SKIP] {ip} di whitelist.")
            continue

        if count > REQUEST_LIMIT:
            already_banned = temp_ban_db.get(ip)
            if already_banned and now < already_banned:
                logging.info(f"[INFO] {ip} sudah diblokir sebelumnya.")
                continue

            success = fw.block_ip(ip)
            if success:
                temp_ban_db[ip] = now + BAN_DURATION
                logging.warning(f"[BLOCK] {ip} melebihi limit! Dibanned {BAN_DURATION} detik.")

def cleanup_expired_blocks():
    now = time.time()
    expired = [ip for ip, until in temp_ban_db.items() if until < now]
    for ip in expired:
        if fw.unblock_ip(ip):
            del temp_ban_db[ip]
            logging.info(f"[UNBLOCK] {ip} otomatis dibuka.")

if __name__ == "__main__":
    while True:
        auto_block()
        cleanup_expired_blocks()
        time.sleep(10)  # Jalankan tiap 10 detik
      
