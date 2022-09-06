# track_task
simple tracker for registration work time
Простой трекер для регистрации времени фактической работы


## Параметры и примеры использования

positional arguments:
  action             Возможные действия [track - для регистрации времени работы (указывается в параметре --min), stat - для вывода статистики за период (указывается в параметре --days)]

options:
  -h, --help         show this help message and exit
  --project PROJECT  Имя проекта
  --min MIN          Рабочее время потраченое на проект, в минутах
  --days DAYS        Период вывода статистики, в днях (N-последних дней)

### Для внесения сведений о потраченом времени
$ python3 track.py track --project=python --min=44
$ python3 track.py track --project=project --min=45
$ python3 track.py track --project=project5 --min=78
$ python3 track.py track --project=project --min=32
$ python3 track.py track --project=project15 --min=88

### Для получения статистики
$ python3 track.py stat --project=python --days=5
09.06 05h 11m
09.05 00h 38m
09.04 01h 16m
09.03 00h 38m
09.02 00h 38m