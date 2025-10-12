class HighScores:
    def __init__(self, scores) -> None:
        self.scores: [int] = scores
    
    def latest(self) -> int:
        return self.scores[-1]
        
    def personal_best(self) -> int:
        return max(self.scores)
        
    def personal_top_three(self) -> [int]:
        TOP_AMOUNT = 3
        
        if len(self.scores) < TOP_AMOUNT:
            self.scores.sort(reverse=True)
            return self.scores

        top = self.scores.copy()[0:TOP_AMOUNT]
        top.sort(reverse=True)
        for score in self.scores[TOP_AMOUNT:]:
            if score > top[-1]:
                top[-1] = score
                top.sort(reverse=True)
        return top
                    
    