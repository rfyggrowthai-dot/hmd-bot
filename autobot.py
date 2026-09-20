import requests, time, os
ADDRESS="TRchgE6LAnNawY8NcdSESWeh9EkxxKARZ6"
TOKEN=os.environ.get("BOT_TOKEN")
API=f"https://api.telegram.org/bot{TOKEN}"
offset=0
while True:
 try:
  r=requests.get(f"{API}/getUpdates", params={"offset":offset,"timeout":30}, timeout=40).json()
  for u in r.get("result",[]):
   offset=u["update_id"]+1
   m=u.get("message",{}); cid=m.get("chat",{}).get("id"); t=m.get("text","")
   if t and t.startswith("/start"):
    requests.get(f"{API}/sendMessage", params={"chat_id":cid,"text":f"Pay 200 USDT TRC20 to:\n{ADDRESS}"})
 except: time.sleep(5)
