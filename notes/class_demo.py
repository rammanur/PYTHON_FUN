'A simple demonstration of Python classes'

class Dog:
    'A simple canine class'

    def __init__(self, n):
        self.name = n

    def bark(self):
        print 'Woof!  %s is barking' % self.name

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('Oops, too far!')
        return index * 111

    def __str__(self):
        return 'I am a dog named %s' % self.name

    def __repr__(self):
        return 'Dog(%r)' % self.name

    def __call__(self, action):
        if action == 'fetch':
            return '%s is fetching' % self.name
        elif action == 'owner':
            return 'Raymond'
        else:
            raise ValueError('Unknown action')

if __name__ == '__main__':
    d = Dog('Fido')
    e = Dog('Buddy')






