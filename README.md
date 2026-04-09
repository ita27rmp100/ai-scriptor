# AI-SCRIPTOR

**AI-SCRIPTOR** is an on-demand, AI-assisted script generator that allows users to dynamically generate and save Python, JavaScript - or any programming language you want -scripts based on high-level ideas. The generated scripts are automatically written to files and committed to a Git repository.

---

## 🚀 Features

- 🎯 Idea-based script generation
- 🧠 AI-powered content generation using idea titles and descriptions
- 📁 Supports multiple file formats: `.py`, `.js`, etc.
- 💾 Auto-saves scripts to specified filenames
- 🔁 Git integration: commits and pushes generated files
- 🖥️ Interactive command-line interface (CLI)

---

## 📂 Folder Structure

```
AI-SCRIPTOR/
├── generated/                 # Folder for on-demand scripts
├── Py_random_testing/         # Folder for Python test scripts (for randomly creation)
├── .env                       # Contains API keys / secrets
├── .gitignore                 # Git ignored files list
├── multiple-scripts.py        # A script to create batch of python scripts with random ideas
├── on-demand-generation.py    # Main interactive CLI tool to generate a script "based on a specific idea using a chosen language"
├── random-generator.py        # Random idea picker/generator
└── README.md                  # Project documentation
```

---

## 📦 Usage

1. Run the main script:
    ```bash
    python on-demand-generation.py
    ```

2. Follow the prompts:
    - Enter idea title
    - Describe the idea
    - Select language (`py`, `js`, etc.)
    - Choose the filename with its extension.

3. Generated script will be:
    - Saved in appropriate folder
    - Auto-staged, committed, and pushed to GitHub

---

## 🔧 Requirements

- Python 3.8+
- [Groq](https://groq.com/) API key in `.env`
- Git installed and initialized

---

## 📄 License

MIT License — free to use and modify.

---

## 🤖 Example

> Generate a script titled **"YouTube downloader"** in JavaScript, and save it as `JS_Ud.js`.

```bash
-> ai-scriptor $ Idea you want generate : youtube downloader
-> ai-scriptor $ Give description : a simple script to download youtube videos through their links
-> ai-scriptor $ Select language : javascript
-> ai-scriptor $ choose filenmae (with extension) : JS_Ud.js
```

🎉 Done! File saved and pushed.

---

## 👨‍💻 Author

Made with ❤️ by @ita27rmp100
