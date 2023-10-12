import requests
from tqdm import tqdm

def get_ids(page_number):
    url = f"https://gdbrowser.com/api/search/*?type=daily&page={page_number}"
    response = requests.get(url)
    data = response.json()
    ids = [entry['id'] for entry in data]
    return ids

def save_ids(ids):
    with open('ids.txt', 'a') as file:
        file.write(','.join(ids) + ',')

if __name__ == '__main__':
    total_pages = 249
    progress_bar = tqdm(total=total_pages, desc='Progress', unit='page')

    for page in range(total_pages):
        ids = get_ids(page)
        save_ids(ids)
        progress_bar.set_postfix({'Page': page + 1, 'Percentage': f'{(page + 1) / total_pages * 100:.2f}%'})
        progress_bar.update()

    progress_bar.close()
    print("Done")

