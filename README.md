# QA4A2
Attempt #2 at uploading this program to a repository
# 📰 News Summary Email Script - README

This script fetches top U.S. news headlines, summarizes them using OpenAI's GPT model, and emails the results via SendGrid.

---

## 📁 Project Structure
```
project-folder/
├── QA4A5.1.py         # Main Python script
├── .env               # Environment variables file (DO NOT SHARE)
```

---

## ✅ Prerequisites
- Python 3.10+
- An internet connection
- API keys for:
  - [NewsAPI](https://newsapi.org)
  - [OpenAI](https://platform.openai.com)
  - [SendGrid](https://sendgrid.com)

---

## 🔐 Setup .env File
Create a `.env` file in the same folder as `QA4A5.1.py` and paste your API keys like this:

```env
NEWS_API_KEY=your_newsapi_key_here
OPENAI_API_KEY=your_openai_key_here
SENDGRID_API_KEY=your_sendgrid_key_here
FROM_EMAIL=your_verified_sendgrid_email
TO_EMAIL=recipient_email
```

> ⚠️ Never upload or share your `.env` file publicly.

---

## 📦 Install Dependencies
Run this command in your terminal:

```bash
pip install openai python-dotenv sendgrid requests
```

---

## ▶️ Running the Script
To execute the script:

```bash
python QA4A5.1.py
```

---

## 💡 Features
- Retrieves top 3 U.S. news headlines
- Summarizes article descriptions using OpenAI
- Sends the summaries in a styled HTML email

---

## 🛠 Troubleshooting
- **No articles found**: Check your `NEWS_API_KEY` and its quota.
- **Summarization fails**: Check your OpenAI billing and usage.
- **Email not received**: Verify your `FROM_EMAIL` is registered with SendGrid and check spam folders.

---

## 📬 Example Output
**Subject**: Daily News Digest

**Body**:
```
📰 Today's News Summaries

1. Title of Article
   Read full article
   Summary: A brief 3-4 sentence summary...
```

---

## 📄 License
This script is for educational and personal use. Customize and expand as needed.

---

## ✍️ Author
If you have questions, contact the original script author.


