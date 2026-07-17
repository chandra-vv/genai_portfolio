from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from pipeline import ConfigError, generate_minutes, load_credentials, transcribe_audio


def test_load_credentials_raises_when_missing(monkeypatch):
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr("pipeline.load_dotenv", lambda: None)
    with pytest.raises(ConfigError):
        load_credentials()


def test_load_credentials_returns_tokens(monkeypatch):
    monkeypatch.setenv("HF_TOKEN", "hf_test")
    monkeypatch.setenv("OPENAI_API_KEY", "sk_test")
    monkeypatch.setattr("pipeline.load_dotenv", lambda: None)
    hf_token, openai_key = load_credentials()
    assert hf_token == "hf_test"
    assert openai_key == "sk_test"


@patch("pipeline.InferenceClient")
def test_transcribe_audio_returns_text(mock_client_cls):
    mock_client = MagicMock()
    mock_client.automatic_speech_recognition.return_value = SimpleNamespace(text="hello world")
    mock_client_cls.return_value = mock_client

    result = transcribe_audio("audio.mp3", "hf_test")

    assert result == "hello world"
    mock_client.automatic_speech_recognition.assert_called_once()


@patch("pipeline.InferenceClient")
def test_transcribe_audio_retries_then_succeeds(mock_client_cls):
    mock_client = MagicMock()
    mock_client.automatic_speech_recognition.side_effect = [
        RuntimeError("model loading"),
        SimpleNamespace(text="recovered"),
    ]
    mock_client_cls.return_value = mock_client

    result = transcribe_audio("audio.mp3", "hf_test")

    assert result == "recovered"
    assert mock_client.automatic_speech_recognition.call_count == 2


@patch("pipeline.OpenAI")
def test_generate_minutes_returns_content(mock_openai_cls):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "# Minutes\n..."
    mock_client.chat.completions.create.return_value = mock_response
    mock_openai_cls.return_value = mock_client

    result = generate_minutes("some transcript", "sk_test")

    assert result == "# Minutes\n..."
    mock_client.chat.completions.create.assert_called_once()
