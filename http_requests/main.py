import requests


def print_key_value_pair(dict):
    space_length = 0
    space_between_pairs = 4

    for key in dict:
        space_length = len(key) if len(key) > space_length else space_length
    space_length += space_between_pairs

    for key, value in dict.items():
        adjusted_space_length = space_length - len(key)
        print("{key}{space}{value}".format(key=key, space=''.ljust(adjusted_space_length), value=value))


if __name__ == "__main__":
    website = requests.get('https://google.com')
    website_info = {
        "url": website.url,
        "status_code": website.status_code
    }

    print_key_value_pair(website_info)
