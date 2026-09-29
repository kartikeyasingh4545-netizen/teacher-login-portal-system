import data
import pandas as pd


def rt():
  print('\n--- CREATE NEW TEACHER ACCOUNT ---')
  a = input('Enter new Username: ').strip().lower()

  if a in data.tdb['username'].values:
    print(
        '\nUsername already exists! Please try logging in or use a different'
        ' username.'
    )
    return

  b = input('Enter new Password: ')
  tid = int(data.tdb['tid'].max() + 1)

  c = pd.DataFrame({'tid': [tid], 'username': [a], 'password': [b]})
  # Update the shared dataframe in data.py
  data.tdb = pd.concat([data.tdb, c], ignore_index=True)

  print(f'\nAccount created successfully! Your Teacher ID is {tid}. You can now'
      ' log in.')