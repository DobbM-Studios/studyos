from pathlib import Path

from core import image_utils


def test_returns_local_asset_name_when_file_exists(tmp_path, monkeypatch):
    image_dir = tmp_path / "images"
    image_dir.mkdir()
    (image_dir / "bg-0.jpg").write_bytes(b"test")

    monkeypatch.setattr(image_utils, "BASE_DIR", tmp_path)

    assert image_utils.get_image_src("bg-0.jpg") == "bg-0.jpg"


def test_returns_github_cdn_when_local_file_is_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(image_utils, "BASE_DIR", tmp_path)

    assert image_utils.get_image_src("missing.jpg") == (
        "https://raw.githubusercontent.com/DobbM-Studios/studyos/main/images/missing.jpg"
    )
