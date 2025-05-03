#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import feedparser
import requests
import openai
from datetime import datetime

#――――――――――――――――――――――――
# 設定
#――――――――――――――――――――――――
# 環境変数から読み込み
OPENAI_API_KEY   = os.getenv("OPENAI_API_KEY")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

if not OPENAI_API_KEY or not SLACK_WEBHOOK_URL:
    raise RuntimeError("環境変数 OPENAI_API_KEY と SLACK_WEBHOOK_URL を設定してください。")

openai.api_key = OPENAI_API_KEY

# 取得するRSSフィード一覧
FEEDS = {
    "MIT Technology Review AI": "https://www.technologyreview.com/tag/artificial-intelligence/feed/",
    "AI News"                 : "https://artificialintelligence-news.com/feed/",
    "ITmedia AI＋"            : "https://www.itmedia.co.jp/ai-plus/rss2"
}

# 要約対象の記事数（各サイトごと）
MAX_ARTICLES = 3

def fetch_latest_entries(feed_url, max_items=3):
    '''
    RSSフィードを解析し、最新記事を最大 max_items 件取得して
    タイトルと要約を返す。
    '''
    feed = feedparser.parse(feed_url)
    entries = []
    for entry in feed.entries[:max_items]:
        title = entry.get("title", "").strip()
        summary = entry.get("summary", "").strip()
        link = entry.get("link", "").strip()
        entries.append(f"- <{link}|{title}>: {summary}")
    return entries

def summarize_with_chatgpt(site_name, items):
    '''
    ChatGPTに渡して、箇条書きの要約を生成。
    '''
    prompt = (
        f"以下は「{site_name}」の最新AIニュース記事の見出しと概要です。\n"
        "これらを技術トレンドや注目ポイントがひと目でわかるよう、"
        "日本語で250文字以内の箇条書き要約にしてください。\n\n"
        + "\n".join(items)
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        temperature=0.3,
        messages=[
            {"role": "system", "content": "あなたは有能な技術ニュース要約アシスタントです。"},
            {"role": "user", "content": prompt}
        ]
    )
    text = response.choices[0].message.content.strip()
    return text

def post_to_slack(text):
    '''
    Slack Incoming Webhook でメッセージを送信。
    '''
    payload = {
        "text": text
    }
    resp = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if resp.status_code != 200:
        raise ValueError(f"Slackへの通知に失敗しました: {resp.status_code} {resp.text}")

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    blocks = [f"*AIニュース要約* (`{now}`)"]
    for site_name, feed_url in FEEDS.items():
        entries = fetch_latest_entries(feed_url, MAX_ARTICLES)
        if not entries:
            blocks.append(f"> {site_name} のニュースを取得できませんでした。")
            continue
        summary = summarize_with_chatgpt(site_name, entries)
        blocks.append(f"*{site_name}* の最新要約:\n{summary}")
        blocks.append("")

    message = "\n".join(blocks)
    post_to_slack(message)
    print("Slackへ送信しました。")

if __name__ == "__main__":
    main()
