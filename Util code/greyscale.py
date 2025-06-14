from PIL import Image
import os


def convert_to_greyscale(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_folder, filename)
            # Convert to greyscale using "L" mode
            image = Image.open(img_path).convert("L")
            image.save(os.path.join(output_folder, filename))


if __name__ == "__main__":
    INPUT_FOLDER = r'D:\Projects\Python\Real-Time Driver Drowsiness Detection\Data\data_yawning\no_yawn'
    OUTPUT_FOLDER = r'D:\Projects\Python\Real-Time Driver Drowsiness Detection\Data\data_yawning\greyscale\no_yawn'
    convert_to_greyscale(INPUT_FOLDER, OUTPUT_FOLDER)
