# Уязвимость №3
## Админ может видеть чужие пароли

С правами администратора можнозапросить метод getUsers - и он вернет чужие пароли без какого-либо шифрования.

#### Уязвимый код
```python
cursor = Database().connection.cursor()
            cursor.execute("SELECT login, isAdmin, pw, name FROM user;")
            user = None
            for row in cursor:
                user = {
                    'login': row[0],
                    'isAdmin': bool(row[1]),
                    'password': row[2],
                    'name': row[3]
                }
```
#### Исправление

```python
cursor = Database().connection.cursor()
            cursor.execute("SELECT login, isAdmin, name FROM user;")
            user = None
            for row in cursor:
                user = {
                    'login': row[0],
                    'isAdmin': bool(row[1]),
                    'name': row[2]
                }
```
<sub>[вернуться к Исправлению уязвимостей](../)</sub>
