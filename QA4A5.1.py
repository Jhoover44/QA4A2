import os
import requests
import openai
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()

# --- Set API keys ---
openai.api_key = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")

# --- Fetch top news ---
def fetch_articles():
    url = f'https://newsapi.org/v2/top-headlines?country=us&pageSize=3&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data.get('articles', [])

# --- Summarize using OpenAI 1.x API ---
def summarize_article(text):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You summarize news articles."},
                {"role": "user", "content": f"Summarize this in 3-4 sentences:\n\n{text}"}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"(Error summarizing: {e})"

# --- Create email content ---
def create_email_content(articles):
    html = "<h2>📰 Today's News Summaries</h2><ul>"
    for article in articles:
        title = article.get('title', 'No title')
        url = article.get('url', '#')
        content = article.get('content') or article.get('description') or ''
        summary = summarize_article(content)
        html += f"<li><strong>{title}</strong><br><a href='{url}'>Read full article</a><br><em>{summary}</em></li><br>"
    html += "</ul>"
    return html

# --- Send email ---
def send_email(subject, content_html):
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        message = Mail(from_email=FROM_EMAIL, to_emails=TO_EMAIL, subject=subject, html_content=content_html)
        response = sg.send(message)
        print(f"✅ Email sent! Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

# --- Main ---
if __name__ == "__main__":
    articles = fetch_articles()
    if articles:
        email_html = create_email_content(articles)
        send_email("📰 Daily News Digest", email_html)
    else:
        print("No articles found.")
