# Уязвимость №3
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
<sub>[вернуться к Исправлению уязвимостей](../)</sub>
