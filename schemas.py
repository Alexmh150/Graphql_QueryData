from statistics import mode
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Alumno, db

class SchemaAlumno(SQLAlchemyObjectType):
    class Meta:
        model = Alumno
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    estudiantes = SQLAlchemyConnectionField(SchemaAlumno.connection)

schema = graphene.Schema(query=Query)