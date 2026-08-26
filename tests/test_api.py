import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


class TestHomePage:
    def test_home_returns_200(self, client: TestClient) -> None:
        response = client.get("/")
        assert response.status_code == 200

    def test_home_contains_start_screen(self, client: TestClient) -> None:
        response = client.get("/")
        assert "Soc Ops" in response.text
        assert "Start Game" in response.text
        assert "How to play" in response.text
        assert 'hx-post="/start"' in response.text
        assert 'hx-target="#game-container"' in response.text
        assert 'hx-swap="outerHTML"' in response.text

    def test_home_sets_session_cookie(self, client: TestClient) -> None:
        response = client.get("/")
        assert "session" in response.cookies


class TestStartGame:
    def test_start_returns_game_board(self, client: TestClient) -> None:
        # First visit to get session
        client.get("/")
        response = client.post("/start")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
        assert "← Back" in response.text

    def test_board_has_25_squares(self, client: TestClient) -> None:
        client.get("/")
        response = client.post("/start")
        # Count the toggle buttons (squares with hx-post="/toggle/")
        assert response.text.count('hx-post="/toggle/') == 24  # 24 + 1 free space

    def test_start_scavenger_hunt_returns_question_list(
        self, client: TestClient
    ) -> None:
        client.get("/")
        response = client.post("/start?mode=scavenger_hunt")

        assert response.status_code == 200
        assert "SCAVENGER HUNT" in response.text
        assert "FREE SPACE" not in response.text
        assert 'role="progressbar"' in response.text
        assert response.text.count('type="checkbox"') == 24
        assert response.text.count('hx-post="/toggle/') == 24

    def test_scavenger_hunt_starts_with_zero_progress(self, client: TestClient) -> None:
        client.get("/")
        response = client.post("/start?mode=scavenger_hunt")

        assert 'aria-valuenow="0"' in response.text
        assert "0 / 24" in response.text


class TestToggleSquare:
    def test_toggle_marks_square(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/toggle/0")
        assert response.status_code == 200
        # The response should contain the game screen with a marked square
        assert "FREE SPACE" in response.text

    def test_scavenger_hunt_toggle_updates_progress(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start?mode=scavenger_hunt")
        response = client.post("/toggle/0")

        assert response.status_code == 200
        assert 'aria-valuenow="1"' in response.text
        assert "1 / 24" in response.text
        assert 'aria-pressed="true"' in response.text

    def test_scavenger_hunt_completes_after_all_questions(
        self, client: TestClient
    ) -> None:
        client.get("/")
        client.post("/start?mode=scavenger_hunt")

        response = None
        for square_id in range(24):
            response = client.post(f"/toggle/{square_id}")

        assert response is not None
        assert response.status_code == 200
        assert 'aria-valuenow="24"' in response.text
        assert "24 / 24" in response.text
        assert "SCAVENGER HUNT COMPLETE" in response.text
        assert 'hx-post="/dismiss-modal"' in response.text

    def test_dismissing_scavenger_hunt_modal_keeps_hunt_screen(
        self, client: TestClient
    ) -> None:
        client.get("/")
        client.post("/start?mode=scavenger_hunt")
        for square_id in range(24):
            client.post(f"/toggle/{square_id}")

        response = client.post("/dismiss-modal")

        assert response.status_code == 200
        assert "SCAVENGER HUNT" in response.text
        assert "SCAVENGER HUNT COMPLETE" not in response.text
        assert "24 / 24" in response.text


class TestResetGame:
    def test_reset_returns_start_screen(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/reset")
        assert response.status_code == 200
        assert "Start Game" in response.text
        assert "How to play" in response.text


class TestDismissModal:
    def test_dismiss_returns_game_screen(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/dismiss-modal")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
