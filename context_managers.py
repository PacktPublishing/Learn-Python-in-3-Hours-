with open('sample_folder_structure.txt', 'r') as f:
    for line in f:
        print(line)

for _ in range(1e5):
    open('sample_folder_structure.txt', 'r')

for _ in range(1e5):
    f = open('sample_folder_structure.txt', 'r')
    # do something here
    for line in f:
        print(line)
    f.close()

# testing
def dummy_test(self):
    with self.assertRaises(TypeError):
        ' '.join(2)

# threading
with threading.RLock():
    access_resource()

# connecting to external resources
conn = sqlite3.connect(':memory:')
with conn:
    conn.execute('select * from table')
