# simpliest_tg_parsing
The simplest implementation of a parser of data about users of channels/chats (where participants can be seen by all)

DB format:
  [username,user id,access hash,name,group,group id]

Preparing to use this tools:
  1. python -m venv myenv
  2. source myenv/bin/activate
  3. pip install --upgrade pip
  4. pip install telethon
  5. python ./scrap_msg.py

Example:

![demo2](https://github.com/8evz0/simpliest_tg_parsing/assets/65715287/e0b86d5e-d73e-4897-9859-b15ff08637cd)
