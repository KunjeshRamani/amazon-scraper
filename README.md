# Amazon Price Scraper

A Python-based Amazon product price scraper created for **educational and learning purposes only**.

This project demonstrates how web scraping works using Python, `requests`, and `BeautifulSoup`, including extracting product information, processing prices, and sending email notifications when a price meets a specified condition.

> [!WARNING]
> **Educational Use Only**
>
> This project is provided strictly for educational purposes. It is intended to help developers understand web scraping concepts and Python programming.
>
> Amazon's terms and policies may restrict automated access, scraping, crawling, data mining, and other forms of automated data collection from its websites. Developers should review Amazon's current terms and policies before using automated tools against Amazon websites.

## ⚠️ Important Disclaimer

The author does **not** encourage or endorse unauthorized scraping, crawling, automated access, or circumvention of Amazon's security and anti-bot mechanisms.

This repository is intended to demonstrate concepts such as:

- HTTP requests
- HTML parsing
- CSS selectors
- BeautifulSoup
- Extracting product information
- Price parsing
- Conditional logic
- Email notifications
- Python project organization

**Do not use this project to bypass CAPTCHAs, bot protection, authentication, rate limits, access controls, or other technical restrictions.**

The legal status of web scraping varies depending on the jurisdiction, website terms, method of access, type of data, and intended use. A website's terms of use and applicable laws should be reviewed before using automated data collection.

## Features

- Fetch product pages using Python
- Parse HTML with BeautifulSoup
- Extract product title
- Extract product price
- Convert price text into a numeric value
- Compare the price against a target value
- Send an email notification when a condition is met

## Technologies

- Python
- Requests
- BeautifulSoup 4
- SMTP
- Gmail / SMTP-compatible email service

## Installation

Clone the repository:

```bash
git clone https://github.com/KunjeshRamani/amazon-scraper
cd amazon-scraper
