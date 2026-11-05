from app import app

def test_index():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json == [
        {"id": 1, "title": "Estudar Docker"},
        {"id": 2, "title": "criar o pipeline"}
    ]