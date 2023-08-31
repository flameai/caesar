# Сервис управления принадлежности пользователей к группам (Caesar)

## Для демонстрации понимания микросервисной архитектуры (постоянно просят показать код :-))

### Предполагаемый контракт сервиса:

1. Получение пользователей из списка в БД
2. Получение групп пользователей
2. Получение принадлежности пользователя к группам в БД
3. Изменение принадлежности пользователя к группе

Требования:
1. Пользователю можно изменить принадлежность к группам только один раз в интервал времени (задается переменной среды)
2. Нагрузка на сервис не менее 600 rps


## Запуск сервиса:
```shell
make run
```
## Линтер
#### Установка линтера:
```shell
pip install -r ./source/requirements_dev.txt
```
#### Исправить форматирование

```shell
make fix_lint
```

#### Проверить линтером:

```shell
make linter
```


(Еще не сделано)
## Тестирование сервиса:
```sh
make test
```