import tomllib

_VERSION: str | None = None


def get_version() -> str:
    global _VERSION
    if _VERSION is not None:
        return _VERSION

    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)

    _VERSION = str(pyproject["project"]["version"])
    return _VERSION


if __name__ == "__main__":
    version = get_version()
    print(version)
