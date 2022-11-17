from random import randint

# problems
problems = ['KSPO', 'ETCJ', 'QRTZ', 'CPSK',
            'HLUO', 'BEDV', 'DFOP', 'BHJK', 'RFID', 'LXAI']

# after you can decrypt text
challenge = ["ให้สมาชิกทุกคนทำท่าดอกไม้", "ถ่ายเซลฟี่กลุ่มให้เห็นทุกคน", "ยืนทำท่าตามตัวอักษรที่ได้รับ", "สมาชิกทุกคนทำรูปดาว", "ให้ทุกคนพูดชื่ออาหาร 1 อย่าง",
             "ปรบมือพร้อมกันเป็นจังหวะ\n1 2 1 2 3 1 2 1 2 1 เฮ่!", "ทำท่ารวมพลังแล้วร้องเฮ่ดังๆ", "หมุนรอบตัวแล้วพูดชื่อกลุ่มพร้อมกัน", "ต่อตัวกันเป็นรูปหัวใจ",
             "ให้ทุกคนพูดชื่อศิลปิน\nที่ชอบ 1 คน/วง", "ทำท่า wakanda forever"]


def get_challenge():
    # random challenge
    return challenge[randint(0, len(challenge)-1)]
