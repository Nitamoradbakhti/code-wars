# Complete the function that returns the color of the given square on a normal, 8x8 chess board:
def square_color(file, rank):
    rank = str(rank)
    odd_files = ['a', 'c', 'e', 'g']
    odd_ranks = ['1', '3', '5', '7']
    
    even_files = ['b', 'd', 'f', 'h']
    even_ranks = ['2', '4', '6', '8']
    
    if (file in odd_files and rank in odd_ranks) or (file in even_files and rank in even_ranks):
        return "black"
    else:
        return "white"