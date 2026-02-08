# 🚀 Quick Start Guide - Enhanced Wordle AI

## ⚡ 60-Second Setup

### Step 1: Install Dependencies
```bash
pip install streamlit pandas numpy plotly
```

### Step 2: Run the App
```bash
streamlit run enhanced_wordle_app.py
```

### Step 3: Open Browser
Navigate to: `http://localhost:8501`

**That's it!** 🎉

---

## 🎮 How to Play

### Basic Controls
1. **Type letters** using your keyboard or click the on-screen keys
2. **Press Enter** or click "✓ Enter" button to submit guess
3. **Press Backspace** or click "⌫ Delete" to remove last letter

### Color Coding
- 🟩 **Green**: Letter is in the word AND in correct position
- 🟨 **Yellow**: Letter is in the word but WRONG position
- ⬛ **Gray**: Letter is NOT in the word

### Game Modes
- **Play Mode**: Play Wordle with optional AI hints
- **Analytics Mode**: View detailed statistics and visualizations
- **AI Comparison Mode**: Compare different AI strategies

---

## 🤖 Using the AI Hints

### In the Sidebar:
1. Choose AI Strategy:
   - **Entropy**: Best for maximizing information gain
   - **Position**: Best for leveraging letter patterns
   - **Hybrid**: Best overall performance

2. Check "Show AI Suggestions" box

3. Click "Get AI Hint" button

### Understanding AI Suggestions:
- **Entropy score**: Higher = more information gained
- **Remaining candidates**: How many words still possible
- **Score breakdown**: See how different metrics contribute

---

## 📊 Exploring Analytics

### Switch to Analytics Mode:
1. Click **"Analytics"** in sidebar
2. View:
   - Win rate and streaks
   - Guess distribution chart
   - Entropy timeline (current game)
   - Letter frequency heatmap
   - Detailed guess analysis table

### Key Metrics:
- **Entropy Timeline**: Shows information gain per guess
- **Candidates Remaining**: Visual of search space reduction
- **Information Gain**: Bits of uncertainty removed

---

## 🔬 Running AI Comparisons

### Strategy Comparison:
1. Switch to **"AI Comparison"** mode
2. Set number of simulations (10-100)
3. Click **"Run Comparison"**
4. Wait for results (may take 30-60 seconds for 100 games)

### Results Show:
- Average guesses per strategy
- Win rate percentages
- Distribution box plots
- Detailed statistics table

**Insight**: See which AI approach performs best!

---

## 💡 Pro Tips

### For Best Experience:
1. **Start with common words** like "SLATE" or "CRANE"
2. **Use AI hints** to learn optimal strategy
3. **Try different AI modes** to see different approaches
4. **Check analytics** after each game to learn patterns

### For Recruiters/Interviewers:
1. **Demo in this order**:
   - Play one game with AI hints ON
   - Switch to Analytics to show charts
   - Run AI Comparison to show sophistication

2. **Talking points**:
   - "Three different ML approaches"
   - "Information theory in practice"
   - "Real-time analytics dashboard"
   - "Performance comparison framework"

---

## 🎯 5-Minute Demo Script

**Perfect for showing to recruiters or in interviews:**

### Minute 1: Introduction
*"This is an advanced Wordle AI I built to demonstrate data science concepts. It features three different ML strategies and real-time analytics."*

### Minute 2: Gameplay
- Start new game
- Make one guess
- Show AI suggestion
- Explain entropy concept

### Minute 3: Analytics
- Switch to Analytics mode
- Show entropy timeline
- Explain information gain
- Show letter frequency heatmap

### Minute 4: AI Comparison
- Switch to AI Comparison
- Run quick simulation (10-20 games)
- Show performance differences
- Explain trade-offs

### Minute 5: Code & Architecture
- Briefly show code structure
- Mention 800+ lines
- Highlight three AI classes
- Discuss technical decisions

**Result**: Clear demonstration of technical skills and communication ability!

---

## 🐛 Troubleshooting

### Common Issues:

#### "Module not found" error
```bash
pip install streamlit pandas numpy plotly
```

#### Port already in use
```bash
streamlit run enhanced_wordle_app.py --server.port 8502
```

#### Slow performance on AI Comparison
- Reduce simulation count to 10-20 games
- Use faster computer 😊
- Or wait ~60 seconds for full analysis

---

## ⌨️ Keyboard Shortcuts

- **Letters (A-Z)**: Add letter to guess
- **Enter**: Submit guess
- **Backspace/Delete**: Remove last letter
- **Ctrl+R**: Refresh page (new game)

---

## 📱 Mobile Support

The app works on mobile, but **desktop is recommended** for:
- Better visualization rendering
- Easier keyboard input
- Full analytics dashboard
- Strategy comparison charts

---

## 🎓 Learning Path

### For Beginners:
1. Play several games manually
2. Turn on AI hints
3. Compare your guesses to AI suggestions
4. Learn why certain words are better

### For Data Scientists:
1. Study the three AI strategies
2. Run strategy comparisons
3. Analyze entropy calculations
4. Modify ensemble weights in code

### For Interviewers:
1. Watch candidate navigate the app
2. Ask about algorithm choices
3. Discuss optimization approaches
4. Explore analytics interpretations

---

## 🔗 Next Steps

### To Customize:
1. Edit `enhanced_wordle_app.py`
2. Modify AI weights in `HybridAI` class
3. Add new word lists
4. Create new AI strategies

### To Deploy:
1. Push to GitHub
2. Connect to Streamlit Cloud
3. Deploy (free!)
4. Share link on LinkedIn/portfolio

### To Learn More:
- Read the [ENHANCED_README.md](ENHANCED_README.md)
- Check [IMPROVEMENTS.md](IMPROVEMENTS.md)
- Study the AI classes in code
- Experiment with parameters

---

## 🎉 You're Ready!

Now you have:
✅ A working Wordle AI  
✅ Three ML strategies  
✅ Beautiful analytics  
✅ Portfolio-worthy project  

**Go impress some recruiters!** 🚀

---

## 📞 Need Help?

If you're stuck:
1. Check this guide again
2. Read error messages carefully
3. Verify all dependencies installed
4. Try restarting the app

**Remember**: This is a portfolio piece - take time to understand how it works! 💡
