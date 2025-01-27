# first we need to install a package called colorgram

import colorgram

rgb_colors = []
colors = colorgram.extract('hirst_painting.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

# color_list = [(127, 173, 198), (222, 219, 210), (179, 174, 160), (197, 209, 215), (25, 22, 8), (112, 108, 67), (7, 32, 39), (65, 113, 127), (198, 193, 181), (164, 200, 214), (143, 141, 87), (219, 225, 223), 
# (80, 79, 27), (8, 14, 12), (156, 165, 163), (91, 140, 156), (93, 106, 101), (23, 80, 93), (238, 235, 237), (184, 195, 194), (26, 20, 22), (116, 134, 129), (87, 55, 45), (42, 75, 70), (143, 122, 
# 115), (89, 77, 80), (168, 162, 164), (186, 192, 199), (205, 187, 180), (97, 133, 159)]
