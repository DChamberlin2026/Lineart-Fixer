from PIL import Image
import numpy as np

img = Image.open("input.png").convert("RGBA")
data = np.array(img)

r = data[:, :, 0]
g = data[:, :, 1]
b = data[:, :, 2]
a = data[:, :, 3]

# Average brightness
brightness = (r.astype(np.uint16) + g.astype(np.uint16) + b.astype(np.uint16)) / 3

# Start with fully transparent output
out = np.zeros_like(data)

# Only decide for pixels that are not already fully transparent
visible = a > 0

# Dark pixels become solid black
dark = visible & (brightness <= 127.5)
out[dark] = [0, 0, 0, 255]

# Light pixels stay transparent automatically

Image.fromarray(out, "RGBA").save("output.png")