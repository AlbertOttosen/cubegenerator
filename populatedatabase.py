from connection import connection
from fetchCardData import fetchCardData

def cleantext(card, param):
	try:
		return card[param].replace("\'", "\'\'")
	except:
		return ''

def insertCard(card, cur):
	try:
		if (card['layout'] == 'normal'):
			sql = """
				INSERT INTO rawcards
				VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', {4}, \'{5}\', \'{6}\', \'{7}\', \'{8}\', \'{9}\', \'{10}\', \'{11}\', \'{12}\', 1, \'{13}\');
				""".format(
					card['oracle_id'],
					cleantext(card, 'uri'),
					cleantext(card, 'name'),
					cleantext(card, 'type_line'),
					card['cmc'],
					cleantext(card, 'mana_cost'),
					cleantext(card, 'oracle_text'),
					cleantext(card, 'power'),
					cleantext(card, 'toughness'),
					cleantext(card, 'loyalty'),
					cleantext(card, 'colors'),
					cleantext(card, 'color_identity'),
					cleantext(card, 'produced_mana'),
					# card['edhrec_rank'],
					cleantext(card, 'layout')
					)
			cur.execute(sql)
	except Exception as error:
		print(error)
		print("couldn't insert card {0} in database {1}".format(card['name'], 'card'))

class populator(connection):
    def whileConnected(self):
        carddata = fetchCardData()
        for card in carddata:
            insertCard(card, self.cur)
        # commit changes
        if (input("Commit changes? ")[0] == 'y'):
            self.conn.commit()
            print("Changes Commited")
        else:
            print("Changes Discarded")

if __name__ == '__main__':
    pop = populator()
    pop.connect()