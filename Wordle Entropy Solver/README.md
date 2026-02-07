# 🧠 Advanced Wordle AI - Technical Portfolio Project

> **A sophisticated implementation of Wordle featuring multiple AI strategies, real-time analytics, and information theory principles**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![ML](https://img.shields.io/badge/ML-Information%20Theory-green.svg)]()

---

## 🎯 Project Overview

This project demonstrates advanced data science and machine learning concepts through an interactive Wordle game featuring:

- **Information Theory**: Entropy-based decision making
- **Machine Learning**: Multiple AI strategies with performance comparison
- **Data Analytics**: Real-time metrics and visualization
- **Algorithm Design**: Efficient candidate filtering and optimization
- **Statistical Analysis**: Performance metrics and distribution analysis

**Perfect for showcasing to Data Science/Analytics recruiters:**
- Demonstrates understanding of information theory and entropy
- Shows ability to implement multiple ML approaches
- Includes comprehensive analytics and visualization
- Clean, production-ready code with proper architecture
- Interactive demo that non-technical stakeholders can appreciate

---

## 🚀 Key Features

### 1. **Multiple AI Strategies**

#### **Entropy-Based AI (Information Theory)**
- Calculates expected information gain for each possible guess
- Uses Shannon entropy: `H(X) = -Σ p(x) log₂ p(x)`
- Maximizes information reduction per guess
- **Key Insight**: Treats each guess as an experiment to gain maximum information

#### **Position-Frequency AI (Statistical Learning)**
- Analyzes letter frequency at each position
- Builds probability distribution from remaining candidates
- Scores words based on positional likelihood
- **Key Insight**: Leverages positional patterns in English words

#### **Hybrid AI (Ensemble Method)**
- Combines entropy, position, and frequency scores
- Weighted ensemble approach with configurable weights
- Adapts strategy based on game state
- **Key Insight**: Different metrics excel at different game stages

### 2. **Real-Time Analytics Dashboard**

- **Performance Metrics**: Win rate, average guesses, streaks
- **Entropy Timeline**: Visualizes information gain over game
- **Letter Frequency Heatmap**: Shows positional patterns
- **Guess Distribution**: Statistical breakdown of outcomes
- **Strategy Comparison**: A/B testing framework for AI approaches

### 3. **Beautiful, Modern UI**

- Smooth animations and transitions
- Responsive design
- Color-coded feedback (green/yellow/gray)
- Interactive keyboard
- Dark mode optimized

---

## 📊 Technical Architecture

### Core Algorithms

```python
# Entropy Calculation
def calculate_entropy(guess: str, candidates: List[str]) -> float:
    """
    Shannon entropy for expected information gain
    Time Complexity: O(n) where n = number of candidates
    """
    pattern_counts = Counter(
        get_feedback_pattern(guess, secret) 
        for secret in candidates
    )
    
    entropy = -Σ (p * log₂(p)) for each pattern
    return entropy
```

### Algorithm Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Best Use Case |
|-----------|----------------|------------------|---------------|
| Entropy AI | O(n × m) | O(n) | Early game, maximize info |
| Position AI | O(n + m) | O(26 × 5) | Mid game, leverage patterns |
| Hybrid AI | O(n × m) | O(n + m) | Full game, balanced approach |

*where n = candidates, m = allowed words*

---

## 🔬 Data Science Concepts Demonstrated

### 1. **Information Theory**
- Entropy as measure of uncertainty
- Information gain optimization
- Bayesian updating of beliefs
- Expected value calculations

### 2. **Statistical Analysis**
- Probability distributions
- Frequency analysis
- Conditional probabilities
- Performance metrics

### 3. **Machine Learning**
- Ensemble methods (hybrid approach)
- Feature engineering (position scores, frequency scores)
- Hyperparameter tuning (ensemble weights)
- Model comparison and evaluation

### 4. **Algorithm Optimization**
- Pruning search space
- Memoization techniques
- Early stopping conditions
- Computational complexity management

### 5. **Data Visualization**
- Interactive dashboards (Plotly)
- Time series analysis (entropy timeline)
- Heatmaps (letter frequency)
- Distribution plots (guess distribution)

---

## 🛠️ Installation & Setup

### Prerequisites
```bash
Python 3.8+
pip or conda
```

### Quick Start

1. **Clone/Download** the project

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
streamlit run enhanced_wordle_app.py
```

4. **Open browser** at `http://localhost:8501`

---

## 📦 Project Structure

```
wordle-ai/
├── enhanced_wordle_app.py      # Main application (800+ lines)
├── requirements.txt             # Dependencies
└── README.md                    # This file
```

---

## 🎓 Educational Value

### For Learners:
- Understand information theory in practice
- See multiple ML approaches compared
- Learn Streamlit for data apps
- Study clean code architecture

### For Recruiters:
- Demonstrates mathematical sophistication
- Shows ability to translate theory to code
- Proves visualization skills
- Exhibits software engineering practices

---

## 📊 Analytics Features

### Game-Level Analytics
- **Win/Loss tracking**: Overall performance metrics
- **Streak tracking**: Current and maximum winning streaks
- **Guess distribution**: Histogram of solve attempts
- **Average performance**: Mean guesses to solve

### Real-Time Analysis
- **Entropy timeline**: Information gain per guess
- **Candidate reduction**: Visual candidate space shrinking
- **Letter frequency**: Positional probability heatmap
- **Strategy scoring**: Real-time AI decision breakdown

---

## 💡 Key Takeaways for Recruiters

### What This Project Demonstrates:

✅ **Mathematical Sophistication**: Information theory, probability, statistics

✅ **Algorithm Design**: Multiple approaches to the same problem

✅ **Data Visualization**: Interactive dashboards and charts

✅ **Software Architecture**: Clean, modular, maintainable code

✅ **Product Thinking**: User experience and interface design

✅ **Analytical Mindset**: Performance comparison and metrics

✅ **Communication**: Complex concepts explained clearly

---

## 🎮 Quick Start Guide

### For Recruiters: 5-Minute Demo

1. **Start the app** → Click "New Game"
2. **Try a guess** → Type a word and hit Enter
3. **View AI Hint** → See the AI's suggested optimal guess
4. **Check Analytics** → Switch to Analytics tab
5. **Compare Strategies** → Go to AI Comparison tab

**What to notice:**
- Real-time entropy calculations
- Multiple AI approaches
- Clean, professional interface
- Comprehensive metrics tracking

---

**Built with ❤️ and a passion for Data Science**
