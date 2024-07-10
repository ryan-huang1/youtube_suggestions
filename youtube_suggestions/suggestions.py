import requests
import json
import time
import random

def get_suggestions(query, proxy=None):
    if not query:
        raise ValueError("Search query was not provided!")

    # Parse proxy string if provided
    proxies = None
    if proxy:
        parts = proxy.split(':')
        if len(parts) != 4:
            raise ValueError("Invalid proxy format. Expected format: host:port:username:password")
        host, port, username, password = parts
        proxies = {
            'http': f'http://{username}:{password}@{host}:{port}',
            'https': f'http://{username}:{password}@{host}:{port}'
        }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    try:
        # Primary method
        url = f"https://suggestqueries-clients6.youtube.com/complete/search?client=youtube&gs_ri=youtube&ds=yt&q={requests.utils.quote(query)}"
        response = requests.get(url, proxies=proxies, headers=headers)
        content = response.text
        
        # Extract JSON data
        start = content.index('window.google.ac.h(') + len('window.google.ac.h(')
        end = content.rindex(')')
        data = json.loads(content[start:end])
        
        return [suggestion[0] for suggestion in data[1]]
    except Exception as e:
        print(f"Primary method failed: {e}")
        time.sleep(random.uniform(1, 3))  # Random delay between 1 and 3 seconds
        try:
            # Fallback method
            url = f"https://clients1.google.com/complete/search?client=youtube&gs_ri=youtube&ds=yt&q={requests.utils.quote(query)}"
            response = requests.get(url, proxies=proxies, headers=headers)
            content = response.text
            
            search_suggestions = []
            for item in content.split('['):
                if item.startswith('"'):
                    suggestion = item.split('"')[1]
                    if suggestion:
                        search_suggestions.append(suggestion)
            
            # Remove the last item as it's usually not a valid suggestion
            if search_suggestions:
                search_suggestions.pop()
            
            return search_suggestions
        except Exception as e:
            print(f"Fallback method failed: {e}")
            return []