from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .appName("Read CSV Example")\
        .getOrCreate()

data = [
    ("O001","Amit","Hyderabad","Spice Hub","Indian",450,35,"UPI","Delivered"),
    ("O002","Neha","Bangalore","Pizza Town","Italian",650,40,"Card","Delivered"),
    ("O003","Rahul","Delhi","Burger Zone","American",520,30,"Cash","Delivered"),
    ("O004","Pooja","Mumbai","Sushi Bar","Japanese",1200,55,"UPI","Cancelled"),
    ("O005","Arjun","Chennai","Curry Leaf","Indian",380,28,"UPI","Delivered"),
    ("O006","Sneha","Hyderabad","Pasta Street","Italian",700,45,"Card","Delivered"),
    ("O007","Karan","Delhi","Taco Bell","Mexican",540,33,"UPI","Delivered"),
    ("O008","Riya","Bangalore","Dragon Bowl","Chinese",600,38,"Wallet","Delivered"),
    ("O009","Vikas","Mumbai","BBQ Nation","Indian",1500,60,"Card","Delivered"),
    ("O010","Anjali","Chennai","Burger Zone","American",480,32,"Cash","Delivered"),
    ("O011","Farhan","Delhi","Biryani House","Indian",520,36,"UPI","Delivered"),
    ("O012","Megha","Hyderabad","Sushi Bar","Japanese",1100,58,"Card","Cancelled"),
    ("O013","Suresh","Bangalore","Curry Leaf","Indian",420,29,"UPI","Delivered"),
    ("O014","Divya","Mumbai","Pizza Town","Italian",780,42,"Wallet","Delivered"),
    ("O015","Nikhil","Delhi","Pasta Street","Italian",690,47,"UPI","Delivered"),
    ("O016","Kavya","Chennai","Dragon Bowl","Chinese",560,34,"UPI","Delivered"),
    ("O017","Rohit","Hyderabad","BBQ Nation","Indian",1400,62,"Card","Delivered"),
    ("O018","Simran","Bangalore","Burger Zone","American",510,31,"Cash","Delivered"),
    ("O019","Ayesha","Mumbai","Taco Bell","Mexican",570,35,"UPI","Delivered"),
    ("O020","Manish","Delhi","Curry Leaf","Indian",390,27,"Wallet","Delivered"),
    ("O021","Priya","Hyderabad","Pizza Town","Italian",720,41,"Card","Delivered"),
    ("O022","Yash","Chennai","Sushi Bar","Japanese",1150,57,"UPI","Delivered"),
    ("O023","Naina","Bangalore","Pasta Street","Italian",680,44,"UPI","Delivered"),
    ("O024","Sameer","Mumbai","Dragon Bowl","Chinese",610,39,"Wallet","Delivered"),
    ("O025","Ritika","Delhi","Burger Zone","American",500,30,"Cash","Delivered"),
    ("O026","Gopal","Hyderabad","Curry Leaf","Indian",410,28,"UPI","Delivered"),
    ("O027","Tina","Bangalore","Pizza Town","Italian",760,43,"Card","Delivered"),
    ("O028","Irfan","Mumbai","BBQ Nation","Indian",1550,65,"Card","Delivered"),
    ("O029","Sahil","Chennai","Taco Bell","Mexican",590,37,"UPI","Delivered"),
    ("O030","Lavanya","Delhi","Dragon Bowl","Chinese",630,40,"Wallet","Delivered"),
    ("O031","Deepak","Hyderabad","Burger Zone","American",520,33,"Cash","Delivered"),
    ("O032","Shweta","Bangalore","Curry Leaf","Indian",450,31,"UPI","Delivered"),
    ("O033","Aman","Mumbai","Pizza Town","Italian",810,46,"Card","Delivered"),
    ("O034","Rekha","Chennai","Pasta Street","Italian",700,45,"UPI","Delivered"),
    ("O035","Zubin","Delhi","BBQ Nation","Indian",1480,63,"Card","Delivered"),
    ("O036","Pallavi","Hyderabad","Dragon Bowl","Chinese",580,36,"Wallet","Delivered"),
    ("O037","Naveen","Bangalore","Taco Bell","Mexican",560,34,"UPI","Delivered"),
    ("O038","Sonia","Mumbai","Sushi Bar","Japanese",1180,59,"Card","Delivered"),
    ("O039","Harish","Chennai","Burger Zone","American",490,29,"Cash","Delivered"),
    ("O040","Kriti","Delhi","Curry Leaf","Indian",420,26,"UPI","Delivered")
]

columns = [
    "order_id","customer_name","city","restaurant","cuisine",
    "order_amount","delivery_time_minutes","payment_mode","order_status"
]

df = spark.createDataFrame(data, columns)
df.show()
df.printSchema()
