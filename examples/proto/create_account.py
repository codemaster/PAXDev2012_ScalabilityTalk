import create_account_pb2
acc = create_account_pb2.CreateAccount()
acc.username = 'user123'
acc.password = 'popsicles'
acc.email = 'user123@example.com'
acc.first_name = 'Joe'
acc.last_name = 'Schmo'
print acc.SerializeToString()
