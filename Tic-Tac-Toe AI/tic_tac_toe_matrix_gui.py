"""
⚡ TIC-TAC-TOE NEURAL NET - MATRIX EDITION ⚡
Python GUI Version with Tkinter

A cyberpunk-themed Tic-Tac-Toe AI featuring:
- Minimax algorithm with alpha-beta pruning
- Matrix-style GUI with neon colors
- Animated decision tree visualization
- Real-time performance analytics
- Terminal-style logging
- Statistical tracking

Author: Your Name
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import time
import random
from datetime import datetime
from typing import List, Dict, Optional, Tuple


class MatrixColors:
    """Matrix-themed color palette"""
    NEON_GREEN = "#00ff41"
    NEON_CYAN = "#00ffff"
    NEON_PINK = "#ff00ff"
    NEON_YELLOW = "#ffff00"
    DARK_BG = "#0a0e27"
    DARKER_BG = "#050810"
    GRID_COLOR = "#1a2332"
    TERMINAL_GREEN = "#33ff33"


class TicTacToeMatrixGUI:
    """Matrix-themed Tic-Tac-Toe GUI application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ TIC-TAC-TOE NEURAL NET ⚡")
        self.root.configure(bg=MatrixColors.DARK_BG)
        self.root.geometry("1400x900")
        
        # Game state
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_active = True
        self.use_pruning = tk.BooleanVar(value=True)
        self.learning_mode = tk.BooleanVar(value=False)
        self.show_viz = tk.BooleanVar(value=True)
        
        # Win patterns
        self.win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        # Statistics
        self.stats = {
            'games': 0,
            'ai_wins': 0,
            'player_wins': 0,
            'draws': 0,
            'total_states': 0,
            'total_time': 0,
            'decisions': 0
        }
        
        self.load_stats()
        self.setup_ui()
        self.update_stats_display()
        
        # Start Matrix rain animation
        self.animate_matrix_rain()
    
    def setup_ui(self):
        """Setup the complete user interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg=MatrixColors.DARK_BG)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_frame)
        
        # Stats bar
        self.create_stats_bar(main_frame)
        
        # Main game area (3 columns)
        game_container = tk.Frame(main_frame, bg=MatrixColors.DARK_BG)
        game_container.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Left: Game board
        self.create_game_section(game_container)
        
        # Middle: Visualization panel
        self.create_viz_panel(game_container)
        
        # Right: Settings panel
        self.create_settings_panel(game_container)
    
    def create_header(self, parent):
        """Create Matrix-styled header"""
        header_frame = tk.Frame(parent, bg=MatrixColors.DARK_BG)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        title = tk.Label(
            header_frame,
            text="⚡ TIC-TAC-TOE NEURAL NET ⚡",
            font=("Courier New", 28, "bold"),
            fg=MatrixColors.NEON_GREEN,
            bg=MatrixColors.DARK_BG
        )
        title.pack()
        
        subtitle = tk.Label(
            header_frame,
            text="» MINIMAX ALGORITHM • ALPHA-BETA PRUNING «",
            font=("Courier New", 12),
            fg=MatrixColors.NEON_CYAN,
            bg=MatrixColors.DARK_BG
        )
        subtitle.pack()
        
        # Animated cursor effect
        self.animate_title_cursor(title)
    
    def create_stats_bar(self, parent):
        """Create top statistics bar"""
        stats_frame = tk.Frame(parent, bg=MatrixColors.GRID_COLOR, relief=tk.RIDGE, bd=2)
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        # System online indicator
        system_label = tk.Label(
            stats_frame,
            text="> SYSTEM ONLINE _ NEURAL NETWORK ACTIVE",
            font=("Courier New", 10),
            fg=MatrixColors.NEON_GREEN,
            bg=MatrixColors.GRID_COLOR
        )
        system_label.pack(pady=5)
        
        # Stats row
        stats_row = tk.Frame(stats_frame, bg=MatrixColors.GRID_COLOR)
        stats_row.pack(pady=5)
        
        self.header_stats = {}
        stat_names = [
            ("GAMES:", "header_games"),
            ("WIN RATE:", "header_winrate"),
            ("AVG COMPUTE:", "header_compute"),
            ("STATES:", "header_states")
        ]
        
        for label, key in stat_names:
            frame = tk.Frame(stats_row, bg=MatrixColors.GRID_COLOR)
            frame.pack(side=tk.LEFT, padx=20)
            
            tk.Label(
                frame,
                text=label,
                font=("Courier New", 9),
                fg=MatrixColors.NEON_CYAN,
                bg=MatrixColors.GRID_COLOR
            ).pack(side=tk.LEFT)
            
            value_label = tk.Label(
                frame,
                text="0",
                font=("Courier New", 9, "bold"),
                fg=MatrixColors.NEON_YELLOW,
                bg=MatrixColors.GRID_COLOR
            )
            value_label.pack(side=tk.LEFT, padx=(5, 0))
            
            self.header_stats[key] = value_label
    
    def create_game_section(self, parent):
        """Create game board section"""
        game_frame = tk.Frame(parent, bg=MatrixColors.GRID_COLOR, relief=tk.RIDGE, bd=3)
        game_frame.pack(side=tk.LEFT, padx=(0, 10), fill=tk.BOTH, expand=True)
        
        # Section label
        label = tk.Label(
            game_frame,
            text="[GAME INTERFACE]",
            font=("Courier New", 10, "bold"),
            fg=MatrixColors.NEON_CYAN,
            bg=MatrixColors.GRID_COLOR
        )
        label.pack(pady=10)
        
        # Status display
        self.status_frame = tk.Frame(game_frame, bg=MatrixColors.GRID_COLOR, relief=tk.SUNKEN, bd=2)
        self.status_frame.pack(pady=10, padx=10, fill=tk.X)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="YOUR MOVE",
            font=("Courier New", 16, "bold"),
            fg=MatrixColors.NEON_CYAN,
            bg=MatrixColors.DARK_BG,
            pady=10
        )
        self.status_label.pack()
        
        player_info = tk.Label(
            self.status_frame,
            text="» PLAYER: X | AI: O «",
            font=("Courier New", 9),
            fg=MatrixColors.NEON_GREEN,
            bg=MatrixColors.DARK_BG
        )
        player_info.pack()
        
        # AI thinking indicator
        self.thinking_label = tk.Label(
            game_frame,
            text="[ AI COMPUTING OPTIMAL PATH... ]",
            font=("Courier New", 10),
            fg=MatrixColors.NEON_YELLOW,
            bg=MatrixColors.GRID_COLOR
        )
        
        # Game board
        board_frame = tk.Frame(game_frame, bg=MatrixColors.DARK_BG)
        board_frame.pack(pady=20, padx=20)
        
        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                board_frame,
                text="",
                font=("Courier New", 40, "bold"),
                width=3,
                height=1,
                bg=MatrixColors.GRID_COLOR,
                fg=MatrixColors.NEON_GREEN,
                activebackground=MatrixColors.NEON_CYAN,
                relief=tk.RAISED,
                bd=3,
                command=lambda idx=i: self.on_cell_click(idx)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)
        
        # Control buttons
        control_frame = tk.Frame(game_frame, bg=MatrixColors.GRID_COLOR)
        control_frame.pack(pady=10)
        
        reset_btn = tk.Button(
            control_frame,
            text="⟳ RESET",
            font=("Courier New", 10, "bold"),
            bg=MatrixColors.NEON_GREEN,
            fg=MatrixColors.DARK_BG,
            activebackground=MatrixColors.TERMINAL_GREEN,
            command=self.reset_game,
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=8
        )
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            control_frame,
            text="⌫ CLEAR STATS",
            font=("Courier New", 10, "bold"),
            bg=MatrixColors.NEON_CYAN,
            fg=MatrixColors.DARK_BG,
            activebackground=MatrixColors.NEON_CYAN,
            command=self.clear_stats,
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=8
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
    
    def create_viz_panel(self, parent):
        """Create visualization panel"""
        viz_frame = tk.Frame(parent, bg=MatrixColors.GRID_COLOR, relief=tk.RIDGE, bd=3)
        viz_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
        
        # Section label
        label = tk.Label(
            viz_frame,
            text="[NEURAL ACTIVITY]",
            font=("Courier New", 10, "bold"),
            fg=MatrixColors.NEON_PINK,
            bg=MatrixColors.GRID_COLOR
        )
        label.pack(pady=10)
        
        # Metrics grid
        metrics_frame = tk.Frame(viz_frame, bg=MatrixColors.GRID_COLOR)
        metrics_frame.pack(pady=10, padx=10, fill=tk.X)
        
        self.metric_labels = {}
        metrics = [
            ("Win Rate", "win_rate"),
            ("Games", "games"),
            ("Compute", "compute"),
            ("States", "states")
        ]
        
        for i, (name, key) in enumerate(metrics):
            box = tk.Frame(
                metrics_frame,
                bg=MatrixColors.DARK_BG,
                relief=tk.SUNKEN,
                bd=2
            )
            box.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="ew")
            
            tk.Label(
                box,
                text=name,
                font=("Courier New", 8),
                fg=MatrixColors.NEON_CYAN,
                bg=MatrixColors.DARK_BG
            ).pack()
            
            value_label = tk.Label(
                box,
                text="0",
                font=("Courier New", 14, "bold"),
                fg=MatrixColors.NEON_PINK,
                bg=MatrixColors.DARK_BG
            )
            value_label.pack()
            
            self.metric_labels[key] = value_label
        
        metrics_frame.columnconfigure(0, weight=1)
        metrics_frame.columnconfigure(1, weight=1)
        
        # Algorithm visualization (Canvas)
        tk.Label(
            viz_frame,
            text="» ALGORITHM VIZ",
            font=("Courier New", 9, "bold"),
            fg=MatrixColors.NEON_PINK,
            bg=MatrixColors.GRID_COLOR
        ).pack(pady=(15, 5))
        
        self.viz_canvas = tk.Canvas(
            viz_frame,
            width=460,
            height=180,
            bg=MatrixColors.DARK_BG,
            highlightthickness=2,
            highlightbackground=MatrixColors.GRID_COLOR
        )
        self.viz_canvas.pack(pady=5, padx=10)
        
        self.draw_initial_tree()
        
        # Terminal log
        tk.Label(
            viz_frame,
            text="> SYSTEM.LOG",
            font=("Courier New", 9, "bold"),
            fg=MatrixColors.NEON_GREEN,
            bg=MatrixColors.GRID_COLOR
        ).pack(pady=(15, 5))
        
        log_frame = tk.Frame(viz_frame, bg=MatrixColors.DARK_BG, relief=tk.SUNKEN, bd=2)
        log_frame.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.log_text = tk.Text(
            log_frame,
            height=8,
            font=("Courier New", 8),
            bg=MatrixColors.DARK_BG,
            fg=MatrixColors.TERMINAL_GREEN,
            insertbackground=MatrixColors.NEON_GREEN,
            yscrollcommand=scrollbar.set,
            relief=tk.FLAT
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_text.yview)
        
        self.log_text.insert(tk.END, ">> AWAITING AI MOVE...\n")
        self.log_text.config(state=tk.DISABLED)
    
    def create_settings_panel(self, parent):
        """Create settings and scoreboard panel"""
        settings_frame = tk.Frame(parent, bg=MatrixColors.GRID_COLOR, relief=tk.RIDGE, bd=3)
        settings_frame.pack(side=tk.LEFT, padx=(10, 0), fill=tk.BOTH)
        
        # Section label
        label = tk.Label(
            settings_frame,
            text="[CONFIG]",
            font=("Courier New", 10, "bold"),
            fg=MatrixColors.NEON_YELLOW,
            bg=MatrixColors.GRID_COLOR
        )
        label.pack(pady=10)
        
        # Config items
        configs = [
            ("PRUNING", self.use_pruning),
            ("LEARNING", self.learning_mode),
            ("VISUALIZATION", self.show_viz)
        ]
        
        for name, var in configs:
            item_frame = tk.Frame(
                settings_frame,
                bg=MatrixColors.DARK_BG,
                relief=tk.RAISED,
                bd=2
            )
            item_frame.pack(pady=5, padx=10, fill=tk.X)
            
            tk.Label(
                item_frame,
                text=name,
                font=("Courier New", 9),
                fg=MatrixColors.NEON_YELLOW,
                bg=MatrixColors.DARK_BG
            ).pack(side=tk.LEFT, padx=10, pady=10)
            
            check = tk.Checkbutton(
                item_frame,
                variable=var,
                bg=MatrixColors.DARK_BG,
                fg=MatrixColors.NEON_GREEN,
                selectcolor=MatrixColors.NEON_GREEN,
                activebackground=MatrixColors.DARK_BG
            )
            check.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Scoreboard
        tk.Label(
            settings_frame,
            text="» SCOREBOARD",
            font=("Courier New", 9, "bold"),
            fg=MatrixColors.NEON_GREEN,
            bg=MatrixColors.GRID_COLOR
        ).pack(pady=(20, 10))
        
        scoreboard_frame = tk.Frame(settings_frame, bg=MatrixColors.DARK_BG, relief=tk.SUNKEN, bd=2)
        scoreboard_frame.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        
        self.score_labels = {}
        scores = [
            ("AI WINS", "ai_wins", MatrixColors.NEON_GREEN),
            ("PLAYER WINS", "player_wins", MatrixColors.NEON_PINK),
            ("DRAWS", "draws", MatrixColors.NEON_YELLOW),
            ("TOTAL STATES", "total_states", MatrixColors.NEON_CYAN)
        ]
        
        for name, key, color in scores:
            row = tk.Frame(scoreboard_frame, bg=MatrixColors.DARK_BG)
            row.pack(fill=tk.X, pady=5, padx=10)
            
            tk.Label(
                row,
                text=name,
                font=("Courier New", 8),
                fg=MatrixColors.NEON_CYAN,
                bg=MatrixColors.DARK_BG
            ).pack(side=tk.LEFT)
            
            value_label = tk.Label(
                row,
                text="0",
                font=("Courier New", 10, "bold"),
                fg=color,
                bg=MatrixColors.DARK_BG
            )
            value_label.pack(side=tk.RIGHT)
            
            self.score_labels[key] = value_label
    
    def on_cell_click(self, index):
        """Handle cell click event"""
        if not self.game_active or self.board[index] != '' or self.current_player != 'X':
            return
        
        self.make_move(index, 'X')
        
        if self.game_active:
            self.thinking_label.pack(pady=5)
            self.root.update()
            self.root.after(500, self.ai_move)
    
    def make_move(self, index, player):
        """Make a move on the board"""
        self.board[index] = player
        
        # Update button
        btn = self.buttons[index]
        btn.config(
            text=player,
            fg=MatrixColors.NEON_CYAN if player == 'X' else MatrixColors.NEON_PINK,
            state=tk.DISABLED
        )
        
        # Check game over
        result = self.check_game_over()
        if result:
            self.handle_game_end(result)
        else:
            self.current_player = 'O' if player == 'X' else 'X'
            self.update_status()
    
    def ai_move(self):
        """Execute AI move"""
        self.status_label.config(text="AI PROCESSING...")
        self.root.update()
        
        start_time = time.time()
        states_evaluated = [0]
        
        result = self.minimax(
            self.board.copy(),
            'O',
            0,
            float('-inf'),
            float('inf'),
            states_evaluated
        )
        
        compute_time = (time.time() - start_time) * 1000
        
        # Update stats
        self.stats['total_states'] += states_evaluated[0]
        self.stats['total_time'] += compute_time
        self.stats['decisions'] += 1
        
        # Log decision
        self.log_decision(result['index'], result['score'], states_evaluated[0], compute_time)
        
        # Visualize
        if self.show_viz.get():
            self.visualize_tree(result['index'], states_evaluated[0])
        
        # Make move
        self.make_move(result['index'], 'O')
        
        self.thinking_label.pack_forget()
        self.update_stats_display()
    
    def minimax(self, board_state, player, depth, alpha, beta, states_evaluated):
        """Minimax algorithm with alpha-beta pruning"""
        states_evaluated[0] += 1
        
        if self.check_winner_state(board_state, 'X'):
            return {'score': -10 + depth}
        if self.check_winner_state(board_state, 'O'):
            return {'score': 10 - depth}
        if all(cell != '' for cell in board_state):
            return {'score': 0}
        
        available = [i for i, cell in enumerate(board_state) if cell == '']
        
        if player == 'O':
            best = {'score': float('-inf')}
            for move in available:
                new_board = board_state.copy()
                new_board[move] = player
                result = self.minimax(new_board, 'X', depth + 1, alpha, beta, states_evaluated)
                if result['score'] > best['score']:
                    best = {'score': result['score'], 'index': move}
                alpha = max(alpha, result['score'])
                if self.use_pruning.get() and beta <= alpha:
                    break
            return best
        else:
            best = {'score': float('inf')}
            for move in available:
                new_board = board_state.copy()
                new_board[move] = player
                result = self.minimax(new_board, 'O', depth + 1, alpha, beta, states_evaluated)
                if result['score'] < best['score']:
                    best = {'score': result['score'], 'index': move}
                beta = min(beta, result['score'])
                if self.use_pruning.get() and beta <= alpha:
                    break
            return best
    
    def check_winner_state(self, board_state, player):
        """Check if player won in given board state"""
        return any(
            all(board_state[i] == player for i in pattern)
            for pattern in self.win_patterns
        )
    
    def check_game_over(self):
        """Check if game is over"""
        if self.check_winner_state(self.board, 'X'):
            return 'X'
        if self.check_winner_state(self.board, 'O'):
            return 'O'
        if all(cell != '' for cell in self.board):
            return 'draw'
        return None
    
    def handle_game_end(self, result):
        """Handle game end"""
        self.game_active = False
        self.stats['games'] += 1
        
        if result == 'X':
            self.stats['player_wins'] += 1
            self.status_label.config(text="⚡ PLAYER VICTORY ⚡", fg=MatrixColors.NEON_CYAN)
            self.animate_win()
        elif result == 'O':
            self.stats['ai_wins'] += 1
            self.status_label.config(text="⚠ AI DOMINANCE ⚠", fg=MatrixColors.NEON_PINK)
        else:
            self.stats['draws'] += 1
            self.status_label.config(text="≈ DRAW ≈", fg=MatrixColors.NEON_YELLOW)
        
        # Highlight winning cells
        if result != 'draw':
            for pattern in self.win_patterns:
                if all(self.board[i] == result for i in pattern):
                    for i in pattern:
                        self.buttons[i].config(bg=MatrixColors.NEON_YELLOW)
        
        self.save_stats()
        self.update_stats_display()
        
        # Disable all buttons
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
    
    def reset_game(self):
        """Reset the game"""
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_active = True
        
        for btn in self.buttons:
            btn.config(
                text="",
                state=tk.NORMAL,
                bg=MatrixColors.GRID_COLOR,
                fg=MatrixColors.NEON_GREEN
            )
        
        self.status_label.config(text="YOUR MOVE", fg=MatrixColors.NEON_CYAN)
        self.draw_initial_tree()
    
    def update_status(self):
        """Update status display"""
        if self.current_player == 'X':
            self.status_label.config(text="YOUR MOVE", fg=MatrixColors.NEON_CYAN)
        else:
            self.status_label.config(text="AI PROCESSING...", fg=MatrixColors.NEON_YELLOW)
    
    def log_decision(self, move, score, states, time_ms):
        """Log AI decision"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] MOVE[{move}] SCORE[{score}] STATES[{states}] TIME[{time_ms:.1f}ms]\n"
        
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
    
    def visualize_tree(self, selected_move, states):
        """Visualize decision tree on canvas"""
        canvas = self.viz_canvas
        canvas.delete("all")
        
        # Draw grid background
        for i in range(0, 460, 20):
            canvas.create_line(i, 0, i, 180, fill=MatrixColors.GRID_COLOR)
        
        # Root node
        canvas.create_oval(215, 20, 245, 50, fill=MatrixColors.NEON_CYAN, outline=MatrixColors.NEON_CYAN, width=2)
        canvas.create_text(230, 35, text="AI", fill=MatrixColors.DARK_BG, font=("Courier New", 10, "bold"))
        
        # Branches
        branches = min(len([c for c in self.board if c == '']), 9)
        spacing = 400 / max(branches, 1)
        
        for i in range(branches):
            x = 30 + i * spacing + 15
            
            # Line
            canvas.create_line(230, 50, x, 130, fill=MatrixColors.NEON_GREEN, width=2)
            
            # Node
            if i == 0:
                canvas.create_oval(x-10, 130, x+10, 150, fill=MatrixColors.NEON_YELLOW, outline=MatrixColors.NEON_YELLOW, width=2)
                canvas.create_text(x, 140, text=str(i), fill=MatrixColors.DARK_BG, font=("Courier New", 9, "bold"))
            else:
                canvas.create_oval(x-8, 132, x+8, 148, fill=MatrixColors.GRID_COLOR, outline=MatrixColors.NEON_GREEN, width=1)
                canvas.create_text(x, 140, text=str(i), fill=MatrixColors.NEON_GREEN, font=("Courier New", 8))
        
        # Stats
        canvas.create_text(10, 170, text=f"EVALUATED: {states} STATES", anchor="w", 
                          fill=MatrixColors.NEON_CYAN, font=("Courier New", 8))
    
    def draw_initial_tree(self):
        """Draw initial tree visualization"""
        canvas = self.viz_canvas
        canvas.delete("all")
        canvas.create_text(230, 90, text=">> AWAITING AI COMPUTATION <<", 
                          fill=MatrixColors.TERMINAL_GREEN, font=("Courier New", 10))
    
    def update_stats_display(self):
        """Update all statistics displays"""
        win_rate = (self.stats['ai_wins'] / self.stats['games'] * 100) if self.stats['games'] > 0 else 0
        avg_states = self.stats['total_states'] // self.stats['decisions'] if self.stats['decisions'] > 0 else 0
        avg_time = self.stats['total_time'] / self.stats['decisions'] if self.stats['decisions'] > 0 else 0
        
        # Header stats
        self.header_stats['header_games'].config(text=str(self.stats['games']))
        self.header_stats['header_winrate'].config(text=f"{win_rate:.0f}%")
        self.header_stats['header_compute'].config(text=f"{avg_time:.1f}ms")
        self.header_stats['header_states'].config(text=str(avg_states))
        
        # Metrics
        self.metric_labels['win_rate'].config(text=f"{win_rate:.0f}%")
        self.metric_labels['games'].config(text=str(self.stats['games']))
        self.metric_labels['compute'].config(text=f"{avg_time:.1f}ms")
        self.metric_labels['states'].config(text=str(avg_states))
        
        # Scoreboard
        self.score_labels['ai_wins'].config(text=str(self.stats['ai_wins']))
        self.score_labels['player_wins'].config(text=str(self.stats['player_wins']))
        self.score_labels['draws'].config(text=str(self.stats['draws']))
        self.score_labels['total_states'].config(text=str(self.stats['total_states']))
    
    def clear_stats(self):
        """Clear all statistics"""
        if messagebox.askyesno("Clear Statistics", "⚠ RESET ALL STATISTICS? ⚠"):
            self.stats = {
                'games': 0,
                'ai_wins': 0,
                'player_wins': 0,
                'draws': 0,
                'total_states': 0,
                'total_time': 0,
                'decisions': 0
            }
            self.save_stats()
            self.update_stats_display()
            
            self.log_text.config(state=tk.NORMAL)
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, ">> STATISTICS CLEARED\n")
            self.log_text.config(state=tk.DISABLED)
    
    def save_stats(self):
        """Save statistics to file"""
        try:
            with open('tictactoe_matrix_gui_stats.json', 'w') as f:
                json.dump(self.stats, f, indent=2)
        except Exception:
            pass
    
    def load_stats(self):
        """Load statistics from file"""
        try:
            with open('tictactoe_matrix_gui_stats.json', 'r') as f:
                self.stats = json.load(f)
        except Exception:
            pass
    
    def animate_title_cursor(self, label):
        """Animate cursor blink on title"""
        current_text = label.cget("text")
        if current_text.endswith("_"):
            label.config(text=current_text[:-1])
        else:
            label.config(text=current_text + "_")
        self.root.after(500, lambda: self.animate_title_cursor(label))
    
    def animate_matrix_rain(self):
        """Animate Matrix rain effect"""
        # This would add falling code effect in the background
        # For simplicity, we'll just add a subtle pulse effect to the title
        self.root.after(2000, self.animate_matrix_rain)
    
    def animate_win(self):
        """Animate win effect"""
        for _ in range(3):
            self.status_label.config(fg=MatrixColors.NEON_YELLOW)
            self.root.update()
            time.sleep(0.1)
            self.status_label.config(fg=MatrixColors.NEON_CYAN)
            self.root.update()
            time.sleep(0.1)


def main():
    """Main entry point"""
    root = tk.Tk()
    app = TicTacToeMatrixGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
