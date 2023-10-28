# -*- coding: utf-8 -*-
"""
Project by Rocket Raccoon in 2023
Level: base (free)
Type: VK script
Version: 1.1
Contacts: t.me/single_rocket, vk.com/raccoon_rocket
Comment: This script works on vk api and to use it you need to get a vk token.
        I am not responsible for the performance of the script.
"""
from typing import Union
from vk_api import VkApi
from tqdm import tqdm

token = "*YOUR TOKEN*"
authorize = VkApi(token=token)
vk = authorize.get_api()


def followers_cheat(group_id, count_followers):
    follower_ban = []
    for i in tqdm(range(count_followers // 1000 + 1)):
        followers_all = ""
        followers = vk.groups.getMembers(group_id=group_id, offset=i * 1000, count=1000)["items"]
        for follower in followers:
            followers_all += "id" + str(follower) + ", "

        followers_ban = vk.users.get(user_ids=followers_all, fields="deactivated")
        for follower in followers_ban:
            if "deactivated" in follower:
                if follower["deactivated"] == "banned":
                    follower_ban.append(follower)
                else:
                    follower_ban.append(follower)
    return follower_ban, round((100 / count_followers) * len(follower_ban), 2)


def walls_cheat(group_id, count_followers, pr_antidogs):
    walls = vk.wall.get(owner_id=-group_id, offset=50, count=50)["items"]
    likes, comments, reposts, views, count = 0, 0, 0, 0, 0
    for post in walls:
        likes += post["likes"]["count"]
        comments += post["comments"]["count"]
        reposts += post["reposts"]["count"]
        if "views" in post:
            if "count" in post["views"]:
                views += post["views"]["count"]
        count += 1

    average_data = [round(likes / count, 2), round(comments / count, 2), round(reposts / count, 2),
                    round(views / count, 2)]
    ER = round((round(likes / count, 2) + round(comments / count, 2) +
                round(reposts / count, 2) + round(views / count, 2)) / count_followers, 2)
    ERViews = round((likes + comments + reposts) / views, 2)

    Rtest = []
    # Тест по просмотрам
    if 1000 <= count_followers < views * 2:
        Rtest.append(5)
    elif 1000 <= count_followers < views:
        Rtest.append(4)
    elif 100 <= count_followers < views * 2:
        Rtest.append(3)
    elif 100 <= count_followers < views:
        Rtest.append(2)
    elif views > count_followers:
        Rtest.append(1)
    else:
        Rtest.append(0)

    # Тест активности
    if (average_data[0] > count_followers * 2 or average_data[1] > count_followers * 2
            or average_data[2] > count_followers * 2):
        Rtest.append(5)
    elif average_data[0] > views or average_data[1] > views or average_data[2] > views:
        Rtest.append(5)
    elif average_data[0] > count_followers or average_data[1] > count_followers or average_data[2] > count_followers:
        Rtest.append(4)
    elif (average_data[0] / 2 > average_data[-1] * 2 or average_data[1] / 2 > average_data[-1] * 2
          or average_data[2] / 2 > average_data[-1] * 2):
        Rtest.append(3)
    elif (average_data[0] / 2 > average_data[-1] or average_data[1] / 2 > average_data[-1]
          or average_data[2] / 2 > average_data[-1]):
        Rtest.append(2)
    elif (average_data[0] / 4 > average_data[-1] or average_data[1] / 4 > average_data[-1]
          or average_data[2] / 4 > average_data[-1]):
        Rtest.append(1)
    else:
        Rtest.append(0)

    # Тест по средним показателям
    if pr_antidogs >= 10.00:
        Rtest.append(5)
    else:
        Rtest.append(0)

    ALikes = (100 / count_followers) * (likes / count)
    if ALikes < 1.00:
        Rtest.append(5)
    elif ALikes < 10.00:
        Rtest.append(4)
    elif ALikes < 20.00:
        Rtest.append(3)
    else:
        Rtest.append(0)

    return ER, ERViews, Rtest, average_data


def reactions_cheat(group_id):
    walls = vk.wall.get(owner_id=-group_id, offset=50, count=10)["items"]
    likes = {}
    for i in range(10):
        user_likes = vk.wall.getLikes(owner_id=-group_id, post_id=walls[i]["id"], count=0)
        if user_likes["count"] > 1000:
            counts = user_likes["count"] / 1000 + 1
            like = []
            for j in range(counts):
                user_likes = vk.wall.getLikes(owner_id=-group_id, post_id=walls[i]["id"], fields=j * 1000, count=1000)
                for user_like in user_likes["users"]:
                    like.append("id" + str(user_like["uid"]))
            likes[i] = like
        else:
            user_likes = vk.wall.getLikes(owner_id=-group_id, post_id=walls[i]["id"], count=1000)["users"]
            like = []
            for user_like in user_likes:
                like.append("id" + str(user_like["uid"]))
            likes[i] = like

    left_wing = []
    all_left_wing = []
    all_count = 0
    for i in range(1, len(likes) - 1):
        for j in range(len(likes[i])):
            if likes[i][j] not in likes[int(i + 1)]:
                if likes[i][j] not in all_left_wing:
                    left_wing.append(likes[i][j])
                    all_left_wing.append(likes[i][j])
                else:
                    try:
                        left_wing.remove(likes[i][j])
                    except:
                        pass
        all_count += len(likes[i])
    count = len(left_wing)
    return count, 100 / all_count * count, all_count


def main(group_id: Union[str, int], language):
    if not group_id.isdigit():
        if 'vk.com' in group_id:
            group_id = group_id.split('vk.com/')[-1]
        group_id = vk.groups.getById(group_id=group_id)[0]['id']
    count_followers = vk.groups.getMembers(group_id=group_id)["count"]
    # Запускаем проверку накрутки подписчиков
    antidogs, pr_antidogs = followers_cheat(group_id, count_followers)

    # Запускаем проверку активности стены
    ER, ERViews, Rtest, average_data = walls_cheat(group_id, count_followers, pr_antidogs)

    # Запускаем проверку на накрутку лайков/комментариев
    left_wing, pc_variety, all_people_likes = reactions_cheat(group_id)

    if language == 'ru':
        total = f"""Результаты:
    Подписчики: {count_followers} подписчиков из них {len(antidogs)} собачек | {pr_antidogs}%
    Показатели: ER {ER}% | ERViews {ERViews}% | Rtest {sum(Rtest) * 5}% - {Rtest} | Среднее {average_data}
    По накрутке на стене: {left_wing} из {all_people_likes} | {pc_variety}%"""
    else:
        total = f"""Results:
    Subscribers: {count_followers} subscribers from them {len(antidogs)} antidogs | {pr_antidogs}%
    Indicators: ER {ER}% | ERViews {ERViews}% | Rtest {sum(Rtest) * 5}% - {Rtest} | Average {average_data}
    By cheating on the wall: {left_wing} from {all_people_likes} | {pc_variety}%"""
    return total


while True:
    language = input("Введите ваш язык/Enter your language (ru/en): ")
    if language not in ['ru', 'en']:
        print('Не верный язык/Wrong language')
    else:
        print({'ru': 'Был выбран русский язык', 'en': 'English was chosen'}[language])
        break
while True:
    group = input({'ru': 'Введите ID/короткое имя/ссылку сообщества: ',
                   'en': 'Enter the community ID/short name/link: '}[language])
    print(main(group, language))
