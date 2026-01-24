# Nociceptor Innervation Analysis Suite

**Author:** Shelly Gilad
**Course:** Python Final Project (2026)

## Overview

The **Nociceptor Innervation Analysis Suite** is a web-based application designed to streamline the quantification, statistical analysis, and visualization of histological data. Built using **PyScript**, this tool runs Python data science libraries (Pandas, Matplotlib, SciPy) directly in the browser, allowing for a seamless workflow without requiring local Python installation.

This suite was developed to assist in neurobiology research, specifically for analyzing nociceptor innervation in mouse models (e.g., CFA and Carrageenan inflammation models).

## Features

The suite consists of three integrated modules:

1.  **The Quantifier:** An image processing tool that calculates the percentage of innervation in microscopy images (supports `.tif`, `.jpg`, `.png`). It features contrast adjustment, noise reduction, and manual/automatic (Otsu) thresholding.
2.  **The Analyst:** A statistical engine that performs paired t-tests on the quantified data. It generates publication-ready bar charts with significance annotations (*, **, ***).
3.  **The Illustrator:** A figure assembly tool that arranges microscopy images into a grid, merges channels, adds scale bars, and exports high-resolution figures.

## Technologies Used

* **HTML5 / CSS3 / JavaScript**: Core UI and interactivity.
* **PyScript**: Python runtime within the browser.
* **Python Libraries**:
    * `pandas` & `numpy`: Data handling.
    * `scipy`: Statistical analysis (t-tests).
    * `matplotlib`: Plotting and figure generation.
* **UTIF.js**: Support for TIFF image decoding.

---

## How to Run

1.  Clone or download this repository.
2.  Locate the `index.html` file.
3.  Open `index.html` in a modern web browser (Chrome, Edge, or Firefox recommended).
    * *Note: On first load, please wait a few seconds for the Python environment to initialize.*

---

## Step-by-Step User Guide

Below are instructions for using each module with the provided example data.

### 1. Module A: The Quantifier (Image Analysis)
Use this module to turn your raw microscopy images into numerical data.

**Example Data Location:** `example_files_for_quantifier/`

1.  Click the **"1. Quantifier"** tab at the top.
2.  Click the **📂 Load Images** button.
3.  Select the **entire folder** named `example_files_for_quantifier` (or select all `.tif` files inside it).
4.  **Adjust Image:**
    * Use the **Contrast** and **Brightness** sliders to make the nerve fibers stand out.
    * Check **"Show Threshold (Red)"** to see what the computer detects.
    * Select **"Auto (Otsu)"** for automatic detection, or adjust the **Manual Cutoff** number until only the nerves are covered in red.
5.  **Define Region of Interest (ROI):**
    * Click **✏️ Draw ROI**.
    * Click multiple points around the tissue section you want to analyze.
    * **Right-click** to close the shape and finish drawing.
6.  **Calculate:**
    * Click **Calculate Index**. The result (percentage of area innervated) will appear in blue.
    * Click **💾 Save & Next** to record this number and automatically load the next image.
7.  **Finish:**
    * Once all images are processed, click **⬇️ Download Log (.txt)**.
    * Save this file. You will need these files for the next step.

### 2. Module B: The Analyst (Statistics)
Use this module to compare your experimental groups statistically.

**Example Data Location:**
* `CFA_Left/` (Injured)
* `CFA_Right/` (Control)
* `Carr_Left/` (Injured)
* `Carr_Right/` (Control)

1.  Click the **"2. Analyst"** tab.
2.  Look at the sidebar on the left. You will see sections for **CFA Mice** and **Carrageenan Mice**.
3.  **Load Data:**
    * Under **CFA Mice > Left (Inj)**, click `Choose Files` and select the text files from your `CFA_Left` folder. Click **+ Add Left**.
    * Repeat this for **Right (Ctrl)** using the `CFA_Right` folder.
    * Repeat for the **Carrageenan** groups using the `Carr_Left` and `Carr_Right` folders.
    * *Note: Ensure the badges (green numbers) show that files have been loaded.*
4.  **Configure Plot:**
    * In the center panel, you can change the **Title** (e.g., "Innervation Density") and **Y-Label** (e.g., "Area %").
5.  **Run Analysis:**
    * Click the large dark button: **GENERATE STATISTICS**.
    * A bar chart will appear comparing the Left vs. Right sides for both groups.
    * **Significance stars** (*, **, ***) will automatically appear if the difference is statistically significant. P-values are printed at the bottom.

### 3. Module C: The Illustrator (Figure Creation)
Use this module to create a final image grid for your report.

**Example Data:** Use any representative `.tif` or `.jpg` images.

1.  Click the **"3. Illustrator"** tab.
2.  **Grid Configuration:**
    * Set **Cols (Time)** to `4` (e.g., Naive, 24h, 48h, 7d).
    * Set **Rows (Ch)** to `2` (e.g., PGP9.5, CGRP).
    * Check **Include Merge** if you want a bottom row showing combined channels.
    * Click **Create Grid**.
3.  **Upload Images:**
    * A grid of "Drop" boxes will appear.
    * Click each box to upload the corresponding image for that timepoint and channel.
4.  **Finalize:**
    * Set the **Scale** (e.g., `100` µm) and **Px/µm** ratio (based on your microscope).
    * Click **Render Figure**.
    * Once the image is generated below, click **Download PNG** to save your final figure.

---

## License

This project is open-source and available under the MIT License.
