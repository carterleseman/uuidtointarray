import sys
import uuid

def uuid_to_int_array(uuid_str):
    # Convert UUID string to UUID object
    u = uuid.UUID(uuid_str)

    # Split into Most Significant Bits (MSB) and Least Significant Bits (LSB)
    msb = (u.int >> 64) & 0xFFFFFFFFFFFFFFFF
    lsb = u.int & 0xFFFFFFFFFFFFFFFF

    # Convert to signed 64-bit integers
    msb_signed = msb - (1 << 64) if msb >> 63 else msb
    lsb_signed = lsb - (1 << 64) if lsb >> 63 else lsb

    # Convert to 32-bit integer array format
    int_array = [
        (msb_signed >> 32) & 0xFFFFFFFF,
        msb_signed & 0xFFFFFFFF,
        (lsb_signed >> 32) & 0xFFFFFFFF,
        lsb_signed & 0xFFFFFFFF
    ]

    # Convert to signed 32-bit integers
    int_array = [i - (1 << 32) if i >> 31 else i for i in int_array]

    return int_array

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python uuidtointarr.py <uuid>")
        sys.exit(1)

    uuid_str = sys.argv[1]
    int_array = uuid_to_int_array(uuid_str)
    print(f"UUID:[I;{int_array[0]},{int_array[1]},{int_array[2]},{int_array[3]}]")