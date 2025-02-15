from pathlib import Path

from bot.handlers.state_constants import (
    ADDING_ECO_TASK,
    ADDING_VOLUNTEER,
    END,
    SPECIFY_ACTIVITY_RADIUS,
    SPECIFY_CAR_AVAILABILITY,
    SPECIFY_CITY,
    SPECIFY_PHONE_PERMISSION,
)

BASE_PATTERN = "^({command})$"

REPORT_SOCIAL_PROBLEM_CMD = BASE_PATTERN.format(command="Сообщить о социальной проблеме")
REPORT_ECO_PROBLEM_CMD = BASE_PATTERN.format(command=ADDING_ECO_TASK)
BECOME_VOLUNTEER_CMD = BASE_PATTERN.format(command=ADDING_VOLUNTEER)
MAKE_DONATION_CMD = BASE_PATTERN.format(command="Сделать пожертвование")
SPECIFY_CITY_CMD = BASE_PATTERN.format(command="Указать город")
END_CMD = BASE_PATTERN.format(command=END)

SPECIFY_CITY_CMD = BASE_PATTERN.format(command=SPECIFY_CITY)
SPECIFY_ACTIVITY_RADIUS_CMD = BASE_PATTERN.format(command=SPECIFY_ACTIVITY_RADIUS)
SPECIFY_CAR_AVAILABILITY_CMD = BASE_PATTERN.format(command=SPECIFY_CAR_AVAILABILITY)
SPECIFY_PHONE_PERMISSION_CMD = BASE_PATTERN.format(command=SPECIFY_PHONE_PERMISSION)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR.parent / "persistence_data" / "bot_persistence_data"
SAVE_PERSISTENCE_INTERVAL = 30
