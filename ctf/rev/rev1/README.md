# rev1

При дизассемблировании получем следующие функции:

```c
_BOOL8 __fastcall sub_1285(const char *a1)
{
  int v1; // ebx
  __int16 v3; // [rsp+19h] [rbp-17h] BYREF
  char v4; // [rsp+1Bh] [rbp-15h]
  unsigned __int16 v5; // [rsp+1Ch] [rbp-14h]
  unsigned __int16 i; // [rsp+1Eh] [rbp-12h]

  v5 = strlen(a1);
  v3 = 0;
  v4 = 0;
  for ( i = 0; i < (unsigned __int16)(v5 >> 1); ++i )
  {
    v3 = *(_WORD *)&a1[2 * i];
    v1 = dword_4040[i];
    if ( v1 != (unsigned int)sub_125D(&v3, 2LL) )
      return 0LL;
  }
  return dword_4040[i] == 0;
}
```

```c
__int64 __fastcall sub_125D(__int64 a1, unsigned int a2)
{
  return sub_11DE(a1, a2, 0xFFFFFFFFLL);
}
```

```c
__int64 __fastcall sub_11DE(_BYTE *a1, unsigned __int64 a2, unsigned int a3)
{
  _BYTE *v3; // rax
  unsigned int i; // [rsp+1Ch] [rbp-Ch]

  if ( !byte_40A0 )
    sub_1159();
  for ( i = 0; i < a2; ++i )
  {
    v3 = a1++;
    a3 = (a3 >> 8) ^ dword_40C0[(unsigned __int8)(a3 ^ *v3)];
  }
  return ~a3;
}
```

```c
_DWORD *sub_1159()
{
  _DWORD *result; // rax
  int j; // [rsp+0h] [rbp-10h]
  int i; // [rsp+4h] [rbp-Ch]
  unsigned __int64 v3; // [rsp+8h] [rbp-8h]

  for ( i = 0; i <= 255; ++i )
  {
    v3 = i;
    for ( j = 0; j <= 7; ++j )
    {
      if ( (v3 & 1) != 0 )
        v3 = (v3 >> 1) ^ 0xEDB88320;
      else
        v3 >>= 1;
    }
    result = dword_40C0;
    dword_40C0[i] = v3;
  }
  byte_40A0 = 1;
  return result;
}
```



Пример программы, которая получает флаг брутфорсом:
```python
dword_4040 = [0xEDCFE1F3, 0x646BCD23, 0x50F9AD57, 0xF299B1E1, 0xC6A9B6E4, 0x3280614C, 0x93772B02, 0xAB2C3A43, 0x2A0D936A, 0x1BFA14D4, 0x255D6F2F, 0xC447F66B, 0x5AD96CF5, 0xE964AD12]

arr = [0] * 256

for i in range(256):
    tmp = i
    for j in range(8):
        if tmp & 1 == 0:
            tmp = tmp >> 1
        else:
            tmp = tmp >> 1 ^ 0xEDB88320
    arr[i] = tmp

def func(a1, a2):
    ret = 0xFFFFFFFF
    ret = arr[(a1 ^ ret) & 0xFF] ^ ret >> 8
    ret = arr[(a2 ^ ret) & 0xFF] ^ ret >> 8
    return 0xFFFFFFFF - ret

def bruteforce(d):
    for a1 in range(0xFF + 1):
        for a2 in range(0xFF + 1):
            a = func(a1, a2)
            if a == dword_4040[d]:
                print(chr(a1) + chr(a2), end="")
                return

for i in range(len(dword_4040)):
    bruteforce(i)
```

Флаг: ***nto{4n0TH3R_bRu73F0RC3_7ASk}***
