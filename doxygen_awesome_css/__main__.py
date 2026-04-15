"""Main entry point for Doxygen Awesome CSS CLI."""

import argparse
import logging
from pathlib import Path

from . import Installer
from .__about__ import __version__


def setup_logging(verbose: bool = False, quiet: bool = False) -> None:
    """Setup logging configuration based on verbosity."""
    if quiet:
        level = logging.WARNING
    elif verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
        
    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=[logging.StreamHandler()]
    )


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser for CLI."""
    parser = argparse.ArgumentParser(
        description="Doxygen Awesome CSS - A custom CSS theme for Doxygen HTML documentation",
        epilog="""
Examples:
  # Install files to current directory
  python -m doxygen_awesome_css --install .

  # List available files
  python -m doxygen_awesome_css --list

  # Show package path
  python -m doxygen_awesome_css --path

  # Show version
  python -m doxygen_awesome_css --version
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--install",
        type=str,
        metavar="DIR",
        help="Install CSS/JS files to the specified directory",
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="List available CSS/JS files",
    )

    parser.add_argument(
        "--path",
        action="store_true",
        help="Show the package directory path",
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output (DEBUG level)",
    )

    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Enable quiet output (WARNING level)",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"doxygen-awesome-css {__version__}",
    )

    return parser


def main() -> None:
    """Main entry point for CLI."""
    parser = create_parser()
    args = parser.parse_args()

    setup_logging(verbose=args.verbose, quiet=args.quiet)
    logger = logging.getLogger(__name__)

    if args.install:
        installer = Installer()
        installer.install(Path(args.install))
    elif args.list:
        installer = Installer()
        for f in installer.get_package_files():
            print(f.name)
    elif args.path:
        installer = Installer()
        print(installer.package_dir)
    else:
        logger.info("Doxygen Awesome CSS - A custom CSS theme for Doxygen HTML documentation")
        logger.info("Use --help for usage information")


if __name__ == "__main__":
    main()
