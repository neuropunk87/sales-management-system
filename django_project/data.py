from users.models import Customer, Seller
from products.models import Product
from sales.models import Sale
from datetime import date, datetime
from random import choice, randint


customers = [
    Customer(first_name="John", last_name="Doe", phone="1234567890", email="john.doe@example.com"),
    Customer(first_name="Jane", last_name="Smith", phone="1234567891", email="jane.smith@example.com"),
    Customer(first_name="Michael", last_name="Johnson", phone="1234567892", email="michael.johnson@example.com"),
    Customer(first_name="Emily", last_name="Davis", phone="1234567893", email="emily.davis@example.com"),
    Customer(first_name="Chris", last_name="Brown", phone="1234567894", email="chris.brown@example.com"),
    Customer(first_name="Sarah", last_name="Wilson", phone="1234567895", email="sarah.wilson@example.com"),
    Customer(first_name="David", last_name="Miller", phone="1234567896", email="david.miller@example.com"),
    Customer(first_name="Jessica", last_name="Taylor", phone="1234567897", email="jessica.taylor@example.com"),
    Customer(first_name="James", last_name="Anderson", phone="1234567898", email="james.anderson@example.com"),
    Customer(first_name="Laura", last_name="Thomas", phone="1234567899", email="laura.thomas@example.com"),
    Customer(first_name="Robert", last_name="Jackson", phone="1234567800", email="robert.jackson@example.com"),
    Customer(first_name="Anna", last_name="White", phone="1234567801", email="anna.white@example.com"),
    Customer(first_name="Brian", last_name="Harris", phone="1234567802", email="brian.harris@example.com"),
    Customer(first_name="Emma", last_name="Martin", phone="1234567803", email="emma.martin@example.com"),
    Customer(first_name="Steven", last_name="Lee", phone="1234567804", email="steven.lee@example.com"),
    Customer(first_name="Olivia", last_name="Walker", phone="1234567805", email="olivia.walker@example.com"),
    Customer(first_name="Daniel", last_name="Hall", phone="1234567806", email="daniel.hall@example.com"),
    Customer(first_name="Sophia", last_name="Allen", phone="1234567807", email="sophia.allen@example.com"),
    Customer(first_name="Matthew", last_name="Young", phone="1234567808", email="matthew.young@example.com"),
    Customer(first_name="Mia", last_name="King", phone="1234567809", email="mia.king@example.com"),
    Customer(first_name="Liam", last_name="Wright", phone="1234567810", email="liam.wright@example.com"),
    Customer(first_name="Noah", last_name="Lopez", phone="1234567811", email="noah.lopez@example.com"),
    Customer(first_name="Charlotte", last_name="Hill", phone="1234567812", email="charlotte.hill@example.com"),
    Customer(first_name="Amelia", last_name="Scott", phone="1234567813", email="amelia.scott@example.com"),
    Customer(first_name="Evelyn", last_name="Adams", phone="1234567814", email="evelyn.adams@example.com"),
    Customer(first_name="Harper", last_name="Baker", phone="1234567815", email="harper.baker@example.com"),
    Customer(first_name="Alexander", last_name="Garcia", phone="1234567816", email="alexander.garcia@example.com"),
    Customer(first_name="Mason", last_name="Rodriguez", phone="1234567817", email="mason.rodriguez@example.com"),
    Customer(first_name="Ella", last_name="Martinez", phone="1234567818", email="ella.martinez@example.com"),
    Customer(first_name="Aiden", last_name="Hernandez", phone="1234567819", email="aiden.hernandez@example.com"),
    Customer(first_name="Henry", last_name="Clark", phone="1234567820", email="henry.clark@example.com"),
    Customer(first_name="Scarlett", last_name="Lewis", phone="1234567821", email="scarlett.lewis@example.com"),
    Customer(first_name="Zoey", last_name="Lee", phone="1234567822", email="zoey.lee@example.com"),
    Customer(first_name="Elijah", last_name="Walker", phone="1234567823", email="elijah.walker@example.com"),
    Customer(first_name="Lillian", last_name="Hall", phone="1234567824", email="lillian.hall@example.com"),
    Customer(first_name="Sebastian", last_name="Allen", phone="1234567825", email="sebastian.allen@example.com"),
    Customer(first_name="Gabriel", last_name="Young", phone="1234567826", email="gabriel.young@example.com"),
    Customer(first_name="Chloe", last_name="King", phone="1234567827", email="chloe.king@example.com"),
    Customer(first_name="Luna", last_name="Wright", phone="1234567828", email="luna.wright@example.com"),
    Customer(first_name="Levi", last_name="Lopez", phone="1234567829", email="levi.lopez@example.com"),
    Customer(first_name="Grace", last_name="Hill", phone="1234567830", email="grace.hill@example.com"),
    Customer(first_name="Aria", last_name="Scott", phone="1234567831", email="aria.scott@example.com"),
    Customer(first_name="Eleanor", last_name="Adams", phone="1234567832", email="eleanor.adams@example.com"),
    Customer(first_name="Camila", last_name="Baker", phone="1234567833", email="camila.baker@example.com"),
    Customer(first_name="Isaac", last_name="Garcia", phone="1234567834", email="isaac.garcia@example.com"),
    Customer(first_name="Oliver", last_name="Rodriguez", phone="1234567835", email="oliver.rodriguez@example.com"),
    Customer(first_name="Jackson", last_name="Reed", phone="1234567837", email="jackson.reed@example.com"),
    Customer(first_name="Zoe", last_name="Ward", phone="1234567838", email="zoe.ward@example.com"),
    Customer(first_name="Ryan", last_name="Carter", phone="1234567839", email="ryan.carter@example.com"),
    Customer(first_name="Madison", last_name="Turner", phone="1234567840", email="madison.turner@example.com"),
]
Customer.objects.bulk_create(customers)


sellers = [
    Seller(first_name="Alice", last_name="Williams", phone="9876543210", email="alice.williams@example.com", hire_date=date(2021, 1, 15), position="seller"),
    Seller(first_name="Ethan", last_name="Moore", phone="9876543211", email="ethan.moore@example.com", hire_date=date(2020, 6, 12), position="chief_seller"),
    Seller(first_name="Grace", last_name="Taylor", phone="9876543212", email="grace.taylor@example.com", hire_date=date(2019, 3, 10), position="head"),
    Seller(first_name="Luke", last_name="Anderson", phone="9876543213", email="luke.anderson@example.com", hire_date=date(2022, 8, 19), position="seller"),
    Seller(first_name="Mason", last_name="Scott", phone="9876543214", email="mason.scott@example.com", hire_date=date(2023, 2, 5), position="seller"),
    Seller(first_name="Lily", last_name="Baker", phone="9876543215", email="lily.baker@example.com", hire_date=date(2021, 9, 25), position="chief_seller"),
    Seller(first_name="Ava", last_name="Clark", phone="9876543216", email="ava.clark@example.com", hire_date=date(2020, 4, 22), position="seller"),
    Seller(first_name="Jack", last_name="Carter", phone="9876543217", email="jack.carter@example.com", hire_date=date(2018, 11, 30), position="head"),
    Seller(first_name="Oliver", last_name="Green", phone="9876543218", email="oliver.green@example.com", hire_date=date(2023, 7, 14), position="seller"),
    Seller(first_name="Sophia", last_name="Perez", phone="9876543219", email="sophia.perez@example.com", hire_date=date(2017, 5, 9), position="chief_seller"),
    Seller(first_name="Ella", last_name="Roberts", phone="9876543200", email="ella.roberts@example.com", hire_date=date(2021, 6, 16), position="seller"),
    Seller(first_name="Emily", last_name="Hernandez", phone="9876543201", email="emily.hernandez@example.com", hire_date=date(2022, 3, 8), position="seller"),
    Seller(first_name="Henry", last_name="Martinez", phone="9876543202", email="henry.martinez@example.com", hire_date=date(2019, 10, 28), position="chief_seller"),
    Seller(first_name="Abigail", last_name="Lopez", phone="9876543203", email="abigail.lopez@example.com", hire_date=date(2020, 1, 7), position="seller"),
    Seller(first_name="Benjamin", last_name="Gonzalez", phone="9876543204", email="benjamin.gonzalez@example.com", hire_date=date(2023, 9, 13), position="head"),
    Seller(first_name="Charlotte", last_name="Wilson", phone="9876543205", email="charlotte.wilson@example.com", hire_date=date(2021, 12, 17), position="seller"),
    Seller(first_name="Daniel", last_name="Nguyen", phone="9876543206", email="daniel.nguyen@example.com", hire_date=date(2022, 4, 23), position="seller"),
    Seller(first_name="Harper", last_name="Rivera", phone="9876543207", email="harper.rivera@example.com", hire_date=date(2023, 6, 15), position="chief_seller"),
    Seller(first_name="Isabella", last_name="Campbell", phone="9876543208", email="isabella.campbell@example.com", hire_date=date(2020, 2, 2), position="head"),
    Seller(first_name="Logan", last_name="Parker", phone="9876543209", email="logan.parker@example.com", hire_date=date(2022, 11, 11), position="seller"),
]
Seller.objects.bulk_create(sellers)


products = [
    Product(name="Laptop", description="High-performance laptop", stock_quantity=250, price=1200.00),
    Product(name="Smartphone", description="Latest model smartphone", stock_quantity=550, price=800.00),
    Product(name="Tablet", description="Lightweight tablet", stock_quantity=400, price=500.00),
    Product(name="Monitor", description="4K resolution monitor", stock_quantity=200, price=300.00),
    Product(name="Keyboard", description="Mechanical keyboard", stock_quantity=450, price=50.00),
    Product(name="Mouse", description="Wireless mouse", stock_quantity=500, price=25.00),
    Product(name="Headphones", description="Noise-cancelling headphones", stock_quantity=475, price=150.00),
    Product(name="Camera", description="Digital camera", stock_quantity=175, price=700.00),
    Product(name="Smartwatch", description="Wearable smartwatch", stock_quantity=225, price=200.00),
    Product(name="Printer", description="All-in-one printer", stock_quantity=300, price=250.00),
    Product(name="Speaker", description="Bluetooth speaker", stock_quantity=150, price=100.00),
    Product(name="Router", description="Wi-Fi router", stock_quantity=525, price=80.00),
    Product(name="Projector", description="HD projector", stock_quantity=100, price=400.00),
    Product(name="External Drive", description="1TB external drive", stock_quantity=425, price=120.00),
    Product(name="Charger", description="Fast charging device", stock_quantity=575, price=20.00),
    Product(name="Microphone", description="USB microphone", stock_quantity=125, price=100.00),
    Product(name="Gaming Console", description="Next-gen gaming console", stock_quantity=275, price=500.00),
    Product(name="VR Headset", description="Virtual reality headset", stock_quantity=325, price=600.00),
    Product(name="Drone", description="Camera-equipped drone", stock_quantity=375, price=1000.00),
    Product(name="Power Bank", description="Portable power bank", stock_quantity=350, price=40.00),
]
Product.objects.bulk_create(products)


customers = list(Customer.objects.all())
sellers = list(Seller.objects.all())
products = list(Product.objects.all())


sales = []
for _ in range(100):
    product = choice(products)
    quantity = randint(1, 10)
    if product.stock_quantity >= quantity:
        total_amount = round(product.price * quantity, 2)

        sale_date = datetime(
            year=2024,
            month=randint(1, 12),
            day=randint(1, 28),
            hour=randint(0, 23),
            minute=randint(0, 59),
            second=randint(0, 59),
            microsecond=randint(0, 999999)
        )

        sales.append(
            Sale(
                customer=choice(customers),
                seller=choice(sellers),
                product=product,
                sale_date=sale_date,
                quantity=quantity,
                total_amount=total_amount
            )
        )
        product.stock_quantity -= quantity

Sale.objects.bulk_create(sales)
sales = list(Sale.objects.all())


""" 
    ---> settings.py: USE_TZ = True -> False
    ---> sales(app)/models.py: auto_now_add=True -> False
    ! Indents
    python manage.py shell
sales = []
for _ in range(100):
    product = choice(products)
    quantity = randint(1, 10)
    if product.stock_quantity >= quantity:
        total_amount = round(product.price * quantity, 2)
        sale_date = datetime(year=2024, month=randint(1, 12), day=randint(1, 28), hour=randint(0, 23), minute=randint(0, 59), second=randint(0, 59), microsecond=randint(0, 999999))
        sales.append(Sale(customer=choice(customers), seller=choice(sellers), product=product, sale_date=sale_date, quantity=quantity, total_amount=total_amount))
        product.stock_quantity -= quantity
"""