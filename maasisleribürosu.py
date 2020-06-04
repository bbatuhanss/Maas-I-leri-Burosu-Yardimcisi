# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:25:22 2020

@author: Batuhan Sevinç
"""

tum_calısan_net_ucrt_top=tüm_calısan_top_vergi=tum_clsn_top_brt_ucr=top_calısan_say=ikibin_alti_ucrt_say=0
top_banknot_200=top_banknot_100=top_banknot_50=top_banknot_20=top_banknot_10=top_banknot_5=0
top_madeni_para_1=top_madeni_para_050=top_madeni_para_025=top_madeni_para_010=top_madeni_para_005=top_madeni_para_001=0
ver_oran_cal_say1=ver_oran_cal_say2=ver_oran_cal_say3=ver_oran_cal_say4=0
ver_oran_cal_oran1=ver_oran_cal_oran2=ver_oran_cal_oran3=ver_oran_cal_oran4=0
max_top_btür_uct=max_top_btür_uct_vergi=max_top_btür_uct_net_ucr=0
max_net_uct=max_net_uct_vergi=max_net_uct_top_brut_uct=0
tum_cal_bekar_say=tum_cal_evli_say= tum_cal_bekar_yuzde=tum_cal_evli_yuzde=esli_cal_say=esli_cal_yüzde=0
bakmakla_yük_çocuk_say_top=cocuk_bakmakla_yük_calısan=bakmakla_yük_çocuk_say_ort=0
ucten_fazla_cocuga_sahip_calısan=engeli_cal_say=engelli_cal_yüzde=vergi= engel_derecesi=0
devam="e"
while devam=="e" or devam=="E": #kullanıcıya başka çalışan var mı yok mu diye sorması için döngü kullanıldı.
    cocuk_say=ek_ücret =engelli_oranı= aylik_ücret=0

    tc_no=input("Çalışanın TC kimlik numarasını giriniz: ")
    while len(tc_no)!=11: #T.C no 11 haneli değilse bir daha T.C no sorması için döngü yapıldı.
        tc_no =input("Çalışanın TC kimlik numarasını giriniz: ")

    ad_soyad=input("Çalışanın adını ve soyadını giriniz:")

    aylik_brüt_ücr=float(input("Aylık brüt ücreti giriniz(TL):"))
    while aylik_brüt_ücr<1777.50: #Aylık brüt ücret 1777.50 tl'nin altında girildiğinde tekrardan brüt ücreti sorması için while kontrolü yapıldı.
        aylik_brüt_ücr = float(input("Aylık brüt ücreti giriniz(TL):"))

    medeni_durum=input("Çalışanın medeni durumunu giriniz evli(e/E),bekar(b/B):")
    while medeni_durum not in ["e","E","b","B"]: #medeni durum e,E,h,H dışında olursa döngü yine medeni durumu soracak.
        medeni_durum = input("Hatalı girdiniz!Çalışanın medeni durumunu tekrar giriniz evli(e/E),bekar(b/B):")

    if medeni_durum=="e" or medeni_durum=="E": #Eğer medeni durum e,E olursa yani medeni durum evli olursa.
        tum_cal_evli_say += 1
        esli_cal_yüzde = (esli_cal_say * 100) / tum_cal_evli_say #Evli olan çalışanların içinde, eşleri de çalışanların yüzdesi
        es_calısması=input("Çalışanın eşinin çalışıp çalışmadığı  evet(e/E), hayır(h/H) giriniz::")
        while es_calısması not in ["e","E","h","H"]: #Eş çalışması e,E,h,H dışında olursa döngü eş çalısmasını tekrardan soracak.
            es_calısması = input("Hatalı girdiniz!Çalışanın eşinin çalışıp çalışmadığı tekrar giriniz (evet(e/E), hayır(h/H)):")
        if es_calısması=="h" or es_calısması=="H": #Eşi çalışmadığı durumlar için if kullanıldı.
            ek_ücret+=220
        else: #Eşi çalıştığı durumlar için else kullanıldı.
            aylik_brüt_ücr=aylik_brüt_ücr
            esli_cal_say += 1
    else:#Medeni durum bekar olduğunda
        tum_cal_bekar_say += 1

    bakmakla_yük_çocuk_say=int(input("Çalışanın bakmakla yükümlü olduğu çocuk sayısını giriniz:"))
    while bakmakla_yük_çocuk_say<0: #Eğer bakmakla yükümlü çocuk sayısı sıfır altında olursa...Döngü, çocuk sayısının yeniden girilmesini sağlıyor.
        print("Geçesiz sayı!")
        bakmakla_yük_çocuk_say = int(input("Çalışanın bakmakla yükümlü olduğu çocuk sayısını giriniz:"))
    if bakmakla_yük_çocuk_say>0:#Çalşanın bakmakla yükümlü çocuğu olduğu durumlar için if kullanıldı.
        bakmakla_yük_çocuk_say_top+=bakmakla_yük_çocuk_say
        cocuk_bakmakla_yük_calısan+=1
        #Sadece bakmakla yükümlü çocuğu olanlar dikkate alınarak, çalışanların bakmakla yükümlü oldukları çocuk sayısının ortalaması
        bakmakla_yük_çocuk_say_ort = bakmakla_yük_çocuk_say_top / cocuk_bakmakla_yük_calısan

        altı_yas_üstü=int(input("yaşı 6’dan büyük olanların sayısını giriniz:"))
        while altı_yas_üstü<0 or altı_yas_üstü>bakmakla_yük_çocuk_say:#Eğer altı yaşında olan çocuk sayısı sıfırdan az veya bakmakla yükümlü çocuk sayısından fazla ise döngü yeniden altı yas üstü cocuk sayısını istiyor.
            altı_yas_üstü = int(input("Hatalı girdiniz lütfen bir daha giriniz:"))
        cocuk_say+=altı_yas_üstü*45
        cocuk_say+=(bakmakla_yük_çocuk_say-altı_yas_üstü)*25
    engelli_hali=input("Çalışanın Engelli olup olmadığı giriniz evet(e/E), hayır(h/H):)")
    aylik_toplam_brüt_ücr=aylik_brüt_ücr+ek_ücret+cocuk_say
    brüt_vergi=aylik_toplam_brüt_ücr

    while  engelli_hali not in ["e","E","h","H"]: #Engelli  hali e,E,h,H dışında olursa döngü engelli halini tehrardan soracak.
        engelli_hali = input("Hatalı giriş!Çalışanın Engelli olup olmadığı tekrar giriniz evet(e/E), hayır(h/H):")

    if engelli_hali=="e" or engelli_hali=="E":#Çalışan engelli olduğunda.
        engeli_cal_say+=1 #Engelli çalışanların sayısını bulmak için atanan değişken
        engelli_oranı=float(input("engellilik oranını giriniz(1-100) arası:"))

        while engelli_oranı<1 and engelli_oranı>100: #Engelli oranı 1 den küçük ve 100 den büyük ise döngü tekrardan engelli oranını soruyor.
            engelli_oranı = float(input("Hatalı girdiniz!Engellilik oranını (1-100) arası bir daha giriniz:"))
       #Engelli oranına göre brüt ücretten muaf tutulacak miktarlar.

        if engelli_oranı >= 80:
            brüt_vergi-=900
            engel_derecesi=1
        elif engelli_oranı >= 60:
            brüt_vergi-=470
            engel_derecesi=2
        elif engelli_oranı >= 40:
            brüt_vergi-=210
            engel_derecesi=3
    #Aylık toplam brüt ücretinin miktarına göre vergi kesintisi.
    if aylik_toplam_brüt_ücr < 2000:
        vergi = brüt_vergi * 0.15
        ver_oran_cal_say1+=1
    elif aylik_toplam_brüt_ücr < 5000:
        vergi = brüt_vergi * 0.20
        ver_oran_cal_say2+=1
    elif aylik_toplam_brüt_ücr < 10000:
        vergi = brüt_vergi * 0.27
        ver_oran_cal_say3+=1
    else:
        vergi = brüt_vergi * 0.35
        ver_oran_cal_say4+=1

    net_ücret=aylik_toplam_brüt_ücr-vergi

   #Banknot hesaplamaları.

    banknot_200 = net_ücret//200
    kalan = net_ücret % 200
    kalan = round(kalan, 2)
    banknot_100 = kalan//100
    kalan %= 100
    kalan = round(kalan, 2)
    banknot_50 = kalan//50
    kalan %= 50
    kalan = round(kalan, 2)
    banknot_20 = kalan//20
    kalan %= 20
    kalan = round(kalan, 2)
    banknot_10 = kalan//10
    kalan %= 10
    kalan = round(kalan, 2)
    banknot_5 = kalan//5
    kalan %= 5
    kalan = round(kalan, 2)
    madeni_para_1 = kalan//1
    kalan %= 1
    kalan = round(kalan, 2)
    madeni_para_050 = kalan//0.5
    kalan %= 0.5
    kalan = round(kalan, 2)
    madeni_para_025 = kalan//0.25
    kalan %= 0.25
    kalan=round(kalan,2)
    madeni_para_010 = kalan//0.1
    kalan %= 0.1
    kalan = round(kalan, 2)
    madeni_para_005 = kalan//0.05
    kalan %= 0.05
    kalan = round(kalan, 2)
    madeni_para_001 = kalan//0.01

   #Her çalışan için yazdırılacak değerler.
    print("Bu çalışanın kimlik numarası:", tc_no,"ve","adı soyadı:",ad_soyad)
    print("Aylik brüt ücreti:",format(aylik_brüt_ücr,".2f"),"TL")
    print("Eş için aile yardımı ödeneği:",format(ek_ücret,".2f"),"TL")
    print("Çocuk için aile yardımı ödeneği:",format(cocuk_say,".2f"),"TL")
    print("Aylık toplam brüt ücreti:",format(aylik_toplam_brüt_ücr,".2f"),"TL")
    print("Gelir vergisi kesintisi:",format(vergi,".2f"),"TL")
    #Engelli derecesi olmadığı durumlarda engelli derecesini yazdırmamak için if kullanıldı.
    if engelli_oranı>=40:
        print("Engel derecesi :",engel_derecesi)
    print("Aylık net ücret:",format(net_ücret,".2f"),"TL")
    print("Aylık net ücretin ödenebilmesi için tedavüldeki her para türünden gereken adet sayısı;")
    #Banknot ve madeni para çeşitlerinden olmayanların yazdırılmaması için ifler kullanıldı.
    if banknot_200>0:
        print("200 tl bankot:", format(banknot_200,".0f")," adet")
    if banknot_100>0:
        print("100 tl bankot:", format(banknot_100,".0f")," adet")
    if banknot_50>0:
        print("50 tl bankot:", format(banknot_50,".0f")," adet")
    if banknot_20>0:
        print("20 tl bankot:", format(banknot_20,".0f")," adet")
    if banknot_10>0:
        print("10 tl bankot:", format(banknot_10,".0f")," adet")
    if banknot_5>0:
        print("5 tl bankot:", format(banknot_5,".0f")," adet")
    if madeni_para_1>0:
        print("1 tl bankot:", format(madeni_para_1,".0f")," adet")
    if madeni_para_050>0:
        print("50 kuruş :", format(madeni_para_050,".0f")," adet")
    if madeni_para_025>0:
        print("25 kuruş :", format(madeni_para_025,".0f")," adet")
    if madeni_para_010>0:
        print("10 kuruş :", format(madeni_para_010,".0f")," adet")
    if madeni_para_005>0:
        print("5 kuruş :", format(madeni_para_005,".0f")," adet")
    if madeni_para_001>0:
        print("1 kuruş :", format(madeni_para_001,".0f")," adet")
    devam=input("Başka çalışan var mı?")

    top_calısan_say += 1
    tum_calısan_net_ucrt_top += net_ücret  #Tüm çalışanlara bir ayda ödenen aylık toplam net ücret değişeni
    tüm_calısan_top_vergi += vergi #devlete aktarılan aylık toplam gelir vergisi değişkeni
    tum_clsn_top_brt_ucr += aylik_toplam_brüt_ücr #Tüm çalışanların aylık toplam brüt ücretleri değişkeni
    brut_ort = tum_clsn_top_brt_ucr / top_calısan_say #Tüm çalışanların aylık toplam brüt ücretlerinin ortalaması değişkeni
    net_ucrt_ort = tum_calısan_net_ucrt_top / top_calısan_say #Tüm çalışanların net ücretlerinin ortalaması değişkeni
#Çalışanlara aylık net ücretlerinin en az sayıda banknot ve madeni para kullanılarak ödenebilmesi için yapılan işlemler.
    top_banknot_200+=banknot_200
    top_banknot_100+=banknot_100
    top_banknot_50+=banknot_50
    top_banknot_20+=banknot_20
    top_banknot_10+=banknot_10
    top_banknot_5+=banknot_5
    top_madeni_para_1+=madeni_para_1
    top_madeni_para_050+=madeni_para_050
    top_madeni_para_025+=madeni_para_025
    top_madeni_para_010+=madeni_para_010
    top_madeni_para_005+=madeni_para_005
    top_madeni_para_001+=madeni_para_001
    # 2000 TL’nin altında aylık net ücret alan çalışanların sayısı bulmak için yapılan if ve işlemler
    if net_ücret<2000:
        ikibin_alti_ucrt_say+=1
    #Her gelir vergisi oranı için ayrı ayrı çalışan sayı ve yüzdeleri bulmak için yapılan işlemler
    ver_oran_cal_oran1 = (ver_oran_cal_say1 * 100) / top_calısan_say
    ver_oran_cal_oran2=(ver_oran_cal_say2*100)/top_calısan_say
    ver_oran_cal_oran3=(ver_oran_cal_say3*100)/top_calısan_say
    ver_oran_cal_oran4=(ver_oran_cal_say4*100)/top_calısan_say
    #Aylık toplam brüt ücreti en yüksek olan çalışanın TC kimlik numarası, adı soyadı, aylık toplam brüt ücreti, gelir vergisi kesintisi ve aylık net ücreti bulmak için yapılan işlemler
    if aylik_toplam_brüt_ücr > max_top_btür_uct:
        max_top_btür_uct = aylik_toplam_brüt_ücr
        max_top_btür_uct_tc = tc_no
        max_top_btür_uct_ad = ad_soyad
        max_top_btür_uct_vergi = vergi
        max_top_btür_uct_net_ucr = net_ücret
    #Aylık net ücreti en yüksek olan çalışanın TC kimlik numarası, adı soyadı, aylık toplam brüt ücreti, gelir vergisi kesintisi ve aylık net ücreti  bulmak için yapılan işlemler
    if net_ücret>max_net_uct:
        max_net_uct=net_ücret
        max_net_uct_tc=tc_no
        max_net_uct_ad=ad_soyad
        max_net_uct_vergi=vergi
        max_net_uct_top_brut_uct=aylik_toplam_brüt_ücr

    if bakmakla_yük_çocuk_say>3: #Bakmakla yükümlü olduğu çocuk sayısı 3’ten fazla olan çalışanların sayısı
        ucten_fazla_cocuga_sahip_calısan+=1
    # Tüm çalışanlar içindeki bekar olanların yüzdesini bulmak için yapılan işlemler
    tum_cal_bekar_yuzde=(tum_cal_bekar_say*100)/top_calısan_say
    # Tüm çalışanlar içindeki evli olanların yüzdesini bulmak için yapılan işlemler
    tum_cal_evli_yuzde=(tum_cal_evli_say*100)/top_calısan_say
    #Engelli çalışanların  tüm çalışanlar içindeki yüzdesi
    engelli_cal_yüzde = (engeli_cal_say * 100) / top_calısan_say
print("Tüm çalışanların bir ayda ödenen aylık  toplam net ücret tutarı:",format(tum_calısan_net_ucrt_top,".2f"),"TL","ve",
      "devlete aktarılan aylık toplam gelir vergisi tutarı:",format(tüm_calısan_top_vergi,".2f"),"TL")
print("Tüm çalışanların aylık toplam brüt ücretlerinin ortalaması:",format(brut_ort,".2f"),"TL",
      "ve net ücretlerinin ortalaması:",format(net_ucrt_ort,".2f"),"TL")
print("Aylık net ücretin ödenebilmesi için tedavüldeki her para türünden toplam gereken adet sayısı;")
print("         Toplam Banknotlar                                   Toplam Madeni Paralar")
print("200 TL:",format(top_banknot_200,".0f")," adet","                                        ","1 Tl:    ",format(top_madeni_para_1,".0f")," adet")
print("100 TL:",format(top_banknot_100,".0f")," adet","                                        ","50 Kuruş:",format(top_madeni_para_050,".0f")," adet")
print("50  TL:",format(top_banknot_50,".0f")," adet","                                        ","25  Kuruş:",format(top_madeni_para_025,".0f")," adet")
print("20  TL:",format(top_banknot_20,".0f")," adet","                                        ","10  Kuruş:",format(top_madeni_para_010,".0f")," adet")
print("10  TL:",format(top_banknot_10,".0f")," adet","                                        ","5   Kuruş:",format(top_madeni_para_005,".0f")," adet")
print("5   TL:",format(top_banknot_5,".0f")," adet","                                         ","1   Kuruş:",format(top_madeni_para_001,".0f")," adet")
print("2000 TL’nin altında aylık net ücret alan çalışanların sayısı:",ikibin_alti_ucrt_say)
print("Vergi Oranı                Gelir vergisi oranı olanların sayısı             Yüzdesi ")
print("   %15                         ",ver_oran_cal_say1,"                                       %",format(ver_oran_cal_oran1,".2f"))
print("   %20                         ",ver_oran_cal_say2,"                                       %",format(ver_oran_cal_oran2,".2f"))
print("   %27                         ",ver_oran_cal_say3,"                                       %",format(ver_oran_cal_oran3,".2f"))
print("   %35                         ",ver_oran_cal_say4,"                                       %",format(ver_oran_cal_oran4,".2f"))
print("Aylık toplam brüt ücreti en yüksek olan çalışanın;")
print("TC kimlik numarası:",max_top_btür_uct_tc)
print("Adı soyadı:",max_top_btür_uct_ad)
print("Aylık toplam brüt ücreti:",format(max_top_btür_uct,".2f"),"TL")
print("Gelir vergisi kesintisi:",format(max_top_btür_uct_vergi,".2f"),"TL")
print("Aylık net ücreti:",format( max_top_btür_uct_net_ucr,".2f"),"TL")
print("Aylık net ücreti en yüksek olan çalışanın;")
print("TC kimlik numarası:",max_net_uct_tc)
print("Adı soyadı:", max_net_uct_ad)
print("Aylık toplam brüt ücreti:",format(max_net_uct_top_brut_uct,".2f"),"TL")
print("Gelir vergisi kesintisi:",format(max_net_uct_vergi,".2f"),"TL")
print("Aylık net ücreti:",format(max_net_uct,".2f"),"TL")
