import time

print("⏳ Countdown Timer (HH:MM:SS)")

# Kullanıcıdan süreyi dakika cinsinden alıyoruz
minutes = int(input("Enter the countdown time in minutes: "))

# Dakikayı saniyeye çeviriyoruz
total_seconds = minutes * 60

while total_seconds > 0:
    hours, remainder = divmod(total_seconds, 3600)  # Saat hesapla
    mins, secs = divmod(remainder, 60)  # Dakika ve saniye hesapla
    timer = f"{hours:02d}:{mins:02d}:{secs:02d}"
    print(timer, end="\r")  # Aynı satırda güncelle
    time.sleep(1)  # 1 saniye bekle
    total_seconds -= 1

print("⏰ Time's up!")
