import time

from snap7.server import Server
from snap7.type import SrvArea, WordLen

WordCType = WordLen.Byte.ctype


def run_server():
    """
    Starts a simulated PLC server.
    """
    # Create a server instance
    server = Server(log=True)

    # Assign a data area (simulates the PLC DB area)
    # db = bytearray(100)  # For example, 100 bytes

    # Add that area to the server
    size_bytes = 256
    array_type = WordCType * size_bytes
    db_data = array_type(0)

    server.register_area(SrvArea.DB, 1, db_data)
    # Start the server
    server.start(tcp_port=1102)

    print("Simulated PLC server running...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop()


if __name__ == "__main__":
    run_server()
