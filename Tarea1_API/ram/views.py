from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .services import get_episodes, get_episode_info, get_character_info, get_location_info


def index(request):
    template = loader.get_template('ram/index.html')
    context = {
        'x': "place",
        'results': get_episodes()
    }
    return HttpResponse(template.render(context, request))


def episode(request, episode_id):
    template = loader.get_template('ram/episode.html')
    ep_info = get_episode_info(episode_id)
    characters = []
    for c_url in ep_info.characters:
        char_id = c_url.split('/')[-1]
        characters.append(get_character_info(char_id)[0])
    context = {
        'x1': "chao",
        'ep_info': ep_info,
        'char_info': characters
    }
    return HttpResponse(template.render(context, request))


def location(request, location_id):
    template = loader.get_template('ram/places.html')
    loc_info = get_location_info(location_id)
    characters = []
    for c_url in loc_info.residents:
        char_id = c_url.split('/')[-1]
        characters.append(get_character_info(char_id)[0])
    context = {
        'x1': "chao",
        'loc_info': loc_info,
        'char_info': characters
    }
    return HttpResponse(template.render(context, request))


def character(request, character_id):
    template = loader.get_template('ram/character.html')
    get_info = get_character_info(character_id)
    character_info = get_info[0]
    origin = get_info[1]
    location = get_info[2]
    episodes = []
    for ep_url in character_info.episode:
        ep_id = ep_url.split('/')[-1]
        episodes.append(get_episode_info(ep_id))
    context = {
        'x2': "hola2",
        'char_info': character_info,
        'episodes': episodes,
        'origin': origin,
        'location': location
    }
    return HttpResponse(template.render(context, request))


def not_found(request):
    template = loader.get_template('ram/not_found.html')
    context = {
    }
    return HttpResponse(template.render(context, request))



