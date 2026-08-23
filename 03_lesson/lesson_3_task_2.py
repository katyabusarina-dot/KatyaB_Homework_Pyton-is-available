from smartphone import Smartphone

Catalog = [
    Smartphone(marka="Apple", model="iPhone 17 Pro Max",
               phone_number="+79116754329"),
    Smartphone(marka="Samsung", model="Galaxy S26 Ultra",
               phone_number="+79238905467"),
    Smartphone(marka="Huawei", model="Pura 80 Ultra",
               phone_number="+79096748952"),
    Smartphone(marka="Honor", model="Magic 8 Pro",
               phone_number="+79528940473"),
    Smartphone(marka="Realme", model="GT7 Pro",
               phone_number="+79218460926"),
]

for smartphone in Catalog:
    print(smartphone)
