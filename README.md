# Website Content Downloader

A Python-based tool for downloading and organizing website content including HTML, CSS, and JavaScript files. This tool is useful for web development learning, content analysis, and website archiving purposes.

## Features

- Downloads complete webpage HTML
- Extracts and saves CSS stylesheets
- Downloads JavaScript files
- Organizes content in a structured directory
- Handles relative and absolute URLs
- Respects server load with built-in delays
- User-friendly command-line interface

## Requirements

```
requests
beautifulsoup4
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/website-content-downloader.git
cd website-content-downloader
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python web_downloader.py
```

2. Enter the website URL when prompted

3. The content will be downloaded to a `webpage_content` folder with the following structure:
```
webpage_content/
├── index.html
├── css/
│   └── style_0.css
│   └── style_1.css
└── js/
    └── script_0.js
    └── script_1.js
```

## Features

- Automatic directory creation
- Error handling for failed downloads
- Progress tracking
- User agent simulation
- Support for both relative and absolute URLs
- Rate limiting to prevent server overload

## Best Practices

- Always check website's robots.txt before downloading
- Respect the website's terms of service
- Use reasonable delays between requests
- Only download content you have permission to access

## Author

Mahmoud Galal

## Disclaimer

This tool is for educational and personal use only. Users are responsible for ensuring compliance with website terms of service and applicable laws regarding web scraping and content downloads.