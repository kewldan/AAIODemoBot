## AAIO Demo bot

## Настройка

Для работоспособности создайте в корне проекта файл `config.json` с содержимым:

```json
{
  "token": "6849007526:AAF3KV_2KGnuWnvbJ8wiEV1AKOmVGksHA_c",
  "merchant_id": "fe4076a3-1f8c-3793-901f-7484965cee49",
  "key": "ZjMwZGVjZmYtYTM0MC00NzFjLTljNWMtYzFmYzc0MGM1NjM1OnpVdig4eWp3R1V4dmhmSVQxM2lwanJfX1AxTE5jTmRT",
  "secret": "2e48aea549a059ba2232e61e0bae0ec5"
}
```

И заполните его своими данными (текущие приведены для примера)

## Запуск

#### Docker

Для запуска через Docker можно воспользоваться быстрой перезагрузкой через файл `./rebuild.sh` или вручную собрав и
запустив контейнер.

#### CLI

1. `pip install -r requirements.txt`
2. `PYTHONPATH=src python main.py`