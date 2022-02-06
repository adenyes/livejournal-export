import click
from typing import Optional

import requests
import pickle
from pathlib import Path

COOKIE_PATH = Path("lj.cookies")


def load_lj_session_cookies() -> Optional[requests.Session]:
    session = requests.Session()
    if not COOKIE_PATH.exists():
        return None

    with COOKIE_PATH.open("rb") as cfb:
        session.cookies.update(pickle.load(cfb))
    return session


def save_lj_session_cookies(session: requests.Session) -> None:
    with COOKIE_PATH.open("wb") as cfb:
        pickle.dump(session.cookies, cfb)


def clean_lj_session_cookies() -> None:
    if not COOKIE_PATH.exists():
        return None
    COOKIE_PATH.unlink()


def get_auth_cookies(session: requests.Session, username: str, password: str) -> None:
    login_url = "https://www.livejournal.com/login.bml"
    form_data = {
        "ref": "",
        "returnto": "/",
        "user": username,
        "password": password,
        "action": "login",
    }
    response = session.post(url=login_url, data=form_data)
    if response.status_code != 302 and response.status_code != 200:
        print(
            f"Unexpected response to login, {response.status_code}, full response {response}"
        )
        raise Exception("Login failed. Unexpected response from server.")

    if "ljloggedin" not in session.cookies:
        raise Exception("Login failed. Incorrect username/password?")


def login() -> requests.Session:
    session = load_lj_session_cookies()
    if not session:
        username = click.prompt("Username:", type=click.STRING)
        password = click.prompt("Password:", type=click.STRING)
        session = requests.Session()
        get_auth_cookies(session, username, password)
        save_lj_session_cookies(session)
    return session
