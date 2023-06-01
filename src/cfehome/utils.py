from faker import Faker

def get_fake_profiles(count=10):
    fake=Faker()
    user_data = [] 
    for _ in range(count):
        profile = fake.profile()
        data = {
            "username" : profile.get('username'),
            'email': profile.get('mail'),
            'is_active': True
        }

        if 'name' in profile:
            names = profile.get('name').split(' ')
            data['first_name'] = names[0]
            data['last_name']  = names[1]

        user_data.append(data)
    return user_data    
