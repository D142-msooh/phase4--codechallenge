#!/usr/bin/env python3
import json

from app import app


def test_get_heroes():
    client = app.test_client()
    response = client.get("/heroes")
    print(f"GET /heroes: {response.status_code}")
    print(json.dumps(response.get_json()[:2], indent=2))


def test_get_hero():
    client = app.test_client()
    response = client.get("/heroes/1")
    print(f"\nGET /heroes/1: {response.status_code}")
    print(json.dumps(response.get_json(), indent=2))


def test_get_powers():
    client = app.test_client()
    response = client.get("/powers")
    print(f"\nGET /powers: {response.status_code}")
    print(json.dumps(response.get_json()[:2], indent=2))


def test_patch_power():
    client = app.test_client()
    data = {"description": "This is an updated description with more than 20 characters"}
    response = client.patch("/powers/1", json=data)
    print(f"\nPATCH /powers/1: {response.status_code}")
    print(json.dumps(response.get_json(), indent=2))


def test_create_hero_power():
    client = app.test_client()
    data = {"strength": "Average", "power_id": 1, "hero_id": 3}
    response = client.post("/hero_powers", json=data)
    print(f"\nPOST /hero_powers: {response.status_code}")
    print(json.dumps(response.get_json(), indent=2))


if __name__ == "__main__":
    print("Testing Flask Superheroes API\n" + "=" * 50)
    try:
        test_get_heroes()
        test_get_hero()
        test_get_powers()
        test_patch_power()
        test_create_hero_power()
        print("\n" + "=" * 50)
        print("All tests completed!")
    except Exception as e:
        print(f"Error: {e}")
