def test_signup_for_activity(client):
    # Arrange
    url = "/activities/Chess Club/signup"
    params = {"email": "newstudent@mergington.edu"}

    # Act
    response = client.post(url, params=params)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up newstudent@mergington.edu for Chess Club"