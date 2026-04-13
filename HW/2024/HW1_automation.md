# Assignment: Directory Watcher and Image Converter Script

Dr. Emily Harper was a microbiologist who spent her days photographing Petri dishes to study bacterial growth. Every day, she captured hundreds of high-resolution images, filling her computer's storage quickly. One afternoon, her computer flashed a dreaded message: "Disk Space Full." Emily was distraught; she couldn't delete any images as they were crucial for her research.

As she sat worrying, a colleague noticed her distress and suggested a solution. He recommended a Python script that used watchdog to monitor her directory for new images and APScheduler to compress all images into a zip file every night at midnight. Grateful for the idea, Emily implemented the script, freeing up space and allowing her to continue her vital research without interruption.


## Objective
Create a Python script that uses `watchdog` to monitor a user-defined directory for new image files. When a new image file is detected, convert it to a user-defined format using `Pillow`. Additionally, use `APScheduler` to schedule a task that compresses all images in the directory into a single zip file each night at midnight.

## Requirements
1. **Use `argparse`** to allow users to specify:
    - The directory to watch for new images.
    - The output format to which new images should be converted.
    - The prefix for the zip file created at midnight.

2. **Use `watchdog`** to monitor the specified directory for new image files. Supported image formats include: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, and `.tiff`.

3. **Use `Pillow`** to convert new image files to the specified format.

4. **Use `APScheduler`** to schedule a task that compresses all images in the directory into a single zip file each night at midnight. The zip file should be named with the provided prefix followed by the current date.

## Instructions
1. **Set Up Argument Parsing**
    - Use `argparse` to define the following command-line arguments:
        - `--watch_directory`: The directory to watch for new image files.
        - `--output_format`: The format to convert new images to (e.g., `png`, `jpg`).
        - `--zip_filename_prefix`: The prefix for the zip file created at midnight.

2. **Create an Event Handler Class**
    - Create a class that inherits from `FileSystemEventHandler`.
    - Override the `on_created` method to handle new files.
    - In this method, check if the new file is an image, and if so, convert it to the specified format using `Pillow`.

3. **Create a Compression Function**
    - Define a function to compress all images in the watched directory into a zip file.
    - The zip file should be named using the provided prefix followed by the current date.

4. **Set Up the Watchdog Observer**
    - Instantiate the observer and schedule it to monitor the specified directory using the event handler class.

5. **Set Up the Scheduler**
    - Instantiate a `BackgroundScheduler` and add a job to run the compression function at midnight each day.

6. **Run the Script**
    - Start the observer and the scheduler.
    - Keep the script running until interrupted.

## Submission
Submit your completed script along with a short explanation of how you tested it in a compressed Zip file to the course moodle page.
