from PIL import Image
import numpy as np

# Load image with alpha
img = Image.open("input.png").convert("RGBA")

# Convert to numpy array
data = np.array(img)

# Split channels
r, g, b, a = data.T

# Create mask where pixels are not transparent
mask = a > 0

# Set RGB to pure black where mask is true
data[..., :3][mask.T] = (0, 0, 0)

# Save result
result = Image.fromarray(data)
result.save("output.png")