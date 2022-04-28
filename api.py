from graphene_mongo import MongoengineObjectType
from model import CrudeOil as CrudeOilModel
from model import Bitcoin as BitcoinModel
from model import Gold as GoldModel
from mongoengine import connect
from aiohttp import web
import graphene
import json


async def mongo(request):
    data = request
    connect('currency_pairs', host='localhost', port=27017)

    class CrudeOil(MongoengineObjectType):
        class Meta:
            model = CrudeOilModel

    class Gold(MongoengineObjectType):
        class Meta:
            model = GoldModel

    class Bitcoin(MongoengineObjectType):
        class Meta:
            model = BitcoinModel

    class Query(graphene.ObjectType):
        bitcoins = graphene.List(Bitcoin)
        crudeOils = graphene.List(CrudeOil)
        golds = graphene.List(Gold)

        def resolve_bitcoins(self, info):
            return list(BitcoinModel.objects.all())

        def resolve_crudeOils(self, info):
            return list(CrudeOilModel.objects.all())

        def resolve_golds(self, info):
            return list(GoldModel.objects.all())

    schema = graphene.Schema(query=Query, types=[Bitcoin, CrudeOil, Gold])
    query = request.query['query']
    result = schema.execute(query)
    return web.Response(text=json.dumps(result.data), status=200)


app = web.Application()
app.router.add_get('/graphql', mongo)
web.run_app(app, port=4000)
