from pathlib import Path


class LocalStorage:
    """Stores uploaded files on the local filesystem."""

    def __init__(self, upload_dir: Path):
        self.upload_dir = upload_dir
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def save(self, filename: str, content: bytes) -> Path:
        """Persist file bytes to local storage and return the saved path."""
        target_path = self.upload_dir / filename
        target_path.write_bytes(content)
        return target_path
