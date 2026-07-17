import logging
import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from openai import OpenAI
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

DEFAULT_AUDIO_MODEL = "openai/whisper-large-v3"
DEFAULT_TEXT_MODEL = "gpt-4o-mini"

SYSTEM_MESSAGE = (
    "You are an assistant that produces minutes of meetings from transcripts, "
    "in markdown, with a summary (attendees, location, date), key discussion points, "
    "takeaways, and action items with owners."
)


class ConfigError(Exception):
    pass


def load_credentials() -> tuple[str, str]:
    load_dotenv()
    hf_token = os.getenv("HF_TOKEN")
    openai_key = os.getenv("OPENAI_API_KEY")
    if not hf_token or not openai_key:
        raise ConfigError("Missing HF_TOKEN or OPENAI_API_KEY - check your .env file")
    return hf_token, openai_key


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(Exception),
)
def transcribe_audio(audio_path: str, hf_token: str, model: str = DEFAULT_AUDIO_MODEL) -> str:
    logger.info("Transcribing %s with %s", audio_path, model)
    client = InferenceClient(token=hf_token)
    result = client.automatic_speech_recognition(audio_path, model=model)
    logger.info("Transcription complete (%d chars)", len(result.text))
    return result.text


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(Exception),
)
def generate_minutes(transcript: str, openai_key: str, model: str = DEFAULT_TEXT_MODEL) -> str:
    logger.info("Generating minutes with %s", model)
    client = OpenAI(api_key=openai_key)
    user_prompt = (
        "Below is a transcript of a meeting. Write minutes in markdown, including a summary "
        "with attendees, location and date; discussion points; takeaways; and action items "
        "with owners.\n\n"
        f"{transcript}"
    )
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": user_prompt},
        ],
    )
    minutes = response.choices[0].message.content
    logger.info("Minutes generated (%d chars)", len(minutes))
    return minutes
