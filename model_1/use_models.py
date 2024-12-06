from utils.crawl import *
from utils.analyze_data import *
import joblib
from joblib import Parallel, delayed
from perceptron import Perceptron


data = find_vnexpress('bão', 2)

# Dictionary to store locations and their corresponding URLs

model = joblib.load('models/trained_perceptron_model.joblib')

location_urls = {}
def process_url(url):

    analyzed_data = analyze(url)
    if analyzed_data is not None:
        prediction = model.predict([analyzed_data['ratio']])
        if prediction[0] == 1:
            locations = find_location(analyzed_data['article'])
            return url, locations
    return url, []

results = Parallel(n_jobs=-1)(delayed(process_url)(url) for url in data)

for url, locations in results:
    for location in locations:
        if location not in location_urls:
            location_urls[location] = []
        location_urls[location].append(url)

top_locations = sorted(location_urls.items(), key=lambda item: len(item[1]), reverse=True)

# Print the top 5 locations with the most URLs
print("\nTop 5 locations with the most URLs:")
for location, urls in top_locations:
    print(f"Location: {location} - Number of URLs: {len(urls)}")
    for url in urls:
        print(f"  URL: {url}")
        

