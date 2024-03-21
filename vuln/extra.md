# Bad practice
## Possible nginx h2c smuglging (appsec-like, not a vuln, just a messy thing)

H2C smuggling позволяет обновлять соединения HTTP/1.1 до менее популярных соединений HTTP/2 over cleartext (h2c), которые могут позволить обойти контроль доступа через обратный прокси-сервер и привести к долговременному неограниченному HTTP-трафику непосредственно к бэкенду. Для митигейта надо разрешить использовать только значение websocket для заголовков обновления HTTP/1.1 (например, Upgrade: websocket).

#### Уязвимый код
```nginx
        proxy_set_header Upgrade $http_upgrade;
        proxy_http_version 1.1;
        proxy_set_header Connection $http_connection;
```

#### Фикс
```nginx
        proxy_set_header Upgrade websocket;
        proxy_http_version 1.1;
        proxy_set_header Connection $http_connection;
```
