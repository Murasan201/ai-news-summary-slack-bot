# ai-news-summary-slack-bot

**Description:**  
A Python bot that fetches AI news from RSS feeds, uses OpenAI’s ChatGPT to generate concise summaries, and posts them to Slack via Incoming Webhooks.

## Features

- Fetch latest articles from:
  - MIT Technology Review AI
  - AI News
  - ITmedia AI＋
- Summarize articles with OpenAI API (ChatGPT)
- Post summaries to Slack using Incoming Webhooks
- **Notebook Version:** Interactive Jupyter Notebook available for experimentation and step-by-step execution

## Prerequisites

- Python 3.7 or higher
- Jupyter Notebook or Jupyter Lab (for interactive usage)

## Setup

1. Create and activate a virtual environment, then install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install feedparser openai requests jupyter
   ```

2. Optionally, install Jupyter Lab:

   ```bash
   pip install jupyterlab
   ```

## Configuration

Set the following environment variables before running the script or notebook:

```bash
export OPENAI_API_KEY="your_openai_api_key"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
```

## Usage

### 1. Script Version

Run the Python script directly:

```bash
python ai_news_summary_slack_bot.py
```

### 2. Notebook Version

1. Launch Jupyter Notebook in the project root:
   ```bash
   jupyter notebook
   ```
2. Open the notebook file at `notebook/ai_news_summary_slack_bot.ipynb`.
3. Execute cells interactively to fetch, summarize, and post news to Slack.

## Scheduling

You can automate the script execution with cron or systemd. For example, to run daily at 9 AM:

```cron
0 9 * * * /usr/bin/env python3 /path/to/ai_news_summary_slack_bot.py
```

## Directory Structure

```
├── ai_news_summary_slack_bot.py
├── notebook/
│   └── ai_news_summary_slack_bot.ipynb
├── requirements.txt
└── README.md
```

## Author

Murasan  
https://murasan-net.com/

## License

This project is released under the MIT License.
