# Philosophical Text Analysis and Visualization

# Overview
This project explores patterns and themes in philosophical discourses using data visualization and natural language processing techniques. The dataset contains sentences from philosophical works, along with metadata such as author, school of thought, and publication date. The project includes interactive and static visualizations to analyze trends in word usage, sentiment, and philosophical influences over time.

# Datasets
The project uses two primary datasets:
1. philosophy_data.csv (Too large for GitHub)
Contains text sentences, metadata, and tokenized text from various philosophical works.
Includes columns such as title, author, school, sentence_str, original_publication_date, sentence_length, and more.

Due to its large size, this file is not stored in the GitHub repository. You can download it from the following link:
https://drive.google.com/file/d/1t59uq-Au2Ew1UvHMXv6kluMxX4ylTQ4w/view?usp=drive_link

2. philosopher.csv
It represents relationships between philosophers and is useful for network analysis.
Columns: A (Philosopher A), B (Philosopher B), and Weight (strength of influence between A and B).

# Features
- Network Graph of Philosophers: A directed graph illustrating the relationships and influences between philosophers, focusing on the most influential figures.
- Timeline of Philosophical Schools Publications: An interactive scatter plot displaying publications over time, categorized by school of thought.
- Word Cloud Analysis: Visual representation of the most common words used by different philosophical schools.
- Sentiment Analysis Over Time: A line graph tracking the average sentiment of philosophical texts by publication date.
- Word Trend Analysis (Dash App): An interactive dashboard allowing users to explore the occurrence of specific words in philosophical texts over time.

# Installation
Ensure you have Python installed along with the required dependencies. Install the necessary libraries using the following command:
   pip install pandas numpy matplotlib networkx plotly dash wordcloud textblob

# Usage Guide
1. Running the Jupyter Notebook
   To explore the analysis, open and run the Jupyter notebooks in the notebooks/ directory. Note: Some interactive or large visualizations may not display properly on GitHub. To view them correctly, download the repository and run the notebooks locally in Jupyter or VS Code.
   After installing the required dependencies in the kernel, run the cells sequentially to execute the analysis and generate the visualizations.

2. Running the Dash Application
   To run the interactive Dash app, execute:
      python3 WordTrend.py
   This will launch a local server, and you can interact with the dashboard in your web browser.
   Users can input a word, and the app will filter the dataset to count how often that word appears in sentences for each publication date.
   The results are visualized in a line graph, providing insight into the historical trends of philosophical topics and concepts.

# Critical Analysis
Limitations of the Current Approach

While this project successfully visualizes influential philosophers, key concepts, and trends over time, there are several limitations:
The dataset is limited to specific sources, potentially missing key philosophers or texts. Certain schools of thought may be underrepresented or missing, influencing the clustering results. Moreover, the choice of sentences is subjective and may not represent the themes of each school listed in the datasets (susceptible to misrepresentation). Regarding methodology, the sentiment analysis is based on TextBlob, which provides a basic polarity measure. However, philosophical texts are complex and may not be accurately represented by simple positive/negative scores.

Potential Improvements and Future Directions

Integrating more sources of philosophical texts could provide a more comprehensive analysis. A promising extension of this project is to integrate the philosophy_data.csv and philosopher.csv datasets by linking them through the author column. This would allow for a deeper exploration of how different philosophical schools influence each other and how the network of philosophical thought evolves.However, this approach presents several data cleaning challenges:
a. The same philosopher may be recorded differently across the datasets (e.g., "Immanuel Kant" vs. "Kant"), requiring careful standardization.
b. Some authors appear in only one of the datasets, meaning the merged data may not fully represent all philosophers.
c. Philosophers associated with multiple schools may introduce complexity in mapping influences.

Despite these challenges, developing a more structured approach to aligning the datasets would significantly enhance philosophical discourse analysis.


# Data Source
https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadsphilosophycsv

https://www.kaggle.com/datasets/kouroshalizadeh/history-of-philosophy
