import subprocess
import re


def get_ip_addresses():
    cmd = "ip -4 a"  # -4 for IPv4 only
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    # Regex to extract IPs (skip 127.0.0.1 and loopbacks)
    ip_pattern = r'inet (\d+\.\d+\.\d+\.\d+)/'
    ip_matches = re.findall(ip_pattern, result.stdout)

    # Optionally filter out loopback
    ip_list = [ip for ip in ip_matches if not ip.startswith("127.")]

    return ip_list
