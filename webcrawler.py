import wget
from bs4 import BeautifulSoup, SoupStrainer
import requests
import os

path_for_save = 'data/'
url = 'http://data.caida.org/datasets/topology/ark/ipv4/probe-data/'

num_team = 3
year = 2018
month = 11
date = 29

def caida_ipv4_prob_data():
    for team_id in range(num_team):
        folder_for_team = 'team-' + str(team_id + 1) + '/'
        url_for_team = url + folder_for_team
        path_for_team = path_for_save + folder_for_team

        page_for_team = requests.get(url_for_team)
        data_for_team = page_for_team.text
        soup_for_team = BeautifulSoup(data_for_team)
        links_for_year = []

        for link in soup_for_team.find_all('a'):
            links_for_year.append(link.get('href'))

        links_for_year = links_for_year[5:]

        if len(links_for_year) > 0:
            if not os.path.exists(path_for_team):
                os.mkdir(path_for_team)

        for folder_for_cycle in links_for_year:
            url_for_cycle = url_for_team + folder_for_cycle
            path_for_cycle = path_for_team + folder_for_cycle

            page_for_cycle = requests.get(url_for_cycle)
            data_for_cycle = page_for_cycle.text
            soup_for_cycle = BeautifulSoup(data_for_cycle)
            links_for_file = []

            for link in soup_for_cycle.find_all('a'):
                links_for_file.append(link.get('href'))

            links_for_file = links_for_file[5:]

            if len(links_for_file) > 0:
                if not os.path.exists(path_for_cycle):
                    os.mkdir(path_for_cycle)

            for folder_for_file in links_for_file:
                url_for_file = url_for_cycle + folder_for_file
                path_for_file = path_for_cycle + folder_for_file

                page_for_file = requests.get(url_for_file)
                data_for_file = page_for_file.text
                soup_for_file = BeautifulSoup(data_for_file)
                links_for_dataset = []

                for link in soup_for_file.find_all('a'):
                    links_for_dataset.append(link.get('href'))

                links_for_dataset = links_for_dataset[5:-1]

                if len(links_for_dataset) > 0:
                    if not os.path.exists(path_for_file):
                        os.mkdir(path_for_file)

                for data in links_for_dataset:
                    url_for_data = url_for_file + data
                    if not os.path.exists(path_for_file + data):
                        filename = wget.download(url_for_data, path_for_file)

if __name__ == '__main__':
    caida_ipv4_prob_data()
