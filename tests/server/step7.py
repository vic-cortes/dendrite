import ctypes
import threading
import time

from snap7.server import Server
from snap7.type import SrvArea, WordLen

WordCType = WordLen.Byte.ctype


class MockS7Server:
    """
    Simulated S7 server for testing with pytest.
    Starts on localhost tcp_port=1102, registers DB 20, and exposes methods to read/write bytes.
    """

    def __init__(self, tcp_port: int = 1102, size_bytes: int = 256, log: bool = False):
        self.tcp_port = tcp_port
        self.size_bytes = size_bytes
        self._server = Server(log=log)

        # Create an array of type WordLen.Byte.ctype (usually c_int8) as expected by Snap7.
        array_type = WordCType * size_bytes
        self._db20_data = array_type(0)  # Default to all 0

        # Register area DB number 20
        self._server.register_area(SrvArea.DB, 20, self._db20_data)  # index=20
        self._server.start(tcp_port=tcp_port)

        # Start a thread that periodically empties the event queue with pick_event()
        # If not consumed, after certain requests the server may freeze.
        self._stop_flag = threading.Event()
        self._ev_thread = threading.Thread(
            target=self._event_loop, name="MockS7ServerEventLoop", daemon=True
        )
        self._ev_thread.start()

    def _event_loop(self):
        while not self._stop_flag.is_set():
            ev = self._server.pick_event()
            # Do not print, just release
            time.sleep(0.01)

    def stop(self):
        # First set stop_flag, then stop and destroy
        self._stop_flag.set()
        self._ev_thread.join(timeout=1.0)
        self._server.stop()
        self._server.destroy()

    def set_db20(self, start: int, data: bytes):
        """Write bytes directly to the buffer registered by the server."""
        end = start + len(data)
        if end > self.size_bytes:
            raise IndexError(f"DB20 overflow: {end} > {self.size_bytes}")
        ctypes.memmove(
            ctypes.addressof(self._db20_data) + start,
            (ctypes.c_char * len(data)).from_buffer_copy(data),
            len(data),
        )

    def get_db20(self, start: int, length: int) -> bytes:
        """Read bytes from the server buffer without connecting a client."""
        buf = bytes(self._db20_data[start : start + length])
        return buf


if __name__ == "__main__":
    # Example usage
    server = MockS7Server(tcp_port=1102, size_bytes=512, log=True)
    try:
        server.set_db20(0, b"\x01\x02\x03\x04")
        print(server.get_db20(0, 4))  # Should print: b'\x01\x02\x03\x04'
    except Exception as e:
        print(f"Error: {e}")
