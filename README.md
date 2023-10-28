# Rocket Raccoon project: cheat_radar_vk
# EN
Deceptive VK radar determines the honesty of communities in a social network: cheating, really active users.
## What is this?
The script was created for advertisers and other people who need to be sure that the community is active with minimal cheating when buying ads in the community or for other purposes.
This is a Python script written by raccoon paws on the [vk_api](https://github.com/python273/vk_api) and [tqdm](https://github.com/tqdm/tqdm) libraries. 
The main essence of the script is to determine how much the community in the social network "Vkontakte" is active, screwed up. To do this, the concepts ER, ERR (ER views) and antidogs are used:
* ER is an indicator of audience engagement, which is calculated using the formula: ${reactions/posts\over subscribers}$
* ERR (ER views) is an indicator of audience engagement by the number of users covered, which is calculated using the formula: ${reactions/posts\over averagepostcoverage}$
* Antidogs are users who are bots or zero accounts created to cheat various indicators.
## How to use
1. Clone this repo:
   ```
   git clone https://github.com/rocket-ru/cheat_radar_vk.git
   ```
2. Insert the token into the code:
   - Follow the link [*click* ](https://oauth.vk.com/authorize?client_id=6121396&scope=1385558&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1 )
   - Allow access
   - Copy the link where you were thrown, and then copy the access_token variable
   - Paste this token into the file `main.py` to the `token` variable
3. Install the required libraries
* using conda:
  ```
  conda env create -f requirements/environment.yml
  ```
* using pip:
  ```
  pip install -r requirements.txt
  ```
4. Run the script and use:
   ```
   python main.py
   ```
## A few last words
This script is not an ideal and a benchmark, but it is a good base for development in the field of community activity research. From this script, you can make a full-fledged VK bot, which only needs to throw a post from the group and he will say what kind of community it is. Don't throw stones at the raccoon - the raccoon shared a freebie.
# RU
Радар-накрутка вконтакте определяет накрученность сообществ в социальной сети: накрутку, действительно активных пользователей.
## Что это?
Скрипт был создан для рекламодателей и других людей, которым необходимо быть уверенными в том, что сообщество активно с минимальной накруткой при покупке рекламы в сообществе или для других целей.
Это скрипт на Python, написанный еночьими пальчиками на [vk_api](https://github.com/python273/vk_api) и [tqdm](https://github.com/tqdm/tqdm) библиотеках. 
Основная суть скрипта заключается в том, чтобы определить, насколько сообщество в социальной сети "Вконтакте" активно, накручено. Для этого используются понятия ER, ERR (ER views) и собачки:
* ER - это показатель вовлеченности аудитории, который рассчитывается по формуле: ${реакции/посты\over подписчиков}$
* ERR (количество просмотров ER) - показатель вовлеченности аудитории по количеству охваченных пользователей, который рассчитывается по формуле: ${реакции/публикации\over средний показатель охвата}$
* Собачки - это пользователи, которые являются ботами или нулевыми аккаунтами, созданными для накрутки различных показателей.
## Как использовать
1. Клонируйте это репозиторий:
   ```
   git clone https://github.com/rocket-ru/cheat_radar_vk.git
   ```
2. Вставьте токен в код:
   - Перейдите по ссылке [*тык* ](https://oauth.vk.com/authorize?client_id=6121396&scope=1385558&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1)
   - Разрешите доступ
   - Скопируйте ссылку, куда вас перекинуло, а затем скопируйте переменную access_token
   - Вставьте данный токен в файл `main.py` в переменную `token`
3. Установите необходимые библиотеки
* через conda:
  ```
  conda env create -f requirements/environment.yml
  ```
* через pip:
  ```
  pip install -r requirements.txt
  ```
4. Запустите скрипт и используйте:
   ```
   python main.py
   ```
## Несколько последних слов
Этот скрипт не является идеалом и эталоном, но он является хорошей базой для разработок в области исследования активности сообщества. Из этого скрипта можно сделать полноценного бота вконтакте, которому нужно только скинуть пост из группы и он скажет, что это за сообщество. Не бросайте камни в енота - енот поделился халявой.
