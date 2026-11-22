#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:01:39 2026

@author: gustavo
"""

import nbformat as nbf

# Create a new Jupyter Notebook
nb = nbf.v4.new_notebook()

cells = []

# ------------------------------------------------
# CELL 1: INTRODUCTION
# ------------------------------------------------

cells.append(nbf.v4.new_markdown_cell("""
# Celebrating Mahendra Mahey
## A Word Cloud Visualisation

This notebook explores descriptive adjectives associated
with Mahendra Mahey through an engaging word cloud.

### Objectives
- Explore descriptive language.
- Highlight creativity and innovation.
- Visualise professional qualities.
- Generate a high-resolution poster.

The word sizes represent their assigned importance,
not measured personality ratings.
"""))

# ------------------------------------------------
# CELL 2: INSTALLATION
# ------------------------------------------------

cells.append(nbf.v4.new_markdown_cell("""
## 1. Importing libraries

We use three main libraries:

- WordCloud: generates the word cloud.
- Matplotlib: displays the visualisation.
- Counter: calculates word frequencies.
"""))

cells.append(nbf.v4.new_code_cell("""
%pip install wordcloud matplotlib pillow
"""))

cells.append(nbf.v4.new_code_cell("""
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

print("Libraries imported successfully!")
"""))

# ------------------------------------------------
# CELL 3: DATASET
# ------------------------------------------------

cells.append(nbf.v4.new_markdown_cell("""
## 2. Creating the adjective dataset

The following adjectives describe five broad themes:

1. Personality and character
2. Professional qualities
3. Creativity and innovation
4. Leadership and collaboration
5. Intellectual and cultural qualities

These are interpretative descriptions rather than
independently verified personality assessments.
"""))

words = [
    "Inspiring", "Kind", "Approachable", "Generous",
    "Enthusiastic", "Passionate", "Humble", "Warm",
    "Friendly", "Empathetic", "Thoughtful", "Genuine",
    "Respectful", "Encouraging", "Supportive",
    "Open-minded", "Curious", "Optimistic", "Patient",
    "Compassionate", "Innovative", "Visionary",
    "Strategic", "Collaborative", "Resourceful",
    "Knowledgeable", "Experienced", "Adaptable",
    "Proactive", "Dedicated", "Committed", "Organised",
    "Analytical", "Reflective", "Professional",
    "Reliable", "Responsible", "Independent",
    "Resilient", "Multidisciplinary", "Creative",
    "Imaginative", "Experimental", "Inventive",
    "Entrepreneurial", "Exploratory", "Original",
    "Forward-thinking", "Transformative", "Ambitious",
    "Adventurous", "Progressive", "Dynamic",
    "Pioneering", "Community-minded", "Empowering",
    "Inclusive", "Democratic", "Participatory",
    "Trustworthy", "Facilitative", "Cooperative",
    "Interdisciplinary", "People-oriented", "Diplomatic",
    "Motivational", "Enabling", "Unifying", "Accessible",
    "Engaging", "Appreciative", "Inquisitive",
    "Informed", "Scholarly", "Culturally aware",
    "Digitally minded", "Interconnected",
    "Thought-provoking", "Insightful", "Open",
    "Knowledge-sharing", "Intercultural",
    "Human-centred", "Intergenerational", "Impactful"
]

cells.append(nbf.v4.new_code_cell("""
words = """ + repr(words) + """

print("Number of adjectives:", len(words))
"""))

# ------------------------------------------------
# CELL 4: WORD FREQUENCIES
# ------------------------------------------------

cells.append(nbf.v4.new_markdown_cell("""
## 3. Assigning importance to selected adjectives

Word clouds use frequency values to determine
the relative size of words.

We increase the weights of selected adjectives
to make them visually prominent.
"""))

cells.append(nbf.v4.new_code_cell("""
frequencies = Counter(words)

important_words = {
    "Collaborative": 40,
    "Innovative": 38,
    "Inspiring": 36,
    "Visionary": 34,
    "Creative": 32,
    "Generous": 30,
    "Inclusive": 28,
    "Empowering": 27,
    "Experimental": 26,
    "Community-minded": 25,
    "Passionate": 24,
    "Transformative": 23
}

frequencies.update(important_words)

print("Word frequencies created successfully!")
"""))

# ------------------------------------------------
# CELL 5: COLOUR AND DESIGN
# ------------------------------------------------

cells.append(nbf.v4.new_markdown_cell("""
## 4. Defining the visual identity

Our colour palette uses:

- Navy blue: professionalism and trust.
- Teal: collaboration and openness.
- Coral: creativity and energy.
- Gold: inspiration and achievement.

The background is warm off-white.
"""))

cells.append(nbf.v4.new_code_cell("""
wc = WordCloud(
    width=2400,
    height=1600,
    background_color="#F7F7F2",
    colormap="viridis",
    max_words=100,
    prefer_horizontal=0.9,
    relative_scaling=0.6,
    margin=12,
    collocations=False,
    random_state=42
).generate_from_frequencies(frequencies)

print("Word cloud generated successfully!")
"""))

# ------------------------------------------------
# CELL 6: VISUALISATION
# ------------------------------------------------

cells.append(nbf.v4.new_markdown_cell("""
## 5. Displaying the word cloud

We use Matplotlib to display the final visualisation.

The largest words represent the adjectives
that have been assigned the highest weights.
"""))

cells.append(nbf.v4.new_code_cell("""
plt.figure(figsize=(18, 12))

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")

plt.title(
    "MAHENDRA MAHEY",
    fontsize=36,
    fontweight="bold",
    color="#12355B",
    pad=30
)

plt.text(
    0.5, 0.02,
    "A celebration of creativity, collaboration and innovation",
    transform=plt.gca().transAxes,
    ha="center",
    fontsize=17,
    color="#087E8B"
)

plt.tight_layout()
plt.show()
"""))

# ------------------------------------------------
# CELL 7: EXPORT
# ------------------------------------------------

cells.append(nbf.v4.new_markdown_cell("""
## 6. Exporting the visualisation

We save the word cloud as a high-resolution PNG image.

This image can be used in:
- Presentations
- Posters
- Reports
- Workshops
- Digital exhibitions
"""))

cells.append(nbf.v4.new_code_cell("""
wc.to_file("mahendra_mahey_wordcloud.png")

print("Image saved as mahendra_mahey_wordcloud.png")
"""))

# ------------------------------------------------
# CELL 8: CONCLUSION
# ------------------------------------------------

cells.append(nbf.v4.new_markdown_cell("""
# Conclusion

This notebook demonstrates how Python can transform
descriptive language into an engaging visual artefact.

The visualisation celebrates themes of:

- Creativity
- Collaboration
- Innovation
- Knowledge sharing
- Community building

The result is a visual tribute to Mahendra Mahey's
professional contributions and collaborative spirit.
"""))

# ------------------------------------------------
# CREATE NOTEBOOK FILE
# ------------------------------------------------

nb.cells = cells

nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3"
    }
}

filename = "Mahendra_Mahey_Wordcloud.ipynb"

nbf.write(nb, filename)

print("\nNotebook created successfully!")
print("Filename:", filename)
print("Total cells:", len(nb.cells))