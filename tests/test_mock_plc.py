import snap7

ADDRESS = "127.0.0.1"
RACK = 0
SLOT = 1
TCP_PORT = 1102


def test_plc_connection(mock_s7_server):
    """Test basic connectivity to the mock PLC server."""
    client = snap7.client.Client()

    # Connect to the mock server
    client.connect(ADDRESS, RACK, SLOT, TCP_PORT)

    # Verify connection
    assert client.get_connected() == True

    # Clean up
    client.disconnect()


# def test_db_read_write(mock_s7_server):
#     """Test basic DB read/write operations."""
#     client = snap7.client.Client()
#     client.connect("127.0.0.1", 0, 1, 102)

#     # Write test data to DB 20 (matching StatusDataBlock)
#     test_data = bytearray([0x00, 0x01, 0x02, 0x03, 0x04])
#     mock_s7_server.set_db_data(20, 0, test_data)

#     # Read data back and verify
#     read_data = client.db_read(20, 0, len(test_data))
#     assert read_data == test_data

#     # Test integer field (byte 5 in StatusDataBlock)
#     test_int = bytearray([0x00, 0x2A])  # Value 42
#     mock_s7_server.set_db_data(20, 5, test_int)
#     read_int = client.db_read(20, 5, 2)
#     assert read_int == test_int

#     client.disconnect()
