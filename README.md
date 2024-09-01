# Financial News Sentiment and Stock Market Analysis

## Overview

This project focuses on the detailed analysis of a large corpus of financial news data to discover correlations between news sentiment and stock market movements. The goal is to enhance predictive analytics capabilities for financial forecasting at Nova Financial Solutions. The project involves tasks in Data Engineering (DE), Financial Analytics (FA), and Machine Learning Engineering (MLE), aimed at refining skills in analyzing complex datasets and applying innovative thinking.

## Business Objective

Nova Financial Solutions aims to enhance its predictive analytics capabilities to significantly boost financial forecasting accuracy and operational efficiency. The primary tasks are:

1. **Sentiment Analysis:** Quantify the tone and sentiment expressed in financial news headlines using NLP techniques. Associate sentiment scores with stock symbols to understand the emotional context around stock-related news.

2. **Correlation Analysis:** Establish statistical correlations between news sentiment and stock price movements. Analyze the impact of news sentiment on stock performance considering publication dates and times.

3. **Investment Strategies:** Develop actionable investment strategies based on the relationship between news sentiment and stock price fluctuations.

## Dataset Overview

**Financial News and Stock Price Integration Dataset (FNSPID):** A comprehensive dataset combining quantitative and qualitative financial data.

- **headline:** Article release headline, often including key financial actions.
- **url:** Direct link to the full news article.
- **publisher:** Author/creator of the article.
- **date:** Publication date and time (UTC-4 timezone).
- **stock:** Stock ticker symbol (e.g., AAPL for Apple).

## Competency Mapping

The tasks in this project contribute to various competencies:

- **Professionalism:** Articulating business values.
- **Collaboration and Communication:** Reporting to stakeholders.
- **Software Development Frameworks:** Using GitHub for CI/CD, writing modular code.
- **Python Programming:** Advanced use of Python modules like Pandas, Matplotlib, Numpy, Scikit-learn, Prophet.
- **Data & Analytics Engineering:** Data filtering, transformation, and warehouse management.
- **MLOps & AutoML:** Pipeline design, data and model versioning.
- **Deep Learning and Machine Learning:** NLP, topic modeling, sentiment analysis.
- **Web & Mobile App Programming:** HTML, CSS, Flask, Streamlit.

## Minimum Essential Tasks

### Task 1: Exploratory Data Analysis (EDA)

1. **Setup:**
   - Create a GitHub repository for the project.
   - Create a new branch called `task-1`.
   - Commit your work at least three times a day with descriptive messages.

2. **Perform EDA:**
   - **Descriptive Statistics:**
     - Obtain basic statistics for textual lengths (e.g., headline length).
     - Count the number of articles per publisher.
     - Analyze publication dates for trends over time.
   - **Text Analysis:**
     - Perform sentiment analysis on headlines.
     - Use NLP for keyword extraction and topic modeling.
   - **Time Series Analysis:**
     - Analyze publication frequency and identify spikes related to market events.
   - **Publisher Analysis:**
     - Determine the most active publishers and analyze the type of news they report.

### Task 2: Quantitative Analysis with TA-Lib and PyNance

1. **Setup:**
   - Merge `task-1` branch into the main branch using a Pull Request.
   - Create a new branch called `task-2`.
   - Commit your work with descriptive messages.

2. **Perform Quantitative Analysis:**
   - **Prepare Data:**
     - Load and prepare stock price data into a pandas DataFrame.
   - **Apply Analysis Indicators:**
     - Calculate technical indicators using TA-Lib (e.g., moving averages, RSI, MACD).
   - **Use PyNance for Financial Metrics:**
     - Calculate financial metrics and visualize the data.

3. **Visualize Data:**
   - Create visualizations to understand the impact of different indicators on stock price.

## Contributing

Feel free to open issues or submit pull requests with suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the various libraries and tools used in this project.
- Inspiration from financial analytics and machine learning sources.

