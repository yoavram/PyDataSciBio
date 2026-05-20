# Assignment: Directory Watcher and Neural Data Analytics for Zorgian Research

Professor Zorglax, a furry Zorgian neurobiologist, had filled their quantum storage device with thousands of high-resolution images of the Luminari Glowsquid's neural network. These bioluminescent cephalopods, native to Zorg's deep oceans, possess the most complex neural structures on the planet, with remarkable cognitive abilities and color-shifting communication patterns. When their device displayed "Quantum Storage Capacity Exceeded," a fellow researcher suggested an automated solution: a Python script to monitor for new neural images, convert them, compile basic statistical data for research, and compress the original images at dual-moon alignment (which conveniently occurs at what Earth dwellers would call "midnight"). This would allow Zorglax to continue their groundbreaking study of Glowsquid neurobiology while building a valuable database of these fascinating creatures' neural properties.

## Objective

Create a Python script that uses `watchdog` to monitor a user-defined directory for new Luminari Glowsquid neural specimen images. When a new image file is detected, convert it to a user-defined format using `Pillow`, keep the original file, and extract basic statistical data about the neural patterns. Additionally, use `APScheduler` to schedule a task that compresses all original (non-converted) images in the directory into a single zip file each night at the Zorgian midnight (when both moons align). The script should continuously build a database of Glowsquid neural statistics to support Zorgian neurobiology research.

## Requirements

1. **Use `argparse`** to allow Zorgian researchers to specify:
   - The directory to watch for new specimen images.
   - The output format to which new images should be converted.
   - The prefix for the zip file created at Zorgian midnight.

2. **Use `watchdog`** to monitor the specified directory for new neuron image files. Supported Zorgian neural imaging formats include: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, and `.tiff`.

3. **Use `Pillow`** to convert new neural specimen image files to the specified format.

4. **Use `APScheduler`** to schedule a task that compresses all original Glowsquid neural images in the directory into a single zip file each Zorgian night at dual-moon alignment (which conveniently corresponds to Earth midnight — 00:00). The zip file should be named with the provided prefix followed by the current date.

## Instructions

### 1. Set Up Argument Parsing

Use `argparse` to define the following command-line arguments:

- `--watch_directory`: The directory to watch for new Glowsquid neural specimen image files.
- `--output_format`: The format to convert new neural images to (e.g., `png`, `jpg`).
- `--zip_filename_prefix`: The prefix for the zip file created at midnight.
- `--statistics_csv`: The path where Glowsquid neural statistics CSV should be saved.

### 2. Create an Event Handler Class

- Create a class that inherits from `FileSystemEventHandler`.
- Override the `on_created` method to handle new files.
- In this method, check if the new file is a supported neural image (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`). If so:
  - Convert it to the specified output format using `Pillow`.
  - Keep the original file — it will be archived by the nightly compression job.
  - Call the neural statistics analysis function on the converted image (see Section 5).

### 3. Create a Compression Function

- Define a function to compress all **original** (non-converted) neural specimen images in the watched directory into a zip file. Original images are those whose extension differs from the configured output format, matching the supported formats list (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`).
- The zip file should be named using the provided prefix followed by the current Zorgian date (simulated using Earth date).

### 4. Set Up the Watchdog Observer

Instantiate the observer and schedule it to monitor the specified directory using the event handler class.

### 5. Create a Neural Statistics Analysis Function

Define a function that uses PIL (Pillow) to analyze each neural image:

- Calculate basic image properties (dimensions, file size).
- Measure average brightness across the image.
- Determine simple RGB histogram data to estimate "neuron activity".
- Track image processing time.

Append the calculated statistics to the specified CSV file.

### 6. Set Up the Scheduler

Instantiate a `BackgroundScheduler` and add a job to run the compression function at midnight (00:00) each day, which is when the dual-moon alignment occurs on Zorg.

### 7. Run the Script

- Start the observer and the scheduler.
- Keep the script running until interrupted.

## Submission

Submit your completed script along with a short explanation of how you tested it in a compressed Zip file to the course's quantum data repository (Moodle).

## Testing Guidelines

### 1. Test Multiple Image Formats

- Your solution must demonstrate successful conversion between **all supported image formats** (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`).
- Include test results showing conversions from each format to at least two other formats.
- Document any variations in file size, quality, or processing differences between formats.

### 2. Test the Statistical Analysis

- Generate and include sample CSV output from your statistical analysis function.
- Briefly explain how the statistics vary between different Glowsquid neural images and different file formats.

### 3. Test the Nightly Compression

- Do not wait until midnight to test this. Instead, call the compression function directly once at script startup (before starting the scheduler loop), or temporarily replace the `cron` trigger with an `interval` trigger set to a short period (e.g., 30 seconds) to verify the zip file is created correctly. Remember to revert to the `cron` trigger in your final submission.
- Verify the zip contains only original (non-converted) images and is named correctly.