from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *




# Modeling types converstion https://code-maven.com/slides/python-programming/sqlalchemy-types
# SQLAlchemy documentaion https://docs.sqlalchemy.org/en/13/orm/tutorial.html#creating-a-session
# connection time out doc https://docs.sqlalchemy.org/en/13/dialects/mysql.html
Base = declarative_base()
OSinstance = "Server" #Mac or Server
if OSinstance == "Server":
    engine = create_engine("config.mysqlLogin")
else:
    engine = create_engine("config.mysqlLogin")
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    userid = Column(Integer, primary_key=True)
    username = Column(String(32))
    email = Column(String(64))
    password = Column(String(32))
    #password2 = Column(String(255))
    #passhashmd5 = Column(Boolean(4))
    #enabled = Column(Boolean(4))
    lastseentime = Column(DateTime())
    joinedtime = Column(DateTime())
    #verificationcode = Column(String(32))
    passresetcode = Column(String(32))
    agreetowarranty = Column(DateTime())
    attendantcardagreement = Column(DateTime())
    #shippingfirstname = Column(String(32))
    #shippinglastname = Column(String(32))
    #shippingcompany = Column(String(64))
    #shippingaddress = Column(String(128))
    #shippingcountry = Column(String(32))
    #shippingcity = Column(String(32))
    #shippingstate = Column(String(String(2)))
    #shippingzipcode = Column(String(10))
    phonenumber = Column(String(32))
    #genesys = Column(Boolean(4))
    customername = Column(String(64))
    #flexibility = Column(Boolean(4))
    #trialflags = Column(Integer())

    '''def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)'''

class Site(Base):
    __tablename__ = 'sites'

    siteid = Column(String(16), primary_key=True)
    owneruserid = Column(Integer(), primary_key=True)
    sitename = Column(String(32))
    oldaddress = Column(String(256))
    timezone = Column(String(32))
    address1 = Column(String(256))
    address2 = Column(String(256))
    city = Column(String(32))
    state = Column(String(32))
    zip = Column(String(8))
    ip = Column(String(16))
    lastip = Column(String(16))
    notes = Column(String(256))
    setupcomplete = Column(Boolean(1))
    nextid = Column(String(16))
    diagnostics = Column(Boolean(1))
    diagnosticslogin = Column(Boolean(1))
    coordlock = Column(Boolean(1))
    swiperlock = Column(Boolean(1))
    reflashlock = Column(Boolean(1))
    mac = Column(String(20))
    holdcharge = Column(Integer())
    merchantpw = Column(String(14))
    serveraddress = Column(String(32))
    storedpurch = Column(Integer())
    youngestblock = Column(Integer())
    mqxversion = Column(String(16))
    zbcversion = Column(String(16))
    swversion = Column(String(16))
    crccarddb = Column(String(20))
    crccarddbcmd = Column(String(20))
    sitetype = Column(Integer())
    flcardver = Column(Boolean())
    server = Column(String(20))

class Swiper(Base):
    __tablename__ = 'swipers'
    siteid = Column(String(16), primary_key=True)
    uniqueid = Column(Integer())
    name = Column(String(8))
    purchtype = Column(Integer())
    macaddr = Column(String(16), primary_key=True)
    csumstate = Column(Integer())
    lastcontact = Column(DateTime())
    coincount = Column(Integer())
    coinval = Column(Integer())
    lastcollectioncoinid = Column(Integer())
    lastcollectiontime = Column(DateTime())
    lastchecked = Column(DateTime())
    lastnotified = Column(DateTime())
    notificationlimit = Column(Integer())
    machinecapacity = Column(String(24))

class SwiperConfig(Base):
    __tablename__ = 'SwiperConfigs'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    SiteID = Column(String(12))
    Version = Column(Integer)
    Swiper_MAC_address = Column(String(16))
    SwiperProfile = Column(String(12))
    MinCh = Column(Integer)
    MaxCh = Column(Integer)
    CoinVal = Column(Integer)
    Rate = Column(Integer)
    BnsCoin = Column(Integer)
    SigType = Column(String(8))
    Cancel = Column(String(3))
    Amex = Column(String(3))
    MustApp = Column(String(3))
    Fleet = Column(String(3))
    Debug = Column(String(3))
    BtnAdd = Column(String(3))
    AppDly = Column(Integer)
    PrchTyp = Column(String(10))
    SwiperName = Column(String(8))
    CoinTim = Column(Integer)
    ICTime = Column(Integer)
    AppTime = Column(Integer)
    BnsMode = Column(String(10))
    BnsCnt = Column(Integer)
    BnsTime = Column(Integer)
    PrchLim = Column(Integer)

class Alarm(Base):
    __tablename__ = 'alarms'
    siteid =Column(String(12), primary_key=True)
    carwashname =Column(String(32))
    sitedownenable =Column(Integer)
    sitedownstat =Column(Integer)
    sitedownemail =Column(Integer)
    sitedowndate = Column(DateTime())
    sitepurchenable =Column(Integer)
    sitepurchstat =Column(Integer)
    sitepurchemail =Column(Integer)
    email1 =Column(String(255))
    email2 =Column(String(255))
    email3 =Column(String(255))

class Purchase(Base):
    __tablename__ = 'purchases'
    purchaseid = Column(Integer(), primary_key=True)
    siteid = Column(String(16))
    name = Column(String(16))
    cpid = Column(Integer())
    transid = Column(String(16))
    authcode = Column(String(8))
    cardtype = Column(Integer())
    time = Column(DateTime())
    totalcharge = Column(Integer())
    cardnumber = Column(Integer())
    fleetinvoiceid = Column(Integer())
    genesysinvoiceid = Column(Integer())
    cardaccountid = Column(Integer())
    transidfinal = Column(String(20))

class Transaction(Base):
    __tablename__ = 'transactions'
    transactionid = Column(Integer(), primary_key=True)
    purchaseid = Column(Integer())
    saleid = Column(Integer())
    swiperid = Column(Integer())
    charge = Column(Integer())
    purchtype = Column(Integer())
    modpurchtype = Column(Integer())
    macaddr = Column(String(16))



if __name__ == '__main__':

    def SwipersbySiteID(siteID):
        session = Session()
        listOfSwipers = []
        for instance in session.query(SwiperConfig).\
                filter(SwiperConfig.SiteID == siteID):
            DictOfSwiperConfig = {}
            DictOfSwiperConfig["Swiper_MAC_address"] = instance.Swiper_MAC_address
            DictOfSwiperConfig["SwiperName"] = instance.SwiperName
            DictOfSwiperConfig["SwiperProfile"] = instance.SwiperProfile
            DictOfSwiperConfig["Rate"] = instance.Rate
            DictOfSwiperConfig["MinCh"] = instance.MinCh
            DictOfSwiperConfig["MaxCh"] = instance.MaxCh
            DictOfSwiperConfig["Amex"] = instance.Amex
            DictOfSwiperConfig["BtnAdd"] = instance.BtnAdd
            listOfSwipers.append(DictOfSwiperConfig)
        if len(listOfSwipers) == 0:
            return None
        else:
            return listOfSwipers


    list = SwipersbySiteID('MPM540873054')

    for i in (list):
        print(i)




