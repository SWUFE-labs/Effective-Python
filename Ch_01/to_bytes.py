"""This helper function takes a 'str' or 'bytes' & always returns a 'bytes'."""

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value    # Instance of bytes
