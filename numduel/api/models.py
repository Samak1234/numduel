from pydantic import BaseModel

class StartGameRequest(BaseModel):
    player_name: str
    difficulty: str

class GuessRequest(BaseModel):
    game_id: str
    guess: int