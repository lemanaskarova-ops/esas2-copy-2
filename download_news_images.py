import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    'https://rabitakolleci.edu.az/news/3569',
    'https://rabitakolleci.edu.az/news/3554',
    'https://rabitakolleci.edu.az/news/3422',
]

def download_image(url, filename):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        
        # Look for images in the content. Usually under <div class="entry-content"> or similar
        # Let's just find the first large image or the first img tag that looks like a photo
        img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.IGNORECASE)
        img_url = None
        for match in img_matches:
            # ignore logos or small icons
            if 'logo' not in match.lower() and 'icon' not in match.lower() and 'avatar' not in match.lower():
                img_url = match
                break
                
        if img_url:
            if not img_url.startswith('http'):
                img_url = 'https://rabitakolleci.edu.az' + img_url
            
            print(f"Downloading {img_url} to {filename}")
            img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            img_data = urllib.request.urlopen(img_req, context=ctx).read()
            with open(filename, 'wb') as f:
                f.write(img_data)
        else:
            print(f"No suitable image found for {url}")
            
    except Exception as e:
        print(f"Error processing {url}: {e}")

download_image(urls[0], 'real_news1.jpg')
download_image(urls[1], 'real_news2.jpg')
download_image(urls[2], 'real_news3.jpg')
