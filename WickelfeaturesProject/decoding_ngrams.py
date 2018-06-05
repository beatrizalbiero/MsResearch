"""Decodification of ngrams."""

import pandas as pd
from trigrams_nodes import trigrams_dict


def decoding(vector, verbose=False):
    """
    Receive a vector that represents the activation of trigrams and decode it
    back to a verb. You can choose to display the string or the dataset with
    the values.

    :vector type: numpy array
    :verbose type: boolean
    :r type: string
    """
    def createdf(vector):
        """
        Create a dataframe of trigrams and prediction values.

        :vector type: list
        :rtype: dataframe (pandas)
        """
        df = pd.DataFrame()
        df['trigram'] = trigrams_dict
        df['value'] = vector
        return df

    def best(df, n):
        """
        Select sixteen best wickelfeatures.

        :df type: df (pandas)
        :r type: df (pandas)
        """
        x = df.sort_values(by=['value'], axis=0, ascending=False,
                           inplace=False, kind='quicksort',
                           na_position='last')
        r = x.head(n)
        return r.sort_index(axis=0)

    def find_compatible(df1, df2):
        """
        Find Compatible.
        returns a new df with compatible trigrams

        :df1 type: df
        :df2 type: df
        :r type: df
        """
        import pandas as pd

        df3 = pd.DataFrame()
        df2['aux'] = ''
        for index, row in df2.iterrows():
            df2.iloc[index,
                     df2.columns.get_loc('aux')] = (row['trigram'][0] +
                                                    row['trigram'][1])
        for index, row in df1.iterrows():
            last_two = row[0][-2]+row[0][-1]
            df3 = df3.append(df2[df2['aux'].isin([last_two])])
        return df3

    df = createdf(vector)  # df com todos os trigramas e seus respectivos valores

    first = df[:117]
    decoded = []
    decoded = best(first, 1)

    i = 0
    while decoded.tail(1).iloc[0]['trigram'][-1] != '#':
        new = best(find_compatible(decoded.tail(1), df), 1)
        decoded = decoded.append(new[['trigram', 'value']])
        i += 1
        if i > 8:
            break

    if verbose is True:
        return decoded
    else:
        joining = ''.join(decoded['trigram'].iloc[0])
        for item in decoded['trigram'].iloc[1:]:
            joining = joining + item[2]
        return joining
