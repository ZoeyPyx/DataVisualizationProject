Philosophical Text Analysis and Visualization

Overview
This project explores patterns and themes in philosophical discourses using data visualization and natural language processing techniques. The dataset contains sentences from philosophical works, along with metadata such as author, school of thought, and publication date. The project includes interactive and static visualizations to analyze trends in word usage, sentiment, and philosophical influences over time.

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

Repository Structure
├── data/			# Raw and processed datasets
├── code/		
  ├── project.ipynb    # Jupyter notebook file
  ├── WordTrend.py    # Dash interactive visualization
├── visualizations/	# Generated plots and graphs
├── README.md		# Project overview and instruction

Usage
1. Use `app.py` to interactively explore word frequency trends over time.
   Users can input a word, and the app will filters the dataset to count how often that word appears in sentences for each publication date.
   The results are visualized in a line graph, providing insight into the historical trends of philosophical topics and concepts.
2. Open the Jupyter Notebook in JupyterLab or Jupyter Notebook.
   After installing the required dependencies, run the cells sequentially to execute the analysis and generate the visualizations.


Data Source
https://www.kaggle.com/datasets/mpwolke/cusersmarildownloadsphilosophycsv
https://www.kaggle.com/datasets/kouroshalizadeh/history-of-philosophy
