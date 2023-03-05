from graphqlclient import GraphQLClient
import pandas as pd
import json
import time

API = 'https://api.github.com/graphql'
TOKEN = 'token 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'

args ={'after': None}

query =  """
    query ($after: String) {
  search(query: "stars:>100", type: REPOSITORY, first: 10, after: $after) {
    pageInfo {
      hasPreviousPage
      hasNextPage
      startCursor
      endCursor
    }
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
          acceptedPullRequests: pullRequests(states: MERGED) {
            totalCount
          }
          releases {
            totalCount
          }
          primaryLanguage {
            name
          }
          createdAt
          updatedAt: defaultBranchRef {
            target {
              ... on Commit {
                history(first: 1) {
                  edges {
                    node {
                      ... on Commit {
                        committedDate
                      }
                    }
                  }
                }
              }
            }
          }
          closedIssues: issues(first: 1, states: CLOSED) {
            totalCount
          }
          totalIssues: issues(first: 1) {
            totalCount
          }
        }
      }
    }
  }
}
    """



client = GraphQLClient(API)
client.inject_token(TOKEN)

df = pd.DataFrame()

for i in range(100):
    response = json.loads(client.execute(query= query, variables=args))
    print(response)
    args['after'] = response['data']['search']['pageInfo']['endCursor']

    data = response['data']['search']['edges']
    df = pd.concat([df, pd.json_normalize(data)], ignore_index=True)

    time.sleep(1)
    


# Renomeia as colunas do dataframe
df.columns = ['ID',
              'URL',
              'Name',
              'NameWithOwner',
              'Stargazers',
              'PullRequests',
              'AcceptedPullRequests',
              'Releases',
              'PrimaryLanguage',
              'createdAt',
              'updatedAt',
              'closedIssues',
              'totalIssues',
              '']

# Extrai a data na coluna updatedAt
def extract_date(updatedAt):
    return updatedAt[0]['node']['committedDate']

df['updatedAt'] = df['updatedAt'].apply(extract_date)

df = df.drop(df.columns[-1], axis=1)

# Salva o dataframe em um arquivo CSV
df.to_csv('repositorios.csv', sep=';', index=False)
