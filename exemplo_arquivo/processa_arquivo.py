from conexao import MongoConnect
#exemplo caminho absoluto
#arquivo = open("C:\\Users\\gisele\\Downloads\\google-play-store-apps\\googleplay.txt", "r")


arquivo = open("googleplay.txt", "r")
mongo_con = MongoConnect()
for linha in arquivo:
    dados = linha.split(',')
    dict = {'App': dados[0], 'Category': dados[1], 'Rating': dados[2], 'Reviews': dados[3], 'Size': dados[4]}
    mongo_con.save(dict)

arquivo.close()






"""
Exemplo comandos mongo:


db.getCollection('google').find({})

db.google.update({'App':'teste'},
   {$set:{'App':'aaaaaaaaaaaaaaaaa'}})
   
db.google.count()

db.google.remove( {"App":"App"});

db.google.insertOne(
   { App: "teste", Category: "teste" } 
)

db.google.find().sort( { "_id": -1 } )

db.google.find({ "App": "teste"} ).limit(1)

db.google.find( { Category: { $in: [ "ART_AND_DESIGN", "DEVELOP" ] } } )"""