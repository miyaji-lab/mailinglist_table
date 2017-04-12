# encoding:utf-8
import subprocess
from prettytable import PrettyTable
import random

def get_mailinglist_addresses():
	#cmd = "list_lists"
	#return subprocess.check_output(cmd, shell=True).split()
	return ["a@waa", "b@waa", "c@waa", "d@waa"]

def get_members(address):
	# cmd = "list_member " + address
	# return subprocess.check_output(cmd, shell=True).split()
	people = ["taro", "ziro", "sabro", "siro", "goro"]
	random.shuffle(people)
	return people[:3]

s = set()
malinglists = {}
malinglist_addresses = get_mailinglist_addresses()
for address in malinglist_addresses:
	members = get_members(address)
	malinglists[address] = members
	for m in members:
		s.add(m)

allmember = list(s)
iallmember = {}
for i, v in enumerate(allmember):
	iallmember[v] = i

H = len(malinglists)
W = len(allmember)
table = [[False]*W for i in range(H)]

for h, address in enumerate(malinglists):
	for member in malinglists[address]:
		table[h][iallmember[member]] = True

# HACK
for row, address in zip(table, malinglists):
	print row, address

ptable = PrettyTable(['Malinglist'] + allmember)
for row, address in zip(table, malinglists):
	l = ["o" if v else "-" for v in row]
	ptable.add_row([address] + l)
print ptable
