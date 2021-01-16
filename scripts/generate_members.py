from collections import defaultdict

import requests
import yaml


def get_github_userinfo(user):

    user_url = f"https://api.github.com/users/{user}"
    user_result = requests.get(user_url)
    user_json = user_result.json()

    user_info = {
        "name": user_json["name"],
        "avatar_url": user_json["avatar_url"],
        "bio": user_json["bio"],
        "twitter": user_json["twitter_username"],
        "gh-user": user,
    }

    return user_info


def get_members():

    user_dict = defaultdict()

    url_orgs = "https://api.github.com/orgs/codigobonito/members"

    result = requests.get(url_orgs)

    for user in result.json():

        user_dict[user["login"]] = get_github_userinfo(user["login"])

    return user_dict


def write_yaml(members):

    for member in members:

        with open(f"../docs/_pessoas/{member}.yaml", "w") as f:
            f.write("---\n")
            content = yaml.dump(members[member], allow_unicode=True)
            f.write(content)
            f.write("---")


if __name__ == "__main__":

    members = get_members()

    write_yaml(members)
