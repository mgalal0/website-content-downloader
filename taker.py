import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time

def download_webpage_content():
    # Ask for the website URL
    url = input("Please enter the website URL you want to download: ")
    
    # Create output directory
    output_dir = 'webpage_content'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        os.makedirs(os.path.join(output_dir, 'css'))
        os.makedirs(os.path.join(output_dir, 'js'))

    # Headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print(f"\nDownloading content from {url}...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')





        
        # Save HTML
        print("Saving HTML...")
        with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        # Function to download external resources
        def download_resource(resource_url, local_path):
            try:
                if resource_url.startswith('//'):
                    resource_url = 'https:' + resource_url
                elif not resource_url.startswith(('http://', 'https://')):
                    resource_url = urljoin(url, resource_url)
                
                resource_response = requests.get(resource_url, headers=headers)
                resource_response.raise_for_status()
                
                with open(local_path, 'w', encoding='utf-8') as f:
                    f.write(resource_response.text)
                print(f"Downloaded: {os.path.basename(local_path)}")
                return True
            except Exception as e:
                print(f"Failed to download {resource_url}: {str(e)}")
                return False

        # Download CSS
        print("\nDownloading CSS files...")
        css_files = set()
        for css in soup.find_all('link', rel='stylesheet'):
            if css.get('href'):
                css_files.add(css['href'])
        
        for i, css_url in enumerate(css_files):
            css_filename = f'style_{i}.css'
            download_resource(css_url, os.path.join(output_dir, 'css', css_filename))
            # Small delay to be nice to the server
            time.sleep(0.5)

        # Download JavaScript
        print("\nDownloading JavaScript files...")
        js_files = set()
        for script in soup.find_all('script', src=True):
            if script.get('src'):
                js_files.add(script['src'])
        
        for i, js_url in enumerate(js_files):
            js_filename = f'script_{i}.js'
            download_resource(js_url, os.path.join(output_dir, 'js', js_filename))
            # Small delay to be nice to the server
            time.sleep(0.5)

        print("\nDownload completed! Files are saved in the 'webpage_content' folder:")
        print(f"- HTML file: webpage_content/index.html")
        print(f"- CSS files: webpage_content/css/")
        print(f"- JavaScript files: webpage_content/js/")
        
    except requests.exceptions.RequestException as e:
        print(f"\nError accessing the website: {str(e)}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("=== Website Content Downloader ===")
    print("This tool will download HTML, CSS, and JavaScript files from a website.")
    print("The files will be saved in a 'webpage_content' folder.\n")
    
    while True:
        download_webpage_content()
        
        again = input("\nWould you like to download another website? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the Website Content Downloader!")
            break