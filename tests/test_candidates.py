def test(client):
    response = client.post("/candidates")
    assert response.status_code == 200
    assert len(response.json) == 10
    response = client.post("/candidates", json={"date_from": "2019", "date_to": "2020"})
    assert response.status_code == 200
    assert response.json == [
        {
            "average": 2,
            "card": "Dreams of the Sphinx",
            "deviation": 0.85,
            "score": 0.6887,
        },
        {
            "average": 1,
            "card": "Pentex™ Subversion",
            "deviation": 0.45,
            "score": 0.649,
        },
        {"average": 3, "card": "On the Qui Vive", "deviation": 1.47, "score": 0.6026},
        {"average": 4, "card": "Villein", "deviation": 1.91, "score": 0.5629},
        {"average": 1, "card": "Giant's Blood", "deviation": 0.0, "score": 0.5033},
        {"average": 1, "card": "Wider View", "deviation": 0.55, "score": 0.4106},
        {
            "average": 2,
            "card": "Information Highway",
            "deviation": 0.87,
            "score": 0.3907,
        },
        {"average": 3, "card": "Vessel", "deviation": 1.24, "score": 0.3709},
        {"average": 5, "card": "Deflection", "deviation": 2.13, "score": 0.3444},
        {
            "average": 5,
            "card": "Telepathic Misdirection",
            "deviation": 1.57,
            "score": 0.3377,
        },
    ]
    response = client.post(
        "/candidates",
        json={
            "cards": ["Cybele", "Nana Buruku"],
            "date_from": "2015",
            "date_to": "2020",
        },
    )
    assert response.status_code == 200
    assert response.json == [
        {"average": 14, "card": "Ashur Tablets", "deviation": 6.25, "score": 1.0},
        {"average": 1, "card": "Giant's Blood", "deviation": 0.0, "score": 1.0},
        {"average": 2, "card": "The Parthenon", "deviation": 0.81, "score": 1.0},
        {"average": 1, "card": "Archon Investigation", "deviation": 0.0, "score": 0.9},
        {"average": 5, "card": "Villein", "deviation": 1.7, "score": 0.9},
        {"average": 1, "card": "Wider View", "deviation": 0.42, "score": 0.9},
        {"average": 3, "card": "Aksinya Daclau", "deviation": 0.43, "score": 0.8},
        {"average": 2, "card": "Dreams of the Sphinx", "deviation": 0.6, "score": 0.8},
        {"average": 8, "card": "Liquidation", "deviation": 2.42, "score": 0.8},
        {"average": 1, "card": "Pentex™ Subversion", "deviation": 0.48, "score": 0.8},
    ]
