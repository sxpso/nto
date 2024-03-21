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

---

## CORS
CORS игнорирует Origin – ввиду чего мы можем выполнять запросы от имени администратора.

#### Уязвимый код
```python
response.headers.add(“Access-Control-Allow-Origin”, ““) CORS(app, resources={r”/“: {“origins”: “*”}})
```
#### Фикс

Заменить звездочку на домен.

---

## Race Condition in SQL queries

В конфигурации работы с базой явно установлен флаг на разрешение использования подключения другими потоками, что открывает возможность проводить Race Condition атаки.

#### Уязвимый код
```python
                self._instance.connection = sqlite3.connect(DB_PATH, check_same_thread=False)
```

#### Фикс
```python
                self._instance.connection = sqlite3.connect(DB_PATH)
```

---

## Слепая SQL-иньекция и возможный Mass Assignment

С правами администратора можно манипулировать запросом для изменения пользователя так, чтобы он вызывал сторонний SQL-код.
Однако, такой же код содержится и в методе updateLight -- а благодаря [уязвимости №4](../4) у нас получается SQL-иньекция от обычного Пользователя.

#### Уязвимый код
```python
for item in changes:
  if isFirst:
    isFirst = False
  else:
    sql_query += ", "
  sql_query += item + " = ?"
  if item == 'isAdmin':
    sql_data += (isAdmin,)
  elif item == 'pw':
    sql_data += (password1,)
  elif item == 'name':
    sql_data += (name,)
  else:
    log.debug('А это как сюда попало?! [' + str(item) + ']')
```
#### Исправление

```python
for item in changes:
    if isFirst:
        isFirst = False
    else:
        sql_query += ", "
    if item == 'isAdmin':
        sql_query += "isAdmin = ?"
        sql_data += (isAdmin,)
    elif item == 'pw':
        sql_query += "pw = ?"
        sql_data += (password1,)
    elif item == 'name':
        sql_query += "name = ?"
        sql_data += (name,)
```
