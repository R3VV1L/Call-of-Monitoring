﻿# Call-of-Monitoring
 ![Version 1.0.0](https://img.shields.io/badge/Version-1.0.0-green) ![Python 3.9](https://img.shields.io/badge/Python-3.9-yellow) ![Telegram](https://img.shields.io/badge/Telegram-bot-blue)
## Описание проекта
Проект представляет собой бота для Telegram, который собирает информацию о системе и отправляет её в указанный чат. Бот использует библиотеку telebot для взаимодействия с API Telegram и subprocess для выполнения команд системы.
## Установка
* Убедитесь, что у вас установлен Python 3.9 или выше и необходимые библиотеки:  
```pip install pyTelegramBotAPI```  
* Замените TOKEN и ID в коде на ваш токен бота и идентификатор чата соответственно.
## Использование
### Основные функции
* Получение информации о системе: Бот собирает данные о загрузке системы, использовании памяти и диска, а также информацию о запущенных контейнерах Docker.
* Отправка сообщений в Telegram: Все собранные данные отправляются в указанный чат в формате HTML.
### Автозапуск
Настройка cron
Откройте терминал и введите команду для редактирования crontab:  
```crontab -e```  
Добавьте новую задачу в crontab. Например, если вы хотите запускать скрипт каждый час, добавьте следующую строку:  
```0 * * * * /usr/bin/python3 /path/to/your/Monitoring.py```  
### _Примечания_
Убедитесь, что ваш скрипт имеет права на выполнение. Вы можете установить права с помощью команды:  
```chmod +x /path/to/your/Monitoring.py```
