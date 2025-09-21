from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

#Test home endpoint
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello World"}
    
# Test Post
def test_create_todo():
    response = client.post("/todo",json={
        "id":1,
        "name":"SEL",
        "des":"Software Engineering Lab"
    })
    assert response.status_code ==200
    assert response.json()[0] == {"id":1,"name":"SEL","des":"Software Engineering Lab"}

# Test Get All
def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    #option 1 - if is there any instance
    assert isinstance(response.json(),list) #option 2 - if the length is greater than 0
    assert len(response.json())>0

# Test Put
def test_update_todo():
    response = client.put("/todos/1",json={
        "id":1,
        "name":"SE",
        "des":"Software Engineering"
    })
    assert response.status_code == 200
    assert response.json()[0]["name"] == "SE"

# Test Delete
def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {
        "id":1,
        "name":"SE",
        "des":"Software Engineering"
    }