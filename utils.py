from pathlib import Path
import json


def get_creds(file_path):
    """
    JSON Format
    {
        "email": "example@gmail.com",
        "password": "example_password"
    }
    """

    path = Path(file_path)
    with open(path, "r") as f:
        try:
            data = json.load(f)
            return data.get("email"), data.get("password")
        except json.JSONDecodeError as e:
            return None, None
