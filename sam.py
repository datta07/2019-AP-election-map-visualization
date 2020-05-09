import sqlite3
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np
import requests
from difflib import SequenceMatcher
import matplotlib
import pandas
import sqlite3


# for getting values
def getAltName(name):
	con = sqlite3.connect('data.db')
	data = con.execute('select name from altnames where altname=?',(name,))
	name = False
	for i in data:
		name = i[0]
	con.commit()
	con.close()
	return name

df = pandas.read_excel("res1.xlsx")
arr=['Puthalapattu ', 'Kuppam', 'Kaikalur', 'Machilipatnam', 'Kakinada City', 'Avanigadda', 'Penamaluru', 'Parchur ', 'Puttaparthi', 'Mangalagiri', 'Yerragondapalem ', 'Udayagiri', 'ELAMANCHILI', 'Gajuwaka', 'Peddapuram', 'Guntur West', 'Kandukur', 'Gajapathinagaram', 'Nellimarla', 'Kurupam ', 'Alur', 'Srikakulam', 'Tuni', 'Visakhapatnam  North', 'Anaparthy', 'Giddalur', 'Kodumur ', 'Gannavaram (SC)', 'Thamballapalle', 'Proddatur', 'Tekkali', 'Srungavarapukota', 'Gangadhara Nellore', 'Repalle', 'Cheepurupalli', 'Chodavaram', 'Kovvur ', 'Parvathipuram ', 'Kanigiri', 'Guntur East', 'Nidadavole', 'Bhimli', 'Ongole', 'Kothapeta', 'Sarvepalli', 'Rayachoti', 'Pattikonda', 'KALYANDURG', 'Penukonda', 'Punganur', 'Achanta', 'Unguturu', 'Nellore City', 'Sullurpeta ', 'Vijaywada West', 'Ramachandrapuram', 'Vijayawada East', 'Tadikonda (SC)', 'Venkatagiri', 'Jaggampeta ', 'Srisailam', 'Nandikotkur ', 'Nagari', 'Rajamundry Rural', 'Tenali  ', 'Pedana', 'Nandyal', 'Rampachodavaram ', 'Rajampet', 'Mylavaram', 'Prathipadu (SC)', 'Pamarru ', 'Madakasira ', 'Macherla', 'Chittoor', 'Palamaner', 'Chandragiri', 'Rajahmundry City', 'Kakinada Rural', 'Kovur', 'Pithapuram', 'Narsipatnam', 'Mandapeta', 'Allagadda', 'Kadiri', 'Gurazala', 'V.Madugula', 'Gopalapuram ', 'Vizianagaram', 'Chirala', 'Razole ', 'Vijayawada central', 'Etcherla', 'Nellore Rural', 'Rajanagaram', 'Anakapalli', 'Narasaraopet', 'Dharmavaram', 'TANUKU', 'Salur ', 'Amadalavalasa', 'Banaganapalle', 'Addanki ', 'Kavali', 'Ichchapuram', 'Singanamala ', 'Gannavaram', 'Narasannapeta', 'Uravakonda', 'Denduluru ', 'Palakonda  (ST)', 'Atmakur', 'Pathapatnam', 'Kodur ', 'Amalapuram ', 'Bobbili ', 'Pendurthi', 'Madanapalle', 'Kurnool', 'Mydukur', 'Adoni', 'Visakhapatnam South', 'Ponnur', 'Anantapur urban', 'Pedakurapadu', 'Paderu ', 'Eluru', 'Tirupati', 'Panyam', 'Yemmiganur', 'Chilakaluripet', 'Palasa', 'Jammalamadugu', 'Gudivada ', 'Narasapuram', 'PAYAKARAOPETA ', 'Prathipadu', 'Rayadurg', 'Jaggayyapeta', 'Badvel ', 'Nuzvid ', 'Polavaram ', 'Darsi', 'Vinukonda', 'Kadapa', 'Kamalapuram ', 'Undi', 'Araku valley ', 'Visakhapatnam East', 'Markapuram', 'Srikalahasti', 'Raptadu', 'Tadipatri', 'Gudur ', 'Tiruvuru ', 'Satyavedu ', 'Chintalapudi ', 'Dhone', 'Hindupur', 'Mantralayam', 'Kondapi ', 'Bhimavaram', 'Sattenapalli', 'Rajam (SC)', 'Tadepalligudem', 'Visakhapatnam  West', 'Bapatla', 'Guntakal', 'Pulivendla', 'Palacole', 'Nandigama ', 'Mummidivaram', 'Pileru', 'Santhanuthalapadu ', 'Vemuru (SC)']

def getMaxwin(con):
	if (con==False):
		return (1,1,1,1)
	df1=df[df[' AC NAME ']==con]
	party=df1[' PARTY '].values.tolist()
	votes=df1[' TOTAL '].values.tolist()
	mx=votes.index(max(votes))
	votes.remove(votes[mx])
	party.remove(party[mx])
	mx=votes.index(max(votes))
	votes.remove(votes[mx])
	party.remove(party[mx])
	par={'YSRCP':(0,0,1,1),'TDP':(1,1,0,1),'JnP':(1,0,0,1),'IND':(139/255, 158/255, 144/255,1),'CPM':(1,0,0,0.25),'NOTA':(0,0,0,1),'INC':(0,1,0,1),'CPI':(1,0,0,0.5),'BSP':(1,0,0,0.75),'BJP':(250/255, 181/255, 5/255,1),'AIFB':(250/255, 5/255, 181/255,1)}
	return par[party[votes.index(max(votes))]]


def getAge(con):
	if (con==False):
		return (1,1,1,1)
	df1=df[df[' AC NAME ']==con]
	ages=df1[' AGE '].values.tolist()
	votes=df1[' TOTAL '].values.tolist()
	mx=votes.index(max(votes))
	if (int(ages[mx])<50)&(int(ages[mx])>40):
		return (1,0,0,1)
	return (1,1,1,1)

def getMajority(con):
	if (con==False):
		return (1,1,1,1)
	df1=df[df[' AC NAME ']==con]
	party=df1[' PARTY '].values.tolist()
	votes=df1[' % VOTES POLLED '].values.tolist()
	names=df1[' CANDIDATE NAME '].values.tolist()
	mx=votes.index(max(votes))
	winner=party[mx]
	majority=votes[mx]
	win_name=names[mx]
	votes.remove(votes[mx])
	party.remove(party[mx])
	names.remove(win_name)
	mx=votes.index(max(votes))
	sec_majority=votes[mx]
	losser_name=names[mx]
	diff=majority-sec_majority
	par={'YSRCP':(0,0,1,1),'TDP':(1,1,0,1),'JnP':(1,0,0,1),'IND':(139/255, 158/255, 144/255,1),'CPM':(1,0,0,0.25),'NOTA':(0,0,0,1),'INC':(0,1,0,1),'CPI':(1,0,0,0.5),'BSP':(1,0,0,0.75),'BJP':(250/255, 181/255, 5/255,1),'AIFB':(250/255, 5/255, 181/255,1)}
	if (diff>30):
		print(con,winner,'with',diff)
		print('		--->',win_name,majority,losser_name,sec_majority)
		return par[winner]
	return (1,1,1,1)



fig, ax = plt.subplots()
map=Basemap(projection="mill",lat_0=0, lon_0=0,llcrnrlon=76.7, llcrnrlat=12.55, urcrnrlon=84.8, urcrnrlat=19.2)
map.readshapefile('data/data/India_AC','ap')


disp=["ADILABAD","KARIMNAGAR","NIZAMABAD","KHAMMAM","MEDAK","WARANGAL","RANGAREDDI","HYDERABAD","NALGONDA","MAHBUBNAGAR"]


for info,shape in zip(map.ap_info, map.ap):
	#print(info['AC_NAME'])
	#if (info['ST_NAME']!='Andhra Pradesh'):
	ax.add_collection(PatchCollection([Polygon(np.array(shape))], facecolor= (1,1,1,1), edgecolor=(1,1,1,1), linewidths=.3, zorder=2))

for info,shape in zip(map.ap_info, map.ap):
	if (info['ST_NAME']=='ANDHRA PRADESH'):
		if (info['DIST_NAME'] in disp):
			continue
		ax.add_collection(PatchCollection([Polygon(np.array(shape))], facecolor= getMajority(getAltName(info['AC_NAME'])) , edgecolor=(0,0,0,1), linewidths=.2, zorder=2))
		
plt.show()