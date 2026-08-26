from dataclasses import dataclass, field

from app.game_logic import (
    check_bingo,
    check_scavenger_hunt_complete,
    generate_board,
    generate_hunt_list,
    get_winning_square_ids,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameMode, GameState


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    game_state: GameState = GameState.START
    game_mode: GameMode = GameMode.BINGO
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False
    show_scavenger_hunt_modal: bool = False

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def has_bingo(self) -> bool:
        return self.game_state == GameState.BINGO

    @property
    def is_scavenger_hunt(self) -> bool:
        return self.game_mode == GameMode.SCAVENGER_HUNT

    @property
    def marked_count(self) -> int:
        return sum(item.is_marked for item in self.board if not item.is_free_space)

    def _hide_modals(self) -> None:
        self.show_bingo_modal = False
        self.show_scavenger_hunt_modal = False

    def start_game(self, game_mode: GameMode = GameMode.BINGO) -> None:
        self.game_mode = game_mode
        self.board = (
            generate_hunt_list() if self.is_scavenger_hunt else generate_board()
        )
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self._hide_modals()

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return
        self.board = toggle_square(self.board, square_id)

        if self.winning_line is None:
            bingo = check_bingo(self.board)
            if bingo is not None:
                self.winning_line = bingo
                self.game_state = GameState.BINGO
                self.show_bingo_modal = True
        if self.is_scavenger_hunt and check_scavenger_hunt_complete(self.board):
            self.show_scavenger_hunt_modal = True

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.game_mode = GameMode.BINGO
        self.board = []
        self.winning_line = None
        self._hide_modals()

    def dismiss_modal(self) -> None:
        self._hide_modals()
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
