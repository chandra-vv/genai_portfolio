# AI Image Generation with OpenAI

A Jupyter Notebook project that uses OpenAI's `gpt-image-1` model to generate images from text prompts, with a Gradio UI for interactive use.

## Features

- Generate images from city/location names with unique pop-art style prompts
- Uses OpenAI's latest `gpt-image-1` image generation model
- Returns high-quality 1024x1024 images
- Gradio integration for an interactive web UI

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd image_generation
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and add your OpenAI API key:

```bash
cp .env.example .env
```

Then edit `.env`:

```
OPENAI_API_KEY=your_openai_api_key_here
```

> You can get an API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).

### 4. Run the notebook

Open and run `week2_day5_Image_Generation.ipynb` in Jupyter or VS Code.

## Usage

The `artist(city)` function generates an image for a given city or scene:

```python
image = artist("Tokyo")
display(image)
```

## Requirements

- Python 3.9+
- OpenAI API key with access to `gpt-image-1`
