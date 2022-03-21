from fastapi.testclient import TestClient

from app.server import app


client = TestClient(app)

def test_read_server():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_full_url():
    url = "https://www.paddle.com/en"
    response = client.get(f"/extract?url={url}")
    assert response.status_code == 200
    assert response.json() == {
        "url": f"{url}",
        "domain": f"paddle.com",
        "freemail_provider": False
    }
 

def test_domain_provider():
    url = "https://www.paddle.herokuapp.com/website"
    response = client.get(f"/extract?url={url}")
    assert response.status_code == 200
    assert response.json() == {
        "url": f"{url}",
        "domain": f"paddle.herokuapp.com",
        "freemail_provider": False
    }

def test_freemail_provider():
    url = "gmail.com"
    response = client.get(f"/extract?url={url}")
    assert response.status_code == 200
    assert response.json() == {
        "url": f"{url}",
        "domain": f"{url}",
        "freemail_provider": True
    }