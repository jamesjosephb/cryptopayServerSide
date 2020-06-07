#!flask/bin/python
from flask import Flask
from flask import Flask, jsonify, request, render_template, json

from QueryFunctions import *

app = Flask(__name__)


@app.route('/')
def index():
    return "You Got Here!"






#Example: http://127.0.0.1:5000/sites?id=8
@app.route('/sites', methods=['GET'])
def id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    return jsonify(sitesByOwnerID(id))


'''@app.route('/swipersconfig', methods=['POST'])
def swipersconfig():
    print("Hello, World!")
    #return json.dumps(request .json)
    #return jsonify(swiperconfigBySiteIDMAC(SiteID, MacAddress))'''

'''curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/swipersconfig -d '{"message":"Hello Data"}'''


@app.route('/login=<UserName>', methods=['GET'])
def login(UserName):
    SitesArray = []
    OwnerID = ownerIDByUserName(UserName)
    OwnersSiteIDs = sitesByOwnerID(OwnerID)
    LoginDict = {"OwnerID" : ownerIDByUserName(UserName)}
    for MPM in OwnersSiteIDs:
        #MPMArrayofDicts = []
        #MPMArrayofDicts = (CordinatorStatusbySiteID(MPM)) + (SiteInfobySiteID(MPM))
        #MPMArrayofDicts.append({"Swipers": swipersBySiteID(MPM)})
        #MPMArrayofDicts.append(CordinatorStatusbySiteID(MPM))
        #MPMArrayofDicts.append(SiteInfobySiteID(MPM))
        SitesArray.append({**(CordinatorStatusbySiteID(MPM)), **(SiteInfobySiteID(MPM)), **{"Swipers": swipersBySiteID(MPM)}, **{"siteID" : MPM}})
    LoginDict["SiteArray"] = SitesArray
    return jsonify(LoginDict)

@app.route('/swipersstatus=<SiteID>', methods=['GET'])
def swipersstatus(SiteID):
    Swipers = {"Swipers" : swipersBySiteID(SiteID)}
    return jsonify(Swipers)

@app.route('/swipersconfig/site=<SiteID>/swiper=<MacAddress>', methods=['GET'])
def swipersconfig(SiteID,MacAddress):
    return jsonify(swiperconfigBySiteIDMAC(SiteID, MacAddress))

@app.route('/purchases=<SiteID>', methods=['GET'])
def purchases(SiteID):
    purchases = {"purchases" : purchasebySiteID(SiteID)}
    return jsonify(purchases)

@app.route('/coordinatorstatus=<SiteID>', methods=['GET'])
def coordinatorstatus(SiteID):
    return jsonify(CordinatorStatusbySiteID(SiteID))

@app.route('/alarmcontacts=<SiteID>', methods=['GET'])
def alarmcontacts(SiteID):
    return jsonify(AlarmContactsbySiteID(SiteID))

@app.route('/transaction=<purchID>', methods=['GET'])
def transaction(purchID):
    transaction = {"transactions" : transactionsbypurchaseid(purchID)}
    return jsonify(transaction)


@app.route('/siteinfo=<siteID>', methods=['GET'])
def siteinfo(siteID):
    return jsonify(SiteInfobySiteID(siteID))

if __name__ == '__main__':
    #app.run(debug=True) #Test Locally
    app.run(host='0.0.0.0') # Run but don't leave on becasue it is not secure
