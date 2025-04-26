# Description:

# Help prepare for the entrance exams to art school.

# It is known in advance that this year, the school chose the symmetric letter “W” as the object for the image, and the only condition for its image is only the size that is not known in advance, so as training, you need to come up with a way that accurately depicts the object.

# Write a function that takes an integer as height and returns a list of strings with a line-by-line image of the object.

# Below is an example function:

# # height = 3 should return:
# [
#   "*   *   *",
#   " * * * * ",
#   "  *   *  "
# ]

# # height = 5 should return:
# [
#   "*       *       *",
#   " *     * *     * ",
#   "  *   *   *   *  ",
#   "   * *     * *   ",
#   "    *       *    "
# ]

def get_w(height):
    if height < 2:
        return []
    width = 4 * height - 3 
    result = []
    for i in range (height):
        row = [" "] * width
        row[i] = "*"
        row[width // 2 - i] = "*"
        row[width // 2 + i] = "*"
        row[width - 1 - i] = "*"
        result.append("".join(row))
    return result