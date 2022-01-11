import requests


def create_dir_in_Yandex(token1,name_dir):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token1)
              }
    params = {"path": name_dir}
    response =requests.put(url=url, headers=headers, params=params)
    return response

def delete_dir_in_Yandex(token1,name_dir):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token1)
    }
    params = {"path": name_dir}
    response = requests.delete(url=url, headers=headers, params=params)
    return response



