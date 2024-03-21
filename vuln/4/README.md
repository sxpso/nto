# Уязвимость №4
## Администраторский запрос не закрыт за проверкой на админа

Подменив приходящий с сервера ответ, злоумышленник может заставить GUI отобразить управление состоянием светофоров, которое, хоть и нуждается в админке для отрисовки, не нуждается в ней со стороны API.

#### Уязвимый код
```python
def updateLight(request):
    code = HTTPStatus.OK
    data, error = auth_api.validateAuthHeader(request)
    if error:
        code = HTTPStatus.UNAUTHORIZED
    else:
        id = -1
        interval = -1
        status = 0
        changes = []
        bad_values = []
        content = request.get_json()
```
#### Исправление

```python
todo by @nailgil
```
<sub>[вернуться к Исправлению уязвимостей](../)</sub>
