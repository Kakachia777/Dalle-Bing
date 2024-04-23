<!DOCTYPE html>
<html>
<head>
  <title>bingart - Bing Image Creator API Wrapper</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    header {
      background-color: #333;
      color: #fff;
      padding: 20px;
      text-align: center;
    }
    main {
      padding: 20px;
    }
    section {
      margin-bottom: 40px;
    }
    h1, h2, h3 {
      color: #333;
    }
    pre {
      background-color: #f5f5f5;
      padding: 10px;
      border-radius: 5px;
    }
    .warning {
      background-color: #ffeeee;
      border: 1px solid #ff9999;
      padding: 10px;
      border-radius: 5px;
    }
    .feature-list {
      list-style-type: none;
      padding: 0;
    }
    .feature-list li {
      display: flex;
      align-items: center;
      margin-bottom: 10px;
    }
    .feature-list li:before {
      content: "🔑";
      margin-right: 10px;
    }
    .code-block {
      background-color: #f5f5f5;
      padding: 20px;
      border-radius: 5px;
      font-family: monospace;
      white-space: pre-wrap;
      word-wrap: break-word;
    }
    .exception-list {
      list-style-type: none;
      padding: 0;
    }
    .exception-list li {
      display: flex;
      align-items: center;
      margin-bottom: 10px;
    }
    .exception-list li:before {
      content: "🚨";
      margin-right: 10px;
    }
  </style>
</head>
<body>
  <header>
    <h1>🎨 bingart</h1>
  </header>
  <main>
    <section>
      <h2>Description</h2>
      <p>bingart is an unofficial 🤫 API wrapper for Bing Image Creator (based on DALL-E 3). It allows you to programmatically generate 🖼️ AI-powered images using Bing's image creation tool.</p>
      <div class="warning">
        <p>⚠️ <strong>Warning:</strong> The `_U` auth cookie should be changed every 2-4 weeks for working.</p>
      </div>
    </section>
    <section>
      <h2>Key Features</h2>
      <ul class="feature-list">
        <li>🖼️ <strong>Generate images</strong> by providing a text prompt</li>
        <li>📸 <strong>Get image URLs</strong> for up to 4 generated images</li>
        <li>🔐 <strong>Authentication</strong> via saved Bing cookies or auto-fetched from browsers</li>
        <li>⚠️ <strong>Custom exceptions</strong> for common issues</li>
      </ul>
    </section>
    <section>
      <h2>Usage</h2>
      <p>Import and instantiate the `BingArt` class with a valid `_U` cookie value:</p>
      <div class="code-block">
from bingart import BingArt

bing_art = BingArt(auth_cookie_U='...')

try:
    results = bing_art.generate_images('sunset')
    print(results)
finally:
    bing_art.close_session()
      </div>
      <p>Sometimes an extra cookie called `KievRPSSecAuth` is required for it to work properly:</p>
      <div class="code-block">
bing_art = BingArt(auth_cookie_U='...', auth_cookie_KievRPSSecAuth='...')
      </div>
      <p>You can also try the auto cookie search feature:</p>
      <div class="code-block">
bing_art = BingArt(auto=True)
      </div>
      <p>Call `generate_images()` with your query text:</p>
      <div class="code-block">
results = bing_art.generate_images("a cat painting in Picasso style")
      </div>
      <p>The return value contains image URLs and original prompt:</p>
      <div class="code-block">
{
  "images": [
    {"url": "https://..."}
  ],
  "prompt": "a cat painting in Picasso style"
}
      </div>
    </section>
    <section>
      <h2>Exceptions</h2>
      <ul class="exception-list">
        <li><code>AuthCookieError</code>: Invalid authentication cookie</li>
        <li><code>PromptRejectedError</code>: Prompt rejected as unethical</li>
      </ul>
    </section>
    <section>
      <h2>Contributing</h2>
      <p>Pull requests welcome! Please open an issue to discuss major changes.</p>
    </section>
  </main>
</body>
</html>
