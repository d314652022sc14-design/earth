import requests
import json
from datetime import datetime

# 目標衛星：福衛七號系列 + 獵風者 + 福衛八號
target_ids = ['28254', '29047', '29048' , '29049', '29050', '29051', '29052', '42920', '44343', '44349', '44350', '44351', '44353', '44358', '58017', '60535', '66666', '66766', '68474']
results = []

print(f"[{datetime.now()}] 🤖 開始向 Celestrak 請求最新資料...")

for norad_id in target_ids:
    url = f"https://celestrak.org/NORAD/elements/gp.php?CATNR={norad_id}&FORMAT=TLE"
    try:
        # 設定 10 秒 timeout 避免卡死
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            results.append(response.text)
            print(f"✅ 成功獲取 ID: {norad_id}")
        else:
            print(f"❌ 獲取失敗 ID: {norad_id}, HTTP 狀態碼: {response.status_code}")
    except Exception as e:
        print(f"⚠️ 發生連線錯誤 ID: {norad_id}, 錯誤訊息: {e}")

# 將抓到的陣列儲存成純文字的 JSON 檔
with open('satellites.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("🎉 資料抓取完畢，已成功覆蓋 satellites.json！")
