import subprocess
import re
import random

EMOTIONS = [
    "happy",
    "sad",
    "angry",
    "scared",
    "surprised",
    "disgusted",
    "confident",
    "nervous",
    "bold",
    "engaged",
    "excited",
    "muted",
    "worried",
]

COLORS = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "teal",
    "maroon",
]

ANIMALS = [
    "tiger",
    "elephant",
    "giraffe",
    "zebra",
    "kangaroo",
    "panda",
    "dolphin",
    "fox",
    "lion",
    "bear",
    "rabbit",
    "wolf",
    "tapir",
    "dog",
    "cat",
]


def get_random_coupon_code(num: int) -> list[str]:
    """gives up to 8*8*12 = 768 coupon codes"""
    # Create all possible combinations
    all_combinations = [
        f"{emotion}-{color}-{animal}"
        for emotion in EMOTIONS
        for color in COLORS
        for animal in ANIMALS
    ]

    # Shuffle to ensure randomness
    random.shuffle(all_combinations)

    # Return the requested number of coupon codes (capped at total combinations)
    return all_combinations[:min(num, len(all_combinations))]


def get_ip_addresses():
    cmd = "ip -4 a"  # -4 for IPv4 only
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    # Regex to extract IPs (skip 127.0.0.1 and loopbacks)
    ip_pattern = r'inet (\d+\.\d+\.\d+\.\d+)/'
    ip_matches = re.findall(ip_pattern, result.stdout)

    # Optionally filter out loopback
    ip_list = [ip for ip in ip_matches if not ip.startswith("127.")]

    return ip_list
