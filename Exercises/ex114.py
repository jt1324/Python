# Source - https://stackoverflow.com/a/61059892
# Posted by Mayank Porwal, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-19, License - CC BY-SA 4.0
import requests

try:
  response = requests.get('https://globo.com', timeout=5)
  if response.status_code == 200:
    print("Site is accessible")
  else:
    print(f"Site returned status code: {response.status_code}")
except requests.exceptions.RequestException as e:
  print("Site is not accessible")
