from qa_forge.tools.health import ping


def test_ping_returns_pong() -> None:
    assert ping() == "pong"
