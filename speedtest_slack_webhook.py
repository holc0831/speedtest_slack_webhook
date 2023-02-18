from slack_sdk.webhook import WebhookClient
import speedtest
import time

url = "https://hooks.slack.com/"
webhook = WebhookClient(url)
server=[]
threads=60

def sptest():
    
    st=speedtest.Speedtest()
    st.get_servers()
    st.get_best_server()
    downlink=st.download(threads=threads) * 1e-6
    uplink=st.upload(threads=threads,pre_allocate=True) * 1e-6
    latency= st.results.ping
    return round(downlink,2), round(uplink,2), round(latency,2)

while True:
    print("start test")
    result=sptest()
    payload="Production: "+"DL"+str(result[0])+", UL"+str(result[1])+", PING"+str(result[2])
    response = webhook.send(text=payload)
    assert response.status_code == 200
    assert response.body == "ok"
    time.sleep(3600)
