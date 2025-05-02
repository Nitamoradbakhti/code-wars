# Description:

# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here
def rgb(r, g, b):
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'A', 'B', 'C', 'D', 'E', 'F']

    def to_hex(x):
        x = max(0, min(x, 255))
        return hex_chars[x // 16] + hex_chars[x % 16]

    return to_hex(r) + to_hex(g) + to_hex(b)
