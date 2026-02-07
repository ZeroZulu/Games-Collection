"""
⚡ TIC-TAC-TOE NEURAL NET - MATRIX EDITION ⚡
Python CLI Version with Matrix Aesthetic

A cyberpunk-themed Tic-Tac-Toe AI featuring:
- Minimax algorithm with alpha-beta pruning
- Real-time performance analytics
- Matrix-style terminal interface
- Colored output with ASCII art
- Decision logging and visualization
- Statistical tracking

Author: Your Name
"""

import os
import sys
import time
import json
import random
from datetime import datetime
from typing import List, Dict, Tuple, Optional

# ANSI color codes for terminal
class Colors:
    NEON_GREEN = '\033[38;5;46m'
    NEON_CYAN = '\033[38;5;51m'
    NEON_PINK = '\033[38;5;201m'
    NEON_YELLOW = '\033[38;5;226m'
    DARK_GRAY = '\033[38;5;240m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Background colors
    BG_DARK = '\033[48;5;16m'
    
    # Effects
    BLINK = '\033[5m'
    REVERSE = '\033[7m'


class MatrixEffect:
    """Matrix rain and visual effects"""
    
    @staticmethod
    def clear_screen():
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_matrix_rain(lines=3):
        """Print Matrix-style rain effect"""
        chars = ['0', '1', 'ア', 'イ', 'ウ', 'エ', 'オ']
        width = 80
        
        for _ in range(lines):
            line = ''.join(random.choice(chars) for _ in range(width))
            print(f"{Colors.NEON_GREEN}{Colors.DIM}{line}{Colors.RESET}")
            time.sleep(0.05)
    
    @staticmethod
    def print_header():
        """Print Matrix-themed header"""
        MatrixEffect.clear_screen()
        MatrixEffect.print_matrix_rain(2)
        
        header = f"""
{Colors.NEON_GREEN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║        ⚡ TIC-TAC-TOE NEURAL NET - MATRIX EDITION ⚡              ║
║                                                                   ║
║           » MINIMAX ALGORITHM • ALPHA-BETA PRUNING «             ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
{Colors.RESET}
        """
        print(header)
    
    @staticmethod
    def print_terminal_prompt(text: str):
        """Print text with terminal prompt style"""
        print(f"{Colors.NEON_CYAN}> {Colors.RESET}{text}")
    
    @staticmethod
    def print_status(text: str, color=Colors.NEON_YELLOW):
        """Print status message"""
        print(f"{color}{Colors.BOLD}[STATUS] {text}{Colors.RESET}")
    
    @staticmethod
    def print_thinking():
        """Animate AI thinking"""
        sys.stdout.write(f"{Colors.NEON_YELLOW}[AI COMPUTING")
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.3)
        sys.stdout.write(f"]{Colors.RESET}\n")
    
    @staticmethod
    def print_explosion():
        """Print win explosion effect"""
        explosion = [
            "        *    ",
            "      * * *  ",
            "    * * * * *",
            "  * * * * * * *",
            "* * * ⚡ * * * *",
            "  * * * * * * *",
            "    * * * * *",
            "      * * *  ",
            "        *    "
        ]
        for line in explosion:
            print(f"{Colors.NEON_YELLOW}{Colors.BOLD}{line:^60}{Colors.RESET}")
            time.sleep(0.05)


class TicTacToeAI:
    """Tic-Tac-Toe game with AI using Minimax algorithm"""
    
    def __init__(self):
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_active = True
        self.use_pruning = True
        self.learning_mode = False
        
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
        
        # Win patterns
        self.win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        self.load_stats()
    
    def display_board(self):
        """Display the game board with Matrix styling"""
        print(f"\n{Colors.NEON_CYAN}{'─' * 60}{Colors.RESET}")
        print(f"{Colors.NEON_GREEN}{Colors.BOLD}[GAME INTERFACE]{Colors.RESET}\n")
        
        # Board display with colored pieces
        for i in range(0, 9, 3):
            row = []
            for j in range(3):
                idx = i + j
                cell = self.board[idx]
                if cell == 'X':
                    row.append(f"{Colors.NEON_CYAN}{Colors.BOLD} X {Colors.RESET}")
                elif cell == 'O':
                    row.append(f"{Colors.NEON_PINK}{Colors.BOLD} O {Colors.RESET}")
                else:
                    row.append(f"{Colors.DARK_GRAY} {idx} {Colors.RESET}")
            
            # Print row with borders
            print(f"     {Colors.NEON_GREEN}║{Colors.RESET}", end="")
            print(f"{Colors.RESET} │ {Colors.RESET}".join(row), end="")
            print(f" {Colors.NEON_GREEN}║{Colors.RESET}")
            
            if i < 6:
                print(f"     {Colors.NEON_GREEN}║───┼───┼───║{Colors.RESET}")
        
        print(f"{Colors.NEON_CYAN}{'─' * 60}{Colors.RESET}\n")
    
    def check_winner(self, board_state: List[str], player: str) -> bool:
        """Check if a player has won"""
        return any(
            all(board_state[i] == player for i in pattern)
            for pattern in self.win_patterns
        )
    
    def is_board_full(self, board_state: List[str]) -> bool:
        """Check if board is full"""
        return all(cell != '' for cell in board_state)
    
    def get_available_moves(self, board_state: List[str]) -> List[int]:
        """Get list of available moves"""
        return [i for i, cell in enumerate(board_state) if cell == '']
    
    def minimax(self, board_state: List[str], player: str, depth: int, 
                alpha: float, beta: float, states_evaluated: List[int]) -> Dict:
        """
        Minimax algorithm with alpha-beta pruning
        
        Args:
            board_state: Current board configuration
            player: Current player ('X' or 'O')
            depth: Current depth in game tree
            alpha: Alpha value for pruning
            beta: Beta value for pruning
            states_evaluated: List to track evaluated states
        
        Returns:
            Dictionary with 'score' and optionally 'index'
        """
        states_evaluated[0] += 1
        
        # Terminal state checks
        if self.check_winner(board_state, 'X'):
            return {'score': -10 + depth}
        if self.check_winner(board_state, 'O'):
            return {'score': 10 - depth}
        if self.is_board_full(board_state):
            return {'score': 0}
        
        available_moves = self.get_available_moves(board_state)
        
        if player == 'O':  # Maximizing player (AI)
            best = {'score': float('-inf')}
            
            for move in available_moves:
                new_board = board_state.copy()
                new_board[move] = player
                
                result = self.minimax(new_board, 'X', depth + 1, alpha, beta, states_evaluated)
                
                if result['score'] > best['score']:
                    best = {'score': result['score'], 'index': move}
                
                alpha = max(alpha, result['score'])
                
                if self.use_pruning and beta <= alpha:
                    break  # Beta cutoff
            
            return best
        
        else:  # Minimizing player (Human)
            best = {'score': float('inf')}
            
            for move in available_moves:
                new_board = board_state.copy()
                new_board[move] = player
                
                result = self.minimax(new_board, 'O', depth + 1, alpha, beta, states_evaluated)
                
                if result['score'] < best['score']:
                    best = {'score': result['score'], 'index': move}
                
                beta = min(beta, result['score'])
                
                if self.use_pruning and beta <= alpha:
                    break  # Alpha cutoff
            
            return best
    
    def ai_move(self) -> Tuple[int, Dict]:
        """Execute AI move and return statistics"""
        MatrixEffect.print_thinking()
        
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
        
        compute_time = (time.time() - start_time) * 1000  # Convert to ms
        
        # Update statistics
        self.stats['total_states'] += states_evaluated[0]
        self.stats['total_time'] += compute_time
        self.stats['decisions'] += 1
        
        move_stats = {
            'move': result['index'],
            'score': result['score'],
            'states': states_evaluated[0],
            'time': compute_time
        }
        
        # Log the decision
        self.log_decision(move_stats)
        
        return result['index'], move_stats
    
    def log_decision(self, stats: Dict):
        """Log AI decision to terminal"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = (
            f"{Colors.DARK_GRAY}[{timestamp}]{Colors.RESET} "
            f"{Colors.NEON_GREEN}MOVE[{stats['move']}]{Colors.RESET} "
            f"{Colors.NEON_YELLOW}SCORE[{stats['score']}]{Colors.RESET} "
            f"{Colors.NEON_CYAN}STATES[{stats['states']}]{Colors.RESET} "
            f"{Colors.NEON_PINK}TIME[{stats['time']:.1f}ms]{Colors.RESET}"
        )
        MatrixEffect.print_terminal_prompt(log_entry)
    
    def make_move(self, position: int, player: str) -> bool:
        """Make a move on the board"""
        if position < 0 or position > 8 or self.board[position] != '':
            return False
        
        self.board[position] = player
        return True
    
    def check_game_over(self) -> Optional[str]:
        """Check if game is over and return winner or 'draw'"""
        if self.check_winner(self.board, 'X'):
            return 'X'
        if self.check_winner(self.board, 'O'):
            return 'O'
        if self.is_board_full(self.board):
            return 'draw'
        return None
    
    def display_stats(self):
        """Display current statistics"""
        print(f"\n{Colors.NEON_PINK}{Colors.BOLD}[NEURAL ACTIVITY - STATISTICS]{Colors.RESET}\n")
        
        win_rate = (self.stats['ai_wins'] / self.stats['games'] * 100) if self.stats['games'] > 0 else 0
        avg_states = self.stats['total_states'] // self.stats['decisions'] if self.stats['decisions'] > 0 else 0
        avg_time = self.stats['total_time'] / self.stats['decisions'] if self.stats['decisions'] > 0 else 0
        
        stats_display = f"""
    {Colors.NEON_CYAN}╔══════════════════════════════════════════════╗
    ║  WIN RATE:        {Colors.NEON_PINK}{win_rate:>6.1f}%{Colors.NEON_CYAN}                   ║
    ║  GAMES PLAYED:    {Colors.NEON_GREEN}{self.stats['games']:>6}{Colors.NEON_CYAN}                     ║
    ║  AVG COMPUTE:     {Colors.NEON_YELLOW}{avg_time:>6.1f}ms{Colors.NEON_CYAN}                 ║
    ║  STATES/MOVE:     {Colors.NEON_PINK}{avg_states:>6}{Colors.NEON_CYAN}                     ║
    ╠══════════════════════════════════════════════╣
    ║  AI WINS:         {Colors.NEON_GREEN}{self.stats['ai_wins']:>6}{Colors.NEON_CYAN}                     ║
    ║  PLAYER WINS:     {Colors.NEON_PINK}{self.stats['player_wins']:>6}{Colors.NEON_CYAN}                     ║
    ║  DRAWS:           {Colors.NEON_YELLOW}{self.stats['draws']:>6}{Colors.NEON_CYAN}                     ║
    ║  TOTAL STATES:    {Colors.NEON_GREEN}{self.stats['total_states']:>6}{Colors.NEON_CYAN}                     ║
    ╚══════════════════════════════════════════════╝{Colors.RESET}
        """
        print(stats_display)
    
    def reset_game(self):
        """Reset the game board"""
        self.board = [''] * 9
        self.current_player = 'X'
        self.game_active = True
    
    def save_stats(self):
        """Save statistics to file"""
        try:
            with open('tictactoe_matrix_stats.json', 'w') as f:
                json.dump(self.stats, f, indent=2)
        except Exception as e:
            print(f"{Colors.NEON_PINK}[ERROR] Could not save stats: {e}{Colors.RESET}")
    
    def load_stats(self):
        """Load statistics from file"""
        try:
            if os.path.exists('tictactoe_matrix_stats.json'):
                with open('tictactoe_matrix_stats.json', 'r') as f:
                    self.stats = json.load(f)
                print(f"{Colors.NEON_GREEN}[LOADED] Previous statistics restored{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.NEON_PINK}[ERROR] Could not load stats: {e}{Colors.RESET}")
    
    def play_game(self):
        """Main game loop"""
        MatrixEffect.print_header()
        
        print(f"{Colors.NEON_GREEN}[SYSTEM ONLINE]{Colors.RESET}")
        print(f"{Colors.NEON_CYAN}> NEURAL NETWORK ACTIVE{Colors.RESET}\n")
        
        time.sleep(1)
        
        while True:
            self.reset_game()
            MatrixEffect.print_status("NEW GAME INITIALIZED", Colors.NEON_GREEN)
            
            while self.game_active:
                self.display_board()
                
                if self.current_player == 'X':
                    # Player's turn
                    MatrixEffect.print_status("YOUR MOVE", Colors.NEON_CYAN)
                    
                    try:
                        move = input(f"{Colors.NEON_GREEN}> Enter position (0-8) or 'q' to quit: {Colors.RESET}")
                        
                        if move.lower() == 'q':
                            self.save_stats()
                            print(f"\n{Colors.NEON_YELLOW}[SYSTEM] Shutting down...{Colors.RESET}\n")
                            return
                        
                        move = int(move)
                        
                        if self.make_move(move, 'X'):
                            result = self.check_game_over()
                            if result:
                                self.handle_game_end(result)
                                break
                            self.current_player = 'O'
                        else:
                            MatrixEffect.print_status("⚠ INVALID MOVE", Colors.NEON_PINK)
                    
                    except ValueError:
                        MatrixEffect.print_status("⚠ INVALID INPUT", Colors.NEON_PINK)
                    except KeyboardInterrupt:
                        self.save_stats()
                        print(f"\n\n{Colors.NEON_YELLOW}[SYSTEM] Emergency shutdown...{Colors.RESET}\n")
                        return
                
                else:
                    # AI's turn
                    MatrixEffect.print_status("AI PROCESSING...", Colors.NEON_YELLOW)
                    
                    move, stats = self.ai_move()
                    self.make_move(move, 'O')
                    
                    result = self.check_game_over()
                    if result:
                        self.handle_game_end(result)
                        break
                    
                    self.current_player = 'X'
            
            # Show stats after each game
            self.display_board()
            self.display_stats()
            
            # Ask to play again
            print(f"\n{Colors.NEON_CYAN}> Play again? (y/n): {Colors.RESET}", end="")
            choice = input().lower()
            
            if choice != 'y':
                self.save_stats()
                print(f"\n{Colors.NEON_GREEN}[SYSTEM] Statistics saved{Colors.RESET}")
                print(f"{Colors.NEON_YELLOW}[SYSTEM] Shutting down neural network...{Colors.RESET}\n")
                MatrixEffect.print_matrix_rain(2)
                break
            
            MatrixEffect.print_header()
    
    def handle_game_end(self, result: str):
        """Handle game end and update statistics"""
        self.game_active = False
        self.stats['games'] += 1
        
        if result == 'X':
            self.stats['player_wins'] += 1
            MatrixEffect.print_status("⚡ PLAYER VICTORY ⚡", Colors.NEON_CYAN)
            MatrixEffect.print_explosion()
        elif result == 'O':
            self.stats['ai_wins'] += 1
            MatrixEffect.print_status("⚠ AI DOMINANCE ⚠", Colors.NEON_PINK)
        else:
            self.stats['draws'] += 1
            MatrixEffect.print_status("≈ DRAW ≈", Colors.NEON_YELLOW)
        
        self.save_stats()


def main():
    """Main entry point"""
    try:
        game = TicTacToeAI()
        game.play_game()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.NEON_YELLOW}[SYSTEM] Emergency shutdown...{Colors.RESET}\n")
    except Exception as e:
        print(f"\n{Colors.NEON_PINK}[ERROR] {e}{Colors.RESET}\n")


if __name__ == "__main__":
    main()
