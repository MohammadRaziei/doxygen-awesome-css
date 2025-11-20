"""Doxygen Awesome CSS - A custom CSS theme for Doxygen HTML documentation."""

import logging
import shutil
import sys
from pathlib import Path
from typing import List

# Read version from VERSION.txt
_version_file = Path(__file__).parent.parent / "VERSION.txt"
if _version_file.exists():
    __version__ = _version_file.read_text().strip()
else:
    __version__ = "0.0.0"

__license__ = "MIT"


class Installer:
    """Handles installation of Doxygen Awesome CSS files."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.package_dir = Path(__file__).parent.parent
        self.files_to_copy = [
            "doxygen-awesome.css",
            "doxygen-awesome-darkmode-toggle.js",
            "doxygen-awesome-fragment-copy-button.js",
            "doxygen-awesome-interactive-toc.js",
            "doxygen-awesome-paragraph-link.js",
            "doxygen-awesome-sidebar-only-darkmode-toggle.css",
            "doxygen-awesome-sidebar-only.css",
            "doxygen-awesome-tabs.js",
        ]

    def get_package_files(self) -> List[Path]:
        """Get list of package files that exist."""
        package_files = []
        for filename in self.files_to_copy:
            file_path = self.package_dir / filename
            if file_path.exists():
                package_files.append(file_path)
            else:
                self.logger.warning(f"{filename} not found in package")
        return package_files

    def install(self, target_dir: Path) -> None:
        """Install CSS/JS files to target directory."""
        if not target_dir.exists():
            self.logger.error(f"Target directory '{target_dir}' does not exist")
            sys.exit(1)

        if not target_dir.is_dir():
            self.logger.error(f"'{target_dir}' is not a directory")
            sys.exit(1)

        package_files = self.get_package_files()

        if not package_files:
            self.logger.error("No Doxygen Awesome CSS files found in package")
            sys.exit(1)

        self.logger.info(f"Installing Doxygen Awesome CSS files to '{target_dir}'...")

        copied_count = 0
        for source_file in package_files:
            target_file = target_dir / source_file.name
            try:
                shutil.copy2(source_file, target_file)
                self.logger.debug(f"Copied: {source_file.name}")
                copied_count += 1
            except Exception as e:
                self.logger.error(f"Error copying {source_file.name}: {e}")
                sys.exit(1)

        self.logger.info(f"Successfully installed {copied_count} files to '{target_dir}'")

        # Show installation summary
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            self.logger.debug("Installed files:")
            for source_file in package_files:
                self.logger.debug(f"  - {source_file.name}")


__all__ = ["Installer", "__version__"]
