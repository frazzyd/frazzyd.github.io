import os
import re

# Configuration
fullsize_folder = './images/albums/norway2025/fullsize'  # Folder with full-size images
thumbnail_folder = './images/albums/norway2025/thumbnails'  # Folder with thumbnails
html_file_path = 'norway2025.html'                  # Path to the HTML file to modify
insert_marker = '<!-- INSERT GALLERY HERE -->' # Marker in HTML file where new HTML should be inserted

def generate_html_for_image(image_name):
    # Extract the base name (without extension) for using in the thumbnail and title
    base_name = os.path.splitext(image_name)[0]
    # Generate paths for the full image and thumbnail
    full_image_path = f"{fullsize_folder}/{image_name}".replace("\\", "/")
    thumbnail_path = f"{thumbnail_folder}/{image_name}".replace("\\", "/")
    
    # Generate HTML structure for the image
    html = f"""
            <div class="albumImage" data-tags="street,portrait,color">
                <a href="{full_image_path}" data-lightbox="gallery" data-title="Norway, April 2025">
                    <img data-src="{thumbnail_path}" alt="Norway" class="fade-in lazy-image">
                </a>	
            </div>"""
    return html

def natural_sort_key(filename):
    """Extracts numbers from filenames to sort naturally by number."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', filename)]

def insert_gallery_html(html_file, fullsize_folder, insert_marker):
    # Check if the HTML file exists
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found.")
        return

    # List all images in the full-size folder and sort them numerically
    images = sorted(
        [img for img in os.listdir(fullsize_folder) if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))],
        key=natural_sort_key
    )

    if not images:
        print(f"No images found in {fullsize_folder}.")
        return

    # Generate HTML for each image
    gallery_html = "\n".join([generate_html_for_image(img) for img in images])

    # Read the HTML file content
    with open(html_file, 'r') as file:
        content = file.read()

    # Insert the generated HTML at the insert marker
    if insert_marker in content:
        new_content = content.replace(insert_marker, f"{insert_marker}\n{gallery_html}")
    else:
        print(f"Marker '{insert_marker}' not found in {html_file}.")
        return

    # Write the modified content back to the HTML file
    with open(html_file, 'w') as file:
        file.write(new_content)

    print(f"Successfully added {len(images)} images to {html_file}.")

# Run the function
insert_gallery_html(html_file_path, fullsize_folder, insert_marker)