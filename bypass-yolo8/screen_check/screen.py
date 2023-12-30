from PIL import Image, ImageDraw

x1, y1, x2, y2 = 330, 265, 590, 525


def draw_and_divide_square(output_path, num_rows, num_cols):
    existing_image_path = "vm2.PNG"
    image = Image.open(existing_image_path)
    draw = ImageDraw.Draw(image)
    cell_width = (x2 - x1) // num_cols
    cell_height = (y2 - y1) // num_rows
    draw.rectangle([x1, y1, x2, y2], outline="black", width=2)
    for i in range(num_rows):
        for j in range(num_cols):
            cell_x1 = x1 + j * cell_width
            cell_y1 = y1 + i * cell_height
            cell_x2 = cell_x1 + cell_width
            cell_y2 = cell_y1 + cell_height
            draw.rectangle([cell_x1, cell_y1, cell_x2, cell_y2], outline="black", width=2)
    # image.show()


def find_cell_position(x, y, x1, y1, x2, y2, num_rows, num_cols):
    cell_width = (x2 - x1) // num_cols
    cell_height = (y2 - y1) // num_rows
    col = max(0, min((x - x1) // cell_width, num_cols - 1))
    row = max(0, min((y - y1) // cell_height, num_rows - 1))
    return row, col


def find_cell_center(x1, y1, cell_width, cell_height, row, col):
    center_x = x1 + (col + 0.5) * cell_width
    center_y = y1 + (row + 0.5) * cell_height
    return center_x, center_y


num_rows, num_cols = 4, 4
x, y = 543, 415
row, col = find_cell_position(x, y, x1, y1, x2, y2, num_rows, num_cols)
center_x, center_y = find_cell_center(x1, y1, (x2 - x1) // num_cols, (y2 - y1) // num_rows, row, col)
draw_and_divide_square("output_4x4.png", num_rows=4, num_cols=4)

print(f"Điểm ({x}, {y}) nằm ở ô hàng {row + 1}, cột {col + 1}")
print(f"Vị trí trung tâm của ô nằm ở ({center_x}, {center_y})")
