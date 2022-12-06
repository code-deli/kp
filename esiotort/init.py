from domain.mymods import Event
from tortoise import Tortoise

async def run():
    # postgres://postgres:pass@db.host:5432/somedb
    await Tortoise.init(db_url="postgres://postgres:postgres@localhost:5432/exampledb",
                        modules={"models": ["_models_"],'default_connection': 'default'})
    #await Tortoise.generate_schemas()
    #
    event = await Event.create(name="Test")
    await Event.filter(id=event.id).update(name="Updated name")
    #
    # print(await Event.filter(name="Updated name").first())
    # # >>> Updated name
    #
    # await Event(name="Test 2").save()
    # print(await Event.all().values_list("id", flat=True))
    # # >>> [1, 2]
    # print(await Event.all().values("id", "name"))
    # # >>> [{'id': 1, 'name': 'Updated name'}, {'id': 2, 'name': 'Test 2'}]


