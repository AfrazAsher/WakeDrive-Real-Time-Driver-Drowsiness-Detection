import os
import random
import shutil


def pick_random_pictures(input_dir, output_dir, num_pics=1):
    """
    Pick a specified number of random pictures from the input directory, 
    save them to the output directory, and delete the original pictures from the input directory.

    Parameters:
    - input_dir (str): Path to the directory containing pictures.
    - output_dir (str): Path to the directory where the randomly selected pictures will be saved.
    - num_pics (int): Number of pictures to move. Default is 1.
    """

    # List all files in the input directory
    all_files = [f for f in os.listdir(
        input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    # Filter for common image extensions
    image_files = [f for f in all_files if f.lower().endswith(
        ('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    if not image_files:
        print("No images found in the provided directory.")
        return

    # Check if there are enough images to move
    if len(image_files) < num_pics:
        print(
            f"Only {len(image_files)} images found, but {num_pics} were requested.")
        return

    # Pick a specified number of random images
    selected_images = random.sample(image_files, num_pics)

    for random_image in selected_images:
        # Print the full path of the file being copied
        print(f"Copying file from: {os.path.join(input_dir, random_image)}")

        # Copy the random image to the output directory
        shutil.copy(os.path.join(input_dir, random_image),
                    os.path.join(output_dir, random_image))
        print(f"Copied {random_image} to {output_dir}")

        # Delete the original file from the source directory
        os.remove(os.path.join(input_dir, random_image))
        print(f"Deleted original {random_image} from {input_dir}")


# Example Usage:
input_file_path = r'D:\Projects\Python\Real-Time Driver Drowsiness Detection\Data\data_yawning\new_no_yawn'
output_file_path = r'D:\Projects\Python\Real-Time Driver Drowsiness Detection\Data\data_yawning\test\no_yawn'
pick_random_pictures(input_file_path, output_file_path, 1000)
