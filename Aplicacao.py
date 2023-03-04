from graphqlclient import GraphQLClient
import pandas as pd
import json

rafaelchato = 'https://api.github.com/graphql'
TOKEN = 'token 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'

args ={'after': None}

query =  """
    query ($after: String) {
  search(query: "stars:>100", type: REPOSITORY, after: $after, first:2) {
       pageInfo {
                hasPreviousPage
                hasNextPage
                startCursor
                endCursor
            }
            repositoryCount
            edges {
                node {
                    ... on Repository {
                        id
                        url
                        name
                        nameWithOwner
                        stargazers {
                          totalCount
                        }
                        pullRequests {
                          totalCount
                        }
                        acceptedPullRequests: pullRequests(states: MERGED) { totalCount }
                        releases{
                          totalCount
                        }
                        primaryLanguage {
                            name
                          }
                          createdAt
                          updatedAt
                          closedIssues: issues(first:1,states:CLOSED){totalCount}
                          totalIssues: issues(first:1){totalCount}
                    }
                }
            }
  }
}
    """



client = GraphQLClient(rafaelchato)
client.inject_token(TOKEN)

df = pd.DataFrame()

for i in range(10):
    response = json.loads(client.execute(query= query, variables=args))
    print(response)
    args['after'] = response['data']['search']['pageInfo']['endCursor']

    data = response['data']['search']['edges']
    df = pd.concat([df, pd.json_normalize(data)], ignore_index=True)
    

# df.drop(['cursor', 'node.id', 'node.owner.id'], axis=1, inplace=True)

# Renomeia as colunas do dataframe
df.columns = ['id',
    'name',
    'nameWithOwner',
    'url',
    'createdAt',
    'updatedAt',
    'stargazers',
    'pullRequests',
    'acceptedPullRequests',
    'releases',
    'primaryLanguage',
    'totalIssues',
    'closedIssues',
    'batata']

# Salva o dataframe em um arquivo CSV
df.to_csv('repositorios.csv', sep=';', index=False)
