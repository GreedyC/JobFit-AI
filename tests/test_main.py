from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_setup_profile_rejects_malformed_pdf():
    response = client.post(
        "/setup/profile",
        files={
            "resume": (
                "malformed.pdf",
                b"%PDF-1.4\n%Malformed PDF content",
                "application/pdf",
            )
        },
    )

    assert response.status_code == 422
    assert response.json() == {"detail": "Unable to read PDF file"}