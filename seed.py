import os
from app import app, db
from models import Item

def seed_data():
    # Clear existing data
    db.drop_all()
    db.create_all()
    
    # Create dummy items
    items = [
        Item(
            name='Shirt',
            price=702000,
            description='This work-or-weekend perfect casual button-front shirt in gingham plaid is made in our Signature Tumbled Cotton for a soft, yet sturdy, hand. We utilize a unique Heritage Wash to give our garments a custom, lived-in feel right away',
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/04/9453071/1.jpg?4796"
        ),
        Item(
            name="Shoe",
            price=260000,
            description="This product you are currently browsing is fashionable, practical and cost-effective, making it to be a must-have one. At the same time, you can also click on the store name to enter our store and explore more fashionable surprises",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/88/5730102/1.jpg?6373"
        ),
        Item(
            name="Trousers",
            price=536000,
            description="This trouser is Stretching and breathable hence easier movement. Men Fashion-plus Offers the Best Price for this BluePerfect Quality. you can wear this trouser for casual, business and official.",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/27/84175/1.jpg?9528"
        ),
        Item(
            name="Watch",
            price=202000,
            description="This trouser is Stretching and breathable hence easier movement. Men Fashion-plus Offers the Best Price for this BluePerfect Quality. you can wear this trouser for casual, business and official.",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/46/275362/1.jpg?6934"
        ),
        Item(
            name="Dress",
            price=30000,
            description="Show your curves some love with our Most elegant dera maxi dresses. Made of  93% cotton fabric to absorb excess heat and moisture giving you a softest hug of maximum comfort",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/68/601243/1.jpg?2607"
        ),
        Item(
            name="Jacket",
            price=25000,
            description="As an essential part of your closet Berrykey-sea-cod jackets are a versatile choice for casual outings and also brilliant gear for chilled days.",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/46/375575/1.jpg?6191"
        ),
        Item(
            name="Boots",
            price=280000,
            description="1. Due to differences in display and lighting effects, the actual color of the item may differ slightly from the color displayed on the image. Thank you!",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/56/5919351/1.jpg?4493"
        ),
        Item(
            name="Belt",
            price=140000,
            description="This is a stylish and durable belt that complements any outfit.",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/87/0598011/1.jpg?8564"
        ),
        Item(
            name="Necklace",
            price=25000,
            description="The necklace has moon and star pendant design, which makes the necklace more elegant.",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/33/995193/1.jpg?7812"
        ),
        Item(
            name="T-shirt",
            price=380000,
            description="Moisture wicking fabric is quick-drying, ultra-soft & has a soft feel, keeping you comfortable through any athletic activity.",
            image_url="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/64/018813/1.jpg?2732"
        ),
        Item(
            name="Socks",
            price=240000,
            description="Low cut no show socks that are great for activities such as yoga, running, biking, or casual wear. These low-cut ankle length socks are made to look like they are barely there",
            image_url="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/96/285925/1.jpg?8773"
        ),
        Item(
            name="Blanket",
            price=160000,
            description="This premium throw blanket is a very useful for your living or bedroom space. It keeps you warm and cozy for a nap or movie time and protects your couch/bed from catching dirt or stains",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/99/102446/1.jpg?2476"
        ),
        Item(
            name="Pillow",
            price=24000,
            description="Features: High quality set of two pillows. Virgin Fiber filling. 600gms Highly comfortable for perfect sleep Fashion style, easy to use, comfortable.",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/81/724053/1.jpg?5345"
        ),
        Item(
            name="Bedsheet",
            price=350000,
            description="Cute super soft baby Swaddlers made of pure cotton that feels soft on baby skin with a motherly lovely warmth",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/24/414331/1.jpg?0585"
        ),
        Item(
            name="Sandals",
            price=440000,
            description="Get the most comfortable experience in these Unisex sneaker shoes made of the best quality. available in Size 2-9 normal fitting",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/25/526249/1.jpg?1061"
        ),
        Item(
            name="Blanket",
            price=660000,
            description="This Butterfly Maridadi Blanket provides warmth and comfort during fragile weather. ORDER NOW for the Butterfly Maridadi Blanket",
            image_url="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/51/755466/1.jpg?0835"
        )
    ]

    # Add all items to the session
    db.session.add_all(items)

    # Commit the session to save the items to the database
    db.session.commit()

    print('Database seeded!')

if __name__ == '__main__':
    with app.app_context():
        seed_data()
