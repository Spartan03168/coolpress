from bs4 import BeautifulSoup
import requests

def get_stars(url):
    reponse = requests.get(url, headers={"User-Agent": "Chrome/5.0"})
    reponse_code = reponse.status_code
    if reponse_code == 200:
        htmlContent = reponse.content
        soup = BeautifulSoup(htmlContent, "html.parser")
        star = soup.find("a", class_="Link--secondary no-underline mr-3")
        star = star.find("span",  class_="text-bold")
        return star.text
    else:
        print("Error: Unable to fetch trending repositories")

def get_all_repositories(url):
    reponse = requests.get(url, headers={"User-Agent": "Chrome/5.0"})
    reponse_code = reponse.status_code
    stars=0
    if reponse_code == 200:
        htmlContent = reponse.content
        soup = BeautifulSoup(htmlContent, "html.parser")
        all_repos = soup.find_all("span", class_="repo")
        for link in all_repos:
            new_url = url+"/"+link.text
            repo_star = get_stars(new_url)
            stars = stars+ int(repo_star)
    else:
        print("Error: Unable to fetch trending repositories")

    return stars

