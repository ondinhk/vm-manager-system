import time

import cv2
import easyocr
from matplotlib import pyplot as plt
from ultralytics import YOLO

from name import NAME

model = YOLO("yolov8x-seg.pt")


def calculate_image(image_path, index_name):
    centers_list = []
    cel_list = []
    # x1, y1, x2, y2 = 330, 265, 590, 525
    x1, y1, x2, y2 = 65, 223, 358, 518
    results = model.predict(image_path, save=False, conf=0.3, classes=index_name,
                            device=0, show_labels=False, show_boxes=False)
    result = results[0]
    masks = result.masks
    if not masks:
        return centers_list
    # img = Image.open(image_path)
    # draw = ImageDraw.Draw(img)
    num_rows, num_cols = count_cells(image_path)
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
        # draw.polygon(polygon, outline=(0, 255, 0), width=1)
        # draw = ImageDraw.Draw(img)
    # img.show()
    # print(cel_list)
    print(centers_list)
    return centers_list


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


def count_cells(_image_path, threshold=200):
    x, y, width, height = 65, 223, 294, 294
    image = cv2.imread(_image_path, cv2.IMREAD_GRAYSCALE)
    roi = image[y:y + height, x:x + width]
    _, binary_image = cv2.threshold(roi, threshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cell_count = 0
    min_cell_area = 1750
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_cell_area:
            cell_count += 1
    # print(cell_count)
    if 1 <= cell_count <= 11:
        return 3, 3
    return 4, 4


def show_img(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.axis('off')
    plt.imshow(image_rgb)
    plt.show()


def convert_image_to_text(image):
    x, y, width, height = 70, 150, 200, 70
    roi = image[y:y + height, x:x + width]
    # show_img(roi)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(roi)
    if not result:
        return ""
    print(result[1][1])
    return str(result[1][1])


def get_index_name(text_val):
    try:
        if text_val == 'buses':
            return 5
        index = list(NAME.values()).index(text_val)
        key = list(NAME.keys())[index]
        return key
    except ValueError:
        return None


if __name__ == '__main__':
    start_time = time.time()
    end_time = time.time()

    image_path = './images/16.PNG'
    image = cv2.imread(image_path)
    show_img(image)
    # text = convert_image_to_text(image)
    # index_name = get_index_name(text)
    # calculate_image(image_path, int(index_name))
    #
    # elapsed_time = end_time - start_time
    # print(f"Time taken: {elapsed_time} seconds")
