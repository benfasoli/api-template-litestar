import tomllib
from functools import cache


@cache
def get_version() -> str:
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)

    version = str(pyproject["project"]["version"])
    return version


if __name__ == "__main__":
    version = get_version()
    print(version)
