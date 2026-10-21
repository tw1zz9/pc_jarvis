import subprocess


def open_dota():
    print("Запускаю Dota 2...")
    try:
        subprocess.Popen([
            "cmd",
            "/c",
            "start",
            "",
            "steam://rungameid/570",
        ])
        return True
    except Exception as e:
        print(f"Ошибка запуска Dota: {e}")
        return False


def close_dota():
    print("Закрываю Dota 2...")
    try:
        subprocess.run(
            ["taskkill", "/IM", "dota2.exe", "/F"],
            capture_output=True,
            text=True,
        )
        return True
    except Exception as e:
        print(f"Ошибка закрытия Dota: {e}")
        return False


def open_browser():
    print("Открываю браузер...")
    try:
        subprocess.Popen([
            "cmd",
            "/c",
            "start",
            "",
            "https://www.google.com",
        ])
        return True
    except Exception as e:
        print(f"Ошибка запуска браузера: {e}")
        return False


def close_browser():
    print("Закрываю браузер...")
    try:
        browsers = [
            "chrome.exe",
            "msedge.exe",
            "firefox.exe",
            "opera.exe",
        ]

        for process in browsers:
            subprocess.run(
                ["taskkill", "/IM", process, "/F"],
                capture_output=True,
                text=True,
            )

        return True

    except Exception as e:
        print(f"Ошибка закрытия браузера: {e}")
        return False


def shutdown_pc():
    print("Выключаю компьютер...")
    try:
        subprocess.run(["shutdown", "/s", "/t", "5"])
        return True
    except Exception as e:
        print(f"Ошибка выключения ПК: {e}")
        return False