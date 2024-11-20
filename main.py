from PIL import Image

ROBINSON_MASKS = [
    [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]],  
    [[0, 1, 2], [-1, 0, 1], [-2, -1, 0]],  
    [[1, 2, 1], [0, 0, 0], [-1, -2, -1]],  
    [[2, 1, 0], [1, 0, -1], [0, -1, -2]],  
    [[1, 0, -1], [2, 0, -2], [1, 0, -1]],  
    [[0, -1, -2], [1, 0, -1], [2, 1, 0]],  
    [[-1, -2, -1], [0, 0, 0], [1, 2, 1]],  
    [[-2, -1, 0], [-1, 0, 1], [0, 1, 2]],  
]


def readimg(filename):
    image = Image.open(filename).convert("L")
    pixels = list(image.getdata())
    width, height = image.size
    return [pixels[i * width:(i + 1) * width] for i in range(height)], width, height

def save(image, filename):
    height = len(image)
    width = len(image[0])
    output = Image.new("L", (width, height))
    flat_pixels = [image[y][x] for y in range(height) for x in range(width)]
    output.putdata(flat_pixels)
    output.save(filename)

def apply(image, width, height):
    edge_image = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            max_gradient = 0
            for mask in ROBINSON_MASKS:
                gradient = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        gradient += image[y + dy][x + dx] * mask[dy + 1][dx + 1]
                max_gradient = max(max_gradient, abs(gradient))
            edge_image[y][x] = min(255, max_gradient)
    return edge_image

def process(filepaths):
    for filepath in filepaths:
        try:
            image, width, height = readimg(filepath)
            edge_image = apply(image, width, height)
            op = "output" + filepath.split(".")[0] + ".jpeg"
            save(edge_image, op)
        except Exception as e:
            print(f"Failed to process {filepath}: {e}")

filepaths = ["image1.jpeg", "image2.jpeg", "image3.jpeg", "image4.jpeg", "image5.jpeg"]
process(filepaths)
