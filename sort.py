import os
import re
from collections import defaultdict
from pprint import pprint

import matplotlib.pyplot as plt
import nltk
import numpy as np
import omdb
import pandas as pd
import seaborn as sns
import spacy
from gensim.models import KeyedVectors, Word2Vec
from googleapiclient.discovery import build
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from wordcloud import WordCloud
