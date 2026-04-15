# ✦ The Rewriter — Journalistic Article Rewriter

A single-file web app that rewrites any article in a journalistic, SEO-optimised, copyright-free style — powered by Claude (Anthropic). Runs entirely on GitHub Pages with **no backend, no server, no cost to host**.

---

## 🚀 Deploy to GitHub Pages (5 steps)

1. **Create a new GitHub repository** (e.g. `article-rewriter`) — set it to Public

2. **Upload `index.html`** — drag it into the repo root

3. **Enable GitHub Pages**:
   - Go to `Settings` → `Pages`
   - Source: `Deploy from a branch`
   - Branch: `main` / `(root)`
   - Click **Save**

4. **Wait ~60 seconds**, then your app is live at:
   ```
   https://<your-username>.github.io/<repo-name>/
   ```

5. **Open the app, enter your Anthropic API key** → it's saved in your browser locally

---

## ✨ Features

| Feature | Detail |
|---|---|
| 🔗 URL fetch | Paste any article URL — auto-extracts text via CORS proxy |
| 📋 Paste mode | Paste raw article text directly |
| 🎭 5 tones | Journalistic · Analytical · Conversational · Investigative · Editorial |
| 📏 Length control | Same / Shorter / Longer |
| 🔑 SEO keywords | Weaves your target keywords in naturally |
| 📡 Streaming | Real-time word-by-word output |
| 📊 Stats | Word count, read time, character count |
| ⬇️ Export | Download as `.txt` or formatted `.html` |
| 🔐 Privacy | API key stored in your browser only — never sent anywhere except Anthropic |

---

## 🔑 Getting an Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up / Log in
3. Navigate to **API Keys** → **Create Key**
4. Paste the key (`sk-ant-...`) into the app and click **Save**

---

## ⚠️ URL Fetching Note

URL fetching uses public CORS proxies (`allorigins.win` / `corsproxy.io`). Some sites block these. If a URL fails, simply **copy-paste the article text** using the Paste tab — it works perfectly.

---

## 🏗 Tech Stack

- Pure HTML + CSS + JS (zero dependencies, zero build step)
- Claude API (`claude-sonnet-4-20250514`) with streaming
- Hosted on GitHub Pages (free, permanent URL)

---

## 📄 License

MIT — use freely, modify as needed.
