import os
import sys
import requests
import logging

from tqdm import tqdm


def download_csv(url, destination):
    if os.path.exists(destination):
        logging.info("🟩 Files already exists!")

        return
    
    try:
        response = requests.get(url, stream=True)

        response.raise_for_status()

        if not os.path.exists("data"):
            os.mkdir("data")

        file_size = int(response.headers.get("content-length", 0))

        logging.info("🟩 Downloading...")

        with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            with open(destination, "wb") as file:
                for data in response.iter_content(chunk_size=1024):
                    pbar.update(len(data))
                    file.write(data)

        logging.info("🟩 Download Success!")

    except requests.exceptions.RequestException as e:
        logging.error("🟥 Download Failed!")
        logging.error(f"🟥 Error {url}: {e}")

        raise SystemExit(1)