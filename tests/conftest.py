import pytest
from snap7.server import Server
from snap7.type import Area, SrvArea


class MockS7Server:
    def __init__(self):
        self.server = Server()
        self._setup_server()
        self.db_data = {}  # Store DB data

    def _setup_server(self):
        self.server.start()  # Standard S7 port
        # Initialize DB 20 (StatusDataBlock from test.py)
        self.server.register_area(SrvArea.DB, 20, bytearray(10))  # 10 bytes for demo

    def get_db_data(self, db_number: int, start: int, size: int) -> bytearray:
        return self.server.read_area(Area.DB, db_number, start, size)

    def set_db_data(self, db_number: int, start: int, data: bytearray):
        self.server.write_area(Area.DB, db_number, start, data)

    def stop(self):
        if self.server:
            self.server.stop()
            self.server.destroy()


@pytest.fixture(scope="session")
def mock_s7_server():
    server = MockS7Server()
    yield server
    server.stop()
