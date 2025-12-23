from unittest.mock import patch

from app.api import movielist


def test_get_awards_intervals_error(client):
    with patch.object(movielist, "AwardsService") as mock_service:
        instance = mock_service.return_value
        instance.get_intervals.return_value = {
            "min": [{"producer": "Producer A", "interval": 1}],
            "max": [{"producer": "Producer B", "interval": 10}],
        }

        response = client.get("/movielist/v1/intervals")

    assert response.status_code == 500
