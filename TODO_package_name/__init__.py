"""Module-wide constants for `TODO_package_name`."""
# ruff: noqa: N999
import os
from pathlib import Path

import TODO_package_name

__version__ = "0.0.1"

# Module-wide path constants as in
# https://stackoverflow.com/a/59597733.

__package_path = os.path.split(TODO_package_name.__path__[0])[0]
DATA_DIR = Path(__package_path, "data")
# TODO(eringrant): Rethink tmpdir.
TMP_DIR = Path("/tmp", "TODO_package_name")  # noqa: S108
Path.mkdir(TMP_DIR, parents=True, exist_ok=True)

scratch_home = os.environ.get("SCRATCH_HOME")
SCRATCH_DIR = (
  Path(scratch_home, "TODO_package_name") if scratch_home is not None else TMP_DIR
)
Path.mkdir(SCRATCH_DIR, parents=True, exist_ok=True)

del TODO_package_name
del os
del __package_path
