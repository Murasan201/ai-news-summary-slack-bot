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

## Prerequisites

- Python 3.7 or higher
- Install dependencies:
  ```bash
  pip install feedparser openai requests
  ```

## Configuration

Set the following environment variables before running the script:

```bash
export OPENAI_API_KEY="your_openai_api_key"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
```

## Usage

Run the script:

```bash
python ai_news_summary_slack_bot.py
```

## Scheduling

You can automate the script execution with cron or systemd. For example, to run daily at 9 AM:

```cron
0 9 * * * /usr/bin/env python3 /path/to/ai_news_summary_slack_bot.py
```

## Author

Murasan  
https://murasan-net.com/

## License

This project is released under the MIT License.
