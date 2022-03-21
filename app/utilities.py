
def sanitize_url(url: str):
    result = url.lstrip()
    result = result.rstrip()
    result = result.lower()

    return result