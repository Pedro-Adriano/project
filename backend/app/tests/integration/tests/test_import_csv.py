from unittest.mock import AsyncMock, patch

from app.api import movielist


def test_import_csv_movielist(client):
    csv_content = """year;title;studios;producers;winner
1980;Movie A;Studio A;Producer 1;yes
"""

    response = client.post(
        "/movielist/v1/import",
        files={"file": ("Movielist.csv", csv_content, "text/csv")},
    )

    assert response.status_code in (200, 201)


def test_import_csv_movielist_invalid_file(client):
    with patch.object(movielist, "AwardsService") as mock_service:
        instance = mock_service.return_value
        instance.import_csv_movielist = AsyncMock(
            side_effect=ValueError("Internal Server Error")
        )

        response = client.post(
            "/movielist/v1/import",
            files={"file": ("errado.txt", b"arquivo errado", "text/plain")},
        )

    assert response.status_code == 500
    assert "Internal Server Error" in response.text


def test_import_csv_movielist_missing_field(client):
    csv_content = """year;title;producers;winner
1980;Movie A;Producer 1;yes
"""

    response = client.post(
        "/movielist/v1/import",
        files={"file": ("Movielist.csv", csv_content, "text/csv")},
    )

    assert response.status_code == 400


def test_import_csv_movielist_invalid_year(client):
    csv_content = """year;title;studios;producers;winner
abc;Movie A;Studio A;Producer 1;yes
"""
    response = client.post(
        "/movielist/v1/import",
        files={"file": ("Movielist.csv", csv_content, "text/csv")},
    )
    assert response.status_code == 500
