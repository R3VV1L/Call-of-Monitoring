import telebot
import subprocess

TOKEN = "TOKEN"
ID = "-ID"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

bot = telebot.TeleBot(TOKEN)


# Получение информации о системе
def get_system_info():
    UPT = subprocess.check_output("uptime", shell=True).decode()
    DF_process = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    GREP_process = subprocess.Popen(
        ["grep", "sda"], stdin=DF_process.stdout, stdout=subprocess.PIPE
    )
    DF_process.stdout.close()  # Закрытие stdin для df
    DF_output = GREP_process.communicate()[0].decode()
    FREEM = subprocess.check_output("free -m", shell=True).decode()
    FIRST = subprocess.check_output(
        "cat /proc/loadavg | awk {'print $2'} | cut -d . -f 1", shell=True
    ).decode()
    OUTPUT = (
        "ALARM"
        if int(
            subprocess.check_output(
                "cat /proc/loadavg | awk {'print $2'} | cut -d . -f 1", shell=True
            )
        )
        > 0
        else ""
    )

    return f"<pre>{UPT} {FREEM} {DF_output} {FIRST} {OUTPUT}</pre>"


# Отправка информации в Telegram
def send_message(text, parse_mode="HTML", disable_web_page_preview=True):
    bot.send_message(
        chat_id=ID,
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=disable_web_page_preview,
    )


# Проверка использования диска
def check_disk_usage():
    DISK_USAGE = int(
        subprocess.check_output(
            "df -h / | awk '{print $5}' | tail -n 1 | sed 's/%//'", shell=True
        )
    )
    if DISK_USAGE >= 75 and DISK_USAGE < 90:
        MESSAGE = f"«Погода в Хилл-Вэлли ясная»\nМесто на сервере заполненно на {DISK_USAGE}%."
        send_message(MESSAGE, parse_mode="HTML", disable_web_page_preview=True)
    elif DISK_USAGE >= 88:
        MESSAGE = f"Что за чёрт? Место на сервере заполненно на {DISK_USAGE}%!"
        send_message(MESSAGE, parse_mode="HTML", disable_web_page_preview=True)


# Получение информации о запущенных контейнерах Docker
def get_container_info():
    CONTAINERS = (
        subprocess.check_output(
            "docker ps --format '{{.ID}} {{.Image}} {{.Command}} {{.CreatedAt}} {{.Status}}'",
            shell=True,
        )
        .decode()
        .strip()
    )

    return f"Гендзюцу Docker:<pre>{CONTAINERS}</pre>"


# Отправка информации о запущенных контейнерах в Telegram
def send_container_info():
    send_message(get_container_info(), parse_mode="HTML", disable_web_page_preview=True)


# Вызов функций
send_message(get_system_info(), parse_mode="HTML", disable_web_page_preview=True)
check_disk_usage()
send_container_info()

print("Done!")
