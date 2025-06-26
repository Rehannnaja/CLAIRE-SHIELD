import subprocess
import logging
import json
from pathlib import Path

WHITELIST_PATH = Path(__file__).parent / "whitelist.json"
BLACKLIST_PATH = Path(__file__).parent / "blacklist.json"

logging.basicConfig(level=logging.INFO)

class FirewallController:
    def __init__(self):
        self.whitelist = self._load_json(WHITELIST_PATH)
        self.blacklist = self._load_json(BLACKLIST_PATH)

    def _load_json(self, path):
        if not path.exists():
            return []
        with open(path, "r") as f:
            return json.load(f)

    def _save_json(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def is_whitelisted(self, ip):
        return ip in self.whitelist

    def is_blacklisted(self, ip):
        return ip in self.blacklist

    def block_ip(self, ip):
        if self.is_whitelisted(ip):
            logging.info(f"[!] {ip} in whitelist, skip blocking.")
            return False
        if ip in self.blacklist:
            logging.info(f"[=] {ip} already blocked.")
            return False
        try:
            subprocess.run(
                ["iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"],
                check=True
            )
            self.blacklist.append(ip)
            self._save_json(BLACKLIST_PATH, self.blacklist)
            logging.info(f"[+] Blocked IP: {ip}")
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"[!] Failed to block IP {ip}: {e}")
            return False

    def unblock_ip(self, ip):
        if ip not in self.blacklist:
            logging.info(f"[-] {ip} not in blacklist.")
            return False
        try:
            subprocess.run(
                ["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"],
                check=True
            )
            self.blacklist.remove(ip)
            self._save_json(BLACKLIST_PATH, self.blacklist)
            logging.info(f"[✓] Unblocked IP: {ip}")
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"[!] Failed to unblock IP {ip}: {e}")
            return False

    def list_blocked(self):
        return self.blacklist
      
