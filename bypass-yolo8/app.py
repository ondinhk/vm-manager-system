from PIL import Image, ImageDraw
from ultralytics import YOLO

model = YOLO("yolov8x-seg.pt")


def calculate_image(image_path, index_name, num_rows, num_cols):
    centers_list = []
    cel_list = []
    x1, y1, x2, y2 = 330, 265, 590, 525
    results = model.predict(image_path, save=False, conf=0.3, classes=index_name,
                            device=0, show_labels=False, show_boxes=False)
    result = results[0]
    masks = result.masks
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    # Draw mask
    for item in masks:
        mask1 = item
        polygon = mask1.xy[0]
        for point in polygon:
            x, y = point
            row, col = find_cell_position(x, y, x1, y1, x2, y2, num_rows, num_cols)
            center_x, center_y = find_cell_center(x1, y1, (x2 - x1) // num_cols, (y2 - y1) // num_rows, row, col)
            if (center_x, center_y) not in centers_list:
                centers_list.append((center_x, center_y))
                cel_list.append({"Hàng": row + 1, "Cột": col + 1})
        draw.polygon(polygon, outline=(0, 255, 0), width=2)
        draw = ImageDraw.Draw(img)
    # Draw cell
    # cell_width = (x2 - x1) // num_cols
    # cell_height = (y2 - y1) // num_rows
    # draw.rectangle([x1, y1, x2, y2], outline="black", width=1)
    # for i in range(num_rows):
    #     for j in range(num_cols):
    #         cell_x1 = x1 + j * cell_width
    #         cell_y1 = y1 + i * cell_height
    #         cell_x2 = cell_x1 + cell_width
    #         cell_y2 = cell_y1 + cell_height
    #         draw.rectangle([cell_x1, cell_y1, cell_x2, cell_y2], outline="black", width=1)
    print(cel_list)
    print(centers_list)
    img.show()


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


if __name__ == '__main__':
    num_rows, num_cols = 4, 4
    # print("Bikecycle")
    # calculate_image('./images/3.PNG', 1, num_rows, num_cols)
    # calculate_image('./images/1.PNG', 1, num_rows, num_cols)
    # calculate_image('./images/4.PNG', 3, num_rows, num_cols)
    # calculate_image('./images/5.PNG', 3, num_rows, num_cols)
    # calculate_image('./images/2.PNG', 9, num_rows, num_cols)
    # calculate_image('./images/11.PNG', 3, num_rows, num_cols)
    calculate_image('./images/2.PNG', 9, num_rows, num_cols)
