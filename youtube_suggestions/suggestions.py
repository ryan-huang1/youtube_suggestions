import requests
import json
import time
import random
import concurrent.futures

def fetch_suggestions(url, proxies, headers):
    try:
        response = requests.get(url, proxies=proxies, headers=headers)
        content = response.text
        return content
    except Exception as e:
        print(f"Request to {url} failed: {e}")
        return None

def parse_primary_response(content):
    try:
        start = content.index('window.google.ac.h(') + len('window.google.ac.h(')
        end = content.rindex(')')
        data = json.loads(content[start:end])
        return [suggestion[0] for suggestion in data[1]]
    except Exception as e:
        print(f"Parsing primary response failed: {e}")
        return []

def parse_fallback_response(content):
    try:
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
        print(f"Parsing fallback response failed: {e}")
        return []

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

    primary_url = f"https://suggestqueries-clients6.youtube.com/complete/search?client=youtube&gs_ri=youtube&ds=yt&q={requests.utils.quote(query)}"
    fallback_url = f"https://clients1.google.com/complete/search?client=youtube&gs_ri=youtube&ds=yt&q={requests.utils.quote(query)}"

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_primary = executor.submit(fetch_suggestions, primary_url, proxies, headers)
        future_fallback = executor.submit(fetch_suggestions, fallback_url, proxies, headers)
        
        content_primary = future_primary.result()
        content_fallback = future_fallback.result()

    suggestions_primary = parse_primary_response(content_primary) if content_primary else []
    suggestions_fallback = parse_fallback_response(content_fallback) if content_fallback else []

    # Combine and deduplicate suggestions
    combined_suggestions = list(set(suggestions_primary + suggestions_fallback))
    return combined_suggestions

# Example usage:
# print(get_suggestions("python programming", "proxy_host:proxy_port:username:password"))
