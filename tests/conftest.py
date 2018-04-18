import os
import pytest
import tempfile


@pytest.fixture()
def tmp_file(request):
    fd, path = tempfile.mkstemp()
    def teardown():
        os.close(fd)
        os.remove(path)
    request.addfinalizer(teardown)
    return path
