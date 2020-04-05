import requests
from .models import Character, Episode, Location


def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


def get_episodes():
    response1 = generate_request('https://rickandmortyapi.com/api/episode/')
    if response1:
        results_p1 = response1.get('results')
        page_2 = response1.get('info').get('next')
        response2 = generate_request(page_2)
        results_p2 = response2.get('results')
        total_results = results_p1 + results_p2
        episodes = []
        for ep in total_results:
            x = Episode(id=ep.get('id'),name=ep.get('name'), air_date=ep.get('air_date'), episode=ep.get('episode'))
            episodes.append(x)
        return episodes
    return ''


def get_episode_info(episode_id):
    ep = generate_request('https://rickandmortyapi.com/api/episode/{}'.format(episode_id))
    if ep:
        ep_info = Episode(
            id=ep.get('id'),
            name=ep.get('name'),
            air_date=ep.get('air_date'),
            episode=ep.get('episode'),
            characters=ep.get('characters')
        )
        return ep_info


def get_character_info(character_id):
    cha = generate_request('https://rickandmortyapi.com/api/character/{}'.format(character_id))
    aux = []
    if cha:
        char_info = Character(
            id=cha.get('id'),
            name=cha.get('name'),
            status=cha.get('status'),
            species=cha.get('species'),
            type=cha.get('type'),
            gender=cha.get('gender'),
            origin=cha.get('origin').get('name'),
            location=cha.get('location').get('name'),
            image=cha.get('image'),
            episode=cha.get('episode')
        )
        aux.append(cha.get('origin').get("url"))
        aux.append(cha.get('location').get("url"))
        aux2 = [x.split("/")[-1] for x in aux]
        origin_id = Location(id=aux2[0])
        location_id = Location(id=aux2[1])
        return char_info, origin_id, location_id


def get_location_info(location_id):
    loc = generate_request('https://rickandmortyapi.com/api/location/{}'.format(location_id))
    if loc:
        loc_info = Location(
            id=loc.get('id'),
            name=loc.get('name'),
            type=loc.get('type'),
            dimension=loc.get('dimension'),
            residents=loc.get('residents')
        )
        return loc_info
    return ""
