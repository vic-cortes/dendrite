def compute_integer_byte(value: int, print_string: bool = True) -> bytearray:
    """
    Computes the number of required bytes and
    create the corresponding payload
    """
    MAX_BYTE_VALUE = 255
    BYTE_LENGTH = 8
    EMPTY_BYTE = 0
    MAX_ALLOWED_INTEGER = 65_536 - 1

    if value > MAX_ALLOWED_INTEGER:
        raise ValueError("You passed max supported integer value")

    if value > MAX_BYTE_VALUE:
        closest_byte = value.bit_length() + 7
        payload = value.to_bytes(closest_byte // BYTE_LENGTH)

    else:
        payload = bytearray([EMPTY_BYTE, value])

    if print_string:
        binary_string = " | ".join(format(byte, "08b") for byte in payload)
        print(f"Binary representation: {binary_string}")

    return payload
