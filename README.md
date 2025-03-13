Philosophical Text Analysis and Visualization

Overview
This project explores patterns and themes in philosophical discourses using data visualization and natural language processing techniques. The dataset contains sentences from philosophical works, along with metadata such as author, school of thought, and publication date. The project includes interactive and static visualizations to analyze trends in word usage, sentiment, and philosophical influences over time.

Datasets
The project uses two primary datasets:
1. philosophy_data.csv (Too large for GitHub)
Contains text sentences, metadata, and tokenized text from various philosophical works.
Includes columns such as title, author, school, sentence_str, original_publication_date, sentence_length, and more.

Due to its large size, this file is not stored in the GitHub repository. You can download it from the following link:

Download philosophy_data.csv

philosopher.csv

Represents relationships between philosophers, useful for network analysis.

Contains columns: A (Philosopher A), B (Philosopher B), and Weight (strength of influence between A and B).

Features
- Network Graph of Philosophers: A directed graph illustrating the relationships and influences between philosophers, focusing on the most influential figures.
- Timeline of Philosophical Schools Publications: An interactive scatter plot displaying publications over time, categorized by school of thought.
- Word Cloud Analysis: Visual representation of the most common words used by different philosophical schools.
- Sentiment Analysis Over Time: A line graph tracking the average sentiment of philosophical texts by publication date.
- Word Trend Analysis (Dash App): An interactive dashboard allowing users to explore the occurrence of specific words in philosophical texts over time.

Installation
Ensure you have Python installed along with the required dependencies. Install the necessary libraries using the following command:
pip install pandas numpy matplotlib networkx plotly dash wordcloud textblob

Running the Dash Application
To run the interactive Dash app, execute:
python3 WordTrend.py
This will launch a local server, and you can interact with the dashboard in your web browser.

Usage
1. Use `app.py` to interactively explore word frequency trends over time.
   Users can input a word, and the app will filters the dataset to count how often that word appears in sentences for each publication date.
   The results are visualized in a line graph, providing insight into the historical trends of philosophical topics and concepts.
2. Open the Jupyter Notebook in JupyterLab or Jupyter Notebook.
   After installing the required dependencies, run the cells sequentially to execute the analysis and generate the visualizations.


Data Source
https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadsphilosophycsv
https://www.kaggle.com/datasets/kouroshalizadeh/history-of-philosophy
