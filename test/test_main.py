
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from fastapi import status
from app.infrastructure.database import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL="sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False }, poolclass=StaticPool)

TestSession = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def override_get_db():
    db = TestSession()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def setup():
    Base.metadata.create_all(bind=engine)
def teardown():
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)
def test_return_users():
    
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    
def test_create_users():
    response = client.post("/users", json={
  "username": "string",
  "email": "string",
  "first_name": "string",
  "last_name": "string",
  "role": "string",
  "active": True
},
    headers={"Content-Type": "application/json"},)
    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert result.get("username") == "string"


def test_update_users():
    response = client.put("/users/1", json={
  "username": "string",
  "email": "string",
  "first_name": "bryan",
  "last_name": "string",
  "role": "string",
  "active": True
},
    headers={"Content-Type": "application/json"},)
    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert result.get("first_name") == "bryan"

def test_error_update_users():
    response = client.put("/users/1000", json={
  "username": "string",
  "email": "string",
  "first_name": "bryan",
  "last_name": "string",
  "role": "string",
  "active": True
},
    headers={"Content-Type": "application/json"},)
    assert response.status_code == status.HTTP_200_OK
    result = response.text
    assert result == "{}"


def test_find_users():
    response = client.get("/users/1",
    headers={"Content-Type": "application/json"},)
    assert response.status_code == status.HTTP_200_OK
    result = response.json()
    assert result.get("username") == "string"

def test_delete_users():
    response = client.delete("/users/1",
    headers={"Content-Type": "application/json"},)
    assert response.status_code == status.HTTP_200_OK
    result = response.text
    assert result == "true"

def test_error_delete_users():
    response = client.delete("/users/100",
    headers={"Content-Type": "application/json"},)
    assert response.status_code == status.HTTP_200_OK
    result = response.text
    assert result == "false"
