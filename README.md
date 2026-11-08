# GdpsMasiPanel 🛠️
**Portable Command-Line Admin Panel for Cvolton GDPS**

---

### 📖 About the Project / О проекте
**GdpsMasiPanel** is a lightweight, portable command-line tool designed for Geometry Dash Private Server (GDPS) administrators. It allows you to manage players, stats, and levels instantly through simple commands. No Python installation or coding skills required — just download, configure your database settings, and run!

**GdpsMasiPanel** — это легкий и портативный консольный инструмент, созданный для администраторов приватных серверов Geometry Dash (GDPS). Он позволяет управлять игроками, статистикой и уровнями через простые команды. Установка Python не требуется — просто скачайте, настройте подключение к базе данных и запускайте!

---

### 🧪 Compatibility Note / Совместимость
*   ⚠️ **Important:** Currently, this panel is **fully optimized for Cvolton-based GDPS cores only**. Support for a wider variety of server cores and custom database structures is planned for future updates.
*   ⚠️ **Важно:** На данный момент панель **полностью оптимизирована только для сборок на базе Cvolton**. Поддержка большинства других серверных ядер и кастомных структур баз данных появится в скором времени.

---

### ✨ Implemented Features / Реализованные фичи:

*   📦 **Portable & Ready-to-Run / Портативность**
    Fully pre-compiled. No installation needed. / Полностью скомпилировано в готовый файл. Не требует установки.
    
*   🌐 **Multi-language Support / Мультиязычность**
    Built-in support for both English and Russian interfaces. / Встроенная поддержка английского и русского интерфейсов.

*   👤 **Player Management / Управление игроками**
    Ban users instantly or grant administrative privileges (`isAdmin`). / Быстрый бан пользователей или выдача прав администратора (`isAdmin`).

*   📊 **Stat Modification / Изменение статистики**
    Add stars, demons, gems, orbs, and secret coins directly by player ID. / Начисление звезд, демонов, гемов (алмазов), орбов и секретных монет по ID игрока.

*   🗺️ **Level Moderation / Модерация уровней**
    Permanently delete levels from your database. / Безвозвратное удаление уровней из базы данных.

---

### 💻 Commands / Список команд

| Command / Команда | Arguments / Аргументы | Description / Описание |
| :--- | :--- | :--- |
| `/ban` | `<ID>` | Ban user by ID / Забанить игрока |
| `/stars` | `<ID> <amt>` | Add stars to user / Выдать звезды |
| `/demons` | `<ID> <amt>` | Add demons to user / Выдать демонов |
| `/gems` | `<ID> <amt>` | Add gems to user / Выдать алмазы (гемы) |
| `/orbs` | `<ID> <amt>` | Add orbs to user / Выдать орбы |
| `/coins` | `<ID> <amt>` | Add secret coins to user / Выдать секретные монетки |
| `/isAdmin` | `<ID>` | Grant administrative status / Выдать админку |
| `/dellevel` | `<ID>` | Permanently delete a level / Удалить уровень |
| `/infoserv` | *None* | Show server config details / Информация о сервере |
| `/statusserv` | *None* | Test database connection / Проверить подключение |
| `/InfoProgramm`| *None* | About the program / О программе |
| `/exit` | *None* | Close the panel / Выйти из панели |

---

### ⚙️ Setup / Настройка

1. Open the pre-included `settings.json` file in any text editor.
   *Откройте идущий в комплекте файл `settings.json` в любом текстовом редакторе.*
2. Fill in your GDPS database connection details:
   *Заполните данные для подключения к вашей базе данных GDPS:*

```json
{
  "DB_HOST": "localhost",
  "DB_USER": "gdps_user",
  "DB_PASS": "your_database_password",
  "DB_NAME": "gdps_database_name"
}
```
3. Run the executable file and select your language.
   *Запустите исполняемый файл программы и выберите язык.*

---
### 🤝 Credits / Благодарности
*   Developed by **fgn** (MasiGdps / MasiVera Team)
*   Special thanks to the GDPS administration community.

*Originally started with MasiGdps. 🐾*
