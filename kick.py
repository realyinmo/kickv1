from kickpy import *
from time import sleep
from datetime import datetime, timedelta
import time, asyncio, json, os, sys, traceback
cl = LINE()
print("登入成功")
oepoll = OEPoll(cl)
clID = cl.getProfile().mid
Me = ["ufe1707ae9b2ff7ab61505795b7995440"] #權限者
def bot(op):
     try:
         if op.type == 0:
            print("操作結束")
            return
         if op.type == 13:
             cl.acceptGroupInvitation(op.param1)
             try:
                 G = cl.getGroup(op.param1)
                 targets = []
                 time.sleep(0.0001)
                 for member in G.members + G.invitee:
                      targets.append(member.mid)
                 for target in targets:
                     if target not in Me:
                       try:
    	                   cl.kickoutFromGroup(op.param1, [target])
                       except:
                           pass
                       try:
                           cl.cancelGroupInvitation(op.param1, [target])
                       except:
                           pass
             except:
             	pass
     except Exception as e:
        cl.log("Error : " + str(e))
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops:
          bot(op)
          oepoll.setRevision(op.revision)
    except Exception as e:
        cl.log("Error : " + str(e))
