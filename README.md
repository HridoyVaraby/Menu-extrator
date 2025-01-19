# Menu Extractor

Menu Extractor is a Python program that extracts menu items from a given website URL and saves them to a text file. It also includes a simple GUI built with Tkinter to load and save menu items.

## Features

- Extracts menu items from a given website URL.
- Saves the extracted menu items to a text file.
- Provides a simple GUI to load and save menu items.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup library
- Tkinter (included with Python standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HridoyVaraby/Menu-extrator.git
   cd menu-extractor
   ```

2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

### Command Line

1. Run the main script:
   ```bash
   python menu_extractor.py
   ```

2. Enter the URL of the website when prompted.

3. The extracted menu items will be saved to a text file named `website_name_menu_items.txt`.

### GUI

1. Run the GUI script:
   ```bash
   python menu_extractor_gui.py
   ```

2. Use the "Load Menu Items" button to load menu items from `menu_items.txt`.

3. Use the "Save Menu Items" button to save the current content of the text area back to `menu_items.txt`.

## File Structure

- `menu_extractor.py`: The main script to extract menu items from a website.
- `menu_extractor_gui.py`: The GUI script to load and save menu items.
- `menu_items.txt`: A sample text file containing menu items.
- `www.hriindia.com_menu_items.txt`: An example output file containing menu items extracted from www.hriindia.com.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the developers of the Requests and BeautifulSoup libraries for making web scraping easier.
- Thanks to the Tkinter team for providing a simple and effective GUI toolkit.
