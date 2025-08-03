import pytest

from .server.step7 import MockS7Server


@pytest.fixture(scope="session")
def mock_s7_server():
    server = MockS7Server(tcp_port=1102, size_bytes=512)
    yield server
    server.stop()
