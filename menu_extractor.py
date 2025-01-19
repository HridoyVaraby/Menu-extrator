import requests
from bs4 import BeautifulSoup

def extract_menu_items(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    menu_items = []

    # Assuming menu items are within <a> tags with specific class or id
    # Update to handle different types of menu item tags and classes
    # Update to handle different types of menu item tags and classes more broadly
    # Update to handle nested menu items more effectively
    for item in soup.find_all(['a', 'li', 'div'], class_=['menu-item', 'nav-item', 'menu-link']):
        name = item.get_text(strip=True)
        href = item.get('href') if item.name == 'a' else None
        if href:
            menu_items.append((name, href))
        else:
            # Check for nested menu items
            nested_items = item.find_all('a', href=True)
            for nested_item in nested_items:
                nested_name = nested_item.get_text(strip=True)
                nested_href = nested_item.get('href')
                menu_items.append((nested_name, nested_href))
            print(f"Skipping item with no href: {item}")

    # Debugging output to understand what the script is seeing
    print(f"Found {len(menu_items)} menu items")

    return menu_items

def save_to_file(menu_items, website_name):
    filename = f"{website_name}_menu_items.txt"
    with open(filename, 'w') as file:
        for name, url in menu_items:
            file.write(f"{name}\n")

if __name__ == "__main__":
    url = input("Enter the URL of the website: ")
    website_name = url.split('//')[-1].split('/')[0]  # Extract the domain name
    menu_items = extract_menu_items(url)
    if menu_items:
        save_to_file(menu_items, website_name)
        print(f"Menu items have been saved to menu_items.txt")
    else:
        print("No menu items found.")
