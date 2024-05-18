import re
import tkinter as tk
from tkinter import filedialog
import os

# Copyright and advertisement text to be added to each output file
HEADER_TEXT = """
======================================
Copyright: https://t.me/jamalabueldahab
======================================
"""
AD_TEXT = """
======================================
Servers available 💎
2 RAM 2 Core 80GB SSD 
4 RAM 2 Core 140 GB SSD
8 RAM 4 core 240 GB SSD
16 RAM 8 core 320 SSD
Good prices 💎💎💎💎
@gamald 🫡🫡🫡🫡🫡
======================================
"""

def process_file(file_path):
    # Setup output files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    outputs = {
        "netflix": open(os.path.join(script_dir, "netflix_accounts.txt"), "w", encoding='utf-8'),
        "ionos": open(os.path.join(script_dir, "ionos_accounts.txt"), "w", encoding='utf-8'),
        "shahid": open(os.path.join(script_dir, "shahid_accounts.txt"), "w", encoding='utf-8'),
        "watchit": open(os.path.join(script_dir, "watchit_accounts.txt"), "w", encoding='utf-8'),
        "paypal": open(os.path.join(script_dir, "paypal_accounts.txt"), "w", encoding='utf-8'),
        "payeer": open(os.path.join(script_dir, "payeer_accounts.txt"), "w", encoding='utf-8'),
        "bet365": open(os.path.join(script_dir, "bet365_accounts.txt"), "w", encoding='utf-8'),
        "azure": open(os.path.join(script_dir, "azure_accounts.txt"), "w", encoding='utf-8'),
        "aws": open(os.path.join(script_dir, "aws_accounts.txt"), "w", encoding='utf-8'),
        "canal_plus": open(os.path.join(script_dir, "canal_plus_accounts.txt"), "w", encoding='utf-8'),
        "sfr": open(os.path.join(script_dir, "sfr_accounts.txt"), "w", encoding='utf-8'),
        "pia_proxy": open(os.path.join(script_dir, "pia_proxy_accounts.txt"), "w", encoding='utf-8'),
        "922_proxy": open(os.path.join(script_dir, "922_proxy_accounts.txt"), "w", encoding='utf-8'),
        "spotify": open(os.path.join(script_dir, "spotify_accounts.txt"), "w", encoding='utf-8'),
        "anghami": open(os.path.join(script_dir, "anghami_accounts.txt"), "w", encoding='utf-8'),
        "osn": open(os.path.join(script_dir, "osn_accounts.txt"), "w", encoding='utf-8'),
        "ovh": open(os.path.join(script_dir, "ovh_accounts.txt"), "w", encoding='utf-8'),
        "godaddy": open(os.path.join(script_dir, "godaddy_accounts.txt"), "w", encoding='utf-8'),
        "vyprvpn": open(os.path.join(script_dir, "vyprvpn_accounts.txt"), "w", encoding='utf-8'),
        "expressvpn": open(os.path.join(script_dir, "expressvpn_accounts.txt"), "w", encoding='utf-8'),
        "windscribe": open(os.path.join(script_dir, "windscribe_accounts.txt"), "w", encoding='utf-8'),
        "aliexpress": open(os.path.join(script_dir, "aliexpress_accounts.txt"), "w", encoding='utf-8'),
        "cpanel": open(os.path.join(script_dir, "cpanel_accounts.txt"), "w", encoding='utf-8'),
        "steampowered": open(os.path.join(script_dir, "steampowered_accounts.txt"), "w", encoding='utf-8'),
        "chatgpt": open(os.path.join(script_dir, "chatgpt_accounts.txt"), "w", encoding='utf-8'),
    }

    # Regular expression to extract email and password
    pattern = re.compile(r'https?://[^\s:]+:(\S+?@\S+?):(\S+)')

    for file_handle in outputs.values():
        # Write the header and ad text to each file
        file_handle.write(HEADER_TEXT)
        file_handle.write("\n")
        file_handle.write(AD_TEXT)
        file_handle.write("\n")

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            matches = pattern.findall(line)
            for email, password in matches:
                for domain, file_handle in outputs.items():
                    if domain.replace('_', '') in line:
                        file_handle.write(f"{email}:{password}\n")

    # Close all files
    for file_handle in outputs.values():
        file_handle.close()

    print("Processing complete. Check the output files in the script directory.")

def main():
    root = tk.Tk()
    root.withdraw()
    input_file_path = filedialog.askopenfilename(title="Select the input file")
    if not input_file_path:
        print("No input file selected, exiting.")
        return

    process_file(input_file_path)

if __name__ == "__main__":
    main()
