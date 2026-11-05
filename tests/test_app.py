from app import app

client = app.test_client()

def test_tasks():
  response = client.get("/")
  assert response.status_code == 200
  assert len(response.get_json()) == 2
