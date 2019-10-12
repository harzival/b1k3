
class Product:
    def __init__ ( self, name, url, price, ammount, parts = [] ):
        self.name = name
        self.url = url
        self.price = price
        self.ammount = ammount
        self.parts = parts

class Part:
    def __init__ ( self ):
        #self.name = name
        self.name = None

myMoney = 500

partDictionary = {
    "frame":                    Part(),
    "seatPost":                 Part(),
    "forks":                    Part(),
    "headset":                  Part(),
    "mechFront":                Part(),
    "mechBack":                 Part(),
    "brakesFront":              Part(),
    "brakesBack":               Part(),
    "shifters":                 Part(),
    "cassette":                 Part(),
    "chain":                    Part(),
    "wheels":                   Part(),
    "tyres":                    Part(),
    "handlebars":               Part(),
    "handlebarGrips":           Part(),
    "stem":                     Part(),
    "bottomBracket":            Part(),
    "saddle":                   Part(),
    "pedals":                   Part(),
    "gearCable":                Part(),
    "brakeCable":               Part(),
    "chainMasterLink":          Part(),
    "inlineBarrelAdjusters":    Part(),
    "spacers":                  Part(),
    "batteryBox":               Part(),
    "ignitionSwitch":           Part(),

}

productList = [ 
    
    # Product ( "name",
    # "url",
    # price,
    # numberOfItem,
    # partsGainedList [ "partname1", "partname2" ],
    # )

    # Product ( "name", "url", price, numberOfItem, partsGainedList [ "partname1", "partname2" ] )

    Product ( "Stealth bomber electric bicycle frame", 
    "https://www.alibaba.com/product-detail/Wholesale-price-of-manufacturer-e-bike_60507483283.html?spm=a2700.galleryofferlist.normalList.27.7d636d74wC7zPP", 
    129.96,
    1,
    [
        partDictionary["frame"],
        partDictionary["batteryBox"],
        partDictionary["ignitionSwitch"]
    ] ),
    Product ( "CE electric bike frame suspension motorized bicycle frame",
    "https://www.alibaba.com/product-detail/CE-electric-bike-frame-suspension-motorized_60554108200.html?spm=a2700.galleryofferlist.normalList.166.427b6d74DYEOu9",
    450,
    1,
    [
        partDictionary["frame"],
        partDictionary["batteryBox"],
    ] ),
    Product ( "Maikale 8000W High power Electric Motorcycle Electric Scooter Electric Off-road Bicycle Frame parts ",
    "https://www.alibaba.com/product-detail/Maikale-8000W-High-power-Electric-Motorcycle_62186837072.html?spm=a2700.galleryofferlist.normalList.1.17436d74M1UlfA",
    129.96,
    1,
    [
        partDictionary["frame"],
        partDictionary["batteryBox"],
    ]
    ),
    Product ( "MTB Folding frame 26x17 inch aluminium folding mountain bicycle frame bike suspension frame bicycle frame",
    "https://www.aliexpress.com/item/32704090257.html?spm=a2g0o.productlist.0.0.5fda5bc58uUB1d&algo_pvid=ac2c6196-6270-4e44-a601-6757f528c672&algo_expid=ac2c6196-6270-4e44-a601-6757f528c672-33&btsid=bdaf8f2a-a009-4d2e-94b1-db70e55ae91a&ws_ab_test=searchweb0_0,searchweb201602_4,searchweb201603_55",
    93.84,
    1,
    [
        partDictionary["frame"],
    ]),
    Product ( "No painting new 26*17inch super light 1590g MTB bicycle frame 26er mountain bike frames spare ultralight aluminum alloy frame",
    "https://www.aliexpress.com/item/33016819476.html?spm=2114.12010612.8148356.11.5dfd464eINziKG",
    61.81,
    1,
    [
        partDictionary["frame"],
    ]),
]

