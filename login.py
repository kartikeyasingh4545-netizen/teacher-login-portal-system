import data


def lt():
  print('\n--- TEACHER PORTAL LOGIN ---')
  a = input('Enter Username: ').strip().lower()
  b = input('Enter Password: ')

  m = data.tdb[(data.tdb['username'] == a) & (data.tdb['password'] == b)]

  if m.empty:
    print('\nInvalid username or password. Access Denied.')
  else:
    tid = m.iloc[0]['tid']

    print(f'\nLogin Successful! Welcome, {a}.\n')
    print('--- YOUR STUDENT DASHBOARD ---')

    st = data.sdb[data.sdb['tid'] == tid]

    if st.empty:
      print('No students assigned to your ID yet.')
    else:
      d = st[['ano', 'name', 'marks']]
      print(d.to_string(index=False))

    print('------------------------------')
