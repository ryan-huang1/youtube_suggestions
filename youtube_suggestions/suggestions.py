import requests
import json

def get_suggestions(query):
    if not query:
        raise ValueError("Search query was not provided!")

    try:
        # Primary method
        url = f"https://suggestqueries-clients6.youtube.com/complete/search?client=youtube&gs_ri=youtube&ds=yt&q={requests.utils.quote(query)}"
        response = requests.get(url)
        content = response.text
        
        # Extract JSON data
        start = content.index('window.google.ac.h(') + len('window.google.ac.h(')
        end = content.rindex(')')
        data = json.loads(content[start:end])
        
        return [suggestion[0] for suggestion in data[1]]
    except Exception as e:
        print(f"Primary method failed: {e}")
        try:
            # Fallback method
            url = f"https://clients1.google.com/complete/search?client=youtube&gs_ri=youtube&ds=yt&q={requests.utils.quote(query)}"
            response = requests.get(url)
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
