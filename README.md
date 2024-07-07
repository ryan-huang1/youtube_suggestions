# YouTube Suggestions

A simple Python package to get YouTube search suggestions with optional proxy support.

## Installation

You can install the YouTube Suggestions package using pip:

```
pip install youtube-suggestions
```

## Usage

Here's a quick example of how to use the package:

```python
from youtube_suggestions import get_suggestions

# Without proxy
suggestions = get_suggestions("python programming")
print(suggestions)

# With proxy
proxy = "gate.dc.smartproxy.com:1111:proxyname:password"
suggestions_with_proxy = get_suggestions("python programming", proxy=proxy)
print(suggestions_with_proxy)
```

This will print a list of search suggestions for "python programming", first without a proxy and then using the specified proxy.

## Features

- Get YouTube search suggestions
- Optional proxy support
- Fallback method if the primary method fails
- Easy to use

## Proxy Format

The proxy should be specified in the following format:

```
host:port:username:password
```

For example:

```
gate.dc.smartproxy.com:1111:proxyname:password
```

## Requirements

- Python 3.6+
- requests library

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
