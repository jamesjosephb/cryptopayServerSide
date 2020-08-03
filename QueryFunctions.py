from DataBaseModel import *
import datetime


def swipersBySiteID(siteID):
    session = Session()
    listOfSwipers = []
    for instance in session.query(Swiper). \
            filter(Swiper.siteid == siteID):
        # print(instance.name)
        DictOfSwiper = {}
        DictOfSwiper["name"] = instance.name
        #DictOfSwiper["purchtype"] = instance.purchtype
        DictOfSwiper["macaddr"] = instance.macaddr
        DictOfSwiper["lastcontact"] = instance.lastcontact
        listOfSwipers.append(DictOfSwiper)
    if len(listOfSwipers) == 0:
        return None
    else:
        return listOfSwipers


def swipersBySiteID(siteID):
    session = Session()
    listOfSwipers = []
    for instance in session.query(Swiper). \
            filter(Swiper.siteid == siteID):
        # print(instance.name)
        DictOfSwiper = {}
        DictOfSwiper["name"] = instance.name
        # DictOfSwiper["purchtype"] = instance.purchtype
        DictOfSwiper["macaddr"] = instance.macaddr
        DictOfSwiper["lastcontact"] = instance.lastcontact
        #DictOfSwiper["SwiperName"] = instance.name
        DictOfSwiper["SwiperProfile"] = "Out of Service"
        DictOfSwiper["PrchTyp"] = "None"
        DictOfSwiper["Rate"] = 60
        DictOfSwiper["MinCh"] = 100
        DictOfSwiper["MaxCh"] = 1500
        DictOfSwiper["Amex"] = "No"
        DictOfSwiper["BnsCoin"] = 0
        for secondInstance in session.query(SwiperConfig). \
            filter(SwiperConfig.SiteID == siteID and SwiperConfig.Swiper_MAC_address == instance.macaddr):
            if instance.macaddr == secondInstance.Swiper_MAC_address:
                print(instance.macaddr)
                #DictOfSwiper["SwiperName"] = secondInstance.SwiperName
                DictOfSwiper["SwiperProfile"] = secondInstance.SwiperProfile
                DictOfSwiper["PrchTyp"] = secondInstance.PrchTyp
                DictOfSwiper["Rate"] = secondInstance.Rate
                DictOfSwiper["MinCh"] = secondInstance.MinCh
                DictOfSwiper["MaxCh"] = secondInstance.MaxCh
                DictOfSwiper["Amex"] = secondInstance.Amex
                DictOfSwiper["BnsCoin"] = secondInstance.BnsCoin
                break
        listOfSwipers.append(DictOfSwiper)
    if len(listOfSwipers) == 0:
        return None
    else:
        return listOfSwipers


def swiperconfigBySiteIDMAC(siteID, swiperMAC):
    session = Session()
    for instance in session.query(SwiperConfig). \
            filter(SwiperConfig.SiteID == siteID and SwiperConfig.Swiper_MAC_address == swiperMAC):
        DictOfSwiper = {}
        DictOfSwiper["SwiperName"] = instance.SwiperName
        DictOfSwiper["SwiperProfile"] = instance.SwiperProfile
        DictOfSwiper["PrchTyp"] = instance.PrchTyp
        DictOfSwiper["Rate"] = instance.Rate
        DictOfSwiper["MinCh"] = instance.MinCh
        DictOfSwiper["MaxCh"] = instance.MaxCh
        DictOfSwiper["Amex"] = instance.Amex
        DictOfSwiper["BnsCoin"] = instance.BnsCoin
        return DictOfSwiper


def AlarmContactsbySiteID(siteID):
    session = Session()
    for instance in session.query(Alarm). \
            filter(Alarm.siteid == siteID):
        DictofAlarmContacts = {}
        DictofAlarmContacts["email1"] = instance.email1
        DictofAlarmContacts["email2"] = instance.email2
        DictofAlarmContacts["email2"] = instance.email2
        return DictofAlarmContacts

def CordinatorStatusbySiteID(siteID):
    session = Session()
    for instance in session.query(Alarm). \
            filter(Alarm.siteid == siteID):
        DictofAlarm = {}
        DictofAlarm["sitedownstat"] = ("Connected" if instance.sitedownstat == 0 else "Not Connected")
        DictofAlarm["sitedowndate"] = instance.sitedowndate
        DictofAlarm["sitepurchstat"] = ("Yes" if instance.sitepurchstat == 0 else "No")
        DictofAlarm["sitepurchemail"] = ("Yes" if instance.sitepurchemail == 0 else "No")
        return DictofAlarm


def purchasebySiteID(siteID):
    session = Session()
    listOfPurchases = []
    # current_time = datetime.datetime.utcnow() Don't use this because the copy of the database end at the beginning of Nov which is over 6 months ago.
    current_time = datetime.datetime(2019,11,3,20,25,0)
    sixMonthsAgo = current_time - datetime.timedelta(weeks=25)
    purchaseQuery = session.query(Purchase).filter(Purchase.siteid == siteID).\
        filter(Purchase.time > sixMonthsAgo).\
        order_by(Purchase.time.desc())
    #listOfPurchaseObjects = purchaseQuery.all()
    #for i in listOfPurchaseObjects:
    for i in purchaseQuery:
        DictOfPurchase = {}
        DictOfPurchase["purchaseid"] = i.purchaseid
        DictOfPurchase["siteid"] = i.siteid
        DictOfPurchase["name"] = i.name
        DictOfPurchase["cpid"] = i.cpid
        if (i.transid != None):
            DictOfPurchase["transid"] = i.transid
        else:
            continue
        DictOfPurchase["time"] = i.time
        DictOfPurchase["totalcharge"] = i.totalcharge
        DictOfPurchase["transidfinal"] = i.transidfinal
        listOfPurchases.append(DictOfPurchase)
    if len(listOfPurchases) == 0:
        return None
    else:
        return listOfPurchases


def transactionsbypurchaseid(purchaseID):
    session = Session()
    listOfTransactions = []
    for instance in session.query(Transaction). \
                            filter(Transaction.purchaseid == purchaseID):
        DictOfTransactions = {}
        DictOfTransactions["purchtype"] = instance.purchtype
        DictOfTransactions["charge"] = instance.charge
        DictOfTransactions["macaddr"] = instance.macaddr
        listOfTransactions.append(DictOfTransactions)
    if len(listOfTransactions) == 0:
        return None
    else:
        return listOfTransactions


def SiteInfobySiteID(SiteID):
    session = Session()
    for instance in session.query(Site). \
                            filter(Site.siteid == SiteID):
        DictOfSite = {}
        DictOfSite["sitename"] = instance.sitename
        DictOfSite["mqxversion"] = instance.mqxversion
        DictOfSite["setupcomplete"] = instance.setupcomplete
        DictOfSite["address1"] = instance.address1
        DictOfSite["city"] = instance.city
        DictOfSite["state"] = instance.state
        DictOfSite["zip"] = instance.zip
        DictOfSite["timezone"] = instance.timezone
        return DictOfSite


def sitesByOwnerID(ownerID):
    session = Session()
    listOfSites = []
    for instance in session.query(Site):
        if instance.owneruserid == ownerID:
            listOfSites.append(instance.siteid)
    if listOfSites == []:
        return None
    return listOfSites


def ownerIDByUserName(userName):
    session = Session()
    for instance in session.query(User):
        if instance.username == userName:
            return instance.userid


if __name__ == '__main__':
    #print(purchasebySiteIDwithTransactions("MPM084938123"))
    #print(sitesByOwnerID(8))
    #print(purchasebySiteID("MPM084938123"))
    #print(swipersBySiteID("MPM084938123"))
    print(transactionsbypurchaseid(71232170))
