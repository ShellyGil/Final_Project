import matplotlib.pyplot as plt
import numpy as np
import tifffile
from matplotlib.patches import Rectangle

# ==========================================
# 1. CONFIGURATION (EDIT THIS SECTION)
# ==========================================

# List your columns (Time points/Conditions)
COL_LABELS = ["Naive", "6h", "24h", "7d"]

# List your rows (Channel Names)
ROW_LABELS = ["p-AKT", "tdTom", "Merged"]

# MAP YOUR FILES HERE
# Replace these filenames with your actual .tif files.
# The structure is a list of lists: [ [Green_Files], [Red_Files] ]
file_matrix = [
    # Row 1: Green Channel Files (p-AKT)
    ["naive_green.tif", "6h_green.tif", "24h_green.tif", "7d_green.tif"],
    
    # Row 2: Red Channel Files (tdTom)
    ["naive_red.tif",   "6h_red.tif",   "24h_red.tif",   "7d_red.tif"]
]

# Scale bar settings
ADD_SCALEBAR = True
PIXELS_PER_MICRON = 2.5  # Check your microscope settings! (e.g., 20x objective usually ~2-3 px/um)
SCALE_BAR_LENGTH_UM = 100 # How long the bar should be in microns

# ==========================================
# 2. PROCESSING FUNCTIONS
# ==========================================

def load_and_normalize(filepath):
    """Loads a tiff and normalizes brightness to 0-1 range for display."""
    try:
        img = tifffile.imread(filepath)
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return np.zeros((100, 100)) # Return black square placeholder
        
    # Normalize (Min-Max scaling)
    img = img.astype(float)
    img -= img.min()
    if img.max() > 0:
        img /= img.max()
    return img

def colorize(img_data, color):
    """Converts grayscale to RGB (Green or Red)."""
    h, w = img_data.shape
    rgb = np.zeros((h, w, 3))
    
    if color == 'green':
        rgb[..., 1] = img_data # Set Green channel
    elif color == 'red':
        rgb[..., 0] = img_data # Set Red channel
        
    return rgb

def create_merge(green_img, red_img):
    """Overlays green and red channels."""
    # Create empty RGB
    h, w = green_img.shape
    merge = np.zeros((h, w, 3))
    
    # Add channels
    merge[..., 1] = green_img # Green
    merge[..., 0] = red_img   # Red
    
    # Clip values to stay within valid RGB range (0-1)
    merge = np.clip(merge, 0, 1)
    return merge

# ==========================================
# 3. MAIN APP LOGIC
# ==========================================

def generate_figure():
    num_cols = len(COL_LABELS)
    num_rows = 3 # Green, Red, Merge
    
    # Create the figure with high resolution (DPI)
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8), dpi=300)
    plt.subplots_adjust(wspace=0.05, hspace=0.05) # Tight spacing

    print("Generating figure...")

    for col_idx in range(num_cols):
        # 1. Load Images
        g_path = file_matrix[0][col_idx]
        r_path = file_matrix[1][col_idx]
        
        raw_green = load_and_normalize(g_path)
        raw_red = load_and_normalize(r_path)
        
        # 2. Create RGB versions
        vis_green = colorize(raw_green, 'green')
        vis_red = colorize(raw_red, 'red')
        vis_merge = create_merge(raw_green, raw_red)
        
        # 3. Plot them in the grid
        # Row 0: Green
        ax_g = axes[0, col_idx]
        ax_g.imshow(vis_green)
        
        # Row 1: Red
        ax_r = axes[1, col_idx]
        ax_r.imshow(vis_red)
        
        # Row 2: Merge
        ax_m = axes[2, col_idx]
        ax_m.imshow(vis_merge)

        # 4. Cleanup Axes (Remove ticks/boxes)
        for ax in [ax_g, ax_r, ax_m]:
            ax.set_xticks([])
            ax.set_yticks([])
            # Optional: remove border if you want a cleaner look
            for spine in ax.spines.values():
                spine.set_visible(False)

        # 5. Add Column Labels (Only on top row)
        if col_idx == 0:
            # Add Row Labels (only on first column)
            font_props = {'color': 'white', 'fontsize': 14, 'fontweight': 'bold'}
            # Note: We place text inside the image to match your example style
            # Adjust x,y coordinates (0.05, 0.9) to move text position
            ax_g.text(0.05, 0.9, ROW_LABELS[0], transform=ax_g.transAxes, **font_props, ha='left', va='top')
            ax_r.text(0.05, 0.9, ROW_LABELS[1], transform=ax_r.transAxes, **font_props, ha='left', va='top')
            ax_m.text(0.05, 0.9, ROW_LABELS[2], transform=ax_m.transAxes, **font_props, ha='left', va='top')

        # Add Column Headers (Time points) above the top row
        axes[0, col_idx].set_title(COL_LABELS[col_idx], fontsize=16, pad=10, color='black')

    # 6. Add Scale Bar (Only on bottom right image)
    if ADD_SCALEBAR:
        last_ax = axes[2, -1] # Bottom right
        bar_len_px = SCALE_BAR_LENGTH_UM * PIXELS_PER_MICRON
        
        # Get image dimensions to position bar correctly
        img_h, img_w = raw_green.shape 
        
        # Position: 10% from right, 10% from bottom
        rect = Rectangle((img_w - bar_len_px - (img_w*0.05), img_h - (img_h*0.1)), 
                         bar_len_px, (img_h*0.02), # Width, Height of bar
                         color='yellow')
        last_ax.add_patch(rect)

    # Add the main Figure "B" label
    fig.text(0.01, 0.95, "B", fontsize=24, fontweight='bold', color='black')

    # Save
    output_filename = "final_figure.png"
    plt.savefig(output_filename, bbox_inches='tight', facecolor='white')
    print(f"Done! Saved as {output_filename}")
    plt.show()

if __name__ == "__main__":
    generate_figure()
