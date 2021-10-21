import struct


header_struct = struct.Struct('!i')


def receive_all(sock, length):
    blocks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError("socket closed with %d bytes left "
                           "in this block".format(length))
        length -= len(block)
        blocks.append(block)
    return b''.join(blocks)


def send_message(sock, message):
    block_length = len(message)
    sock.sendall(header_struct.pack(block_length))
    sock.sendall(message)


def receive_message(sock):
    bl = receive_all(sock, header_struct.size)
    (length_message, ) = header_struct.unpack(bl)
    return receive_all(sock, length_message)
