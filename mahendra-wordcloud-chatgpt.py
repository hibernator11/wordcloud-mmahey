#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:58:01 2026

@author: gustavo
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# Words describing Mahendra Mahey
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

# Give more prominence to selected words
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
    "Transformative": 23,
}

# Create word frequencies
frequencies = Counter(words)

for word, weight in important_words.items():
    frequencies[word] = weight

# Colour palette
colours = [
    "#12355B",  # Navy
    "#087E8B",  # Teal
    "#FF5A5F",  # Coral
    "#3CBBB1",  # Turquoise
    "#F2B134",  # Gold
]

def custom_colour(word, font_size, position,
                  orientation, random_state=None):
    import random
    random.seed(hash(word) % 10000)
    return random.choice(colours)

# Generate word cloud
wc = WordCloud(
    width=2400,
    height=1600,
    background_color="#F7F7F2",
    colormap="viridis",
    max_words=100,
    prefer_horizontal=0.9,
    relative_scaling=0.6,
    margin=12,
    collocations=False
).generate_from_frequencies(frequencies)

# Create visualisation
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

# Save high-resolution image
plt.savefig(
    "mahendra_mahey_wordcloud.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="#F7F7F2"
)

plt.show()
