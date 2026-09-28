from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_REPO_URL = "https://raw.githubusercontent.com/DobbM-Studios/studyos/main/images"


def get_image_src(image_name: str) -> str:
    local_image_path = BASE_DIR / "images" / image_name
    if local_image_path.exists():
        return image_name
    return f"{RAW_REPO_URL}/{image_name}"
