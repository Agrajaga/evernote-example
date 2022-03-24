# Взаимодействие с API Evernote.

Набор скриптов для демонстрации работы с API сервиса [Evernote](https://evernote.com/intl/ru/)

## Установка
Для запуска необходим Python2.7. Установите зависимости используя `pip2`
```
pip2 install -r requirements.txt
```
Так же для запуска Вам понадобится ключ API для авторизации в сервисе. Получить его можно зарегистрировавшись на внутреннем сайте для разработчиков и тестировщиков [Sandbox Evernote](https://sandbox.evernote.com/Registration.action). После создания аккаунта пройдите на [сайт с документацией API](https://dev.evernote.com/doc/) и после регистрации своего приложения Вы получите ключ API.  
Создайте файл `.env` и поместите в него следующие переменные, значения которых Вы получите при оформлении ключа API:
```
EVERNOTE_CONSUMER_KEY=<your_consumer_key>
EVERNOTE_CONSUMER_SECRET=<your_consumer_secret>
EVERNOTE_PERSONAL_TOKEN=<your_personal_token>
```

## Использование

_`list_notebook.py`_ - получает список GUID и названий блокнотов. 
```
python2.7 list_notebooks.py
```
Результатом выполнения будет список блокнотов
```
df801af5-ba10-4b8c-b1e0-45fa51ab653f - Первый блокнот
09427be2-59fe-4e7b-b5f4-a20333043706 - Второй блокнот
```  

_`dump_inbox.py`_ - получает список заметок в указанном блокноте.  
Добавьте в файл `.env` ключ
```
INBOX_NOTEBOOK_GUID=<guid_блокнота>
```
Формат запуска
```
$python2.7 dump_inbox.py --help
usage: dump_inbox.py [-h] [number]

Dumps notes from Evernote inbox to console

positional arguments:
  number      number of records to dump

optional arguments:
  -h, --help  show this help message and exit
```
Результатом выполнения будет список заметок
```

--------- 1 ---------


Текст заметки 1

--------- 2 ---------


Текст заметки 2

--------- 3 ---------


Текст заметки 3
```  

_`add_note2journal.py`_ - добавляет в указанный блокнот новую заметку на основе другой заметки-шаблона. 
Формат запуска
```
$ python2.7 add_note2journal.py --help
usage: add_note2journal.py [-h] [date]

Adds note to notebook "Дневник", uses template note

positional arguments:
  date        date in format "YYYY-MM-DD"

optional arguments:
  -h, --help  show this help message and exit
```
Заметка-шаблон имеет следующий формат `Текст заголовка {date}{dow}#текст комментария`. При создании новой заметки `текст комментария` будет опущен, а поля `{date}` и `{dow}` будут заменены на указанную дату и день недели, соответственно. По-умолчанию будет использована текущая дата.  
Перед запуском добавьте в файл `.env` следующие ключи:
```
JOURNAL_TEMPLATE_NOTE_GUID=<guid заметки-шаблона>
JOURNAL_NOTEBOOK_GUID=<guid блокнота, куда будет добавлена заметка>
```

_`config.py`_ - содержит описание класса с переменными окружения. Не предназначен для запуска.