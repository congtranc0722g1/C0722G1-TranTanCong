from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import ChannelsTooMuchError, ChannelInvalidError, ChannelPrivateError



api_id = 6038426
api_hash = "4bb1168e9cd9748fb330fa29ad646ccb"


def joinChannel (phone, group):
	client = TelegramClient ("session/" + phone, api_id, api_hash)
	client.connect ()
	try:
		client (JoinChannelRequest (group))
		print ("\033[1;32m[%s] đã join vào [%s] - ✓" % (phone, group))
	except	ChannelsTooMuchError:
		print ("\033[1;31m[%s] đã bị limit join channel ✗" % phone)
	except ChannelInvalidError:
		print ("\033[1;31m[%s] không tồn tại group này [%s] ✗" % (phone, group))
	except ChannelPrivateError:
		print ("\033[1;31m[%s] bạn không có quyền vào group [%s] ✗" % (phone, group))

	client.disconnect ()


group = input ("Nhập group > ")
listPhone = open ("phone.txt", "r", encoding = "utf8").readlines ()
for i in listPhone:
	phone = i.replace ("\n", "")
	joinChannel (phone, group)
