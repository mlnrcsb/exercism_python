class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError('row not positive')
        if row > 7:
            raise ValueError('row not on board')
        if column < 0:
            raise ValueError('column not positive')
        if column > 7:
            raise ValueError('column not on board')
        
        self.row = row
        self.column = column

    def can_attack(self, other):
        same_row = self.row == other.row
        same_column = self.column == other.column 
        
        if same_row and same_column: 
            raise ValueError('Invalid queen position: both queens in the same square')
        
        same_ascending_diagonal = (self.row + self.column) == (other.row + other.column)
        same_descending_diagonal = (self.row - self.column) == (other.row - other.column)
        
        return same_row or same_column or same_ascending_diagonal or same_descending_diagonal