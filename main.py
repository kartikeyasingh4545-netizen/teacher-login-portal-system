import login
import signup


def main():
  while True:
    print('\n==============================')
    print('    TEACHER PORTAL SYSTEM      ')
    print('==============================')
    print('1. Login')
    print('2. Create New Account (Sign Up)')
    print('3. Exit')

    ch = input('Choose an option (1-3): ').strip()

    if ch == '1':
      login.lt()
    elif ch == '2':
      signup.rt()
    elif ch == '3':
      print('\nThank you for using the Teacher Portal. Goodbye!')
      break
    else:
      print('\nInvalid choice. Please enter 1, 2, or 3.')


if __name__ == '__main__':
  main()