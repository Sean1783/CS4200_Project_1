class PuzzleExtractor:

    def extract_numbers(self, filename):
        matrices = list()

        with open(filename, 'r') as file:
            lines = file.readlines()

        current_puzzle_matrix = list()
        for line in lines:
            if "/" in line:
                if current_puzzle_matrix:
                    matrices.append(current_puzzle_matrix)
                    current_puzzle_matrix = list()
            else:
                row_string = line.split()
                num_row = [int(i) for i in row_string]
                current_puzzle_matrix.append(num_row)
        if current_puzzle_matrix:
            matrices.append(current_puzzle_matrix)
        return matrices

