# Python Amazon Product Scraper
This Python project is designed to scrape product details from Amazon for a set of search queries. The script is developed with modularity, efficiency, and readability in mind.

# Objective
The objective of this project is to develop a Python script that can:

# Read search queries from an input file (user_queries.json).
Scrape product details from the first 20 pages of Amazon search results for each query.
Extract product details such as title, total reviews, price, image URL, and optionally other fields.
Save the scraped data into JSON files named after the search query (e.g., headphones.json).
Implement error handling for network requests, parsing errors, and file operations.
Code Organization
The codebase is organized as follows:

main.py: Orchestrates the reading of queries, the scraping process, and saving of data.
query_reader.py: Contains functionality to read search queries from the user_queries.json file.
scraper.py: Defines a Scraper class responsible for fetching web pages and extracting product details.
product.py: Defines a Product class to model the product data.
data_saver.py: Contains functionality to save extracted data into JSON files.
Additional Considerations

Dependencies
This project requires the following dependencies:


Clone the repository to your local machine.
Install the dependencies by running pip install -r requirements.txt.
Ensure user_queries.json is present in the project directory with a list of search queries.
Run main.py using Python: python main.py.

Documentation
For further details on design decisions and usage instructions, refer to the inline comments in the source code.






