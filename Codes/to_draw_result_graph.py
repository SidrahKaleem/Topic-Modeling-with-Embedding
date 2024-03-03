# -*- coding: utf-8 -*-
"""To draw result Graph

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mEZuR5MRy4m2OH5bDrgjI1nLf-Ks85Jc
"""

import matplotlib.pyplot as plt
import numpy as np  # For data manipulation if needed

fig, ax = plt.subplots()  # Create a figure and an axes object

# Assuming data is stored in lists or arrays:
x_values = [97,56,87]
y_values_1 = [89,56,78]
y_values_2 = [45,87,66]  # Assuming multiple lines

ax.plot(x_values, y_values_1, label='Line 1')
ax.plot(x_values, y_values_2, label='Line 2')  # Add more lines as needed

ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')

ax.set_title('Graph Title')

ax.grid(True)  # Enable grid

ax.plot(color='blue', linestyle='--')  # Customize line appearance

y_values = [90,50,80]

ax.plot(x_values, y_values, marker='o', linestyle='None')  # Add markers

ax.legend()  # Display legend for multiple lines

plt.show()

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 15, 11]

# Plotting the line chart
plt.plot(x, y, marker='o', label='Sample Data')

# Adding labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Sample Line Chart')

# Adding a legend
plt.legend()

# Display the chart
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Hypothetical data for SVM and LR
categories = ['Logistic Regression', 'Random Forest', 'Decision Tree']
svm_values = [ 0.79, 0.97, 0.80]  # Replace with your SVM data
lr_values =  [0.96, 0.97, 0.81]  # Replace with your LR data

# Width of the bars
bar_width = 0.25

# Set the positions for the bars on X-axis
index = np.arange(len(categories))

# Plotting the bars
fig, ax = plt.subplots()
bar1 = ax.bar(index, svm_values, bar_width, label='Hybrid Model', color='pink')
bar2 = ax.bar(index + bar_width, lr_values, bar_width, label='WELDA Model', color='purple')

# Adding labels and title
ax.set_xlabel('')
ax.set_ylabel('Micro-F1 values')
#ax.set_title('')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(categories)
ax.legend()

# Display the chart
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate example data
actual_values = np.random.randint(100)  # Replace with your actual values
model1_predictions = actual_values + np.random.normal(0.88)  # Model 1 predictions
model2_predictions = actual_values + np.random.normal(0.372)  # Model 2 predictions

# Create scatter plot
plt.scatter(actual_values, model1_predictions, label='Model 1', alpha=0.7)
plt.scatter(actual_values, model2_predictions, label='Model 2', alpha=0.7)

# Add labels and title
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Comparison of Model Predictions')
plt.legend()

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [
    np.random.normal(0, 1, 100),
    np.random.normal(2, 1, 100),
    np.random.normal(-2, 1, 100)
]

# Create a box plot
fig, ax = plt.subplots()
ax.boxplot(data, labels=['Dataset 1', 'Dataset 2', 'Dataset 3'])

# Add labels and title
ax.set_xlabel('Datasets')
ax.set_ylabel('Values')
ax.set_title('Comparison of Datasets using Box Plot')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
x_values = np.linspace(0, 10, 100)
y_values1 = np.sin(x_values)
y_values2 = np.cos(x_values)

# Create a line chart
plt.plot(x_values, y_values1, label='Sin(x)')
plt.plot(x_values, y_values2, label='Cos(x)')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Chart Example')

# Add legend
plt.legend()

# Show the plot
plt.show()

import matplotlib.pyplot as plt

# Replace the following with your actual data
data = {
    "Category 1": [10, 20, 30, 40, 50],
    "Category 2": [30, 25, 20, 15, 10],
    "Category 3": [20, 30, 40, 50, 60],
    "Category 4": [40, 35, 30, 25, 20],
    "Category 5": [50, 45, 40, 35, 30],
}

categories = list(data.keys())
values = list(data.values())

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = [25, 40, 30, 20]
values2 = [15, 20, 10, 30]

# Create a stacked bar chart
fig, ax = plt.subplots()
ax.bar(categories, values1, label='Dataset 1', color='skyblue')
ax.bar(categories, values2, bottom=values1, label='Dataset 2', color='orange')

# Add labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Stacked Bar Chart Example')

# Add legend
ax.legend()

# Show the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Replace the following with your actual data
data = {
    'Actual': ['A', 'B', 'A', 'A', 'B', 'C', 'B', 'A', 'B', 'C'],
    'Predicted': ['A', 'A', 'C', 'B', 'B', 'C', 'A', 'C', 'B', 'A'],
}

df = pd.DataFrame(data)

# Calculate counts for each category combination
results_count = df.value_counts().unstack()

results_count.plot(kind='bar', stacked=True, figsize=(6, 6))
plt.title('Actual vs. Predicted Categories')
plt.xlabel('Category')
plt.ylabel('Count')

# Add lines and fill color for diagonals (correct predictions)
for i, (category, values) in enumerate(results_count.iterrows()):
    plt.bar(i - 0.15, values[category], color='green', alpha=0.3, label=f'Correct {category}')

# Add legend and display the chart
plt.legend()
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values_start = [10, 25, 15, 30]
values_end = [20, 40, 25, 35]

# Create a horizontal bar chart with line segments
fig, ax = plt.subplots()
for start, end, category in zip(values_start, values_end, categories):
    ax.barh(category, end - start, left=start, color='skyblue')
    ax.plot([start, end], [category, category], color='black')  # Line segments

# Add labels and title
ax.set_xlabel('Values')
ax.set_ylabel('Categories')
ax.set_title('Horizontal Bar Chart with Line Segments')

# Show the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Replace the following with your actual data
data = {
    'Feature 1': [10, 15, 20, 25],
    'Feature 2': [25, 20, 15, 10],
    'Feature 3': [30, 25, 20, 15],
    'Category': ['A', 'A', 'B', 'B'],
}

df = pd.DataFrame(data)

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
features = ['Feature 1', 'Feature 2', 'Feature 3']
values = np.random.rand(len(categories), len(features)) * 10  # Random values

# Create a horizontal bar chart with line segments
fig, ax = plt.subplots()
bar_height = 0.2  # Adjust this value based on your preference

for i, category in enumerate(categories):
    feature_values = values[i]
    colors = plt.cm.viridis(np.linspace(0, 1, len(features)))  # Different colors for each line segment
    for j, feature_value in enumerate(feature_values):
        ax.barh(y=category, width=feature_value, left=0, height=bar_height, color=colors[j])
        ax.plot([0, feature_value], [i + bar_height / 2, i + bar_height / 2], color=colors[j])  # Line segments

# Add labels and title
ax.set_xlabel('Values')
ax.set_ylabel('Categories')
ax.set_title('Horizontal Bar Chart with Line Segments')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
features = ['Feature 1', 'Feature 2', 'Feature 3']
values = np.random.rand(len(categories), len(features)) * 10  # Random values

# Create a horizontal bar chart with line segments
fig, ax = plt.subplots()
bar_height = 0.2  # Adjust this value based on your preference

for i, category in enumerate(categories):
    feature_values = values[i]
    line_colors = plt.cm.viridis(np.linspace(0, 1, len(features)))  # Different colors for each line segment
    for j, (feature_value, line_color) in enumerate(zip(feature_values, line_colors)):
        ax.barh(y=category, width=feature_value, left=0, height=bar_height, color=line_color)
        ax.plot([0, feature_value], [i + bar_height / 2, i + bar_height / 2], color=line_color)  # Line segments

# Add labels and title
ax.set_xlabel('Values')
ax.set_ylabel('Categories')
ax.set_title('Horizontal Bar Chart with Line Segments')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
features = ['Feature 1', 'Feature 2', 'Feature 3']
values =  ['0.34', '0.65', '0.89','0.94','0.64']#np.random.rand(len(categories), len(features)) * 10  # Random values

# Create a horizontal bar chart with line segments
fig, ax = plt.subplots()
bar_height = 0.2  # Adjust this value based on your preference

# Custom color palette with shades of pink
custom_colors = ['Blue', 'Red', '#FF1493']

for i, category in enumerate(categories):
    feature_values = values[i]
    for j, (feature_value, color) in enumerate(zip(feature_values, custom_colors)):
        ax.barh(y=category, width=feature_value, left=0, height=bar_height, color=color)
        ax.plot([0, feature_value], [i + bar_height / 2, i + bar_height / 2], color=color)  # Line segments

# Add labels and title
ax.set_xlabel('Values')
ax.set_ylabel('Categories')
ax.set_title('Horizontal Bar Chart with Line Segments')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
features = ['Feature 1', 'Feature 2', 'Feature 3']
values = np.random.rand(len(categories), len(features)) * 10  # Random values

# Create a horizontal bar chart with line segments
fig, ax = plt.subplots()
bar_height = 0.2  # Adjust this value based on your preference

# Custom color palette with shades of pink
custom_colors = ['#FFD1DC', '#FF69B4', '#FF1493']

for i, category in enumerate(categories):
    feature_values = values[i]
    for j, (feature_value, color) in enumerate(zip(feature_values, custom_colors)):
        ax.barh(y=category, width=feature_value, left=0, height=bar_height, color=color)
        ax.plot([0, feature_value], [i + bar_height / 2, i + bar_height / 2], color='black')  # Line segments

# Add labels and title
ax.set_xlabel('Values')
ax.set_ylabel('Categories')
ax.set_title('Horizontal Bar Chart with Line Segments')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['WELDA','TF-IDF', 'LDA', 'Word2vec', 'Glove', 'SGL', 'CGL', 'SWL','CWL']
features = ['Feature 1', 'Feature 2', 'Feature 3','Feature 4','Feature 5','Feature 6','Feature 7','Feature 8','Feature 9' ]
values = ['0.88','0.37', '0.68', '0.71', '0.73', '0.78', '0.74', '0.74','0.78']

#np.random.rand(len(categories), len(features)) * 10  # Random values

# Create a horizontal bar chart with line segments
fig, ax = plt.subplots()
bar_height = 0.2  # Adjust this value based on your preference

# Custom color palette for each category
category_colors = {'TF-IDF': 'pink', 'LDA': 'skyblue', 'Word2vec': 'yellow', 'Glove': 'lightgreen', 'SGL': 'orange', 'CGL': 'orange', 'SWL': 'purple', 'CWL': 'lightblue' }

for i, category in enumerate(categories):
    feature_values = values[i]
    color = category_colors.get(category, 'gray')  # Default to gray if category color is not defined
    for j, feature_value in enumerate(feature_values):
        ax.barh(y=category, width=feature_value, left=0, height=bar_height, color=color)
        ax.plot([0, feature_value], [i + bar_height / 2, i + bar_height / 2], color='black')  # Line segments

# Add labels and title
ax.set_xlabel('Values')
ax.set_ylabel('Categories')
ax.set_title('Horizontal Bar Chart with Line Segments')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
features = ['Feature 1', 'Feature 2', 'Feature 3']
values = np.random.rand(len(categories), len(features)) * 0.6 + 0.4  # Adjusted range for better visibility

# Create a horizontal bar chart with line segments
fig, ax = plt.subplots()
bar_height = 0.2  # Adjust this value based on your preference

# Custom color palette for each category
category_colors = {
    'Category A': 'pink',
    'Category B': 'skyblue',
    'Category C': 'yellow',
    'Category D': 'lightgreen',
}

for i, category in enumerate(categories):
    feature_values = values[i]
    color = category_colors.get(category, 'gray')  # Default to gray if category color is not defined
    for j, feature_value in enumerate(feature_values):
        ax.barh(y=category, width=feature_value, left=0, height=bar_height, color=color)
        ax.plot([0, feature_value], [i + bar_height / 2, i + bar_height / 2], color='black')  # Line segments

# Set custom x-axis ticks
ax.set_xticks([0.2,0.4, 0.6, 0.8, 1.0])
ax.set_xticklabels(['','0.40', '0.60', '0.80', '1.00'])

# Add labels and title
ax.set_xlabel('Values')
ax.set_ylabel('Categories')
ax.set_title('Horizontal Bar Chart with Line Segments')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['WELDA', 'TF-IDF', 'LDA', 'Word2vec', 'Glove', 'SGL', 'CGL', 'SWL', 'CWL']
features = ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4', 'Feature 5', 'Feature 6', 'Feature 7', 'Feature 8', 'Feature 9']
values = [0.88, 0.37, 0.68, 0.71, 0.73, 0.78, 0.74, 0.74, 0.78]  # Convert to float

# Create a horizontal bar chart with line segments
fig, ax = plt.subplots()
bar_height = 0.2  # Adjust this value based on your preference

# Custom color palette for each category
category_colors = {'TF-IDF': 'pink', 'LDA': 'skyblue', 'Word2vec': 'yellow', 'Glove': 'lightgreen',
                   'SGL': 'orange', 'CGL': 'coral', 'SWL': 'purple', 'CWL': 'lightblue'}

for i, category in enumerate(categories):
    feature_value = values[i]
    color = category_colors.get(category, 'gray')  # Default to gray if category color is not defined
    ax.barh(y=category, width=feature_value, left=0, height=bar_height, color=color)
    ax.plot([0, feature_value], [i + bar_height / 2, i + bar_height / 2], color='black')  # Line segments

# Set custom x-axis ticks
ax.set_xticks([0.20, 0.40, 0.60, 0.80, 1.00])

# Add labels and title
ax.set_xlabel('Micro-F1 score')
ax.set_ylabel('')
ax.set_title('')

# Show the plot
plt.show()

import gensim
import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from gensim.models import LdaModel
from gensim.corpora import Dictionary

def preprocess_text(text):
    # You can modify this function based on your specific text preprocessing needs
    return gensim.utils.simple_preprocess(text, deacc=True, min_len=3)

def hybrid_topic_modeling(documents, word2vec_model, num_topics):
    """
    Performs hybrid topic modeling by combining word2vec and LDA.

    Args:
        documents: List of text documents.
        word2vec_model: Pre-trained word2vec model.
        num_topics: Number of desired topics.

    Returns:
        topic_assignments: List of topic assignments for each document.
        lda_model: Trained LDA model.
    """
    # Tokenize the documents
    tokenized_documents = [preprocess_text(doc) for doc in documents]

    # Create dictionary and corpus
    dictionary = Dictionary(tokenized_documents)
    corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    # Train Word2vec-enhanced document features
    w2v_features = []
    for doc in corpus:
        vec = np.zeros(word2vec_model.vector_size)
        for word, count in doc:
            if word in word2vec_model.wv:
                vec += count * word2vec_model.wv[word]
        w2v_features.append(vec / sum(count for _, count in doc))

    # Combine features with bag-of-words
    combined_features = [list(doc) + [f] for doc, f in zip(corpus, w2v_features)]

    # Train LDA model
    lda_model = LdaModel(combined_features, id2word=dictionary, num_topics=num_topics)

    # Get topic assignments
    topic_assignments = [lda_model[doc] for doc in combined_features]

    return topic_assignments, lda_model

# Example usage
df = pd.read_csv("BBC News Train.csv")
documents = df.Text.tolist()

word2vec_model = Word2Vec.load("/content/food-reviews-short.model")
num_topics = 5

topic_assignments, lda_model = hybrid_topic_modeling(documents, word2vec_model, num_topics)

# Further analysis (e.g., coherence score, topic interpretation)

def hybrid_topic_modeling(documents, word2vec_model, num_topics):
    """
    Performs hybrid topic modeling by combining word2vec and LDA.

    Args:
        documents: List of text documents.
        word2vec_model: Pre-trained word2vec model.
        num_topics: Number of desired topics.

    Returns:
        topic_assignments: List of topic assignments for each document.
        lda_model: Trained LDA model.
    """
    # Tokenize the documents
    tokenized_documents = [preprocess_text(doc) for doc in documents]

    # Create dictionary and corpus
    dictionary = Dictionary(tokenized_documents)
    corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    # Train Word2vec-enhanced document features
    w2v_features = []
    for doc in corpus:
        vec = np.zeros(word2vec_model.vector_size)
        for word, count in doc:
            if word in word2vec_model.wv:
                vec += count * word2vec_model.wv[word]
        w2v_features.append(vec / sum(count for _, count in doc))

    # Combine features with bag-of-words
    combined_features = [list(doc) + [f] for doc, f in zip(corpus, w2v_features)]

    # Train LDA model
    lda_model = LdaModel(combined_features, id2word=dictionary, num_topics=num_topics)

    # Get topic assignments
    topic_assignments = [lda_model[doc] for doc in combined_features]

    return topic_assignments, lda_model

import gensim
import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from gensim.models import LdaModel
from gensim.corpora import Dictionary

def preprocess_text(text):
    # You can modify this function based on your specific text preprocessing needs
    return gensim.utils.simple_preprocess(text, deacc=True, min_len=3)

def hybrid_topic_modeling(documents, word2vec_model, num_topics):
    """
    Performs hybrid topic modeling by combining word2vec and LDA.

    Args:
        documents: List of text documents.
        word2vec_model: Pre-trained word2vec model.
        num_topics: Number of desired topics.

    Returns:
        topic_assignments: List of topic assignments for each document.
        lda_model: Trained LDA model.
    """
    # Tokenize the documents
    tokenized_documents = [preprocess_text(doc) for doc in documents]

    # Create dictionary and corpus for LDA
    dictionary = Dictionary(tokenized_documents)
    corpus_lda = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    # Train Word2vec-enhanced document features
    w2v_features = []
    for doc in corpus_lda:
        vec = np.zeros(word2vec_model.vector_size)
        for word_id, count in doc:
            word = dictionary[word_id]
            if word in word2vec_model.wv:
                vec += count * word2vec_model.wv[word]
        w2v_features.append(vec / sum(count for _, count in doc))

    # Combine features with bag-of-words
    combined_features = [list(doc) + [f] for doc, f in zip(corpus_lda, w2v_features)]

    # Train LDA model using the bag-of-words representation
    lda_model = LdaModel(corpus_lda, id2word=dictionary, num_topics=num_topics)

    # Get topic assignments
    topic_assignments = [lda_model[doc] for doc in corpus_lda]

    # Compute coherence score for all topics
    coherence_model = CoherenceModel(model=lda_model, texts=tokenized_documents, dictionary=dictionary, coherence='c_v')
    coherence_scores = coherence_model.get_coherence_per_topic()

    # Print average coherence score
    average_coherence_score = sum(coherence_scores) / len(coherence_scores)
    print(f"Average Coherence Score: {average_coherence_score}")

    # Display topic assignments for each document
    for i, topics in enumerate(topic_assignments):
        print(f"Document {i + 1} - Topics: {topics}")

    # Display the learned topics by the LDA model
    print("\nLearned Topics:")
    for topic_id in range(lda_model.num_topics):
        print(f"Topic {topic_id + 1}: {lda_model.print_topic(topic_id)}")



    return topic_assignments, lda_model

# Example usage
df = pd.read_csv("BBC News Train.csv")
documents = df.Text.tolist()

word2vec_model = Word2Vec.load("/content/food-reviews-short.model")
num_topics = 5

topic_assignments, lda_model = hybrid_topic_modeling(documents, word2vec_model, num_topics)

import gensim
import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel

def preprocess_text(text):
    # You can modify this function based on your specific text preprocessing needs
    return gensim.utils.simple_preprocess(text, deacc=True, min_len=3)

def hybrid_topic_modeling(documents, word2vec_model, num_topics):
    """
    Performs hybrid topic modeling by combining word2vec and LDA.

    Args:
        documents: List of text documents.
        word2vec_model: Pre-trained word2vec model.
        num_topics: Number of desired topics.

    Returns:
        topic_assignments: List of topic assignments for each document.
        lda_model: Trained LDA model.
        coherence_score: Average coherence score for the LDA model.
    """
    # Tokenize the documents
    tokenized_documents = [preprocess_text(doc) for doc in documents]

    # Create dictionary and corpus for LDA
    dictionary = Dictionary(tokenized_documents)
    corpus_lda = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    # Train Word2vec-enhanced document features
    w2v_features = []
    for doc in corpus_lda:
        vec = np.zeros(word2vec_model.vector_size)
        for word_id, count in doc:
            word = dictionary[word_id]
            if word in word2vec_model.wv:
                vec += count * word2vec_model.wv[word]
        w2v_features.append(vec / sum(count for _, count in doc))

    # Combine features with bag-of-words
    combined_features = [list(doc) + [f] for doc, f in zip(corpus_lda, w2v_features)]

    # Train LDA model using the bag-of-words representation
    lda_model = LdaModel(corpus_lda, id2word=dictionary, num_topics=num_topics)

    # Get topic assignments
    topic_assignments = [lda_model[doc] for doc in corpus_lda]

    # Compute coherence score for all topics
    coherence_model = CoherenceModel(model=lda_model, texts=tokenized_documents, dictionary=dictionary, coherence='c_v')
    coherence_scores = coherence_model.get_coherence_per_topic()

    # Calculate average coherence score
    average_coherence_score = sum(coherence_scores) / len(coherence_scores)

    return topic_assignments, lda_model, average_coherence_score

# Example usage
df = pd.read_csv("BBC News Train.csv")
documents = df.Text.tolist()

word2vec_model = Word2Vec.load("/content/bbc-news.model")
num_topics = 300

topic_assignments, lda_model, coherence_score = hybrid_topic_modeling(documents, word2vec_model, num_topics)

# Display average coherence score
print(f"Average Coherence Score: {coherence_score}")

import gensim
import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from gensim.models import LdaMulticore
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel

def preprocess_text(text):
    return gensim.utils.simple_preprocess(text, deacc=True, min_len=3)

def hybrid_topic_modeling(documents, word2vec_model, num_topics):
    # Tokenize the documents
    tokenized_documents = [preprocess_text(doc) for doc in documents]

    # Create dictionary and corpus for LDA
    dictionary = Dictionary(tokenized_documents)
    corpus_lda = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    # Train Word2vec-enhanced document features
    w2v_features = []
    for doc in corpus_lda:
        vec = np.zeros(word2vec_model.vector_size)
        for word_id, count in doc:
            word = dictionary[word_id]
            if word in word2vec_model.wv:
                vec += count * word2vec_model.wv[word]
        w2v_features.append(vec / sum(count for _, count in doc))

    # Combine features with bag-of-words
    combined_features = [list(doc) + [f] for doc, f in zip(corpus_lda, w2v_features)]

    # Train LDA model using LdaMulticore for parallel processing
    lda_model = LdaMulticore(corpus_lda, id2word=dictionary, num_topics=num_topics, workers=3)

    # Get topic assignments
    topic_assignments = [lda_model[doc] for doc in corpus_lda]

    # Compute coherence score for all topics
    coherence_model = CoherenceModel(model=lda_model, texts=tokenized_documents, dictionary=dictionary, coherence='c_v')
    coherence_scores = coherence_model.get_coherence_per_topic()

    # Calculate average coherence score
    average_coherence_score = sum(coherence_scores) / len(coherence_scores)

    return topic_assignments, lda_model, average_coherence_score

# Example usage
df = pd.read_csv("BBC News Train.csv")
documents = df.Text.tolist()

word2vec_model = Word2Vec.load("/content/bbc-news.model")
num_topics = 300

topic_assignments, lda_model, coherence_score = hybrid_topic_modeling(documents, word2vec_model, num_topics)

# Display average coherence score
print(f"Average Coherence Score: {coherence_score}")

import gensim
import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from gensim.models import LdaMulticore
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel

def preprocess_text(text):
    return gensim.utils.simple_preprocess(text, deacc=True, min_len=3)

def hybrid_topic_modeling(documents, word2vec_model, num_topics):
    # Tokenize the documents
    tokenized_documents = [preprocess_text(doc) for doc in documents]

    # Create dictionary and corpus for LDA
    dictionary = Dictionary(tokenized_documents)
    corpus_lda = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    # Train Word2vec-enhanced document features
    w2v_features = []
    for doc in corpus_lda:
        vec = np.zeros(word2vec_model.vector_size)
        for word_id, count in doc:
            word = dictionary[word_id]
            if word in word2vec_model.wv:
                vec += count * word2vec_model.wv[word]
        w2v_features.append(vec / sum(count for _, count in doc))

    # Combine features with bag-of-words
    combined_features = [list(doc) + [f] for doc, f in zip(corpus_lda, w2v_features)]

    # Train LDA model using LdaMulticore for parallel processing
    lda_model = LdaMulticore(
        corpus_lda,
        id2word=dictionary,
        num_topics=num_topics,
        passes=10,  # Increase the number of passes
        iterations=50,  # Increase the number of iterations
        workers=3
    )

    # Get topic assignments
    topic_assignments = [lda_model[doc] for doc in corpus_lda]

    # Compute coherence score for all topics
    coherence_model = CoherenceModel(model=lda_model, texts=tokenized_documents, dictionary=dictionary, coherence='c_v')
    coherence_scores = coherence_model.get_coherence_per_topic()

    # Calculate average coherence score
    average_coherence_score = sum(coherence_scores) / len(coherence_scores)

    return topic_assignments, lda_model, average_coherence_score

# Example usage
df = pd.read_csv("BBC News Train.csv")
documents = df.Text.tolist()

word2vec_model = Word2Vec.load("/content/bbc-news.model")
num_topics = 300

topic_assignments, lda_model, coherence_score = hybrid_topic_modeling(documents, word2vec_model, num_topics)

# Display average coherence score
print(f"Average Coherence Score: {coherence_score}")