import argparse
import os
from pathlib import Path
from typing import Generator
import requests
from datetime import datetime

URL = "http://localhost:8000/contents/"
URL_CATEGORY = "http://localhost:8000/categories/"
HOME = os.environ.get("HOME")
DOCUMENT_ROOT = f"{HOME}/work/90.documents/01.tech"

def get_categories():
    response = requests.get(URL_CATEGORY)
    print(f"response={response.status_code}, json={response.json()}")

def update_content():
    parser = argparse.ArgumentParser(description="upload.py")
    parser.add_argument("target_dir")
    args = parser.parse_args()

    for category, content in read_files(args.target_dir):
        post_content(category, content)
    
def read_files(parent: str) -> Generator[tuple[str, str]]:
    root = Path(DOCUMENT_ROOT) / parent
    print(f"root={root}")
    for md_file in root.glob('*.md'):
        yield (f"{parent}/{md_file.name}", md_file.read_text())

def post_content(category: str, content: str):
    data = {
        "category": category,
        "text": content,
        "created_at": datetime.now().isoformat(),
        "update_at": datetime.now().isoformat(),
        "update_no": 0,
    }
    response = requests.post(URL, json=data)
    print(f"category={category}, response={response.status_code}")
    # if (response.status_code == 200):
        # print(response.json())

if __name__ == "__main__":
    #get_categories()
    update_content()