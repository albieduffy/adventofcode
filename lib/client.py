from pathlib import Path

HERE = Path(__file__).parent.resolve()
DATA = (HERE / "data").resolve()
COOKIES = {
    "session": None  # set this to your session cookie to use that API!
}


def get_day(day):
    filepath = DATA / (day + ".txt")
    if filepath.exists():
        with open(filepath) as f:
            return f.read()

    if COOKIES["session"] is None:
        raise FileNotFoundError(
                f"place input in {filepath}",
                "or set the cookie in client.py to download it"
            )

    # Download and cache the input?
    import requests
    resp = requests.get(
        f"https://adventofcode.com/2023/day/{int(day)}/input", cookies=COOKIES
    )
    resp.raise_for_status()
    resp_data = resp.text

    with open(filepath, "w") as f:
        f.write(resp_data)

    return resp_data
