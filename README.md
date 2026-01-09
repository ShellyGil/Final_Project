# Nociceptor Innervation Analysis Suite

## 1. Project Overview
**Title:** Automated Quantification and Statistical Analysis of Nociceptor Innervation  
**Author:** Shelly Gilad  
**Course:** Python 2025  

### 1.1 Motivation
In neurobiology research, analyzing nociceptor (pain receptor) innervation patterns in tissue samples often involves laborious manual quantification. Researchers need to calculate the density of nerve fibers under various conditions (e.g., inflammation models like CFA or Carrageenan). Current manual methods are time-consuming, prone to observer bias, and lack an integrated workflow for statistical validation and figure generation.

### 1.2 Project Goal
The goal of this project is to develop a comprehensive, Python-based toolkit that streamlines the entire experimental workflow. The suite is composed of three integrated modules:
1.  **Image Analysis GUI:** For calculating innervation indices from raw microscopy data.
2.  **Statistical Dashboard:** For performing hypothesis testing (ANOVA/Tukey) and generating data plots.
3.  **Figure Generator:** For creating publication-ready multi-channel microscopy panels.

---

## 2. System Architecture & Modules

The project is divided into three distinct standalone applications that function as a pipeline.

### Module A: The Quantifier (`innervation_app.py`)
A desktop GUI application built with **Tkinter** designed for high-throughput image processing.
* **Key Features:**
    * **Folder-based workflow:** Automatically loads and iterates through all images in a directory.
    * **Image Pre-processing:** Real-time adjustment of Contrast, Brightness, and Noise Reduction (Gaussian Blur) using `Pillow`.
    * **ROI Selection:** Supports both Polygon and Freehand drawing tools to isolate specific tissue areas (Regions of Interest).
    * **Thresholding Algorithms:**
        * *Manual Cutoff:* User-defined intensity threshold.
        * *Otsu’s Method:* Automatic dynamic thresholding based on histogram bimodal distribution.
    * **Visual Feedback:** Live red overlay of thresholded pixels for accuracy verification.
    * **Zoom Navigation:** Custom "Zoom Select" and drag functionality for precise drawing.

### Module B: The Analyst (`innervation_analyzer.py`)
A web-based analytical dashboard built with **Streamlit** for statistical processing.
* **Key Features:**
    * **Data Ingestion:** Accepts raw text files from Module A or aggregated Excel/CSV datasets.
    * **Statistical Engine:** Automates One-Way ANOVA to test for variance and performs post-hoc Tukey HSD tests for pairwise comparisons.
    * **Dynamic Visualization:**
        * Generates bar charts with overlaid scatter plots (individual data points).
        * Automatically annotates significant differences with brackets and asterisks (*, **, ***).
    * **Reporting:** Outputs statistical summary tables ready for export.

### Module C: The Illustrator (`Fig_create.py`)
A script for generating high-resolution, multi-channel figures using **Matplotlib**.
* **Key Features:**
    * **Multi-Channel Handling:** Merges Green (e.g., p-AKT) and Red (e.g., tdTomato) channels.
    * **Normalization:** Auto-scales pixel intensity for optimal visibility.
    * **Grid Layout:** Automatically arranges images by time-points (columns) and channels (rows).
    * **Metadata Integration:** Adds scale bars (micron-to-pixel conversion) and labels.
    * **Export:** Saves generic "Figure B" style layouts at 300 DPI for publication.

---

## 3. Technologies & Libraries
The project utilizes the following Python libraries:

* **GUI & Interaction:** `tkinter`, `streamlit`
* **Image Processing:** `Pillow` (PIL), `tifffile`
* **Data Manipulation:** `pandas`, `numpy`
* **Statistics:** `scipy.stats`, `statsmodels`
* **Visualization:** `matplotlib`

---

## 4. Usage Workflow

### Step 1: Quantify Images
Run the desktop app to process raw `.tif` or `.png` files.
```bash
python innervation_app.py
```
* Action: Draw ROI -> Calculate Index -> Save.
* Output: A text file containing the innervation index for each image.

### Step 2: Analyze Data
Upload the results to the Streamlit dashboard.
```bash
streamlit run innervation_analyzer.py
```
* Action: Upload text files for Control, CFA, and Carrageenan groups.
* Output: Statistical P-values and an "Innervation Index" graph.

### Step 3: Generate Figures
Configure the file paths in Fig_create.py and run the script to visualize the histology.
```bash
python Fig_create.py
```
* Output: A final_figure.png combining all channels and time points.

---

## 5. Development Roadmap / Features to Implement
* **Zoom Out logic:** Fix crop constraints to allow returning to the original image size in the GUI. (Implemented)
* **Significance Brackets:** Algorithmically calculate the Y-position for significance brackets in Matplotlib to avoid overlap with data points. (Implemented)
* **Otsu Thresholding:** Implement vectorised numpy calculations for fast dynamic thresholding. (Implemented)
* **Future Work:** Add support for batch-processing ROIs without manual drawing using Deep Learning (U-Net) segmentation.

---

## 6. Installation Requirements
To run this suite, install the dependencies using the provided requirements.txt:
```Plaintext
streamlit
pandas
numpy
matplotlib
scipy
statsmodels
Pillow
tifffile
```
