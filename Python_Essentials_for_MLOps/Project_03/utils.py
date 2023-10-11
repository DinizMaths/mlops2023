"""This module contains the utility functions for the project."""

import os
import logging
import requests

from tqdm import tqdm


def download_csv(url: str, destination: str) -> None:
    """
    Download a csv file from a url to a destination.

    Args:
        url (str): The url of the file to download.
        destination (str): The destination of the downloaded file.

    Returns:
        None
    
    """
    if os.path.exists(destination):
        logging.info("🟩 Files already exists!")

        return

    try:
        response = requests.get(url, stream=True, timeout=5)

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
        logging.error("🟥 Error %s: %s", url, e)

        raise SystemExit(1) from e

def is_summer_month(month: str) -> bool:
    """
    Check if a month is a summer month.

    Args:
        month (str): The month to check.
    
    Returns:
        bool: True if the month is a summer month, False otherwise.
    """
    return month in ["jun", "jul", "aug"]
