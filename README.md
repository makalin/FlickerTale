# FlickerTale

FlickerTale is a Python-based tool that crafts and shares microfiction—tiny, 280-character stories—on Twitter (X). Powered by Markov chains, it generates fleeting tales from a customizable text corpus and posts them automatically. Perfect for writers, dreamers, or anyone who loves a quick story.

## Features
- Generates short, unique stories (≤280 characters) using Markovify.
- Posts to Twitter (X) every 4 hours (configurable).
- Lightweight and local—no external servers needed beyond Twitter's API.
- Open to expansion: add your own corpus, tweak timing, or suggest new twists!

## Getting Started

### Prerequisites
- Python 3.6+
- A Twitter Developer account with API credentials (see [Twitter Developer Portal](https://developer.twitter.com)).

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/makalin/FlickerTale.git
   cd FlickerTale
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Twitter API Credentials**:
   - Create a `secrets.py` file in the root directory:
     ```python
     API_KEY = "your_api_key_here"
     API_SECRET = "your_api_secret_here"
     ACCESS_TOKEN = "your_access_token_here"
     ACCESS_TOKEN_SECRET = "your_access_token_secret_here"
     ```
   - Get these from the Twitter Developer Portal. Keep `secrets.py` private (it’s in `.gitignore`).

4. **Customize the Corpus** (Optional):
   - Edit the `CORPUS` string in `flickertale.py` with your own text, or load from a file:
     ```python
     with open("corpus.txt", "r") as f:
         CORPUS = f.read()
     ```
   - A sample `corpus.txt` is included to get you started.

5. **Run FlickerTale**:
   ```bash
   python flickertale.py
   ```
   Watch it post a story every 4 hours!

## Usage
- By default, FlickerTale posts a story every 4 hours (14,400 seconds). Adjust the `time.sleep()` value in `flickertale.py` to change this.
- Check your Twitter account to see the stories live.
- Stop the script with `Ctrl+C`.

## Contributing
We’d love your help to make FlickerTale even better! Here’s how:
- **Add Story Content**: Expand `corpus.txt` with new microfiction snippets.
- **Enhance Features**: Suggest or code interactivity (e.g., reply-based stories), trending topic integration, or genre filters.
- **Improve the Code**: Better error handling, a config file, or a fancier text generator (e.g., Hugging Face models).

1. Fork the repo.
2. Create a branch: `git checkout -b my-feature`.
3. Commit changes: `git commit -m "Added cool thing"`.
4. Push: `git push origin my-feature`.
5. Open a pull request!

## Notes
- Twitter’s free API limits you to ~50 posts/day. The default 4-hour interval keeps you under this (~6 posts/day).
- For more frequent posts, adjust responsibly or upgrade your API tier.

## License
This project is licensed under the MIT License—see [LICENSE](LICENSE) for details.

## Acknowledgments
- Built with [Markovify](https://github.com/jsvine/markovify) and [Tweepy](https://github.com/tweepy/tweepy).
- Inspired by the art of microfiction and the chaos of Twitter.
