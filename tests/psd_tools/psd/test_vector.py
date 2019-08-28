from __future__ import absolute_import, unicode_literals
import pytest
from psd_tools.psd.vector import Path

from ..utils import check_read_write


@pytest.mark.parametrize(
    'fixture', [
        b'\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x04\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00 \x00\x00\x00X'
        b'\xe8\xf2\x00 \x00\x00\x00tz\xe1\x00 \x00\x00\x00\x90\x0c\xcf\x00\x01'
        b'\x004\xa1w\x00\xa6ff\x00N\x14z\x00\xa6ff\x00g\x87~\x00\xa6ff\x00\x01'
        b'\x00|(\xf5\x00\x90\x0c\xcf\x00|(\xf5\x00tz\xe1\x00|(\xf5\x00X\xe8'
        b'\xf2\x00\x01\x00g\x87~\x00B\x8f\\\x00N\x14z\x00B\x8f\\\x004\xa1w'
        b'\x00B\x8f\\\x00\x00'
    ]
)
def test_path_rw(fixture):
    check_read_write(Path, fixture)