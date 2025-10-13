class Allergies:
    ALLERGENS = ['eggs', 'peanuts', 'shellfish', 'strawberries', 
                 'tomatoes', 'chocolate', 'pollen', 'cats']
    
    def __init__(self, score):
        self.score = score
    
    def allergic_to(self, item):
        item_idx = self.ALLERGENS.index(item)
        score = self.score
        for i in range(item_idx):
            score//= 2
        return score % 2 == 1 

    @property
    def lst(self):
        return [allergen for allergen in self.ALLERGENS if self.allergic_to(allergen)] 
