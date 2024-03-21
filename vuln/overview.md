# Обзор предоставленного сервиса
> Ильдар "mimicate" Хужиахметов


Участникам было предоставлено следующее задание:
> Необходимо найти и устранить найденные уязвимости. Сформировать отчет и доказать корректность их исправлений жюри.<br>
> Подключение к серверу: ssh administrator@10.10.[номер команды].10<br>
> Пароль: `redacted`

Так выглядела изначальная структура файлов на сервере:
- Stage3.zip
     - traffic-lights-src.tar.gz
     - traffic-lights.tar
     - users.txt
     - Инструкции.docx

В архивах вида traffic-lights* содержался исходный код сервиса и уже готовый билд для запуска из Docker.
Файл users.txt содержал уже заранее созданных в базе данных пользователей разных ролей (были как обычные пользователи, так и администраторы)
В одноименном файле содержались инструкции участником для взаимодействия с сервисом.

Сам сервис представляет собой служебное приложение для контроля за светофорами. В приложении реализован RBAC - доступными ролями являются Администратор и Оператор.

Операторы имеют права на просмотр информации о светофорах и своего личного профиля - при необходимости есть возможность оставить записку.
Администраторы, в свою очередь, имеют в наличии возможность управления пользователями и редактирования показателей того или иного светофора.
