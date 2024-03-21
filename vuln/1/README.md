# Уязвимость №1
## SQL Injection в changePassword()

При смене пароля username не проходит валидацию, из-за чего возможно исполнить произвольный SQL-код.

#### Уязвимый код
```python
else:
  db = Database().connection
  update_cursor = db.cursor()
  sql_query = "UPDATE user SET pw = '" + str(new_password) + "' WHERE login = '" + str(username) + "';"
```
#### Исправление

```python
- sql_query = "UPDATE user SET pw = '" + str(new_password) + "' WHERE login = '" + str(username) + "';"
+ cursor.execute("UPDATE user SET pw = ? WHERE login = ?;", (new_password, username))
```
<sub>[вернуться к Исправлению уязвимостей](../)</sub>
