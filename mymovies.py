from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.html'), 200

@app.route('/comedies')
def comedies():
	return render_template('comedies.html'), 200


#comedy movies

@app.route('/comedies/grownups')
def grownups():
	return render_template('comedy/grownups.html'), 200

@app.route('/comedies/grownups2')
def grownups2():
	return render_template('comedy/grownups2.html'), 200

@app.route('/comedies/haroldandkumar')
def haroldandkumar():
	return render_template('comedy/haroldandkumar.html'), 200

@app.route('/comedies/neighbors')
def neighbors():
	return render_template('comedy/neighbors.html'), 200

@app.route('/comedies/superbad')
def superbad():
	return render_template('comedy/superbad.html'), 200

@app.route('/comedies/dumbanddumber')
def dumbanddumber():
	return render_template('comedy/dumbanddumber.html'), 200

@app.route('/comedies/thehangover')
def thehangover():
	return render_template('comedy/thehangover.html'), 200

@app.route('/comedies/thehangover2')
def thehangover2():
	return render_template('comedy/thehangover2.html'), 200

@app.route('/comedies/thehangover3')
def thehangover3():
	return render_template('comedy/thehangover3.html'), 200



@app.route('/thrillers')
def thrillers():
	return render_template('thrillers.html'), 200


#thriller movies

@app.route('/thriller/inception')
def inception():
	return render_template('thriller/inception.html'), 200

@app.route('/thriller/therevenant')
def therevenant():
	return render_template('thriller/therevenant.html'), 200

@app.route('/thriller/vforvendeta')
def vforvendeta():
	return render_template('thriller/vforvendeta.html'), 200

@app.route('/thriller/taken')
def taken():
	return render_template('thriller/taken.html'), 200

@app.route('/thriller/saw')
def saw():
	return render_template('thriller/saw.html'), 200

@app.route('/thriller/nowyouseeme')
def nowyouseeme():
	return render_template('thriller/nowyouseeme.html'), 200

@app.route('/thriller/thesilenceofthelambs')
def thesilenceofthelambs():
	return render_template('thriller/thesilenceofthelambs.html'), 200

@app.route('/thriller/memento')
def memento():
	return render_template('thriller/memento.html'), 200

@app.route('/thriller/killlist')
def killlist():
	return render_template('thriller/killlist.html'), 200



@app.route('/drama')
def drama():
	return render_template('drama.html'), 200

#drama movies

@app.route('/drama/thegodfather')
def thegodfather():
	return render_template('drama/thegodfather.html'), 200

@app.route('/drama/thegodfather2')
def thegodfather2():
	return render_template('drama/thegodfather2.html'), 200

@app.route('/drama/thegodfather3')
def thegodfather3():
	return render_template('drama/thegodfather3.html'), 200

@app.route('/drama/grantorino')
def grantorino():
	return render_template('drama/grantorino.html'), 200

@app.route('/drama/braveheart')
def braveheart():
	return render_template('drama/braveheart.html'), 200

@app.route('/drama/thehatefuleight')
def thehatefuleight():
	return render_template('drama/thehatefuleight.html'), 200

@app.route('/drama/prisoners')
def prisoners():
	return render_template('drama/prisoners.html'), 200

@app.route('/drama/oldboy')
def oldboy():
	return render_template('drama/oldboy.html'), 200

@app.route('/drama/hacksawridge')
def hacksawridge():
	return render_template('drama/hacksawridge.html'), 200




@app.route('/romance')
def romance():
	return render_template('romance.html'), 200

#romance movies

@app.route('/romance/titanic')
def titanic():
	return render_template('romance/titanic.html'), 200

@app.route('/romance/astarisborn')
def astarisborn():
	return render_template('romance/astarisborn.html'), 200

@app.route('/romance/shesoutofmyleague')
def shesoutofmyleague():
	return render_template('romance/shesoutofmyleague.html'), 200

@app.route('/romance/phantomthread')
def phantomthread():
	return render_template('romance/phantomthread.html'), 200

@app.route('/romance/forrestgump')
def forrestgump():
	return render_template('romance/forrestgump.html'), 200

@app.route('/romance/twilight')
def twilight():
	return render_template('romance/twilight.html'), 200

@app.route('/romance/fiftyshadesofgrey')
def fiftyshadesofgrey():
	return render_template('romance/fiftyshadesofgrey.html'), 200

@app.route('/romance/grease')
def grease():
	return render_template('romance/grease.html'), 200

@app.route('/romance/overboard')
def overboard():
	return render_template('romance/overboard.html'), 200



@app.route('/action')
def action():
	return render_template('action.html'), 200

#action films

@app.route('/action/georgeofthejungle')
def georgeofthejungle():
	return render_template('action/georgeofthejungle.html'), 200

@app.route('/action/mrright')
def mrright():
	return render_template('action/mrright.html'), 200

@app.route('/action/firstblood')
def firstblood():
	return render_template('action/firstblood.html'), 200

@app.route('/action/rambo2')
def rambo2():
	return render_template('action/rambo2.html'), 200

@app.route('/action/rambo3')
def rambo3():
	return render_template('action/rambo3.html'), 200

@app.route('/action/rambo4')
def rambo4():
	return render_template('action/rambo4.html'), 200

@app.route('/action/theavengers')
def theavengers():
	return render_template('action/theavengers.html'), 200

@app.route('/action/theavengers2')
def theavengers2():
	return render_template('action/theavengers2.html'), 200

@app.route('/action/theavengers3')
def theavengers3():
	return render_template('action/theavengers3.html'), 200


@app.route('/animation')
def animation():
	return render_template('animation.html'), 200

#animation movies

@app.route('/animation/theincredibles')
def theincredibles():
	return render_template('animation/theincredibles.html'), 200

@app.route('/animation/theincredibles2')
def theincredibles2():
	return render_template('animation/theincredibles2.html'), 200

@app.route('/animation/coco')
def coco():
	return render_template('animation/coco.html'), 200

@app.route('/animation/ralphbreakstheinternet')
def ralphbreakstheinternet():
	return render_template('animation/ralphbreakstheinternet.html'), 200

@app.route('/animation/thegrinch')
def thegrinch():
	return render_template('animation/thegrinch.html'), 200

@app.route('/animation/moana')
def moana():
	return render_template('animation/moana.html'), 200

@app.route('/animation/lionking')
def lionking():
	return render_template('animation/lionking.html'), 200

@app.route('/animation/lionking2')
def lionking2():
	return render_template('animation/lionking2.html'), 200

@app.route('/animation/agoofymovie')
def agoofymovie():
	return render_template('animation/agoofymovie.html'), 200






if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)