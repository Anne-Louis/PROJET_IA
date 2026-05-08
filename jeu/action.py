class Action:
    def __init__(self, type_action: str, index_carte: int | None = None):
        self.type_action = type_action
        self.index_carte = index_carte

    def est_pass(self):
        return self.type_action == "passer"

    def est_jouer(self):
        return self.type_action == "jouer"

    def __repr__(self):
        if self.est_pass():
            return "Action(PASSER)"
        return f"Action(JOUER, index={self.index_carte})"