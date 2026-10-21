from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from actions import (
    open_dota,
    close_dota,
    open_browser,
    close_browser,
    shutdown_pc,
)

app = FastAPI()

COMMANDS = {
    "open_dota": open_dota,
    "close_dota": close_dota,
    "open_browser": open_browser,
    "close_browser": close_browser,
    "shutdown_pc": shutdown_pc,
}


class CommandRequest(BaseModel):
    command: str


@app.post("/command")
def command(request: CommandRequest):
    command = request.command

    print()
    print("========================================")
    print("     ПОЛУЧЕНА КОМАНДА ОТ JARVIS")
    print("========================================")
    print(f"Команда: {command}")
    print("========================================")

    action = COMMANDS.get(command)

    if action is None:
        print(f"Неизвестная команда: {command}")

        return {
            "status": "error",
            "message": "unknown command",
            "command": command,
        }

    try:
        result = action()

        if result:
            print(f"Команда выполнена: {command}")

            return {
                "status": "ok",
                "command": command,
            }

        print(f"Команда завершилась ошибкой: {command}")

        return {
            "status": "error",
            "message": "action failed",
            "command": command,
        }

    except Exception as e:
        print(f"Ошибка выполнения команды: {e}")

        return {
            "status": "error",
            "message": str(e),
            "command": command,
        }


def is_process_running(process_names):
    import psutil

    process_names = {name.lower() for name in process_names}

    for process in psutil.process_iter(["name"]):
        try:
            name = process.info["name"]

            if name and name.lower() in process_names:
                return True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            pass

    return False


@app.get("/state")
def get_state():
    dota_running = is_process_running([
        "dota2.exe",
    ])

    browser_running = is_process_running([
        "chrome.exe",
        "msedge.exe",
        "firefox.exe",
        "opera.exe",
    ])

    return {
        "dota": dota_running,
        "browser": browser_running,
    }


if __name__ == "__main__":

    print()
    print("========================================")
    print("       JARVIS PC AGENT")
    print("========================================")
    print("IP: 0.0.0.0")
    print("PORT: 8000")
    print("========================================")
    print()

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )