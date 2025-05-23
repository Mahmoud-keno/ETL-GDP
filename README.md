# GDP Data ETL Pipeline

A Python ETL (Extract, Transform, Load) pipeline that extracts GDP data from Wikipedia, processes it, and stores it in multiple formats.

## Features

- Web scraping of GDP data from Wikipedia
- Data transformation and cleaning
- Multi-format output (CSV, JSON, SQLite)
- Comprehensive logging
- Modular design for easy maintenance

## Technologies Used

- Python 3
- BeautifulSoup4 (web scraping)
- Pandas (data manipulation)
- SQLite3 (database storage)
- Requests (HTTP requests)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mahmoud-keno/gdp-etl-pipeline.git
   cd gdp-etl-pipeline
## Project Structure
```markdown
gdp-etl-pipeline/
├── datasets/               # Processed data outputs
│   ├── gdp.csv
│   ├── gdp.json
│   └── gdp.db
├── main.py                 # Main script
├── README.md               # This file
├── requirements.txt        # Dependencies
└── log.txt                 # Process logs
