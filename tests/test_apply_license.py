import pytest

from os import path

from licensify.apply_license import apply_license_header
from licensify.errors import LicensesOutOfDateError

def _contents(file):
    with open(file) as fp:
        return fp.read()

@pytest.fixture
def tmp_file_factory(tmpdir):
    def _factory(contents=''):
        filename = path.join(str(tmpdir), 'tmp.py')
        with open(filename, 'w') as fp:
            fp.write(contents)
        return filename
    return _factory

def test_license_is_applied_to_empty_file(tmp_file_factory):
    source_path = tmp_file_factory()
    apply_license_header('My Awesome License', [source_path])
    assert _contents(source_path) == '# My Awesome License\n'

def test_license_does_not_overwrite_source(tmp_file_factory):
    contents = 'print(\'hello world\')'
    source_path = tmp_file_factory(contents)
    apply_license_header('My Awesome License', [source_path])
    assert _contents(source_path) == '# My Awesome License\n' + contents

def test_license_not_written_on_dry_run(tmp_file_factory):
    contents = 'print(\'hello world\')'
    source_path = tmp_file_factory(contents)
    apply_license_header('My Awesome License', [source_path], dry_run=True)
    assert _contents(source_path) == contents

def test_returns_files_to_update(tmp_file_factory):
    contents = 'print(\'hello world\')'
    source_path = tmp_file_factory(contents)
    result = apply_license_header('My Awesome License', [source_path], dry_run=True)
    assert result == [source_path]

def test_raises_error_if_check_true_and_file_needs_update(tmp_file_factory):
    contents = 'print(\'hello world\')'
    source_path = tmp_file_factory(contents)
    with pytest.raises(LicensesOutOfDateError):
        apply_license_header('My Awesome License', [source_path], dry_run=True, check=True)

def test_does_not_update_already_up_to_date_file(tmp_file_factory):
    contents = '# My Awesome License\nprint(\'hello world\')'
    source_path = tmp_file_factory(contents)
    results = apply_license_header('My Awesome License', [source_path], dry_run=True, check=True)
    assert _contents(source_path) == contents
    assert results == []
