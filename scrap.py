from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

api_id = 21836109
api_hash = 'ce6540c6ea12bb5d8e58ed919bd6c075'
phone = '+79991145562'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print('Choose groups to scrape members from (separated by commas):')
for i, g in enumerate(groups):
    print(str(i) + '- ' + g.title)

selected_indices = input("Enter Numbers (e.g., 0,2,3): ").split(',')
selected_groups = [groups[int(index.strip())] for index in selected_indices]

print('Fetching Members...')
all_participants = []

for target_group in selected_groups:
    all_participants.extend(client.get_participants(target_group, aggressive=True))

file_name = input("Enter the name of the file (including extension, e.g., members.csv): ")

print('Saving In file...')
with open(file_name, "a", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    for user in all_participants:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])  
print('Members scraped successfully.')

