# fazendo a leitura do arquivo secret_password_file
password_file = open('secret_password_file.txt')

# lendo o conteúdo do arquivo para uma variável auxiliar
secret_password = password_file.read()

# solicitando uma senha para o usuário
typed_password = input('Enter your password: ')

# condicional para verificar se as senhas batem.
if typed_password == secret_password:
    print('Life! Universe! And all that.')
    print('Access granted')

elif typed_password == '12345':
    print('That password is one that an idiot puts on their luggage.')

else:

    print('Acess denied!')
