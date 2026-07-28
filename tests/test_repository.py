from src.common.paths import DATA_DIR, OUTPUT_DIR, ROOT


def test_core_directories_exist() -> None:
    assert DATA_DIR.is_dir()
    assert OUTPUT_DIR.is_dir()
    assert (ROOT / "paper").is_dir()


def test_raw_data_is_documented() -> None:
    assert (DATA_DIR / "raw" / "README.md").is_file()
