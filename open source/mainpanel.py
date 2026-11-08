import mysql.connector
from mysql.connector import Error
import os
import json
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        print("[Error]: File settings.json not found!")
        input("Press Enter to exit...")
        sys.exit(1)
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Error]: Failed to load settings.json - {e}")
        input("Press Enter to exit...")
        sys.exit(1)

config = load_settings()

SSH_HOST = config.get("SSH_HOST", "")
SSH_PORT = int(config.get("SSH_PORT", 0))
SSH_USER = config.get("SSH_USER", "")
SSH_PASS = config.get("SSH_PASS", "")

DB_HOST = config.get("DB_HOST", "")
DB_USER = config.get("DB_USER", "")
DB_PASS = config.get("DB_PASS", "")
DB_NAME = config.get("DB_NAME", "")

LANGUAGES = {
    "1": {
        "name": "English",
        "title": "GdpsMasiPanel - Control Panel",
        "cmd_ban": "  /ban <ID>             - ban user",
        "cmd_stars": "  /stars <ID> <amt>     - add stars",
        "cmd_demons": "  /demons <ID> <amt>    - add demons",
        "cmd_gems": "  /gems <ID> <amt>      - add gems",
        "cmd_orbs": "  /orbs <ID> <amt>      - add orbs",
        "cmd_coins": "  /coins <ID> <amt>     - add secret coins",
        "cmd_admin": "  /isAdmin <ID>         - grant admin",
        "cmd_dellevel": "  /dellevel <ID>        - delete level",
        "cmd_info": "  /infoserv             - show server info",
        "cmd_status": "  /statusserv           - check connection",
        "cmd_about": "  /InfoProgramm         - about the program",
        "cmd_exit": "  /exit                 - exit panel",
        "enter_cmd": "[GdpsMasiPanel]: ",
        "invalid_args": "Invalid arguments. Usage: {}",
        "not_found": "User with ID {} not found.",
        "banned": "User \"{}\" (ID: {}) has been Banned.",
        "added": "User \"{}\" (ID: {}) received {} {}.",
        "admin_granted": "User \"{}\" (ID: {}) is now an Admin.",
        "level_deleted": "Level with ID {} has been deleted.",
        "level_not_found": "Level with ID {} not found.",
        "db_error": "[DB Error]: {}",
        "conn_error": "[Error]: Could not connect to database: {}",
        "unknown": "Unknown command. Type /help for a list of commands.",
        "help": "--- COMMANDS ---",
        "exit": "Exiting...",
        "info_title": "--- SERVER INFO ---",
        "info_host": "Host: {}",
        "info_db": "Database: {}",
        "info_user": "User: {}",
        "status_ok": "[Status]: Connected to database successfully.",
        "status_fail": "[Status]: Connection failed: {}",
        "about_title": "=== ABOUT MASIPANEL ===",
        "about_text": "GdpsMasiPanel v1.0\nCreated by fgn.\nA simple but powerful tool for managing your GDPS.\n\nCommands:\n/ban, /stars, /demons, /gems, /orbs, /coins,\n/isAdmin, /dellevel, /infoserv, /statusserv,\n/InfoProgramm, /exit"
    },
    "2": {
        "name": "Русский",
        "title": "GdpsMasiPanel - Панель управления",
        "cmd_ban": "  /ban <ID>             - забанить игрока",
        "cmd_stars": "  /stars <ID> <кол>     - выдать звезды",
        "cmd_demons": "  /demons <ID> <кол>    - выдать демонов",
        "cmd_gems": "  /gems <ID> <кол>      - выдать алмазы (гемы)",
        "cmd_orbs": "  /orbs <ID> <кол>      - выдать орбы",
        "cmd_coins": "  /coins <ID> <кол>     - выдать секретные монетки",
        "cmd_admin": "  /isAdmin <ID>         - выдать админку",
        "cmd_dellevel": "  /dellevel <ID>        - удалить уровень",
        "cmd_info": "  /infoserv             - информация о сервере",
        "cmd_status": "  /statusserv           - проверить подключение",
        "cmd_about": "  /InfoProgramm         - о программе",
        "cmd_exit": "  /exit                 - выйти из панели",
        "enter_cmd": "[GdpsMasiPanel]: ",
        "invalid_args": "Неверные аргументы. Используйте: {}",
        "not_found": "Пользователь с ID {} не найден.",
        "banned": "Пользователь \"{}\" (ID: {}) Заблокирован.",
        "added": "Пользователю \"{}\" (ID: {}) выдано {} {}.",
        "admin_granted": "Пользователь \"{}\" (ID: {}) теперь Админ.",
        "level_deleted": "Уровень с ID {} удален.",
        "level_not_found": "Уровень с ID {} не найден.",
        "db_error": "[Ошибка БД]: {}",
        "conn_error": "[Ошибка]: Не удалось подключиться к базе данных: {}",
        "unknown": "Неизвестная команда. Введите /help для списка команд.",
        "help": "--- КОМАНДЫ ---",
        "exit": "Выход...",
        "info_title": "--- ИНФОРМАЦИЯ О СЕРВЕРЕ ---",
        "info_host": "Хост: {}",
        "info_db": "База данных: {}",
        "info_user": "Пользователь: {}",
        "status_ok": "[Статус]: Подключение к базе данных успешно.",
        "status_fail": "[Статус]: Ошибка подключения: {}",
        "about_title": "=== О ПРОГРАММЕ ===",
        "about_text": "GdpsMasiPanel v1.0\nСоздано fgn.\nПростой и мощный инструмент для управления твоим GDPS.\n\nКоманды:\n/ban, /stars, /demons, /gems, /orbs, /coins,\n/isAdmin, /dellevel, /infoserv, /statusserv,\n/InfoProgramm, /exit"
    }
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def connect_db():
    try:
        if SSH_PASS != "" and SSH_HOST != "":
            from sshtunnel import SSHTunnelForwarder
            server = SSHTunnelForwarder(
                (SSH_HOST, SSH_PORT),
                ssh_username=SSH_USER,
                ssh_password=SSH_PASS,
                remote_bind_address=('127.0.0.1', 3306),
                ssh_config_file=None,
                allow_agent=False,
                host_pkey_directories=[]
            )
            server.start()
            conn = mysql.connector.connect(
                host="127.0.0.1",
                port=server.local_bind_port,
                user=DB_USER,
                password=DB_PASS,
                database=DB_NAME
            )
            return conn, server
        else:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS,
                database=DB_NAME
            )
            return conn, None
    except Exception as e:
        print(LANGUAGES[lang]["conn_error"].format(e))
        return None, None

def get_user(cursor, user_id):
    cursor.execute("SELECT userName FROM users WHERE userID = %s OR extID = %s", (user_id, user_id))
    return cursor.fetchone()

def close_db(conn, server):
    if conn and conn.is_connected(): conn.close()
    if server: server.stop()

def ban_user(args):
    if len(args) != 1 or not args[0].isdigit():
        print(LANGUAGES[lang]["invalid_args"].format("/ban <ID>"))
        return
    user_id = args[0]
    conn, server = connect_db()
    if not conn: return
    try:
        cursor = conn.cursor(dictionary=True)
        user = get_user(cursor, user_id)
        if not user:
            print(LANGUAGES[lang]["not_found"].format(user_id))
            return
        cursor.execute("UPDATE users SET isBanned = 1 WHERE userID = %s OR extID = %s", (user_id, user_id))
        conn.commit()
        print(LANGUAGES[lang]["banned"].format(user['userName'], user_id))
    except Error as e:
        print(LANGUAGES[lang]["db_error"].format(e))
    finally:
        close_db(conn, server)

def add_stat(args, column, stat_name_key):
    if len(args) != 2 or not args[0].isdigit() or not args[1].isdigit():
        print(LANGUAGES[lang]["invalid_args"].format(f"/{stat_name_key.lower()} <ID> <amt>"))
        return
    user_id, amount = args[0], args[1]
    conn, server = connect_db()
    if not conn: return
    try:
        cursor = conn.cursor(dictionary=True)
        user = get_user(cursor, user_id)
        if not user:
            print(LANGUAGES[lang]["not_found"].format(user_id))
            return
        cursor.execute(f"UPDATE users SET {column} = {column} + %s WHERE userID = %s OR extID = %s", (amount, user_id, user_id))
        conn.commit()
        print(LANGUAGES[lang]["added"].format(user['userName'], user_id, amount, stat_name_key))
    except Error as e:
        print(LANGUAGES[lang]["db_error"].format(e))
    finally:
        close_db(conn, server)

def grant_admin(args):
    if len(args) != 1 or not args[0].isdigit():
        print(LANGUAGES[lang]["invalid_args"].format("/isAdmin <ID>"))
        return
    user_id = args[0]
    conn, server = connect_db()
    if not conn: return
    try:
        cursor = conn.cursor(dictionary=True)
        user = get_user(cursor, user_id)
        if not user:
            print(LANGUAGES[lang]["not_found"].format(user_id))
            return
        cursor.execute("UPDATE accounts SET isAdmin = 1 WHERE accountID = %s", (user_id,))
        conn.commit()
        print(LANGUAGES[lang]["admin_granted"].format(user['userName'], user_id))
    except Error as e:
        print(LANGUAGES[lang]["db_error"].format(e))
    finally:
        close_db(conn, server)

def delete_level(args):
    if len(args) != 1 or not args[0].isdigit():
        print(LANGUAGES[lang]["invalid_args"].format("/dellevel <ID>"))
        return
    level_id = args[0]
    conn, server = connect_db()
    if not conn: return
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT levelID FROM levels WHERE levelID = %s", (level_id,))
        level = cursor.fetchone()
        if not level:
            print(LANGUAGES[lang]["level_not_found"].format(level_id))
            return
        cursor.execute("DELETE FROM levels WHERE levelID = %s", (level_id,))
        conn.commit()
        print(LANGUAGES[lang]["level_deleted"].format(level_id))
    except Error as e:
        print(LANGUAGES[lang]["db_error"].format(e))
    finally:
        close_db(conn, server)

def show_info():
    clear_screen()
    print(LANGUAGES[lang]["info_title"])
    print(LANGUAGES[lang]["info_host"].format(SSH_HOST if SSH_PASS else DB_HOST))
    print(LANGUAGES[lang]["info_db"].format(DB_NAME))
    print(LANGUAGES[lang]["info_user"].format(DB_USER))

def check_status():
    conn, server = connect_db()
    if conn:
        print(LANGUAGES[lang]["status_ok"])
        close_db(conn, server)
    else:
        print(LANGUAGES[lang]["status_fail"].format("Connection failed"))

def show_about():
    clear_screen()
    print(LANGUAGES[lang]["about_title"])
    print(LANGUAGES[lang]["about_text"])

def print_help():
    print("=" * 55)
    print(f"      {LANGUAGES[lang]['title']}")
    print("=" * 55)
    for cmd in ["cmd_ban", "cmd_stars", "cmd_demons", "cmd_gems", "cmd_orbs", "cmd_coins", "cmd_admin", "cmd_dellevel", "cmd_info", "cmd_status", "cmd_about", "cmd_exit"]:
        print(LANGUAGES[lang][cmd])
    print("=" * 55)

def main():
    global lang
    clear_screen()
    print("Select language / Выберите язык:")
    print("1. English")
    print("2. Русский")
    choice = input("> ").strip()
    lang = choice if choice in LANGUAGES else "1"
    
    clear_screen()
    print_help()

    while True:
        command = input(f"\n{LANGUAGES[lang]['enter_cmd']}").strip()
        if not command: continue
        
        parts = command.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == "/ban":
            ban_user(args)
        elif cmd == "/stars":
            add_stat(args, "stars", "Stars" if lang == "1" else "звезд")
        elif cmd == "/demons":
            add_stat(args, "demons", "Demons" if lang == "1" else "демонов")
        elif cmd == "/gems":
            add_stat(args, "diamonds", "Gems" if lang == "1" else "алмазов")
        elif cmd == "/orbs":
            add_stat(args, "orbs", "Orbs" if lang == "1" else "орбов")
        elif cmd == "/coins":
            add_stat(args, "userCoins", "Secret Coins" if lang == "1" else "секретных монет")
        elif cmd == "/isadmin":
            grant_admin(args)
        elif cmd == "/dellevel":
            delete_level(args)
        elif cmd == "/infoserv":
            show_info()
        elif cmd == "/statusserv":
            check_status()
        elif cmd == "/infoprogramm":
            show_about()
        elif cmd == "/help":
            print_help()
        elif cmd == "/exit":
            print(LANGUAGES[lang]["exit"])
            break
        else:
            print(LANGUAGES[lang]["unknown"])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
