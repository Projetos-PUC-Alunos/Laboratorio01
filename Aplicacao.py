from graphqlclient import GraphQLClient
import json

rafaelchato = 'https://api.github.com/graphql'
TOKEN = 'Token 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'

args ={'after': None}

query =  """
    query ($after: String) {
  search(query: "stars:>100", type: REPOSITORY, after: $after, first:100) {
    pageInfo {
      endCursor
    }
    nodes {
      ... on Repository {
        name
      }
    }
  }
}
    """



client = GraphQLClient(rafaelchato)
client.inject_token(TOKEN)

for i in range(100):
    data = json.loads(client.execute(query= query, variables=args))
    args['after'] = data['data']['search']['pageInfo']['endCursor']

    print(data)