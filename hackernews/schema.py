import graphene

import links.schema
import hackernews.users.schema

class Query(links.schema.Query, graphene.ObjectType):
	pass


class Mutation(hackernews.users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
	pass

schema = graphene.Schema(query=Query, mutation=Mutation)